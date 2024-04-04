import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog

programTitle="공백제외글자수세기"
# 메인 윈도우 생성
root = tk.Tk()
root.title(programTitle)
root.geometry("1000x600")  # 초기 크기 설정

# 스크롤 가능한 텍스트 입력 영역 생성
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("맑은 고딕", 10))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 글자수 표시 레이블 생성
status_label = tk.Label(root, text="글자수: 0", anchor=tk.W)
status_label.pack(fill=tk.X)

def update_status(event=None):
    text = text_area.get(1.0, "end-1c")  # 텍스트 영역의 내용을 가져옴
    char_count = len(text) - text.count(" ")-text.count("\n")  # 공백을 제외한 글자수 계산
    status_label.config(text=f"글자수 (공백 제외): {char_count}")  # 상태 레이블 업데이트

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text_area.delete(1.0, tk.END)  # 기존 텍스트 삭제
                text_area.insert(tk.END, file.read())  # 파일 내용을 텍스트 영역에 삽입
                root.title(f"{programTitle} - {file_path}")  # 윈도우 제목 업데이트
        except Exception as e:
            messagebox.showerror("오류", e)
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                text = text_area.get(1.0, tk.END)  # 텍스트 영역의 내용을 가져옴
                file.write(text)  # 파일에 쓰기
                root.title(f"{programTitle} - {file_path}")  # 윈도우 제목 업데이트
        except Exception as e:
            messagebox.showerror("오류", e)
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="종료", command=root.quit)
menu_bar.add_cascade(label="파일", menu=file_menu)
root.config(menu=menu_bar)

# 텍스트 영역에 키보드 입력이 있을 때마다 update_status 함수 호출
text_area.bind("<KeyRelease>", update_status)

root.mainloop()