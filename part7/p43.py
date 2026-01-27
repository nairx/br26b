from tkinter import *
def display():
    name = txtName.get()
    lblDisplay = Label(root,text="Hello " + name)
    lblDisplay.place(relx=0.1,rely=0.55)
def main():
    global txtName,root
    root = Tk()
    root.geometry("500x300")
    root.title("My Application")
    root.option_add("*Font","aerial 14 bold")
    label = Label(root,text="My Application")
    label.place(relx=0.1,rely=0.1)
    root.option_add("*Font","aerial 10 bold")
    label = Label(root,text="Name:")
    label.place(relx=0.1,rely=0.25)
    txtName = Entry(root)
    txtName.place(relx=0.25,rely=0.25)
    btnSubmit = Button(root,text="Submit",command=display)
    btnSubmit.place(relx=0.1,rely=0.4)
    root.mainloop()
main()