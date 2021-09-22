# natural_processing.py 분석

​    

## 1. 가져오기

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #가중치 부여
from sklearn.metrics.pairwise import linear_kernel
```

#### * 단어 카운트 가중치

가중치 부여 문서 벡터화
: TF-IDF (Term Frequency - Inverse Document Frequency, 단어 빈도-역문서 빈도)
단어 꾸러미 (BOW(Bag of Words)) 인코딩 벡터에서
여러 문서에서 사용된 단어의 특성에 대해 문서 구별 능력이 떨어진다고 보아 낮은 가중치를 곱해 중요도를 떨어 뜨리기

```
TF-IDF = TF * IDF = TF * (1/DF) ==> TF * math.log(문서수/(DF+1)

TF(단어 빈도, term frequency): 특정 단어가 특정 문서에 얼마나 나오냐
DF(문서 빈도, document frequency): 특정 단어가 얼마나 많은 문서에 나오냐
IDF(역문서 빈도, inverse document frequency): 특정 단어가 많은 문서에 나오면 낮은 값 가지기
math.log는 밑을 자연 상수 e(e=2.718281...)를 사용하는 자연 로그
```

#### * 단어 카운트 가중치 (TfidfVectorizer)

가중치 부여

sklearn.feature_extraction.text.TfidfVectorizer

```python
class sklearn.feature_extraction.text.TfidfVectorizer(input=’content’, encoding=’utf-8’, decode_error=’strict’, strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None, analyzer=’word’, stop_words=None, token_pattern=’(?u)\b\w\w+\b’, ngram_range=(1, 1), max_df=1.0, min_df=1, max_features=None, vocabulary=None, binary=False, dtype=<class ‘numpy.int64’>, norm=’l2’, use_idf=True, smooth_idf=True, sublinear_tf=False)
```

###### 사용 예

```python
from sklearn.feature_extraction.text import TfidfVectorizer 

text = ['I go to my home my home is very large', 
        'I went out my home I go to the market', 
        'I bought a yellow lemon I go back to home'] 

tfidf_vectorizer = TfidfVectorizer()
```



---

## 2. 

```python
def national(movie_name):

    df_meta = pd.read_csv("movie_natlang.csv")

    db = df_meta[["title", "natlang"]] # 제목, 줄거리

   
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(db['natlang'])
    .
    .
```

판다스 라이브러리를 이용해 movie_natlang.csv 파일을 읽어온다.

movie_natlang.csv 파일에서의 칼럼 **title**, **natlang** 두 열을 가져와 db에 넣는다.







정렬 잘 알아보기
