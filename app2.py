import tkinter as tk


# 名前を表示する関数
def show_name():
    name = entry.get()
    label.config(text=f"こんにちは,{name}さん!")


# 画面作成
root = tk.Tk()
root.title("名前表示アプリ")
root.geometry("300x150")

tk.Label(root, text="名前を入力してください").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="表示", command=show_name).pack()
label = tk.Label(root, text="", fg="#008b8b", font=("Arial", 14))
label.pack()

root.mainloop()
