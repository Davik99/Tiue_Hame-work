import tkinter as tk

class SampleApp(tk. Tk):
    def __init__(self,*arg,**kwargs):
        tk.Tk.__init__(self,*arg,**kwargs)
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in(StartPage, MenuPage, Cars,SirdaryoPage,JizzaxPage,SamarqandPage,QashqadaryoPage,BuxoroPage):
            page_name=F.__name__
            frame=F(parent=container,controller=self)
            self.frames[page_name]=frame

            frame.grid(row=0,column=0,sticky='nsew')

            self.show_frame('StartPage')

    def show_frame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent, bg ="white")
        self.controller=controller
        self.controller.title('QULAY AVTO')
        self.controller.state('zoomed')

        big_lable=tk.Label(self,text='QULAY AVTO', font=('Candara',50,'bold'),fg='black',bg='white')
        big_lable.pack(pady=30)

        login_lable=tk.Label(self,text='Entry login', font=('Candara',15,'bold'),bg='white',fg='black')
        login_lable.pack(pady=30)

        my_login=tk.StringVar()
        login_entry=tk.Entry(self,textvariable=my_login, font=('Candara',15,'bold'),bg='white',fg='black')
        login_entry.pack(pady=30)

        password_lable=tk.Label(self,text='Entry password', font=('Candara',15,'bold'),bg='white',fg='black')
        password_lable.pack(pady=30)

        my_password= tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, font=('Candara', 15, 'bold'), bg='white',fg='black')
        password_entry.pack(pady=30)


        def check_password():
            if my_password.get()=='4' and my_login.get()=='d':
                controller.show_frame('MenuPage')

                #right_lable = tk.Label(self, text = "right answer")
                #right_lable.pack()
            else:
                right_lable['text']='Invalid password or login'

        password_button=tk.Button(self,text='Логин',command=check_password,
                                  font=('Candara',15,'bold'),bg='white',fg='black')
        password_button.pack()
        right_lable=tk.Label(self,font=('Candara',15,'bold'),bg='white',fg='black')
        right_lable.pack(pady=30)

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,bg='black')
        self.controller=controller
        big_lable = tk.Label(self, text='ТАКСИ ХИЗМАТИ QULAY AVTO', font=('Candara', 20, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        big_lable.place(x=200, y=40)

        def cars():
            controller.show_frame('Cars')

        car_button=tk.Button(self,command=cars,text='Маршруты',font=('Candara', 15, 'bold'), fg='black', bg='white')
        car_button.pack()





class Cars(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        def sirdaryo():
            controller.show_frame('SirdaryoPage')
        sirdaryo_button = tk.Button(self,command=sirdaryo,text="Toshkent-Sirdaryo,Sirdaryo-Toshkent",font=('Candara', 15, 'bold'), fg='black', bg='white')
        sirdaryo_button.pack(pady=10)

        def jizzax():
            controller.show_frame('JizzaxPage')
        jizzax_button = tk.Button(self,command=jizzax,text="Toshkent-Jizzax,Jizzax-Toshkent",font=('Candara', 15, 'bold'), fg='black', bg='white')
        jizzax_button.pack(pady=10)

        def samarqand():
            controller.show_frame('SamarqandPage')
        samarqand_button = tk.Button(self,command=samarqand,text="Toshkent-Samarqand,Samarqand-Toshkent",font=('Candara', 15, 'bold'), fg='black', bg='white')
        samarqand_button.pack(pady=10)

        def qashqadaryo():
            controller.show_frame('QashqadaryoPage')
        qashqadaryo_button=tk.Button(self,command=qashqadaryo,text="Toshkent-Qashqadaryo,Qashqadaryo-Toshkent",font=('Candara', 15, 'bold'), fg='black', bg='white')
        qashqadaryo_button.pack(pady=10)

        def buxoro():
            controller.show_frame('BuxoroPage')
        buxoro_button=tk.Button(self,command=buxoro,text="Toshkent-Buxoro,Buxoro-Toshkent",font=('Candara', 15, 'bold'), fg='black', bg='white')
        buxoro_button.pack(pady=10)






class SirdaryoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller

        c1 = tk.Label(self, text='Укажите количество пассажиров\n Цена за одного пассажира - 80.000 сум', font=('Bernard MT Condensed', 15, 'bold'))
        c1.pack(pady=10)
        cc1 = tk.Label(self, text='Оплата', font=(15))
        cc1.pack(pady=10)
        c = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        c.pack(pady=20)
        cc = 80000

        def schet():
            summa = cc
            cc1.config(text=int(summa) * int(c.get()))

        kupit = tk.Button(self, text='Сумма для поездки', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        d2 = tk.Label(self, text='Доставка', font=('Bernard MT Condensed', 15, 'bold'))
        d2.pack(pady=10)
        dd2 = tk.Label(self, text='Оплата', font=(15))
        dd2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 50000

        def dostavka():
            summ = rastoyanie
            dd2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='Цена за доставку',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)


        def return_MenuPage():
            controller.show_frame('Cars')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='black')
        return_button.pack(pady=30)

class JizzaxPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller

        c1 = tk.Label(self, text='Укажите количество пассажиров\n Цена за одного пассажира - 100.000 сум', font=('Bernard MT Condensed', 15, 'bold'))
        c1.pack(pady=10)
        cc1 = tk.Label(self, text='Оплата', font=(15))
        cc1.pack(pady=10)
        c = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        c.pack(pady=20)
        cc = 100000

        def schet():
            summa = cc
            cc1.config(text=int(summa) * int(c.get()))

        kupit = tk.Button(self, text='Сумма для поездки', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        d2 = tk.Label(self, text='Доставка', font=('Bernard MT Condensed', 15, 'bold'))
        d2.pack(pady=10)
        dd2 = tk.Label(self, text='Оплата', font=(15))
        dd2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 50000

        def dostavka():
            summ = rastoyanie
            dd2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='Цена за доставку',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)


        def return_MenuPage():
            controller.show_frame('Cars')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='black')
        return_button.pack(pady=30)

class SamarqandPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller

        c1 = tk.Label(self, text='Укажите количество пассажиров\n Цена за одного пассажира - 120.000 сум', font=('Bernard MT Condensed', 15, 'bold'))
        c1.pack(pady=10)
        cc1 = tk.Label(self, text='Оплата', font=(15))
        cc1.pack(pady=10)
        c = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        c.pack(pady=20)
        cc = 120000

        def schet():
            summa = cc
            cc1.config(text=int(summa) * int(c.get()))

        kupit = tk.Button(self, text='Сумма для поездки', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        d2 = tk.Label(self, text='Доставка', font=('Bernard MT Condensed', 15, 'bold'))
        d2.pack(pady=10)
        dd2 = tk.Label(self, text='Оплата', font=(15))
        dd2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 50000

        def dostavka():
            summ = rastoyanie
            dd2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='Цена за доставку',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)

        def return_MenuPage():
            controller.show_frame('Cars')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='black')
        return_button.pack(pady=30)

class QashqadaryoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller

        c1 = tk.Label(self, text='Укажите количество пассажиров\n Цена за одного пассажира - 150.000 сум', font=('Bernard MT Condensed', 15, 'bold'))
        c1.pack(pady=10)
        cc1 = tk.Label(self, text='Оплата', font=(15))
        cc1.pack(pady=10)
        c = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        c.pack(pady=20)
        cc = 150000

        def schet():
            summa = cc
            cc1.config(text=int(summa) * int(c.get()))

        kupit = tk.Button(self, text='Сумма для поездки', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        d2 = tk.Label(self, text='Доставка', font=('Bernard MT Condensed', 15, 'bold'))
        d2.pack(pady=10)
        dd2 = tk.Label(self, text='Оплата', font=(15))
        dd2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 50000

        def dostavka():
            summ = rastoyanie
            dd2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='Цена за доставку',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)


        def return_MenuPage():
            controller.show_frame('Cars')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='black')
        return_button.pack(pady=30)

class BuxoroPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller

        c1 = tk.Label(self, text='Укажите количество пассажиров\n Цена за одного пассажира - 200.000 сум', font=('Bernard MT Condensed', 15, 'bold'))
        c1.pack(pady=10)
        cc1 = tk.Label(self, text='Оплата', font=(15))
        cc1.pack(pady=10)
        c = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        c.pack(pady=20)
        cc = 200000

        def schet():
            summa = cc
            cc1.config(text=int(summa) * int(c.get()))

        kupit = tk.Button(self, text='Сумма для поездки', command=schet, font=('Bernard MT Condensed', 15, 'bold'))
        kupit.pack(pady=10)
        d2 = tk.Label(self, text='Доставка', font=('Bernard MT Condensed', 15, 'bold'))
        d2.pack(pady=10)
        dd2 = tk.Label(self, text='Оплата', font=(15))
        dd2.pack(pady=10)
        km = tk.Entry(self, font=('Bahnschrift SemiBold', 30, 'bold'), fg='black')
        km.pack(pady=20)
        rastoyanie = 50000

        def dostavka():
            summ = rastoyanie
            dd2.config(text=int(summ) * int(km.get()))

        dostavka_button = tk.Button(self, command=dostavka, text='Цена за доставку',
                                    font=('Bernard MT Condensed', 15, 'bold'))
        dostavka_button.pack(pady=10)

        def return_MenuPage():
            controller.show_frame('Cars')

        return_button = tk.Button(self, text='Back', command=return_MenuPage,font=('Candara', 10, 'bold'), fg='white', bg='black')
        return_button.pack(pady=30)






if __name__=='__main__':
    app = SampleApp()
    app.mainloop()