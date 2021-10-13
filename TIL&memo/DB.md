# Data base

## Django Project Setting

1.  django 프로젝트에서 가상 환경 적용
2.  pip install로 필요한 것들 설치(패키지 설치)
3.  migrate 진행
   - python manage.py  migrate
   - python manage.py sqlmigrate users 0001
4.  db.sqlite3 실행 
   - sqlite3 db.sqlite3



- django shell plust 실행 : python manage.py shell_plus



## sqlite 명령어(키워드를 대문자 쓰는 이유는 가독성 때문!)

- .tables : table 확인
- csv 파일 데이터 베이스에 적용
  - .mode csv
  - .import (파일이름.csv) (table이름)
    - ex) .import users.csv users_user
- schema 확인
  - .schema (table 이름)
- .headers on
- shell 정리 및 종료
  - sqlite : .shell clear(=.shell cls,정리), .exit(종료)
  - django shell plus : clear(= ctrl + l), exit 



## CRUD

- 모든 user 레코드 조회
  - ORM : User.objects.all()
  - SQL : SELECT * FROM users_user;
- user 레코드 생성
  - ORM : User.objects.create(first_name='길동', last_name='홍', age=100, country='제주도',phone='010-1234-5678', balance=10000)
  - SQL : INSERT INTO FROM users_user VALUES(~)

- 특정 레코드 수정
  - ORM :
    - user = User.objects.get(pk=102)
    - user.last_name = '김'
    - user.save()
    - user.last_name 
  - SQL : 
    - UPDATE user_user SET last_name='김' WHERE id=102; (변경)
    - SELECT * FROM users_user WHERE id=102;                     (조회)
- 특정 레코드 삭제
  - ORM : User.objects.get(pk=102).delete()
  - SQL : 
    - DELETE FROM users_user WHERE id=102;
    - SELECT * FROM users_user WHERE id=102;























