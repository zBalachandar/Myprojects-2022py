from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Photo Gallery")

Amma_image = ImageTk.PhotoImage(Image.open(r"C:\Users\S.ELUMALAI\Desktop\my projects in python\Ma.jpg"))
java_image = ImageTk.PhotoImage(Image.open(r"C:\Users\S.ELUMALAI\Desktop\my projects in python\java.png"))
js_image = ImageTk.PhotoImage(Image.open(r"C:\Users\S.ELUMALAI\Desktop\my projects in python\js.png"))

images_list = [Amma_image, java_image, js_image]

my_label = Label(image=images_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def back(index):
    global my_label
    global back_button
    global next_button

    if (index == 0):
     return

    my_label.grid_forget() 
    my_label = Label(image=images_list[index-1])
    my_label.grid(row=0, column=0, columnspan=3)


    back_button = Button(root, text="Back", command=lambda: back(index-1))
    next_button = Button(root, text="Next", command=lambda: next(index-1))
   
    back_button.grid(row=1, column=0)
    next_button.grid(row=1, column=2)
    return

def next(index):
   global my_label
   global back_button
   global next_button

   if (index == 2):
    return

   my_label.grid_forget() 
   my_label = Label(image=images_list[index+1])
   my_label.grid(row=0, column=0, columnspan=3)


   back_button = Button(root, text="Back", command=lambda: back(index+1))
   next_button = Button(root, text="Next", command=lambda: next(index+1))
   
   back_button.grid(row=1, column=0)
   next_button.grid(row=1, column=2)
   return    

back_button = Button(root, text="Back", command=lambda: back(0))
next_button = Button(root, text="Next", command=lambda: next(0))
exit_button = Button(root, text="Exit", command=root.quit)

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
next_button.grid(row=1, column=2)

root.mainloop()