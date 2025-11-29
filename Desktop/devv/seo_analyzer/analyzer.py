"""
SEO Analyzer - AI-Based Scoring System
Analyzes pages for technical SEO issues and assigns quality scores
"""

from typing import Dict, List
from datetime import datetime

class SEOAnalyzer:
    def __init__(self):
        self.issue_weights = {
            'critical': 50,
            'high': 30,
            'medium': 15,
            'low': 5
        }
    
    def analyze_pages(self, crawl_results: Dict) -> Dict:
        """
        Analyze all crawled pages and generate SEO issues
        
        Args:
            crawl_results: Results from web crawler
            
        Returns:
            Dictionary with analysis results and overall score
        """
        all_issues = []
        page_scores = []
        
        for page in crawl_results['pages']:
            page_analysis = self.analyze_single_page(page)
            all_issues.extend(page_analysis.get('issues', []))
            page_scores.append(page_analysis.get('score', 0))
        
        # Calculate overall score
        overall_score = sum(page_scores) / len(page_scores) if page_scores else 0
        
        # Count issues by severity
        issue_counts = {
            'critical': len([i for i in all_issues if i['severity'] == 'critical']),
            'high': len([i for i in all_issues if i['severity'] == 'high']),
            'medium': len([i for i in all_issues if i['severity'] == 'medium']),
            'low': len([i for i in all_issues if i['severity'] == 'low'])
        }
        
        return {
            'overall_score': round(overall_score, 2),
            'page_count': len(crawl_results['pages']),
            'issues': all_issues,
            'issue_summary': issue_counts,
            'timestamp': datetime.now().isoformat()
        }
    
    def analyze_single_page(self, page_data: Dict) -> Dict:
        """Analyze a single page for SEO issues"""
        issues = []
        score = 100
        
        # Title optimization (10 points)
        title = page_data.get('title')
        title_length = page_data.get('title_length', 0)
        
        if not title:
            issues.append({
                'type': 'missing_title',
                'title': 'Missing Page Title',
                'description': 'Page title tag is missing',
                'severity': 'critical',
                'page': page_data.get('url')
            })
            score -= 10
        elif title_length < 30:
            issues.append({
                'type': 'short_title',
                'title': 'Title Too Short',
                'description': f'Title is {title_length} characters. Recommended: 50-60 characters',
                'severity': 'medium',
                'page': page_data.get('url')
            })
            score -= 3
        elif title_length > 60:
            issues.append({
                'type': 'long_title',
                'title': 'Title Too Long',
                'description': f'Title is {title_length} characters. Recommended: 50-60 characters',
                'severity': 'low',
                'page': page_data.get('url')
            })
            score -= 2
        
        # Meta description (10 points)
        meta_desc = page_data.get('meta_description')
        meta_desc_length = page_data.get('meta_description_length', 0)
        
        if not meta_desc:
            issues.append({
                'type': 'missing_meta_description',
                'title': 'Missing Meta Description',
                'description': 'Page meta description is missing',
                'severity': 'high',
                'page': page_data.get('url')
            })
            score -= 10
        elif meta_desc_length < 120:
            issues.append({
                'type': 'short_meta_description',
                'title': 'Meta Description Too Short',
                'description': f'Meta description is {meta_desc_length} characters. Recommended: 150-160 characters',
                'severity': 'medium',
                'page': page_data.get('url')
            })
            score -= 4
        elif meta_desc_length > 160:
            issues.append({
                'type': 'long_meta_description',
                'title': 'Meta Description Too Long',
                'description': f'Meta description is {meta_desc_length} characters. Recommended: 150-160 characters',
                'severity': 'low',
                'page': page_data.get('url')
            })
            score -= 2
        
        # H1 Tags (8 points)
        h1_count = page_data.get('h1_count', 0)
        
        if h1_count == 0:
            issues.append({
                'type': 'missing_h1',
                'title': 'Missing H1 Tag',
                'description': 'Page should have exactly one H1 tag',
                'severity': 'high',
                'page': page_data.get('url')
            })
            score -= 8
        elif h1_count > 1:
            issues.append({
                'type': 'multiple_h1',
                'title': 'Multiple H1 Tags',
                'description': f'Page has {h1_count} H1 tags. Should have only one',
                'severity': 'medium',
                'page': page_data.get('url')
            })
            score -= 4
        
        # Image optimization (8 points)
        images_without_alt = page_data.get('images_without_alt', 0)
        image_count = page_data.get('image_count', 0)
        
        if image_count > 0 and images_without_alt > 0:
            alt_percentage = (images_without_alt / image_count) * 100
            issues.append({
                'type': 'missing_alt_text',
                'title': 'Missing Image Alt Text',
                'description': f'{images_without_alt} of {image_count} images ({alt_percentage:.0f}%) are missing alt text',
                'severity': 'medium' if alt_percentage > 50 else 'low',
                'page': page_data.get('url')
            })
            score -= (4 if alt_percentage > 50 else 2)
        
        # Canonical Tag (7 points)
        if not page_data.get('has_canonical'):
            issues.append({
                'type': 'missing_canonical',
                'title': 'Missing Canonical Tag',
                'description': 'Page should have a canonical tag to prevent duplicate content',
                'severity': 'medium',
                'page': page_data.get('url')
            })
            score -= 3
        
        # Mobile Viewport (8 points)
        if not page_data.get('mobile_viewport'):
            issues.append({
                'type': 'missing_viewport',
                'title': 'Missing Mobile Viewport Meta Tag',
                'description': 'Page is not optimized for mobile devices',
                'severity': 'critical',
                'page': page_data.get('url')
            })
            score -= 8
        
        # Schema Markup (7 points)
        if not page_data.get('has_schema_markup'):
            issues.append({
                'type': 'missing_schema',
                'title': 'Missing Schema Markup',
                'description': 'Page would benefit from structured data (Schema.org)',
                'severity': 'low',
                'page': page_data.get('url')
            })
            score -= 2
        
        # Broken Links (8 points)
        broken_links = page_data.get('broken_links', [])
        if broken_links:
            issues.append({
                'type': 'broken_links',
                'title': 'Broken Links Found',
                'description': f'Page contains {len(broken_links)} broken links',
                'severity': 'high',
                'page': page_data.get('url'),
                'links': broken_links[:5]  # Show first 5
            })
            score -= min(8, len(broken_links) * 2)
        
        # Page Size/Speed (7 points)
        page_size = page_data.get('page_size_kb', 0)
        if page_size > 2000:
            issues.append({
                'type': 'large_page_size',
                'title': 'Large Page Size',
                'description': f'Page is {page_size:.0f}KB. Should be < 2MB for optimal performance',
                'severity': 'low',
                'page': page_data.get('url')
            })
            score -= 3
        
        # Content Length (6 points)
        word_count = page_data.get('word_count', 0)
        if word_count < 300:
            issues.append({
                'type': 'thin_content',
                'title': 'Thin Content',
                'description': f'Page has {word_count} words. Minimum 300 words recommended',
                'severity': 'medium',
                'page': page_data.get('url')
            })
            score -= 4
        
        # Ensure score doesn't go below 0
        score = max(0, score)
        
        return {
            'url': page_data.get('url'),
            'score': score,
            'issues': issues
        }
