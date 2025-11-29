"""
Recommendation Engine
Generates prioritized recommendations and simulates ranking impact
"""

from typing import Dict, List
from datetime import datetime

class RecommendationEngine:
    def __init__(self):
        self.impact_factors = {
            'critical': {'ranking_impact': 15, 'priority': 1},
            'high': {'ranking_impact': 10, 'priority': 2},
            'medium': {'ranking_impact': 5, 'priority': 3},
            'low': {'ranking_impact': 2, 'priority': 4}
        }
    
    def generate_recommendations(self, analysis_results: Dict, auto_fix: bool = False) -> Dict:
        """
        Generate recommendations based on analysis
        
        Args:
            analysis_results: Results from SEO analyzer
            auto_fix: Whether to auto-implement fixes
            
        Returns:
            Dictionary with recommendations and simulated impact
        """
        issues = analysis_results.get('issues', [])
        recommendations = []
        total_potential_impact = 0
        
        # Group issues by type
        issue_groups = self._group_issues(issues)
        
        for issue_type, group_issues in issue_groups.items():
            severity = group_issues[0]['severity'] if group_issues else 'low'
            impact_data = self.impact_factors.get(severity, {})
            
            rec = {
                'id': f"rec_{len(recommendations) + 1}",
                'issue_type': issue_type,
                'severity': severity,
                'affected_pages': len(set(i['page'] for i in group_issues)),
                'title': group_issues[0].get('title', ''),
                'description': group_issues[0].get('description', ''),
                'fix_priority': impact_data.get('priority', 5),
                'estimated_ranking_impact': f"+{impact_data.get('ranking_impact', 0)}%",
                'estimated_traffic_impact': f"+{impact_data.get('ranking_impact', 0) * 2}%",
                'implementation_difficulty': self._estimate_difficulty(issue_type),
                'time_to_fix_minutes': self._estimate_time(issue_type),
                'code_snippet': self._generate_code_snippet(issue_type),
                'auto_fixable': self._is_auto_fixable(issue_type),
                'status': 'fixed' if auto_fix and self._is_auto_fixable(issue_type) else 'pending'
            }
            
            recommendations.append(rec)
            total_potential_impact += impact_data.get('ranking_impact', 0)
        
        # Sort by priority
        recommendations.sort(key=lambda x: x['fix_priority'])
        
        # Simulate ranking impact
        current_score = analysis_results.get('overall_score', 0)
        simulated_impact = self._simulate_impact(
            current_score, 
            total_potential_impact,
            recommendations
        )
        
        return {
            'recommendations': recommendations,
            'total_recommendations': len(recommendations),
            'current_score': current_score,
            'potential_score_increase': total_potential_impact,
            'simulated_impact': simulated_impact,
            'auto_fixed_count': sum(1 for r in recommendations if r['status'] == 'fixed'),
            'timestamp': datetime.now().isoformat()
        }
    
    def _group_issues(self, issues: List[Dict]) -> Dict[str, List[Dict]]:
        """Group issues by type"""
        grouped = {}
        for issue in issues:
            issue_type = issue.get('type', 'unknown')
            if issue_type not in grouped:
                grouped[issue_type] = []
            grouped[issue_type].append(issue)
        return grouped
    
    def _estimate_difficulty(self, issue_type: str) -> str:
        """Estimate implementation difficulty"""
        easy_fixes = [
            'missing_title',
            'missing_meta_description',
            'missing_h1',
            'missing_alt_text',
            'missing_canonical',
            'missing_viewport',
            'missing_schema'
        ]
        
        if issue_type in easy_fixes:
            return 'Easy'
        elif issue_type in ['short_title', 'long_title', 'thin_content']:
            return 'Easy'
        elif issue_type in ['broken_links', 'multiple_h1']:
            return 'Medium'
        else:
            return 'Hard'
    
    def _estimate_time(self, issue_type: str) -> int:
        """Estimate time to fix in minutes"""
        time_estimates = {
            'missing_title': 5,
            'missing_meta_description': 5,
            'short_title': 10,
            'long_title': 10,
            'missing_h1': 15,
            'multiple_h1': 20,
            'missing_alt_text': 30,
            'missing_canonical': 10,
            'missing_viewport': 5,
            'missing_schema': 45,
            'broken_links': 60,
            'large_page_size': 120,
            'thin_content': 60
        }
        return time_estimates.get(issue_type, 30)
    
    def _is_auto_fixable(self, issue_type: str) -> bool:
        """Check if issue can be auto-fixed"""
        auto_fixable = [
            'missing_title',
            'missing_meta_description',
            'missing_canonical',
            'missing_viewport',
            'missing_h1'
        ]
        return issue_type in auto_fixable
    
    def _generate_code_snippet(self, issue_type: str) -> str:
        """Generate code snippet for fixing the issue"""
        snippets = {
            'missing_title': '<title>Your Page Title - Your Brand</title>',
            'missing_meta_description': '<meta name="description" content="Your 150-160 character description here">',
            'missing_canonical': '<link rel="canonical" href="https://example.com/page">',
            'missing_viewport': '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            'missing_h1': '<h1>Your Main Heading</h1>',
            'missing_schema': '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Your Organization",
  "url": "https://example.com"
}
</script>''',
            'missing_alt_text': '<img src="image.jpg" alt="Descriptive alt text">',
        }
        return snippets.get(issue_type, '<!-- Code snippet not available -->')
    
    def _simulate_impact(self, current_score: float, potential_impact: float, 
                        recommendations: List[Dict]) -> Dict:
        """Simulate the impact on ranking"""
        
        # Conservative estimate: 70% of potential impact if all fixes applied
        estimated_new_score = min(100, current_score + (potential_impact * 0.7))
        estimated_traffic_lift = (estimated_new_score - current_score) * 2.5  # 2.5% traffic per 1% score
        
        # Estimate keyword ranking improvements
        critical_recs = [r for r in recommendations if r['severity'] == 'critical']
        high_recs = [r for r in recommendations if r['severity'] == 'high']
        
        return {
            'current_score': round(current_score, 2),
            'estimated_score_after_fixes': round(estimated_new_score, 2),
            'score_improvement': round(estimated_new_score - current_score, 2),
            'estimated_traffic_improvement_percent': round(estimated_traffic_lift, 2),
            'estimated_keyword_ranking_improvement': f"+{len(critical_recs) * 3 + len(high_recs) * 1} positions",
            'confidence_level': 'High' if len(critical_recs) > 0 else 'Medium',
            'timeframe_to_see_results_days': 30 if len(critical_recs) > 0 else 60
        }
