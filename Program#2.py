import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk,Image

def question_result():
    name = simpledialog.askstring("Name", "Please state your name: \n Ex: Juan T. Lazy \n")
        
    input_name = name
    
    age = simpledialog.askstring("Age","Please state your age in years: \n Note: Please input numbers only \n")
    
    input_age = age
    
    address = simpledialog.askstring("Address", "Please state where you currently live: \n")
     
    input_address = address

    question_review = f"Hello! {input_name}!" + f"\nYou are {input_age} years old," + f"\nYou live at {input_address}." + f"\n" + f"\n" + f"\n" + f"Thank you for participating!" + f" Have a nice day ✮⋆˙" + f"\n" + f"__________________________________________________" + f"\n" + f" \n ♡∩_∩                        :¨ ·.· ¨:" + f"\n （„• ֊ •„)♡                     `· . ꔫ" + f"\n ┏━∪∪━━━━━━━━━━━━━━━━━━┓" + f"\n Thank you sir for watching! \n Hope you liked it<3" + f"\n ┗━━━━━━━━━━━━━━━━━━━━━━┛"
    messagebox.showinfo("Results",question_review )

root = tk.Tk()
root.geometry("1280x720")
root.title("My_Program#2")
root.config(bg= "#FDF5DF")

home_label = tk.Label(root, text = "Hi Sir Danilo! This is my work for the \n 2nd Programming Activity.")
home_label.config(font = ("Ink Free", 30,"bold"), fg= '#6499E9', bg= '#FDF5DF')
home_label.pack()

home_label = tk.Label(root, text = "This simple program will asks \n name, age and address of the user")
home_label.config(font = ("Ink Free", 25), fg= '#6499E9', bg= '#FDF5DF')
home_label.pack()

home_img = Image.open("home_image/think_then_forget.png")
resized = home_img.resize((450,350))
new_home_img = ImageTk.PhotoImage(resized)
home_img_label = tk.Label(root, image=new_home_img, borderwidth=5)
home_img_label.pack(padx =20, pady =20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=10)
buttonframe.columnconfigure(1, weight=10)
buttonframe.config(bg='#FDF5DF')

start_btn1 = tk.Button(buttonframe, text = "START", command = question_result)
start_btn1.config(font = ("Ink Free", 18,"bold"), bg= '#FDF5DF', fg = '#6499E9') 
start_btn1.grid(row = 0, column = 0, padx=50)

start_btn2 = tk.Button(buttonframe, text = "CLOSE", command = root.quit)
start_btn2.config(font = ("Ink Free", 18,"bold"), bg= '#FDF5DF', fg = '#6499E9')
start_btn2.grid(row = 0, column = 1, padx=70, pady=50)

buttonframe.pack()

root.mainloop()