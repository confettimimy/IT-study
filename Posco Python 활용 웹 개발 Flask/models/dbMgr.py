# 데이터베이스에 의존하는 유일한 파일

# 실제 Back End에서는 서버 Data Base와 연동되어, 데이터를 실시간으로 불러오고 저장하는 기능을 함.


import pandas as pd

df =  pd.read_csv('./../1_model_data (has_movie).csv')

print(df)
