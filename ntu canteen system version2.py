import tkinter as tk
import datetime
today = datetime.datetime.now()
now = str(today)
hour = int(now[11:13])
minute = int(now[14:16])
sec = int(now[17:19])
time1 = int(now[11:13]+now[14:16])
day = today.strftime('%A')

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
        tk.Button(self, text="Return to Home Page", width = 40,
                  command=lambda: master.switch_frame(HomePage)).pack()

class miniwok(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Mini Wok", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
                if day == 'Sunday':
                    tk.Label(self, text="The stall is closed today.", font=('Helvetica', 18, "bold")).pack(side="top")
                elif day == 'Saturday':
                    if time1>1700 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                else:
                    if time1>2130 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitT)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper1)).pack()
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)

class chicken(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Chicken Rice", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
                if day == 'Sunday':
                    tk.Label(self, text="The stall is closed today.", font=('Helvetica', 18, "bold")).pack(side="top")
                elif day == 'Saturday':
                    if time1>1700 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuchicken = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                else:
                    if time1>2130 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuchicken = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitT)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper2)).pack()
        tk.Button(self, text="Return", width = 40,
                 command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)


class mc(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="McDonald's", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            if day == 'Sunday':
                for i,line in enumerate(menu.readlines()):
                    if hour>=10 and hour<11:
                        if i>=16 and i<=20:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    elif hour>=11 and hour<22:
                        if i>=23 and i<=27:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    else:
                        tk.Label(self, text="McDonald's is closed now.", font=('Helvetica', 18)).pack()
            else:
                for i,line in enumerate(menu.readlines()):
                    if hour>=7 and hour<11:
                        if i>=16 and i<=20:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    elif hour>=11 and hour<24:
                        if i>=23 and i<=27:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    else:
                        tk.Label(self, text="McDonald's is closed now.", font=('Helvetica', 18)).pack()
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitT)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper3)).pack()
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)

class WaitT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Calculation of estimated waiting time", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(ViewS)).pack()

class Oper1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        with open('operating time.txt') as oper:
            for i,line in enumerate(oper.readlines()):
                if i>=1 and i<=6:
                    mini = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(miniwok)).pack()
#operating hours for mini wok

class Oper2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        with open('operating time.txt') as oper:
            for i,line in enumerate(oper.readlines()):
                if i>=9 and i<=14:
                    chick = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(chicken)).pack()
#operating hours for chicken rice

class Oper3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        with open('operating time.txt') as oper:
            for i,line in enumerate(oper.readlines()):
                if i>=17 and i<=22:
                    mc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(mc)).pack()
#operating hours for mcdonald

class dateT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Set system date and time", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Return to Home Page", width = 40,
                  command=lambda: master.switch_frame(HomePage)).pack()


m = NTUsystem()
m.title('NTU Canteen System')
m.mainloop()
