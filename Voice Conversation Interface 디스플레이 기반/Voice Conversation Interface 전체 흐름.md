**기본 논리**
\1. 오디오 파일을 컴퓨터 환경에서 최적화 한 후
\2. 오디오 파일을 구글 클라우드 스토리지에 올려서
\3. **구글 클라우드 STT 플랫폼을 통해 텍스트로 변환한 후**
\4. **로컬에서 텍스트를 받아 저장하여 작업한다.**

​    

# 프로젝트 흐름

#

음성 인식

구글 서버를 통해 인식된 결과를 transcript + overwrite_chars 변수에 받는다.

음성-> 텍스트로 변환된 데이터 획득  <EX> ''혁신''  ("혁신의 용광로" X)  - 책 전체이름은 하지 못했다. '의'와 같은 조사를 빼는 것은 쉽지만 단어가 2개 이상일 경우 좀 복잡해지기 때문에 일단 **단어 하나만** 음성 데이터를 입력했다,

#

''혁신''

```python
    df_meta = pd.read_csv("movie_natlang.csv")
    
    db = df_meta[["title", "natlang"]]
```

파일을 열어서 (읽어서), [title]과 [natlang] 원하는 칼럼 가져오기 (두 칼럼은 csv파일에 실제 존재)

```python
def national(book_title): # book_title = '혁신'
    
    df_meta = pd.read_csv("library_db.csv")
    
    db = df_meta[["title", "location"]]
    
    if db['title'] == book_title: # book_title = '혁신'
        return @@@ # 해당 행의 location 리턴
```

[title]  [location] 두 칼럼 가져오기

*title 칼럼에 있는 모든 책을 <단어 하나로> 정제했다. =개발에 활용할 수 있는 데이터로 만든셈 (=csv파일을 정제했다)

해당 함수에서 파일을 열어, 해당 책에 상응되는 위치를 리턴했다.



#

위 함수호출로 인해 리턴된 위치  <EX> C열2번 (텍스트)

위 텍스트를 TTS화 시킨다.

---

