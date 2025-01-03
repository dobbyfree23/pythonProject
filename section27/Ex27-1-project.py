'''
파일명: Ex27-1-project.py

'''

import tkinter as tk
import sv_ttk   # pip install sv_ttk
from tkinter import ttk, scrolledtext

import threading    # 여러 작업을 동시에 실행할 수 있게 해준다
from openai import OpenAI



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

        self.client = OpenAI()
        self.conversation_history = []

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
            style='Accent.TButton',
            command=self.send_message
        ).pack(side='right')

    def send_message(self, event=None):

        message = self.message_entry.get().strip()

        if not message:
            return

        # 입력 초기화
        self.message_entry.delete(0, tk.END)

        # 채팅창에 메시지 추가
        self.chat_area.insert(tk.END, f'나: {message}\n')
        self.chat_area.see(tk.END) # 스크롤 가장아래로

        threading.Thread(target=self.get_gpt_response, args=(message,)).start()

    def get_gpt_response(self, message):

        self.conversation_history.append({'role':'user', 'content': message})

        response = self.client.chat.completions.create(
            model='gpt-4o-mini',
            messages=self.conversation_history
        )

        assistant_message = response.choices[0].message.content # GPT 응답 TEXT
        self.conversation_history.append(
            {'role':'assistant', 'content': assistant_message}
        )

        # UI 업데이트 요청
        self.root.after(0, self.update_chat_area, assistant_message)

    def update_chat_area(self, response_text):
        # 채팅창에 메시지 추가
        self.chat_area.insert(tk.END, f'AI: {response_text}\n')
        self.chat_area.see(tk.END)  # 스크롤 가장아래로





# 실행코드
if __name__ == '__main__':
    root = tk.Tk()
    app = MultiAIApp(root)
    root.mainloop()