'''
파일명: Ex24-1-Tkinter.py

tkinter
    Python에서 기본적으로 제공하는 GUI 프로그램 모듈

'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# 레이블 위젯 생성
label = tk.Label(root, text='Hello, Tkinter!')
label.pack()

# 한줄 입력 위젯 생성
entry = tk.Entry(root)
entry.pack()

# 여러 줄 텍스트 입력 위젯 생성
text = tk.Text(root)
text.pack()

# 체크박스 변수 위젯 생성
checkbox_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text='Check me!', variable=checkbox_var)
checkbutton.pack()

# 라디오버튼 변수 위젯 생성
radio_var = tk.StringVar()
radio_var.set('option1')
radiobutton1 = tk.Radiobutton(root, text='Option 1', variable=radio_var, value='option1')
radiobutton2 = tk.Radiobutton(root, text='Option 2', variable=radio_var, value='option2')
radiobutton1.pack()
radiobutton2.pack()

# 수평 슬라이더 위젯 생성
scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
scale.pack()

# 스핀박스 위젯 생성
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

# 콤보박스(드랍다운 리스트) 위젯 배치
combo = ttk.Combobox(root, values=['Item 1', 'Item 2', 'Item 3'])
# combo.current(0)
combo.set('Item 1')
combo.pack()

def onClick():
    print('Button Clikc!')

    # 각 위젯의 현재 값을 가져오기
    s_entry = entry.get()   # Entry 위젯의 입력값 가져오기
    s_text = text.get('1.0', tk.END)    # Text 위젯의 모든 텍스트(1행 0열부터 끝까지)
    i_checkbox = checkbox_var.get()
    s_radiobutton = radio_var.get()
    i_scale = scale.get()
    i_spinbox = spinbox.get()
    s_combo = combo.get()
    
    # 가져온 값들을 출력
    print(f's_entry: {s_entry}')
    print(f's_text: {s_text}')
    print(f'i_checkbox: {i_checkbox}')
    print(f's_radiobutton: {s_radiobutton}')
    print(f'i_scale: {i_scale}')
    print(f'i_spinbox: {i_spinbox}')
    print(f's_combo: {s_combo}')

# 버튼 위젯 생성
button = tk.Button(root, text='Click me!', command=onClick)
button.pack()


# 실행코드
if __name__ == '__main__':  # main 코드
    root.mainloop()






