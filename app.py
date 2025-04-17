import tkinter as tk


def say_hello():
    print("こんにちは!")


# ウィンドウ作成
root = tk.Tk()
root.title("タイトル")
root.geometry("400x300")

# ウィジェットを作成と配置
label = tk.Label(root, text="こんにちは!")
label.pack()

# ボタン作成
button = tk.Button(root, text="クリック", command=say_hello)
button.pack()

root.mainloop()
