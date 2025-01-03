'''
파일명: Ex27-1-project.py

'''

import tkinter as tk
import sv_ttk   # pip install sv_ttk
from tkinter import ttk, scrolledtext

from PIL.ImageOps import expand


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
        self.style.configure('Chat.TFrame', padding=10)
        self.style.configure('Title.TLabel', font=('Helvetica', 12, 'bold'))
        self.style.configure('Control.TFrame', padding=5)

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
        # 채팅 탭 UI 구성
        self.chat_frame = ttk.Frame(self.notebook, style='Chat.TFrame')
        self.notebook.add(self.chat_frame, text=' 💬 채팅')
        
        # 타이틀 프레임
        title_frame = ttk.Frame(self.chat_frame)
        title_frame.pack(fill='x', pady=(0, 10))
        ttk.Label(title_frame, text='AI와의 대화', style='Title.TLabel').pack(side='left')

        # 채팅영역
        chat_container = ttk.Frame(self.chat_frame, relief='solid', borderwidth=1)
        chat_container.pack(fill='both', expand=True, pady=(0, 10))

        self.chat_area = scrolledtext.ScrolledText(
            chat_container,
            wrap=tk.WORD,       # 단어 단위로 자동 줄바꿈
            height=20,
            font=('Helvetica', 10),
            bg='#000000'        # 배경 검정색
        )
        self.chat_area.pack(fill='both', expand=True, padx=5, pady=5)

        # 입력 영역 컨테이너
        input_container = ttk.Frame(self.chat_frame, style='Control.TFrame')
        input_container.pack(fill='both', pady=(0, 5))

        # 메시지 입력 프레임
        input_frame = ttk.Frame(input_container)
        input_frame.pack(fill='x', pady=5)

        self.message_entry = ttk.Entry(
            input_frame,
            font=('Helvetica', 10)
        )
        self.message_entry.pack(
            side='left',
            fill='x',
            expand=True,
            padx=(0, 5)
        )

        self.message_entry.bind(
            '<Return>',
            self.send_message
        )

        ttk.Button(
            input_frame,
            text='전송',
            command=self.send_message
        ).pack(side='right')

    def send_message(self, event=None):
        print('전송', self.message_entry.get())




        


# 실행코드
if __name__ == '__main__':
    root = tk.Tk()
    app = MultiAIApp(root)
    root.mainloop()