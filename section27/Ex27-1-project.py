'''
파일명: Ex27-1-project.py

'''

import tkinter as tk
import sv_ttk   # pip install sv_ttk
from tkinter import ttk

from PIL.ImageOps import expand
from matplotlib.pyplot import margins


class MultiAIApp:

    def __init__(self, root):
        # 초기화
        self.root = root
        self.root.title('AI Assistant')
        self.root.geometry('1000x800')

        # 테마 설정
        sv_ttk.set_theme('dark')

        # 스타일 설정
        self.style = ttk.Style()

        # UI 설정 메서드 호출
        self.setup_ui()

    def setup_ui(self):
        # UI 초기화 구성
        main_container = ttk.Frame(self.root, padding='10')
        main_container.pack(fill='both', expand=True)

        # 노트북(탭) 생성
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill='both', expand=True)
        
        # 탭설정
        self.setup_chat_tab()   # 1. 채팅탭 구성

    def setup_chat_tab(self):





        


# 실행코드
if __name__ == '__main__':
    root = tk.Tk()
    app = MultiAIApp(root)
    root.mainloop()