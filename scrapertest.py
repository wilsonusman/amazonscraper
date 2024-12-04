from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')    

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

def main():
    title = getTitle('http://www.pythonscraping.com/pages/page1.html')
    if title == None:
        print('Title could not be found')
    else:
        print(title)

if __name__ == '__main__':
    main()