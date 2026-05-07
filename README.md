# brigit9124.github.io
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Simple Website</title>
    <style>
        /* CSS 스타일링 */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f9;
        }

        header {
            background: #2c3e50;
            color: #fff;
            padding: 2rem 1rem;
            text-align: center;
        }

        nav {
            display: flex;
            justify-content: center;
            background: #34495e;
        }

        nav a {
            color: white;
            padding: 1rem;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 14px;
        }

        nav a:hover {
            background: #1abc9c;
        }

        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 2rem;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        section {
            padding: 2rem 0;
            border-bottom: 1px solid #eee;
        }

        section:last-child {
            border-bottom: none;
        }

        h2 {
            color: #2c3e50;
        }

        footer {
            text-align: center;
            padding: 2rem;
            font-size: 0.9rem;
            color: #777;
        }

        .btn {
            display: inline-block;
            background: #1abc9c;
            color: white;
            padding: 0.7rem 1.5rem;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 1rem;
        }

        .btn:hover {
            background: #16a085;
        }
    </style>
</head>
<body>

    <header>
        <h1>안녕하세요, 반갑습니다! 👋</h1>
        <p>저의 첫 번째 웹사이트에 오신 것을 환영합니다.</p>
    </header>

    <nav>
        <a href="#about">소개</a>
        <a href="#projects">프로젝트</a>
        <a href="#contact">연락처</a>
    </nav>

    <div class="container">
        <section id="about">
            <h2>자기소개</h2>
            <p>이곳은 자신을 소개하는 공간입니다. 현재 이 사이트는 HTML과 CSS만으로 구성되어 있어 매우 가볍고 빠릅니다.</p>
        </section>

        <section id="projects">
            <h2>주요 프로젝트</h2>
            <ul>
                <li><strong>프로젝트 A:</strong> 간단한 웹 게임 만들기</li>
                <li><strong>프로젝트 B:</strong> To-Do List 애플리케이션</li>
                <li><strong>프로젝트 C:</strong> 개인 블로그 테마 제작</li>
            </ul>
        </section>

        <section id="contact">
            <h2>연락처</h2>
            <p>궁금한 점이 있다면 아래 버튼을 눌러 메일을 보내주세요.</p>
            <a href="mailto:example@email.com" class="btn">이메일 보내기</a>
        </section>
    </div>

    <footer>
        <p>&copy; 2026 My Simple Website. All rights reserved.</p>
    </footer>

</body>
</html>
