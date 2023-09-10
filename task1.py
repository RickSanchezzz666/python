from tkinter import *

window = Tk()
window.title('grey59')
window.geometry('666x666')
window.configure(bg='grey')

number1 = 6
number2 = 10.5
boolean = True
stringLine = 'greyfivenine'

labelText = f"{type(number1)}: {number1},\n {type(number2)}: {number2},\n {type(boolean)}: {boolean},\n {type(stringLine)}: {stringLine}"

label = Label(window, text=labelText, font=('Times', '18'),fg='blue')
label.pack()
label.mainloop()


window.mainloop()