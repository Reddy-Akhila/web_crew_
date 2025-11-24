import os
import sys
import importlib.util

# Add project root to sys.path (defensive)
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

backend_app_path = os.path.join(project_root, 'backend', 'app.py')
if not os.path.isfile(backend_app_path):
    raise FileNotFoundError(f"backend app not found at {backend_app_path}")

spec = importlib.util.spec_from_file_location('backend_app', backend_app_path)
# Guard against spec being None (type checker and runtime safety)
assert spec is not None, f"Unable to create module spec for {backend_app_path}"
# spec.loader can be None in some edge cases; ensure loader exists
assert getattr(spec, 'loader', None) is not None, f"No loader available for spec {spec}"
backend_app = importlib.util.module_from_spec(spec)
# Extract loader and assert non-None so the type-checker knows it's safe
loader = spec.loader
assert loader is not None, f"Loader missing for spec {spec}"
loader.exec_module(backend_app)

app = getattr(backend_app, 'app', None)
if app is None:
    raise AttributeError('No Flask `app` found in backend.app')

if __name__ == '__main__':
    # Run the Flask app without the reloader so the process stays stable
    # Use explicit host and disable the automatic reloader
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
