from bs4 import BeautifulSoup # 라이브러리를 불러온다
from urllib.request import urlopen


# 아래줄 코드는 다음과 같다. response = urlopen('url')
with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response: # 해당 주소를 가져와 response에 담는다.
    soup = BeautifulSoup(response, 'html.parser') # response를 'html.parser'를 이용해 분석한 다음 soup에 담는다.
    for anchor in soup.find_all('a'): # soup 중에 모든 a태그들 -> for문을 이용해 하나씩 (주소를) 출력한다
        print(anchor.get('href', '/'))
        
