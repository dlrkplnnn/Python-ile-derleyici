from tkinter import *
import tkinter as tk
from io import StringIO 
import sys



def terminal(): #kodu çalıştırıp gui üzeridneki terminalde çıktı gösterir

    giriş=girdi.get("1.0", tk.END)

    sonuc=sys.stdout
    sonsonuc=sys.stdout=StringIO()
    
    exec(giriş)

    terminal=sonsonuc.getvalue()
    cikti.delete("1.0", tk.END)
    cikti.insert(tk.END, terminal)
    
    sys.stdout =sonuc
   
    
def sil(): 

    cikti.delete("1.0", tk.END)
    girdi.delete("1.0", tk.END)
    

pencere=tk.Tk()
pencere.title=("derleyici")

girdi=tk.Text(pencere, width=40, height=10)
girdi.pack()


cikti =tk.Text(pencere,height=10, width=40)
cikti.pack()

run=tk.Button(text='Çalıştır',command=terminal)
run.pack()

delete=tk.Button(text='Sil',command=sil)
delete.pack()


pencere.mainloop()