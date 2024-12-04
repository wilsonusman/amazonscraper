from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html, 'html.parser')

# nameList = bs.findAll('span', {'class':'green'}, recursive=False)
# for name in nameList:
#     print(name.get_text())


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)


# for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
#     print(sibling)

# print(bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

images = bs.find_all('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])