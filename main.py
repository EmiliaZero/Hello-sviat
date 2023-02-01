import tkinter as tk
import tkinter.messagebox
import sqlite3

default_accounts = {"Sviat": "sviatpass1234",
                    "Admin": "adminPass2@30",
                    "Guest": "guestpass"}
try:
    open("users.sl3", "r")
    connection = sqlite3.connect("users.sl3", 5)
    cur = connection.cursor()
    cur.execute("SELECT rowid, login, password FROM accounts;")
    res = cur.fetchall()
    print(res)
except FileNotFoundError:
    open("users.sl3", "w")
    connection = sqlite3.connect("users.sl3", 5)
    cur = connection.cursor()
    cur.execute("CREATE TABLE accounts (login TEXT, password TEXT);")
    connection.commit()
    cur.execute("CREATE TABLE prod (name TEXT, price TEXT, number TEXT);")
    connection.commit()
    for person in range(0, len(default_accounts)):
        cur.execute(
            f"INSERT INTO accounts (login, password) VALUES ('{list(default_accounts.keys())[person]}', '{list(default_accounts.values())[person]}');")
        connection.commit()
    cur.execute("SELECT rowid, login, password FROM accounts;")
    res = cur.fetchall()
    print(res)

items = []


def get_log(base):
    cur.execute(f"SELECT  login FROM {base};")
    res = cur.fetchall()
    newres = []
    for i in res:
        newres.append(i[0])
    print(newres)
    return newres


def get_pass(base):
    cur.execute(f"SELECT password FROM {base};")
    res = cur.fetchall()
    newres = []
    for i in res:
        newres.append(i[0])
    print(newres)
    return newres


root = tk.Tk()
root.geometry("220x200")
root.resizable(False, True)


def start():
    for i in items:
        i.place_forget()
    ask = tk.Label(text="Виберіть дію:")

    def log():
        for i in items:
            i.place_forget()
        butt2 = tk.Button(text="< Назад", command=start)
        butt2.place(x=5, y=5)
        items.append(butt2)
        log_t = tk.Label(text="Увійдіть у свій \n обліковий запис:")
        log_t.place(x=60, y=10)
        items.append(log_t)

        log_n = tk.Label(text="Ваш логін:")
        log_n.place(x=10, y=50)
        items.append(log_n)
        log_p = tk.Label(text="Пароль:")
        log_p.place(x=20, y=90)
        items.append(log_p)
        log_te = tk.Entry()
        log_te.place(x=75, y=50)
        items.append(log_te)
        log_tn = tk.Entry()
        log_tn.place(x=75, y=90)
        items.append(log_tn)

        def log_ch():
            name = get_log("accounts")
            passw = get_pass("accounts")
            if log_te.get() in name and log_tn.get() == passw[name.index(log_te.get())]:
                tk.messagebox.showinfo(message=f"Ви успішно увійшли в свій акаунт, {log_te.get()}.")
                buy_menu()
            else:
                tk.messagebox.showerror(message="Неправильно введений логін, або пароль.")

        butt1 = tk.Button(text="Увійти", width=15, command=log_ch)
        butt1.place(x=45, y=120)
        items.append(butt1)

    def reg():
        is_human = tk.IntVar()
        for i in items:
            i.place_forget()
        butt2 = tk.Button(text="< Назад", command=start)
        butt2.place(x=5, y=5)
        items.append(butt2)
        log_t = tk.Label(text="Створення \n облікового запису:")
        log_t.place(x=60, y=10)
        items.append(log_t)
        log_n = tk.Label(text="Створіть \n логін:")
        log_n.place(x=20, y=45)
        items.append(log_n)
        log_p = tk.Label(text="Створіть \n пароль:")
        log_p.place(x=20, y=80)
        items.append(log_p)
        log_te = tk.Entry()
        log_te.place(x=75, y=50)
        items.append(log_te)
        log_tn = tk.Entry()
        log_tn.place(x=75, y=90)
        items.append(log_tn)
        ch = tk.Checkbutton(text="Я людина", variable=is_human)
        ch.place(x=60, y=115)
        items.append(ch)

        def reg_ch():
            if len(log_te.get()) >= 4 and len(log_tn.get()) >= 8:
                if is_human.get() == 1:
                    tk.messagebox.showinfo(message="Акаунт успішно створений")
                    cur.execute(f"INSERT INTO accounts (login, password) VALUES ('{log_te.get()}', '{log_tn.get()}')")
                    connection.commit()

                else:
                    tk.messagebox.showerror(message="Підвердіть, що ви людина")

            else:
                tk.messagebox.showerror(message='''Неправильний логін, або пароль.
    Логін має складатися не менше ніж з 4-ох символів, а пароль – не менш ніж з 8-ми.''')

        butt1 = tk.Button(text="Зареєструватися", width=15, command=reg_ch)
        butt1.place(x=45, y=140)
        items.append(butt1)

    def buy_menu():
        root.geometry("220x200")
        for i in items:
            i.place_forget()
        ask1 = tk.Label(text="Виберіть дію:")
        register1 = tk.Button(text="Список товарів", width=15, command=view)
        login1 = tk.Button(text="Добавити товар", width=15, command=add)
        login2 = tk.Button(text="Видалити товар", width=15, command=del1)
        ask1.place(x=70, y=30)
        register1.place(x=50, y=50)
        login1.place(x=50, y=75)
        login2.place(x=50, y=100)
        items.append(ask1)
        items.append(register1)
        items.append(login1)
        items.append(login2)

    def view():
        root.geometry("400x500")
        textname = []
        textprice = []
        textamount = []
        for i in items:
            i.place_forget()
        cur.execute("SELECT name, price, number FROM prod;")
        connection.commit()
        res = cur.fetchall()

        for prod in res:
            textname.append(prod[0])
            textprice.append(prod[1])
            textamount.append(prod[2])



        myentry = tk.Text(root, width=45, height=25)
        nameentry = tk.Text(myentry, width=20, height=25)
        priceentry = tk.Text(myentry, width=10, height=25)
        amountentry = tk.Text(myentry, width=5, height=25)
        myentry.window_create("end", window=nameentry)
        myentry.window_create("end", window=priceentry)
        myentry.window_create("end", window=amountentry)
        myscroll = tk.Scrollbar(root, orient="vertical")
        items.append(myscroll)
        myentry.place(x=7, y=50)
        myscroll.place(x=380, y=50)
        items.append(myentry)
        myentry.config(yscrollcommand=myscroll.set)
        myscroll.config(command=myentry.yview)
        nameentry.insert("end", "\n".join(textname))
        priceentry.insert("end", "\n".join(textprice))
        amountentry.insert("end", "\n".join(textamount))
        label1 = tk.Label(text=f'''Назва:                                           Ціна:                           Кількість:''')
        label1.place(x=7, y=30)
        items.append(label1)
        butt2 = tk.Button(text="< Назад", command=buy_menu)
        butt2.place(x=5, y=5)
        items.append(butt2)

        myentry.config(state="disabled")

    def del1():
        for i in items:
            i.place_forget()
        butt2 = tk.Button(text="< Назад", command=buy_menu)
        butt2.place(x=5, y=5)
        items.append(butt2)
        myentry = tk.Text(root, width=23, height=10)
        cur.execute("SELECT name, price, number FROM prod;")

        # def delete(but1):
        #     print(but1["text"])
        #     cur.execute(f'''DELETE FROM prod WHERE name = '{but1["text"]}' ''')
        #     items.remove(but1)
        #     but1.destroy()

        for x in cur.fetchall():
            myentry.config(state="normal")
            but = tk.Button(myentry, text=x[0], width=25,
                            command=lambda: [cur.execute(f'''DELETE FROM prod WHERE name = '{but["text"]}'; '''), connection.commit(),
                                             tk.messagebox.showinfo(message="Товар успішно видалено з каталогу"), buy_menu()])
            cur.execute("SELECT name FROM prod;")
            connection.commit()
            print(cur.fetchall())
            items.append(but)
            myentry.window_create("end", window=but)
            myentry.insert("end", "\n")

        myscroll = tk.Scrollbar(root, orient="vertical")
        items.append(myscroll)
        items.append(myentry)
        myentry.place(x=7, y=50)
        myscroll.place(x=200, y=40)
        myentry.config(yscrollcommand=myscroll.set)
        myscroll.config(command=myentry.yview)
        myentry.place(x=7, y=30)
        myentry.config(state="disabled")

    def add():
        for i in items:
            i.place_forget()
        butt2 = tk.Button(text="< Назад", command=buy_menu)
        butt2.place(x=5, y=5)
        items.append(butt2)
        log_t = tk.Label(text="Назва \n товару:")
        log_t.place(x=20, y=32)
        items.append(log_t)
        log_n = tk.Label(text="Ціна товару\n (грн):")
        log_n.place(x=5, y=72)
        items.append(log_n)
        log_p = tk.Label(text="Кількість \n товару:")
        log_p.place(x=20, y=112)
        items.append(log_p)
        namet = tk.Entry()
        namet.place(x=75, y=42)
        items.append(namet)
        log_te = tk.Entry()
        log_te.place(x=75, y=82)
        items.append(log_te)
        log_tn = tk.Entry()
        log_tn.place(x=75, y=122)
        items.append(log_tn)

        def add1():
            cur.execute(f"SELECT name FROM prod;")
            res = cur.fetchall()
            newres = []
            for i in res:
                newres.append(i[0])
            print(newres)
            if namet.get() not in newres:
                if namet.get() != '' and log_tn.get() != '' and log_te.get() != '':
                    cur.execute(
                        f"INSERT INTO prod (name, price, number) VALUES ('{namet.get()}', '{log_te.get()}', '{log_tn.get()}');")
                    connection.commit()
                    cur.execute("SELECT name, price, number FROM prod;")
                    tk.messagebox.showinfo(
                        message=f"{namet.get()} ціною {log_te.get()} грн добавлено в каталог у кількості {log_tn.get()}")
            else:
                tk.messagebox.showerror(message="Такий товар вже є у каталозі.")

        butt1 = tk.Button(text="Добавити", width=15, command=add1)
        butt1.place(x=45, y=152)
        items.append(butt1)

    register = tk.Button(text="Зареєструватися", width=15, command=reg)
    login = tk.Button(text="Увійти", width=15, command=log)

    ask.place(x=70, y=30)
    register.place(x=50, y=50)
    login.place(x=50, y=80)
    items.append(ask)
    items.append(register)
    items.append(login)
