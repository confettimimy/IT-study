# app.py
from flask import Flask, render_template

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
  return render_template('index.html',user="MiMi",data={'level':60,'point':360,'exp':45000})
'''<render_template에 매개변수 추가>
   - 첫번째 인자로는 html 파일명
   - 두번째부터는 보낼 데이터의 정보를 넣으면 된다.
'''

if __name__=="__main__":
  app.run(debug=True)
