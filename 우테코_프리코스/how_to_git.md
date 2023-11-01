### 1. 프로젝트를 자신의 계정으로 fork한 후 local로 clone 하기

```
git clone https://github.com/{본인_아이디}/{저장소 아이디}.git
git clone https://github.com/ChiwooKim/java-baseball.git

// clone한 폴더로 이동하는 방법
cd {저장소 아이디}
ex) cd java-baseball
```

### 2. 브랜치 생성과 전환

```
git branch {생성할 브랜치 이름}
git checkout {전환할 브랜치 이름}
git checkout -b {생성 후 전환할 브랜치 이름}

//프리코스에서는 아래와 같은 규칙으로 사용
git checkout -b {본인 아이디}
ex) git checkout -b ChiwooKim
```

### 3. add & commit & push

```
// 변경된 파일 확인
git status

// 변경된 전체 파일을 스테이징
git add . // 한번에 반영
git add {파일명}

// 스테이징된 파일 모두 커밋하기
git commit -m "메시지"

// 본인 원격 저장소에 올리기
git push origin {브랜치 이름}
ex) git push origin ChiwooKim
```

### 4. add 취소

```
// add한 파일 Unstaged 상태로 되돌리기
git reset {파일명}
git reset // 전체 파일

// 커밋되지 않은 모든 로컬 변경 사항을 되돌리기(단, repository의 root에서 실행이 되어야 한다.)
git checkout .

// 커밋되지 않은 변경 사항을 특정 파일이나 디렉터리로만 되돌리기
git checkout [some_dir|file.txt]
```

### 5. commit 취소

```
HEAD: git에서 현재 체크아웃한 브랜치나 커밋을 가리키는 포인터 역할

// commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉터리에 보존
git reset --soft HEAD^

// commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에 보존
git reset --mixed HEAD^ // 기본 옵션
git reset HEAD^ // 위와 동일
git reset HEAD~2 // 마지막 2개의 commit을 취소

// commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에서 삭제
git reset --hard HEAD^
```

- reset 옵션
  – soft : index 보존(add한 상태, staged 상태), 워킹 디렉터리의 파일 보존. 즉 모두 보존.
  – mixed : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 보존 (기본 옵션)
  – hard : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 삭제. 즉 모두 취소.

### 6. 가장 마지막에 commit 한 내용 수정

```
git commit --amend

commit을 수정을 완료한 후 esc -> :wq (저장 후 닫기)
```

### 7. commit 로그와 수정된 파일 함께 보기

```
git log


q를 눌러 나가기
```

### 8. 특정 파일만 commit & push

```
// 작업한 파일 목록 확인하기
git status

// 기존파일의 변경내역 확인하기
git diff

// 원하는 파일 추가하기
git add <경로 및 file명> <경로 및 file명> <경로 및 file명> ...

// 특정 파일 Commit하기
git commit -m "커밋 메세지" {파일명}

// 위의 두 개 한꺼번에 하기
git commit -am "커밋 메세지" {파일명}

// 특정 파일 unstaged 상태 만들기
git restore --staged {파일명}
```
