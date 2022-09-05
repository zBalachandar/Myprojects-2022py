from msilib.schema import RadioButton
from tkinter import StringVar
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.tittle=("Radio Buttons")

player=StringVar()
player.set("High")
playermap =[
    ("CHAN","Higher"),
    ("Selvi", "Supreme"),
    ("Ramu", "High-End")
]
for name, team in playermap:
   Radiobutton(root, text=name, variable= player, value=team).pack()

def buttonclick():
    Label(root, text=player.get()).pack()

Button(root, text="Click HERE", command= buttonclick).pack()

root.mainloop()