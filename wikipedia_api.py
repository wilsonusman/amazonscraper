from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import random
import datetime

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

# for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


random.seed(datetime.datetime.now().timestamp())

# def get_links(article_url: str) -> list[BeautifulSoup]:
#     """
#     Get all valid wiki links from a Wikipedia article
    
#     Args:
#         article_url: The URL path of the Wikipedia article
        
#     Returns:
#         List of anchor tags containing valid wiki links
        
#     Raises:
#         URLError: If the Wikipedia page cannot be accessed
#         AttributeError: If the page structure is invalid
#     """
#     url = f'http://en.wikipedia.org{article_url}'
#     try:
#         html = urlopen(url)
#         soup = BeautifulSoup(html, 'html.parser')
#         return soup.find('div', {'id': 'bodyContent'}).find_all(
#             'a', 
#             href=re.compile('^(/wiki/)((?!:).)*$')
#         )
#     except (URLError, AttributeError) as e:
#         print(f"Error accessing {url}: {str(e)}")
#         return []

# def crawl_wiki(start_url: str, max_pages: int = 100) -> None:
#     """
#     Crawl Wikipedia articles starting from a given URL
    
#     Args:
#         start_url: The starting Wikipedia article URL path
#         max_pages: Maximum number of pages to visit (default 10)
#     """
#     visited_pages = set()
#     pages_visited = 0
#     current_url = start_url
    
#     while pages_visited < max_pages:
#         # Skip if we've already visited this page
#         if current_url in visited_pages:
#             # Get a new random URL from our previously visited pages
#             if visited_pages:
#                 links = []
#                 for visited_url in visited_pages:
#                     links.extend(get_links(visited_url))
#                 if links:
#                     current_url = random.choice(links).attrs['href']
#                     continue
#             break
            
#         visited_pages.add(current_url)
#         print(f"Visiting: {current_url}")
        
#         links = get_links(current_url)
#         if not links:
#             break
            
#         # Filter out links we've already visited
#         new_links = [link for link in links if link.attrs['href'] not in visited_pages]
#         if not new_links:
#             break
            
#         current_url = random.choice(new_links).attrs['href']
#         pages_visited += 1

# # Start crawling from Kevin Bacon's page
# crawl_wiki('/wiki/')

def crawl_wikipedia(start_url: str = '', visited_pages: set = None) -> None:
    """
    Recursively crawl Wikipedia pages starting from a given URL.
    
    Args:
        start_url: The starting Wikipedia article URL path
        visited_pages: Set of already visited pages
    """
    if visited_pages is None:
        visited_pages = set()
        
    try:
        html = urlopen(f'http://en.wikipedia.org{start_url}')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract and print page info
        try:
            print(soup.h1.get_text())
            print(soup.find(id='mw-content-text').find_all('p')[0])
            edit_link = soup.find(id='ca-edit').find('span').find('a')['href']
            print(edit_link)
        except AttributeError:
            print('Page is missing expected elements. Continuing...')
            
        # Find and process links
        for link in soup.find_all('a', href=re.compile('^(/wiki/)')):
            if 'href' not in link.attrs:
                continue
                
            new_url = link['href']
            if new_url not in visited_pages:
                print('-' * 20)
                print(new_url)
                visited_pages.add(new_url)
                crawl_wikipedia(new_url, visited_pages)
                
    except Exception as e:
        print(f'Error crawling {start_url}: {str(e)}')

if __name__ == '__main__':
    crawl_wikipedia()