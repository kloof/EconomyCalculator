import tkinter as tk
from tkinter import *
import sys

class GUI():
    def __init__(self) -> None:
        
        self.scheduler = None
        self.root = tk.Tk()
        self.root.geometry('200x500')


        self.i = StringVar(self.root)
        self.n = StringVar(self.root)
        self.g = StringVar(self.root)

        self.perclable = Label(self.root, text='Interest rate (ex. 15%)')
        self.perclable.pack(pady=(20,0))

        self.percentage = Entry(self.root, justify='center', textvariable=self.i)
        self.percentage.pack(pady=0)

        self.yearslable = Label(self.root, text='Years')
        self.yearslable.pack(pady=(15,0))

        self.years = Entry(self.root, justify='center', textvariable=self.n)
        self.years.pack(pady=0)

        self.geometriclable = Label(self.root, text='Geometric rate (ex. 10%)')
        self.geometriclable.pack(pady=(20,0))

        self.geometric = Entry(self.root, justify='center', textvariable=self.g)
        self.geometric.pack(pady=0)


        self.F_P = StringVar(self.root, 'F/P: N/A')
        self.P_F = StringVar(self.root, 'P/F: N/A')

        self.P_A = StringVar(self.root, 'P/A: N/A')
        self.A_P = StringVar(self.root, 'A/P: N/A')

        self.F_A = StringVar(self.root, 'F/A: N/A')
        self.A_F = StringVar(self.root, 'A/F: N/A')

        self.P_G = StringVar(self.root, 'P/G: N/A')
        self.A_G = StringVar(self.root, 'F/G: N/A')

        self.P_A_g = StringVar(self.root, 'F/A (Geometric): N/A')

        self.F_P_lable = Label(self.root, textvariable=self.F_P, anchor='w')
        self.P_F_lable = Label(self.root, textvariable=self.P_F, anchor='w')

        self.P_A_lable = Label(self.root, textvariable=self.P_A, anchor='w')
        self.A_P_lable = Label(self.root, textvariable=self.A_P, anchor='w')

        self.F_A_lable = Label(self.root, textvariable=self.F_A, anchor='w')
        self.A_F_lable = Label(self.root, textvariable=self.A_F, anchor='w')

        self.P_G_lable = Label(self.root, textvariable=self.P_G, anchor='w')
        self.A_G_lable = Label(self.root, textvariable=self.A_G, anchor='w')

        self.P_A_g_lable = Label(self.root, textvariable=self.P_A_g, anchor='w')


        self.F_P_lable.pack(padx=(35,0), pady=(30,0), fill=BOTH)
        self.P_F_lable.pack(padx=(35,0), fill=BOTH)
        self.P_A_lable.pack(padx=(35,0), fill=BOTH)
        self.A_P_lable.pack(padx=(35,0), fill=BOTH)
        self.F_A_lable.pack(padx=(35,0), fill=BOTH)
        self.A_F_lable.pack(padx=(35,0), fill=BOTH)
        self.P_G_lable.pack(padx=(35,0), fill=BOTH)
        self.A_G_lable.pack(padx=(35,0), fill=BOTH)
        self.P_A_g_lable.pack(padx=(35,0), pady=(15,0), fill=BOTH)

        self.b = Button(self.root, command=sys.exit, text='Quit', width=10)
        self.b.pack(pady=(30,0))

        self.i.trace_add('write', self.on_change)
        self.g.trace_add('write', self.on_change)
        self.n.trace_add('write', self.on_change)

        self.root.mainloop()


    def calculate(self):
        
        try:

            try:
                i = float(self.i.get().strip('%'))/100
                n = float(self.n.get())
            except:
                
                self.F_P.set('F/P: N/A')
                self.P_F.set('P/F: N/A')
                self.P_A.set('P/A: N/A')
                self.A_P.set('A/P: N/A')
                self.F_A.set('F/A: N/A')
                self.A_F.set('A/F: N/A')
                self.P_G.set('P/G: N/A')
                self.A_G.set('F/G: N/A')
                self.P_A_g.set('F/A (Geometric): N/A')
                

            if self.g.get() != '':
                try:
                    g = float(self.g.get().strip('%'))/100
                except:
                    self.P_A_g.set('F/A (Geometric): N/A')

            



            f_p = round((1+i)**n, 4)
            p_f = round(1/f_p, 4)

            self.F_P.set(f'F/P: {f_p}')
            self.P_F.set(f'P/F: {p_f}')

            p_a = round((((1+i)**n - 1)/(i*(1+i)**n)),4)
            a_p = round(1/p_a, 4)

            self.P_A.set(f'P/A: {p_a}')
            self.A_P.set(f'A/P: {a_p}')

            f_a = round((((1+i)**n - 1)/(i)),4)
            a_f = round(1/f_a, 4)

            self.F_A.set(f'F/A: {f_a}')
            self.A_F.set(f'A/F: {a_f}')

            p_G = round((((1+i)**n - i*n - 1)/(i**2 * (1+i)**n)),4)
            a_G = round(((1/i)-(n/((1+i)**n - 1))),4)

            self.P_G.set(f'P/G: {p_G}')
            self.A_G.set(f'A/G: {a_G}')


            if i == g:
                print('here')
                p_a_g = round((n/(1+i)),4)
            else:
                p_a_g = round(((1-((1+g)/(1+i))**n)/(i-g)),4)
            
            self.P_A_g.set(f'F/A (Geometric): {p_a_g}')


        except:
            pass
    
    
    def on_change(self, *args):
        if self.scheduler:
            self.years.after_cancel(self.scheduler)
            self.percentage.after_cancel(self.scheduler)
            self.geometric.after_cancel(self.scheduler)

        self.scheduler = self.years.after(200, self.calculate)
        self.scheduler = self.percentage.after(200, self.calculate)
        self.scheduler = self.geometric.after(200, self.calculate)
    

GUI()