import tkinter as tk
from tkinter import messagebox
import sqlite3

# DB初期化
conn = sqlite3.connect("sales.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT,
    price INTEGER
)"""
)
conn.commit()

# 商品データ
menu = {"ハンバーガー": 300, "ポテト": 200, "ドリンク": 150}

cart = []


def add_to_cart(item):
    price = menu[item]
    cart.append((item, price))
    update_cart_display()


def update_cart_display():
    cart_list.delete(0, tk.END)
    total = 0
    for item, price in cart:
        cart_list.insert(tk.END, f"{item} ¥{price}")
        total += price
    total_label.config(text=f"注文合計: ¥{total}")


def confirm_order():
    for item, price in cart:
        c.execute("INSERT INTO sales (item, price) VALUES (?, ?)", (item, price))
    conn.commit()
    cart.clear()
    update_cart_display()


def show_total_sales():
    c.execute("SELECT SUM(price) FROM sales")
    total_sales = c.fetchone()[0] or 0
    tk.messagebox.showinfo("売上合計", f"現在の売上合計: ¥{total_sales}")


def reset_sales_data():
    if messagebox.askyesno("確認", "本当にデータを初期化しますか?"):
        c.execute("DELETE FROM sales")
        conn.commit()
        messagebox.showinfo("初期化完了", "売上データを初期化しました。")


# GUI構築
root = tk.Tk()
root.title("ハンバーガーショップ")

frame = tk.Frame(root)
frame.pack()

for item in menu:
    btn = tk.Button(frame, text=item, width=15, command=lambda i=item: add_to_cart(i))
    btn.pack(side=tk.LEFT, padx=5, pady=10)

cart_list = tk.Listbox(root, width=40)
cart_list.pack()

total_label = tk.Label(root, text="注文合計: ¥0")
total_label.pack()

confirm_button = tk.Button(root, text="購入確定", command=confirm_order)
confirm_button.pack(pady=5)

sales_button = tk.Button(root, text="売上合計を表示", command=show_total_sales)
sales_button.pack(pady=5)

reset_button = tk.Button(root, text="売上データを初期化", command=reset_sales_data)
reset_button.pack(pady=5)

root.mainloop()
