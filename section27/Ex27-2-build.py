'''
파일명: Ex27-2-build.py

PyInstaller 
    파이썬 프로그램을 독립 실행가능한 실행파일(.exe)로 변환해주는 도구

    pip install pyinstaller
'''

import PyInstaller.__main__
import os
import shutil # 파일/디렉토리 고수준 작업을 위한 모듈

# 빌드전 dist 폴더가 있다면 삭제
if os.path.exists("dist"):
    shutil.rmtree("dist")   # dist 폴더와 그 내용을 전부 삭제

# Pyinstaller 설정 및 실행
PyInstaller.__main__.run([
    'Ex27-1-project.py',  # 빌드할 파일명
    '--onefile',          # 단일 실행 파일로 빌드
    '--noconsole',        # 콘솔 창 숨기기
    '--name=project',             # 출력될 실행파일의 이름
    '--clean',             # 빌드 전 캐시 삭제
    '--icon=NONE',
    '--noconfirm',          # 기존 빌드 폴더 자동 덮어쓰기
    '--windowed'            # GUI 애플리케이션으로 빌드(콘솔 창없음)
])