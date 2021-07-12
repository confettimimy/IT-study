# TF-IDF 구현하기

TF-IDF = Term Frequency-Inverse Document Frequency

(이게 무엇인가, 공식에 대해서는 1에서 이미 설명)

​    

​    

## 1. 파이썬으로 TF-IDF 직접 구현하기

```python
import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해
```

```python
docs = [
  '먹고 싶은 사과',
  '먹고 싶은 바나나',
  '길고 노란 바나나 바나나',
  '저는 과일이 좋아요'
] 
vocab = list(set(w for doc in docs for w in doc.split()))
vocab.sort()
```

​    

#### TF, IDF, 그리고 TF-IDF 값을 구하는 함수를 구현

```python
N = len(docs) # 총 문서의 수

def tf(t, d):
    return d.count(t)

def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df + 1))

def tfidf(t, d):
    return tf(t,d)* idf(t)
```

. . . (이하 생략)

​     

---

## 2. 사이킷런을 이용한 TF-IDF 실습

**사이킷런(sklearn)은 TF-IDF를 자동 계산해주는 TfidfVectorizer를 제공합니다.**

사이킷런의 TF-IDF는 위 파이썬으로 직접 구현한 보편적인 TF-IDF 식에서 좀 더 조정된 다른 식을 사용합니다. 하지만 크게 다른 식은 아니며(IDF의 로그항의 분자에 1을 더해주며, 로그항에 1을 더해주고, TF-IDF에 L2 정규화라는 방법으로 값을 조정하는 등의 차이), 여전히 TF-IDF가 가진 의도를 그대로 갖고 있으므로 사이킷런의 TF-IDF를 그대로 사용하셔도 좋습니다.

-> 이 방식 채택✅

```python
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'you know I want your love',
    'I like you',
    'what should I do ',    
]
tfidfv = TfidfVectorizer().fit(corpus)

print(tfidfv.transform(corpus).toarray())
print(tfidfv.vocabulary_)
```

```python
[[0.         0.46735098 0.         0.46735098 0.         0.46735098 0.         0.35543247 0.46735098]
 [0.         0.         0.79596054 0.         0.         0.         0.         0.60534851 0.        ]
 [0.57735027 0.         0.         0.         0.57735027 0.         0.57735027 0.         0.        ]]
{'you': 7, 'know': 1, 'want': 5, 'your': 8, 'love': 3, 'like': 2, 'what': 6, 'should': 4, 'do': 0}
```

​     

---

[출처](https://wikidocs.net/31698)