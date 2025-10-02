# Flask 개발 환경 세팅

## 1. 가상 환경 생성
cmd에서 다음 명령어를 실행하세요:
```
python -m venv .venv
```

## 2. 가상 환경 활성화
Windows:
```
.venv\Scripts\activate
```

## 3. 의존성 설치
```
pip install -r requirements.txt
```

## 4. 애플리케이션 실행
```
python app.py
```
- Flask 서버가 시작되며, 동시에 Tailwind CSS watch (npm run watch:css)가 백그라운드에서 자동 실행됩니다.
- 변경 감지 시 CSS 자동 재빌드.
- **Windows 팁**: 'npm not found' 오류 시, Node.js PATH 확인 또는 app.py의 subprocess에 shell=True 설정 (이미 적용됨). PowerShell 사용 추천.
- 브라우저에서 http://127.0.0.1:5000/ 에 접속하세요.

## 5. 프로젝트 구조
- `templates/`: HTML 템플릿
- `src/input.css`: Tailwind 입력 파일
- `static/`: CSS, JS 등 정적 파일
  - `css/tailwind.css`: 빌드된 Tailwind CSS

브라우저에서 http://127.0.0.1:5000/ 에 접속하세요.

## 6. Tailwind CSS v4 세팅

### 6.1. 사전 요구사항 (Node.js 설치)
Tailwind CSS v4는 Node.js를 필요로 합니다. 아직 설치되지 않았다면:
1. [Node.js 공식 사이트](https://nodejs.org/)에서 LTS 버전 다운로드 및 설치.
2. 설치 확인: 터미널에서 `node --version`과 `npm --version` 실행 (버전 출력 확인).
3. PATH 설정: Windows에서 npm 명령어가 인식되지 않으면 환경 변수 PATH에 Node.js 설치 경로 추가.

### 6.2. Tailwind CSS 설치
프로젝트 루트에서 다음 명령어 실행:
```
npm install -D tailwindcss @tailwindcss/cli
```
- `-D`: 개발 의존성으로 설치 (프로덕션 배포 시 불필요).
- `@tailwindcss/cli`: v4 CLI 도구 (빌드 명령어 실행).
- 추가 도구 (선택): `npm install -D postcss autoprefixer concurrently` (이미 설치됨).

### 6.3. 입력 파일 생성 및 설정

이미 세팅되어 있지만 참조용입니다.

입력 CSS 파일 생성: `src/input.css`에 아래 내용을 작성하세요.
```css
@import "tailwindcss";
```

### 6.4. 빌드 설정 (package.json scripts)
package.json에 이미 설정되어 있지만, 수동 확인:
```json
"scripts": {
  "watch:css": "tailwindcss -i ./src/input.css -o ./static/css/tailwind.css --watch",
  "build:css": "tailwindcss -i ./src/input.css -o ./static/css/tailwind.css --minify",
  "dev": "concurrently \"@tailwindcss/cli -i ./src/input.css -o ./static/css/tailwind.css --watch\" \"flask run --debug\""
}
```
- **watch:css**: 개발 중 자동 재빌드.
- **build:css**: 프로덕션용 minify 빌드.
- **dev**: Tailwind + Flask 병렬 실행.

### 6.5. 빌드 실행
1. 개발 중 (변경 감지 시 자동 재빌드):
   ```
   npx tailwindcss -i src/input.css -o static/css/tailwind.css --watch
   ```
   또는 package.json scripts 사용:
   ```
   npm run watch:css
   ```

2. 프로덕션 빌드 (minify):
   ```
   npm run build:css
   ```

3. 개발 서버 (Tailwind watch + Flask 동시 실행):
   ```
   npm run dev
   ```
   - Tailwind CSS 자동 빌드 (static/css/tailwind.css 출력)와 Flask 앱 (debug 모드)을 병렬로 실행합니다.
   - concurrently 패키지를 사용합니다.

### 6.6. Flask 통합 및 사용
1. HTML에서 CSS 로드:
   templates/index.html의 head에:
   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='css/tailwind.css') }}">
   ```

2. Tailwind 클래스 적용 (예시):
   ```html
   <div class="bg-gray-100 p-4 rounded-lg">
     <h1 class="text-2xl font-bold text-blue-600">Tailwind 데모</h1>
     <button class="bg-green-500 hover:bg-green-700 text-white px-4 py-2 rounded">버튼</button>
   </div>
   ```

3. 자동 재빌드 확인:
   - src/input.css나 HTML 클래스 수정 → 저장 → 브라우저 새로고침으로 변경 반영.

### 6.7. 문제 해결
- **npm 명령어 오류**: Node.js 재설치 또는 PATH 확인 (`npm --version` 테스트).
- **빌드 실패**: 입력 파일 경로 확인 (`./src/input.css` 존재 여부).
- **스타일 미적용**: static/css/tailwind.css 생성 확인 및 Flask static 서빙 확인.
- **Windows 이슈**: PowerShell 사용 또는 shell=True 옵션 (app.py에서 이미 적용).

기본 설정으로 작동하며, 필요 시 `tailwind.config.js` 생성: `npx tailwindcss init`

## 7. VS Code 설정 (CSS 경고 숨김)

필요 시 직접 수정하세요.

또는 수동 세팅: VS Code 설정 (Ctrl+,)에서 "css.lint.propertyIgnoredDueToDisplay"를 "ignore"로 변경.

## 8. Tailwind CSS 데모 (index.html)
index.html에 다양한 Tailwind 유틸리티를 데모로 추가했습니다:

- **그리드 카드**: 반응형 그리드 (grid-cols-1 md:grid-cols-2 lg:grid-cols-3), 호버 효과 (hover:shadow-lg).
- **폼**: 입력 필드와 버튼 (focus:ring, space-y-4).
- **리스트와 버튼**: 타이포그래피 (font-bold, italic), 색상 변형, 플렉스 (flex flex-wrap gap-2).
- **반응형**: md:block (데스크톱만 표시), 그라데이션 배경 (bg-gradient-to-r).
- JS 버튼 클릭 시 알림 유지.

브라우저에서 확인하세요. Tailwind 클래스 수정 시 자동 재빌드 적용.
