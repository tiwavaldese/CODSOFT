#importing tkinter library
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title("My Calculator")
window.geometry("400x500+400+100")

frame = tk.Frame(master=window,bg="skyblue", padx=10)
frame.pack()
#entry=tk.Entry(master=frame,relief=SUNKEN,borderwidth=3,width=30)
#entry.grid(row=0,column=0,columnspan=4,ipady=2,pady=2)

#Addition
def addition(n1,n2):
    return n1 + n2

#Substraction
def substraction(n1,n2):
    return n1 - n2

#Multiplication
def multiplication(n1,n2):
    return n1 * n2

#Division
def division(n1,n2):
    return n1 / n2

print("Select Operations")
print("1.Addition\n"
      "2.Substraction\n"
      "3.Multiplication\n"
      "4.Division\n")

operation = int(input("Input choice of operation 1/2/3/4:"))
n1 =float(Input("Input first number:"))
n2 =float(Input("Input second number:"))

window.mainloop()
