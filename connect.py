import pymysql, tkinter
from tkinter import messagebox

conn = pymysql.connect(host="localhost", user="root", password="122069", port=3306, database="test", charset="utf8")
if conn:
    print("connect success")


def search(sql_query):
    search_page = tkinter.Tk()
    search_page.title("查询结果")
    search_page.geometry("600x400")
    show_listbox = tkinter.Listbox(search_page)
    show_listbox.pack()
    cur = conn.cursor()
    cur.execute(sql_query)
    data = cur.fetchall()
    for item in data:
        show_listbox.insert(1, item)
    search_page.mainloop()


def show_info_about():
    messagebox.showinfo("关于我们", "小组成员:\n 计181 卢烨凯 \n 计181 陈俊咏")


root = tkinter.Tk()
root.geometry("800x600")
root.title("窗口化数据库系统")
'''
menubar 部分
'''
menubar = tkinter.Menu(root)
menu = tkinter.Menu(menubar, tearoff=False)
menu.add_command(label="查询")
menu.add_command(label="更新")
menu.add_command(label="插入触发器")
menu.add_command(label="插入存储过程")
menubar.add_cascade(label="操作", menu=menu)
menubar.add_command(label="关于", command=show_info_about)
menubar.add_command(label="退出", command=root.quit)
root.config(menu=menubar)

'''
root 主界面
'''
sql_label = tkinter.Label(root, text="输入sql语句")
sql_entry = tkinter.Entry(root, width=60)
sql_label.grid(row=0, column=0)
sql_entry.grid(row=0, column=1)
sql = sql_entry.get()
button = tkinter.Button(root, text="执行", command=lambda:search(sql_entry.get()))
button.grid(row=0, column=2)
root.mainloop()
