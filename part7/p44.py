from tkinter import *
import random as r
def display():
    user_ans = float(txt_ans.get())
    if user_ans == ans:
        result =  "Correct!\n"
    else:
        result = f"Better Luck Next Time! Answer: {ans}\n"
    
    lblDisplay = Label(root, text=result)
    lblDisplay.place(relx=0.1, rely=0.55)
def get_question():
    num1 = r.randint(1, 99)
    num2 = r.randint(1, 9)
    operations = ['+', '-', '*', '/']
    # operations = ['/']
    operation = r.choice(operations)
    if operation == '/':
        num1 = num1 * num2  # ensure divisibility
        if num1>100:
            num1 = r.randint(1, 100//num2)*num2
        
    return f"{num1} {operation} {num2}"
def main():
    global txt_ans, ans, root
    root = Tk()
    root.geometry("500x300")
    root.title("Math Question Paper:")
    root.option_add("*Font","Arial 14 bold")
    label = Label(root, text="Math Quiz")
    label.place(relx=0.1, rely=0.1)
    root.option_add("*Font","Arial 10 bold")
    ans = get_question()
    label_name = Label(root, text=f"What is {ans}:   ")
    label_name.place(relx=0.1, rely=0.25)
    ans = eval(ans)
    txt_ans = Entry(root)
    txt_ans.place(relx = 0.3, rely=0.25)
    btnSubmit = Button(root, text="Submit", command=display)
    btnSubmit.place(relx=0.1, rely=0.4)
    root.mainloop()
main()
 