import tkinter as tk
from PIL import Image, ImageTk


# ねこちゃんを表示させる関数
def cat_button():
    img = Image.open("cat_1.jpg")
    img_tk = ImageTk.PhotoImage(img)

    image_label.config(image=img_tk)
    image_label.image = img_tk


def clear():
    image_label.config(image=None)
    image_label.image = None


# ウィンドウを作成
root = tk.Tk()
root.title("猫画像Viewer")
root.geometry("1000x800")

# ボタン作成
button = tk.Button(root, text="ねこちゃんを表示する", command=cat_button)
button.pack(pady=50)

button2 = tk.Button(root, text="clear", command=clear)
button2.pack()

# 画像表示するラベル作成
image_label = tk.Label(root)
image_label.pack()


root.mainloop()
