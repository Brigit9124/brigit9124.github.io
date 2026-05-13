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
