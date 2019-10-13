import tkinter as tk

class NTUsystem(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Real Time NTU Canteen System", font=('Helvetica', 20, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="View Stalls", width = 40,
                  command=lambda: master.switch_frame(ViewS)).pack()
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitT)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(OperT)).pack()
        tk.Button(self, text="Set date and time", width = 40,
                  command=lambda: master.switch_frame(dateT)).pack()
        tk.Button(self, text="Exit", width = 40, command=self.destroy).pack()

class ViewS(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="View Stalls", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Mini Wok", width = 40,
                  command=lambda: master.switch_frame(miniwok)).pack()
        tk.Button(self, text="Chicken Rice", width = 40,
                  command=lambda: master.switch_frame(chicken)).pack()
        tk.Button(self, text="McDonald's", width = 40,
                  command=lambda: master.switch_frame(mc)).pack()
        tk.Button(self, text="Subway", width = 40,
                  command=lambda: master.switch_frame(subway)).pack()
        tk.Button(self, text="The Sandwich Guys", width = 40,
                  command=lambda: master.switch_frame(sandwich)).pack()
        tk.Button(self, text="Return to Home Page", width = 40,
                  command=lambda: master.switch_frame(HomePage)).pack()

class miniwok(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Mini Wok", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            for i,line in enumerate(menu.readlines()):
                if i>=1 and i<=5:
                    menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)

class chicken(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Chicken Rice", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            for i,line in enumerate(menu.readlines()):
                if i>=8 and i<=12:
                    menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)


class mc(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="McDonald's", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            for i,line in enumerate(menu.readlines()):
                if i>=15 and i<=27:
                    menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)

class subway(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Subway", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            for i,line in enumerate(menu.readlines()):
                if i>=30 and i<=33:
                    menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)

class sandwich(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="The Sandwich Guys", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            for i,line in enumerate(menu.readlines()):
                if i>=36 and i<=37:
                    menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)


class WaitT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Calculation of estimated waiting time", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack()

class OperT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        scrollbar=tk.Scrollbar(self)
        scrollbar.pack(side = tk.RIGHT, fill = 'y')
        mylist = tk.Listbox(self, yscrollcommand = scrollbar.set)
        with open('operating time.txt') as time:
            for line in time.readlines():
                    operatinghour = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    mylist.insert(tk.ACTIVE, operatinghour)
        mylist.pack(fill='both')
        scrollbar.config(command = mylist.yview)
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack()

class dateT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Set system date and time", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack()


m = NTUsystem()
m.title('NTU Canteen System')
m.mainloop()
