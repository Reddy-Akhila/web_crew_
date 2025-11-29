"""
Web Crawler Engine
Crawls websites, extracts meta data, checks links, and measures performance
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
from datetime import datetime
from typing import Dict, List, Set
import re
import validators

class WebCrawler:
    def __init__(self, timeout=5, max_pages=10, allow_external=True):
        self.timeout = timeout
        self.max_pages = max_pages
        self.allow_external = allow_external
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.visited_urls = set()
        self.broken_links = []
        
    def _normalize_url(self, url: str) -> str:
        """Ensure URL has a scheme and is normalized (strip fragments)."""
        if not url:
            return url
        url = url.strip()
        # add scheme if missing
        try:
            parsed = urlparse(url)
            if not parsed.scheme:
                url = 'http://' + url
        except Exception:
            pass
        # strip fragment
        if '#' in url:
            url = url.split('#', 1)[0]
        return url

    def crawl(self, start_url: str, depth: int = 2) -> Dict:
        """
        Crawl a website up to specified depth
        
        Args:
            start_url: Starting URL
            depth: Crawl depth (number of levels)
            
        Returns:
            Dictionary with crawl results
        """
        print(f"Starting crawl: {start_url}")
        start_time = time.time()
        
        self.visited_urls = set()
        self.broken_links = []
        pages = []
        
        start_url = self._normalize_url(start_url)
        self._crawl_recursive(start_url, depth, 0, pages)
        
        crawl_time = time.time() - start_time
        
        return {
            'start_url': start_url,
            'pages': pages,
            'broken_links': self.broken_links,
            'crawl_time': crawl_time,
            'total_pages': len(pages),
            'timestamp': datetime.now().isoformat()
        }
    
    def _crawl_recursive(self, url: str, max_depth: int, current_depth: int, pages: List):
        """Recursively crawl URLs"""
        
        # Stop conditions
        if current_depth > max_depth or len(pages) >= self.max_pages or url in self.visited_urls:
            return
            
        url = self._normalize_url(url)
        if not self._is_valid_url(url):
            return
            
        self.visited_urls.add(url)
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            page_data = self._extract_page_data(url, response)
            pages.append(page_data)
            
            print(f"[{len(pages)}] Crawled: {url}")
            
            # Extract and crawl child links if not at max depth
            if current_depth < max_depth and len(pages) < self.max_pages:
                try:
                    soup = BeautifulSoup(response.content.decode('utf-8', errors='ignore'), 'html.parser')
                    for link in soup.find_all('a', href=True):
                        if len(pages) >= self.max_pages:
                            break
                        child_url = urljoin(url, link['href'])
                        child_url = self._normalize_url(child_url)

                        # Only crawl if valid URL and either external allowed or same domain
                        if not self._is_valid_url(child_url):
                            continue
                        if not self.allow_external and not self._is_same_domain(url, child_url):
                            continue
                        self._crawl_recursive(child_url, max_depth, current_depth + 1, pages)
                except Exception as parse_error:
                    print(f"Error parsing links from {url}: {str(parse_error)}")
                        
        except requests.RequestException as e:
            print(f"Error crawling {url}: {str(e)}")
            self.broken_links.append({'url': url, 'reason': str(e)})
    
    def crawl_single_page(self, url: str) -> Dict:
        """Crawl and analyze a single page"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return self._extract_page_data(url, response)
        except Exception as e:
            return {'url': url, 'error': str(e)}
    
    def _extract_page_data(self, url: str, response) -> Dict:
        """Extract relevant SEO data from a page"""
        try:
            soup = BeautifulSoup(response.content.decode('utf-8', errors='ignore'), 'html.parser')
        except:
            soup = BeautifulSoup(response.text, 'html.parser')
        
        # Basic metrics
        title = soup.find('title')
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_robots = soup.find('meta', attrs={'name': 'robots'})
        canonical = soup.find('link', attrs={'rel': 'canonical'})
        
        # Content analysis
        h1_tags = soup.find_all('h1')
        h2_tags = soup.find_all('h2')
        images = soup.find_all('img')
        links = soup.find_all('a', href=True)
        
        # Performance metrics (basic)
        load_time = len(response.content) / 1000  # Approximate in KB
        
        # Schema markup
        schema_tags = soup.find_all('script', attrs={'type': 'application/ld+json'})
        
        # Extract broken links (skip remote link checking to avoid timeouts)
        internal_broken = []
        
        page_data = {
            'url': url,
            'title': title.text if title else None,
            'title_length': len(title.text) if title else 0,
            'meta_description': meta_description.get('content') if meta_description else None,
            'meta_description_length': len(meta_description.get('content', '')) if meta_description else 0,
            'has_canonical': canonical is not None,
            'h1_count': len(h1_tags),
            'h1_texts': [h.text for h in h1_tags],
            'h2_count': len(h2_tags),
            'image_count': len(images),
            'images_without_alt': sum(1 for img in images if not img.get('alt')),
            'internal_links': len([l for l in links if self._is_internal_link(url, l.get('href', ''))]),
            'external_links': len([l for l in links if not self._is_internal_link(url, l.get('href', ''))]),
            'broken_links': internal_broken,
            'has_schema_markup': len(schema_tags) > 0,
            'robots_directive': meta_robots.get('content') if meta_robots else 'index, follow',
            'page_size_kb': load_time,
            'word_count': len(soup.get_text().split()),
            'mobile_viewport': soup.find('meta', attrs={'name': 'viewport'}) is not None,
            'crawl_timestamp': datetime.now().isoformat()
        }
        
        return page_data
    
    def _is_valid_url(self, url: str) -> bool:
        """Check if URL is valid"""
        return validators.url(url) is True
    
    def _is_same_domain(self, url1: str, url2: str) -> bool:
        """Check if two URLs belong to the same domain"""
        domain1 = urlparse(url1).netloc
        domain2 = urlparse(url2).netloc
        return domain1 == domain2
    
    def _is_internal_link(self, page_url: str, link_url: str) -> bool:
        """Check if link is internal"""
        if not link_url or link_url.startswith('#'):
            return False
        
        full_url = urljoin(page_url, link_url)
        return self._is_same_domain(page_url, full_url)
