from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('http://www.sookmyung.ac.kr/sookmyungkr/index.do')
soup = BeautifulSoup(response, 'html.parser')
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 에서 CSS selectors 참고
for anchor in soup.select("#section_04"):
    print(anchor.get_text())
