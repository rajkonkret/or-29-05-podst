import random
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def rysuj_wykres(ax):
    ax.clear()
    r = random.randint(1, 10)
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, r]
    ax.plot(x, y)
    ax.set_title("TEST")
    ax.set_xlabel("OS x")
    ax.set_ylabel("OS y")


class Appim:
    def __init__(self, master):
        self.master = master
        self.master.title("Wykres matplotlib tkinter")

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        rysuj_wykres(self.ax)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button = ttk.Button(self.master, text="Rysuj wykres",
                            command=self.update_plot)
        button.pack()

    def update_plot(self):
        rysuj_wykres(self.ax)
        self.canvas.draw()


okno = tk.Tk()
app = Appim(okno)
okno.mainloop()
# 14:20
