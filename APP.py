import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3
import pandas as pd



def login():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Data_Table
                    (firstname TEXT, lastname TEXT, username TEXT, dateofbirth TEXT, email TEXT, sex INT,
                    phone TEXT, password TEXT)""")
    cursor.execute('SELECT * FROM Data_Table;')
    resultados = cursor.fetchall()
    conn.close()
    listan = dict()
    for linha in resultados:
        listan[linha[2]] = (linha[7])
    if un_entry.get() in listan and pss_entry.get() == listan[un_entry.get()]:
        mainwindow()
    else:
        if un_entry.get() not in listan:
            messagebox.showinfo(title='ERROR', message="Invalid username!")
        elif pss_entry.get() != listan[un_entry.get()]:
            messagebox.showinfo(title='ERROR', message="Invalid password!")


def mainwindow():
    window.withdraw()

    def on_treeview_scroll(*args):
        tree.yview(*args)

    def close():
        main_window.withdraw()

    def deletar():
        def deletaru():
            usuario_para_excluir = UN_entry.get()

            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            try:
                cursor.execute(f"DELETE FROM Data_table WHERE email = '{usuario_para_excluir}'")
                conn.commit()
                messagebox.showinfo("SUCCESS", f"User '{usuario_para_excluir}' deleted.")
            except Exception as e:
                messagebox.showerror("Error", f"Error trying to delete: {str(e)}")
            finally:
                conn.close()
                main_window.withdraw()

        main_window = ctk.CTkToplevel()
        main_window.title("DELETE")
        main_window.geometry('400x150')
        main_window.resizable(width=False, height=False)
        UN_label = ctk.CTkLabel(main_window, text='Email:', font=ctk.CTkFont(size=12, weight="bold"))
        UN_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                                text_color='#FFFFFF', height=30, width=199)
        R_b = ctk.CTkButton(main_window, text='Delete', font=ctk.CTkFont(size=15, weight="bold"),
                            fg_color='#B2343A', hover_color='#7D2528', command=deletaru)
        UN_entry.place(relx=0.375, rely=0.36, anchor=tk.W)
        UN_label.place(relx=0.26, rely=0.36, anchor=tk.W)
        R_b.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        main_window.mainloop()

    def carregar():
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT firstname, lastname, dateofbirth, email, sex, phone FROM Data_Table')
        for row in tree.get_children():
            tree.delete(row)
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
        conn.close()

    main_window = ctk.CTkToplevel()
    main_window.title("APP")
    main_window.geometry('800x600')
    main_window.resizable(width=False, height=False)
    tree = ttk.Treeview(main_window, columns=('Name', 'Lastname', 'Birth Date', 'Email', 'Sex', 'Phone'),
                        show='headings', height=20)
    tree.heading('Name', text='Name')
    tree.heading('Lastname', text='Lastname')
    tree.heading('Birth Date', text='Birth Date')
    tree.heading('Email', text='Email')
    tree.heading('Sex', text='Sex')
    tree.heading('Phone', text='Phone')
    tree.column('Name', width=100)
    tree.column('Lastname', width=100)
    tree.column('Birth Date', width=100)
    tree.column('Email', width=150)
    tree.column('Sex', width=50)
    tree.column('Phone', width=100)
    scrollbar = ttk.Scrollbar(tree, orient=tk.VERTICAL, command=on_treeview_scroll)

    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(expand=True, fill=tk.BOTH)
    u_label = ctk.CTkLabel(main_window, text='Users:', font=ctk.CTkFont(size=20, weight="bold"))
    ref_b = ctk.CTkButton(main_window, text='Refresh', font=ctk.CTkFont(size=15, weight="bold"),
                          fg_color='#B2343A', hover_color='#7D2528', command=carregar)
    del_b = ctk.CTkButton(main_window, text='Delete', font=ctk.CTkFont(size=15, weight="bold"),
                          fg_color='#B2343A', hover_color='#7D2528', command=deletar)
    c_b = ctk.CTkButton(main_window, text='Close', font=ctk.CTkFont(size=15, weight="bold"),
                        fg_color='#B2343A', hover_color='#7D2528', command=close)
    r_b = ctk.CTkButton(main_window, text='Register', font=ctk.CTkFont(size=15, weight="bold"),
                        fg_color='#B2343A', hover_color='#7D2528', command=register)
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT firstname, lastname, dateofbirth, email, sex, phone FROM Data_Table')
    for row in tree.get_children():
        tree.delete(row)
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)
    conn.close()
    u_label.place(relx=0.1, rely=0.15, anchor=tk.CENTER)
    tree.place(relx=0.55, rely=0.45, anchor=tk.CENTER)
    r_b.place(relx=0.4, rely=0.85, anchor=tk.CENTER)
    c_b.place(relx=0.8, rely=0.85, anchor=tk.CENTER)
    ref_b.place(relx=0.6, rely=0.85, anchor=tk.CENTER)
    del_b.place(relx=0.2, rely=0.85, anchor=tk.CENTER)
    scrollbar.place(relx=0.982, rely=0.5, anchor=tk.CENTER, relheight=0.99)
    main_window.mainloop()


def register():
    def home():
        main_window.withdraw()

    def registerf():
        conexao = sqlite3.connect('data.db')
        cursor = conexao.cursor()
        table = '''CREATE TABLE IF NOT EXISTS Data_Table
                    (firstname TEXT, lastname TEXT, username TEXT, dateofbirth TEXT, email TEXT, sex INT,
                    phone TEXT, password TEXT)'''
        cursor.execute(table)
        cursor.execute('SELECT * FROM Data_Table')
        resultados = cursor.fetchall()
        conexao.close()
        listan = list()
        listap = list()
        for linha in resultados:
            listan.append(linha[2])
            listap.append(linha[4])
        firstname = FN_entry.get().strip()
        lastname = LN_entry.get().strip()
        email = str(email_entry.get().strip())
        if sex.get() == 1:
            sexo = 'Male'
        else:
            sexo = 'Female'
        password = PSS_entry.get()
        dateofbirth = DB_entry.get().strip()
        phone = phone_entry.get().strip()
        username = UN_entry.get().strip()
        if firstname == '':
            messagebox.showinfo(title='ERROR', message="Invalid first name!")
        elif lastname == '':
            messagebox.showinfo(title='ERROR', message="Invalid last name!")
        elif email == '':
            messagebox.showinfo(title='ERROR', message="Invalid email!")
        elif email in listan:
            messagebox.showinfo(title='ERROR', message="Email already registered!")
        elif sexo == 0:
            messagebox.showinfo(title='ERROR', message="Please, choose male or female at sex option!")
        elif dateofbirth == '':
            messagebox.showinfo(title='ERROR', message="Invalid date of birth!")
        elif phone == '':
            messagebox.showinfo(title='ERROR', message="Invalid phone!")
        elif username == '' or username in listap:
            messagebox.showinfo(title='ERROR', message="Invalid username!")
        elif password == '':
            messagebox.showinfo(title='ERROR', message="Invalid password!")
        else:
            messagebox.showinfo(title='message', message="User successfully registered!")
            main_window.withdraw()
            conn = sqlite3.connect('data.db')
            table = '''CREATE TABLE IF NOT EXISTS Data_Table
                    (firstname TEXT, lastname TEXT, username TEXT, dateofbirth TEXT, email TEXT, sex INT,
                    phone TEXT, password TEXT)'''
            conn.execute(table)
            table_insert_q = '''INSERT INTO Data_table (firstname, lastname, username, dateofbirth, email, sex,
                    phone, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            table_insert_t = (firstname, lastname, username, dateofbirth, email, sexo,
                              phone, password)
            cursor = conn.cursor()
            cursor.execute(table_insert_q, table_insert_t)
            conn.commit()
            conn.close()

    main_window = ctk.CTkToplevel()
    main_window.title("REGISTER APPLICATION")
    main_window.geometry('440x540')
    main_window.maxsize(width=440, height=540)
    main_window.minsize(width=440, height=540)
    main_window.resizable(width=False, height=False)
    R_label = ctk.CTkLabel(main_window, text='Register user', font=ctk.CTkFont(size=30, weight="bold"))
    FN_label = ctk.CTkLabel(main_window, text='First name:', font=ctk.CTkFont(size=12, weight="bold"))
    FN_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                            text_color='#FFFFFF',
                            height=30, width=199)
    LN_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                            text_color='#FFFFFF', height=30, width=199)
    LN_label = ctk.CTkLabel(main_window, text='Last Name:', font=ctk.CTkFont(size=12, weight="bold"))
    UN_label = ctk.CTkLabel(main_window, text='Username:', font=ctk.CTkFont(size=12, weight="bold"))
    UN_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                            text_color='#FFFFFF', height=30, width=199)
    DB_label = ctk.CTkLabel(main_window, text='Date of Birth:', font=ctk.CTkFont(size=12, weight="bold"))
    DB_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                            text_color='#FFFFFF', height=30, width=199, placeholder_text='MM/DD/YYYY')
    email_label = ctk.CTkLabel(main_window, text='Email:', font=ctk.CTkFont(size=12, weight="bold"))
    email_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                               text_color='#FFFFFF', height=30, width=199)
    sex_label = ctk.CTkLabel(main_window, text='Sex:', font=ctk.CTkFont(size=12, weight="bold"))
    sex = ctk.IntVar(value=0)
    phone_label = ctk.CTkLabel(main_window, text='Phone:', font=ctk.CTkFont(size=12, weight="bold"))
    phone_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                               text_color='#FFFFFF', height=30, width=199)
    PSS_label = ctk.CTkLabel(main_window, text='Password:', font=ctk.CTkFont(size=12, weight="bold"))
    PSS_entry = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                             text_color='#FFFFFF', height=30, width=199, show='*')
    m_button = ctk.CTkRadioButton(main_window, text='Male', variable=sex, value=1, fg_color='#B2343A',
                                  hover_color='#7D2528')
    f_button = ctk.CTkRadioButton(main_window, text='Female', variable=sex, value=2, fg_color='#B2343A',
                                  hover_color='#7D2528')
    R_button = ctk.CTkButton(main_window, text='Register', font=ctk.CTkFont(size=15, weight="bold"),
                             fg_color='#B2343A', hover_color='#7D2528', command=registerf)
    H_button = ctk.CTkButton(main_window, text='Home Page', font=ctk.CTkFont(size=15, weight="bold"), command=home,
                             fg_color='#B2343A', hover_color='#7D2528')

    # colocando no lugar
    R_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    FN_label.place(relx=0.155, rely=0.24, anchor=tk.W)
    FN_entry.place(relx=0.32, rely=0.24, anchor=tk.W)
    LN_label.place(relx=0.155, rely=0.30, anchor=tk.W)
    LN_entry.place(relx=0.32, rely=0.30, anchor=tk.W)
    UN_entry.place(relx=0.32, rely=0.36, anchor=tk.W)
    UN_label.place(relx=0.165, rely=0.36, anchor=tk.W)
    DB_entry.place(relx=0.32, rely=0.42, anchor=tk.W)
    DB_label.place(relx=0.125, rely=0.42, anchor=tk.W)
    email_entry.place(relx=0.32, rely=0.48, anchor=tk.W)
    email_label.place(relx=0.225, rely=0.48, anchor=tk.W)
    sex_label.place(relx=0.26, rely=0.54, anchor=tk.W)
    phone_entry.place(relx=0.32, rely=0.66, anchor=tk.W)
    phone_label.place(relx=0.215, rely=0.66, anchor=tk.W)
    PSS_entry.place(relx=0.32, rely=0.72, anchor=tk.W)
    PSS_label.place(relx=0.165, rely=0.72, anchor=tk.W)

    m_button.place(relx=0.34, rely=0.54, anchor=tk.W)
    f_button.place(relx=0.34, rely=0.60, anchor=tk.W)
    R_button.place(relx=0.32, rely=0.8, anchor=tk.CENTER)
    H_button.place(relx=0.68, rely=0.8, anchor=tk.CENTER)
    main_window.mainloop()


def forgot():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Data_Table;')
    resultados = cursor.fetchall()
    listan = dict()
    count = 0
    for linha in resultados:
        listan[linha[4]] = (linha[6])
        count += 1
    conn.close()

    def ver():
        if email_e.get() in listan and p_e.get() == listan[email_e.get()]:
            conexao = sqlite3.connect('data.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE Data_Table SET password = ? WHERE email = ?", (s_e.get(), email_e.get()))
            conexao.commit()
            conexao.close()
            messagebox.showinfo(title='SUCCESS', message="The new password is registered!")
            main_window.withdraw()
        else:
            messagebox.showinfo(title='ERROR', message="Something is wrong!\nMake sure everything is typed correctly.")

    def close():
        main_window.withdraw()

    main_window = ctk.CTkToplevel()
    main_window.title("Password recovery")
    main_window.geometry('400x200')
    main_window.resizable(width=False, height=False)

    email_l = ctk.CTkLabel(main_window, font=ctk.CTkFont(size=12, weight="bold"), text_color='#FFFFFF',
                           text='Email:')
    email_e = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                           text_color='#FFFFFF', width=200)
    p_l = ctk.CTkLabel(main_window, font=ctk.CTkFont(size=12, weight="bold"), text_color='#FFFFFF',
                       text='Phone: ')
    p_e = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                       text_color='#FFFFFF', width=200)
    f_b = ctk.CTkButton(main_window, text='Register new password', font=ctk.CTkFont(size=15, weight="bold"),
                        fg_color='#B2343A', hover_color='#7D2528', command=ver)
    c_b = ctk.CTkButton(main_window, text='Close', font=ctk.CTkFont(size=15, weight="bold"),
                        fg_color='#B2343A', hover_color='#7D2528', command=close, width=55)
    s_e = ctk.CTkEntry(main_window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242',
                       text_color='#FFFFFF', width=200)
    s_l = ctk.CTkLabel(main_window, font=ctk.CTkFont(size=12, weight="bold"), text_color='#FFFFFF',
                       text='New Password:')
    email_l.place(relx=0.31, rely=0.2, anchor=tk.E)
    email_e.place(relx=0.32, rely=0.2, anchor=tk.W)
    p_l.place(relx=0.32, rely=0.38, anchor=tk.E)
    p_e.place(relx=0.32, rely=0.38, anchor=tk.W)
    f_b.place(relx=0.16, rely=0.74, anchor=tk.W)
    c_b.place(relx=0.70, rely=0.74, anchor=tk.W)
    s_e.place(relx=0.32, rely=0.56, anchor=tk.W)
    s_l.place(relx=0.31, rely=0.56, anchor=tk.E)
    main_window.mainloop()


window = ctk.CTk()
window.title("REGISTER APPLICATION")
window.geometry('340x440')
window.maxsize(width=340, height=440)
window.minsize(width=340, height=440)
window.resizable(width=False, height=False)

l_label = ctk.CTkLabel(window, text='Login', font=ctk.CTkFont(size=30, weight="bold"))
un_label = ctk.CTkLabel(window, text='Username:', font=ctk.CTkFont(size=15, weight="bold"))
un_entry = ctk.CTkEntry(window, font=ctk.CTkFont(size=12, weight="bold"), fg_color='#424242', text_color='#FFFFFF')
pss_entry = ctk.CTkEntry(window, font=ctk.CTkFont(size=12, weight="bold"), show='*', fg_color='#424242',
                         text_color='#FFFFFF')
pss_label = ctk.CTkLabel(window, text='Password:', font=ctk.CTkFont(size=15, weight="bold"))
l_button = ctk.CTkButton(window, text='Login', font=ctk.CTkFont(size=15, weight="bold"), command=(login),
                         fg_color='#B2343A', hover_color='#7D2528')
c_button = ctk.CTkButton(window, text='Register', font=ctk.CTkFont(size=15, weight="bold"), command=register,
                         fg_color='#B2343A', hover_color='#7D2528')
f_text = ctk.CTkButton(window, text='Forgot the password?', font=ctk.CTkFont(size=15, weight="bold"), command=forgot,
                       fg_color='#424242', hover_color='#424242')
l_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
un_label.place(relx=0.40, rely=0.3, anchor=tk.E)
un_entry.place(relx=0.48, rely=0.3, anchor=tk.W)
pss_label.place(relx=0.40, rely=0.4, anchor=tk.E)
pss_entry.place(relx=0.48, rely=0.4, anchor=tk.W)
l_button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
c_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
f_text.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
window.mainloop()
