# 2024-Herethon-1
2024 여기톤 : HERETHON 1조

- **서비스 소개**

  대법원과 각급법원의 조직은 법률로 정한다. 대통령·국무총리·국무위원·행정각부의 장·헌법재판소 재판관·법관·중앙선거관리위원회 위원·감사원장·감사위원 기타 법률이 정한 공무원이 그 직무집행에 있어서 헌법이나 법률을 위배한 때에는 국회는 탄핵의 소추를 의결할 수 있다. 국가원로자문회의의 의장은 직전대통령이 된다. 다만, 직전대통령이 없을 때에는 대통령이 지명한다.


- **기술 스택**

  <span>프론트엔드: </span> <img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

  <span>백엔드: </span><img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=Django&logoColor=white">

  <span>기획·디자인: </span> <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">

- **팀원 소개**<br/>
| 이름 | 소속 |
| --- | --- |
| 정성윤(개발자, FE) | 충남대학교 인공지능학과 | 
| 정원준(개발자, FE) | 남서울대학교 컴퓨터소프트웨어학과 | 
| 윤윤지(개발자, FE) | 덕성여자대학교 컴퓨터공학과 |  
| 박규리(개발자, BE) | 덕성여자대학교 컴퓨터공학과 | 
| 이예나(개발자, BE) | 숙명여자대학교 IT공학전공 |
| 이예령(개발자, BE) | 성신여자대학교 소프트웨어전공 |
| 임영우(기획 및 디자인) | 충남대학교 행정학부 |

- **폴더 구조**

  ```
  📂 2024-Herethon-1
   ├─ herethon2024
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py
   ├─ accountApp
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ decorators.py
   │  ├─ forms.py
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   ├─ mainApp
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   ├─ static
   │  ├─ css
   │  └─  img
   ├─ .env
   ├─ .gitignore
   ├─ db.sqlite3
   ├─ README.md
   ├─ requirements.txt
   └─ manage.py
  ```

- **개발환경에서의 실행 방법**
  ```
  $ python -m venv myvenv
  $ source myvenv/Scripts/activate
  $ pip install -r requirements.txt
  $ python manage.py runserver
  ```
  <hr/>
