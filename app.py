from flask import Flask, render_template
import subprocess
import atexit
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    # Tailwind CSS watch 자동 시작 (개발 환경에서만 사용. 프로덕션 배포 시 주석 처리 추천)
    tailwind_process = subprocess.Popen('npm run watch:css', shell=True, cwd=os.getcwd())
    def cleanup():
        tailwind_process.terminate()
    atexit.register(cleanup)
    
    app.run(debug=True)
