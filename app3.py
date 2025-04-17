import tkinter as tk
from tkinter import messagebox
import requests


# 郵便番号で住所検索する関数
def search_address():
    zipcode = zipcode_entry.get()
    # print(zipcode)
    if not zipcode:
        messagebox.showwarning("入力エラー", "郵便番号を入力してください")
        return

    # APIリクエスト
    url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
    response = requests.get(url)
    # print(response)
    if response.status_code == 200:
        data = response.json()

        if data["results"] is None:
            messagebox.showerror("エラー", "該当する住所が見つかりませんでした")
            return

        # 結果を取り出して表示
        address1 = data['results'][0]['address1']
        address2 = data['results'][0]['address2']
        address3 = data['results'][0]['address3']
        full_address = f"{address1}{address2}{address3}"

        # 既存の住所をクリア
        address_entry.delete(0, tk.END)

        # 新しい住所を表示
        address_entry.insert(tk.END, full_address)
    else:
        messagebox.showerror("エラー", "該当する住所が見つかりませんでした")
        return
    
# メインのUIを作成
def main():
    # グローバル変数と定義
    global zipcode_entry, address_entry
    # 画面作成
    root = tk.Tk()
    root.title("郵便番号で住所検索")

    # 郵便番号入力フィールドを作成
    tk.Label(root, text="郵便番号:").grid(row=0, column=0, padx=5, pady=10)
    zipcode_entry = tk.Entry(root, width=20)
    zipcode_entry.grid(row=0, column=1, padx=5, pady=5)

    # 検索ボタン作成
    search_button = tk.Button(root, text="検索する", command=search_address)
    search_button.grid(row=0, column=2, padx=5, pady=5)

    # 住所表示フィールド
    tk.Label(root, text="住所: ").grid(row=1, column=0, padx=5, pady=5)

    address_entry = tk.Entry(root, width=50)
    address_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
