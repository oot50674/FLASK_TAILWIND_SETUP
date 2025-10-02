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
- Flask 서버가 시작되며, 동시에 Tailwind CSS watch (npm run watch:css)가 백그라운드에서 자동 실행됩니다. (서비스 배포시 주석처리 필요)
- 변경 감지 시 CSS 자동 재빌드.

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
- 추가 도구 (선택): `npm install -D postcss autoprefixer concurrently`

### 6.3. input.css
```css
@import "tailwindcss";
```

### 6.4. 빌드 설정 (package.json scripts)
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

## 6. VS Code 설정 (CSS 경고 숨김)

필요 시 직접 수정하세요.

또는 수동 세팅: VS Code 설정 (Ctrl+,)에서 "css.lint.propertyIgnoredDueToDisplay"를 "ignore"로 변경.