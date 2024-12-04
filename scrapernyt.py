import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List
from abc import ABC, abstractmethod

@dataclass
class Content:
    url: str
    title: str 
    body: str

class WebScraper(ABC):
    def get_page(self, url: str) -> BeautifulSoup:
        """Get BeautifulSoup object for a URL"""
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    
    @abstractmethod
    def scrape(self, url: str) -> Content:
        """Scrape content from a URL"""
        pass

class NYTimesScraper(WebScraper):
    def scrape(self, url: str) -> Content:
        bs = self.get_page(url)
        title = bs.find("h1").text
        lines = bs.find_all("p", {"class": "story-content"})
        body = '\n'.join([line.text for line in lines])
        return Content(url, title, body)

class BrookingsScraper(WebScraper):
    def scrape(self, url: str) -> Content:
        bs = self.get_page(url)
        title = bs.find("h1").text
        body = bs.find("div", {"class": "post-body"}).text
        return Content(url, title, body)

def print_content(content: Content) -> None:
    """Print formatted content"""
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)

def main():
    # Scrape Brookings article
    brookings_url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
    brookings_scraper = BrookingsScraper()
    content = brookings_scraper.scrape(brookings_url)
    print_content(content)

    # Scrape NYTimes article  
    nytimes_url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
    nytimes_scraper = NYTimesScraper()
    content = nytimes_scraper.scrape(nytimes_url)
    print_content(content)

if __name__ == '__main__':
    main()