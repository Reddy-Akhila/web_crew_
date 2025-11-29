"""
SEO Auditor Backend - Flask Application
Main entry point for the Technical SEO auditing system
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import datetime

# Ensure project root is on sys.path so sibling packages can be imported
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from web_crawler.crawler import WebCrawler
from seo_analyzer.analyzer import SEOAnalyzer
from seo_analyzer.recommendations import RecommendationEngine
from urllib.parse import urlparse
import validators

load_dotenv()

app = Flask(__name__)
CORS(app)


# Log incoming requests for debugging
@app.before_request
def log_request_info():
    try:
        print(f"Incoming request: {request.method} {request.path}")
    except Exception:
        pass

# Initialize components
crawler = WebCrawler()  # allow_external default is True in updated crawler
analyzer = SEOAnalyzer()
recommendation_engine = RecommendationEngine()

# Store audit history in memory (can be upgraded to database)
audit_history = {}

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})


@app.route('/', methods=['GET'])
def root():
    """Root handler to avoid Method Not Allowed when visiting server root in browser"""
    return jsonify({'message': 'SEO Auditor backend', 'health': 'ok'}), 200


@app.route('/favicon.ico')
def favicon():
    return ('', 204)

@app.route('/api/audit', methods=['POST'])
def run_audit():
    """
    Main endpoint to run a comprehensive SEO audit
    Request body:
    {
        "url": "https://example.com",
        "depth": 2,
        "auto_fix": false
    }
    """
    try:
        print("\n[DEBUG] /api/audit called")
        data = request.get_json() or {}
        print(f"[DEBUG] Request data: {data}")
        
        url = data.get('url')
        depth = int(data.get('depth', 2))
        auto_fix = data.get('auto_fix', False)
        
        print(f"[DEBUG] Parsed: url={url}, depth={depth}, auto_fix={auto_fix}")

        if not url:
            print("[DEBUG] URL is empty/missing, returning 400")
            return jsonify({'error': 'URL is required'}), 400

        # Normalize URL: add scheme if missing and strip fragments
        url = url.strip()
        parsed = urlparse(url)
        if not parsed.scheme:
            url = 'http://' + url

        # validate URL
        if not validators.url(url):
            print(f"[DEBUG] Invalid URL after normalization: {url}")
            return jsonify({'error': 'Invalid URL. Please include a valid scheme (http/https) or well-formed domain.'}), 400

        # Step 1: Crawl the website
        print(f"[1/3] Starting crawl of {url} with depth {depth}")
        try:
            crawl_results = crawler.crawl(url, depth)
            print(f"[DEBUG] Crawl completed. Pages: {len(crawl_results.get('pages', []))}")
        except Exception as crawl_err:
            print(f"[ERROR] Crawl failed: {crawl_err}")
            raise

        # Step 2: Analyze with AI-based scoring
        print(f"[2/3] Analyzing {len(crawl_results['pages'])} pages")
        try:
            analysis_results = analyzer.analyze_pages(crawl_results)
            print(f"[DEBUG] Analysis completed. Score: {analysis_results.get('overall_score', 0)}")
        except Exception as ana_err:
            print(f"[ERROR] Analysis failed: {ana_err}")
            raise

        # Step 3: Generate recommendations
        print(f"[3/3] Generating recommendations")
        try:
            recommendations = recommendation_engine.generate_recommendations(
                analysis_results, 
                auto_fix=auto_fix
            )
            print(f"[DEBUG] Recommendations generated. Count: {len(recommendations.get('recommendations', []))}")
        except Exception as rec_err:
            print(f"[ERROR] Recommendation generation failed: {rec_err}")
            raise

        # Compile audit report
        print(f"[DEBUG] crawl_results keys: {crawl_results.keys()}")
        print(f"[DEBUG] crawl_results['pages'] length: {len(crawl_results.get('pages', []))}")
        print(f"[DEBUG] crawl_results: {crawl_results}")
        
        audit_report = {
            'audit_id': f"audit_{datetime.now().timestamp()}",
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'crawl_summary': {
                'total_pages': len(crawl_results.get('pages', [])),
                'broken_links': len(crawl_results.get('broken_links', [])),
                'crawl_time': crawl_results.get('crawl_time', 0)
            },
            'seo_score': analysis_results.get('overall_score', 0),
            'issues': analysis_results.get('issues', []),
            'recommendations': recommendations.get('recommendations', []),
            'simulated_impact': recommendations.get('simulated_impact', {}),
            'pages': crawl_results.get('pages', [])[:5]  # Return first 5 pages summary
        }

        # Store in history
        audit_history[audit_report['audit_id']] = audit_report
        print(f"[DEBUG] Audit stored with total_pages: {audit_report['crawl_summary']['total_pages']}")

        return jsonify(audit_report), 200

    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        # log to file for easier debugging
        with open(os.path.join(project_root, 'backend', 'error.log'), 'a', encoding='utf-8') as fh:
            fh.write(f"[{datetime.now().isoformat()}] Error in /api/audit:\n{tb}\n")
        print(f"Error in /api/audit: {str(e)}")
        return jsonify({'error': 'Internal server error. See backend/error.log for details.'}), 500

@app.route('/api/audit/<audit_id>', methods=['GET'])
def get_audit(audit_id):
    """Retrieve a specific audit report"""
    if audit_id in audit_history:
        return jsonify(audit_history[audit_id]), 200
    return jsonify({'error': 'Audit not found'}), 404

@app.route('/api/audit-history', methods=['GET'])
def get_audit_history():
    """Get list of all audits performed"""
    audits = []
    for audit_id, report in audit_history.items():
        audits.append({
            'audit_id': audit_id,
            'url': report['url'],
            'timestamp': report['timestamp'],
            'seo_score': report['seo_score'],
            'pages_audited': report['crawl_summary']['total_pages'],
            'issues_count': len(report.get('issues', []))
        })
    return jsonify(audits), 200

@app.route('/api/quick-check', methods=['POST'])
def quick_check():
    """Quick SEO check for a single page"""
    try:
        data = request.get_json() or {}
        url = data.get('url')

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Quick analysis without full crawl
        page_data = crawler.crawl_single_page(url)
        analysis = analyzer.analyze_single_page(page_data)

        return jsonify({
            'url': url,
            'score': analysis.get('score', 0),
            'issues': analysis.get('issues', []),
            'timestamp': datetime.now().isoformat()
        }), 200

    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        with open(os.path.join(project_root, 'backend', 'error.log'), 'a', encoding='utf-8') as fh:
            fh.write(f"[{datetime.now().isoformat()}] Error in /api/quick-check:\n{tb}\n")
        print(f"Error in /api/quick-check: {str(e)}")
        return jsonify({'error': 'Internal server error. See backend/error.log for details.'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
