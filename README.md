from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지 경로 설정
@app.route('/')
def home():
    return render_template('index.html')

# 추가 페이지 예시 (소개 페이지)
@app.route('/about')
def about():
    return "<h2>이곳은 소개 페이지입니다!</h2>"

if __name__ == '__main__':
    # debug=True는 수정사항을 바로 반영해주는 개발 모드입니다.
    app.run(debug=True)
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>시범용 웹사이트</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        .container { border: 2px solid #ddd; padding: 20px; display: inline-block; border-radius: 10px; }
        button { padding: 10px 20px; cursor: pointer; background-color: #007bff; color: white; border: none; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Flask 시범용 사이트에 오신 것을 환영합니다!</h1>
        <p>파이썬으로 만든 아주 간단한 웹 서버입니다.</p>
        <button onclick="alert('반가워요!')">클릭해보세요</button>
        <br><br>
        <a href="/about">소개 페이지로 이동</a>
    </div>
</body>
</html>
