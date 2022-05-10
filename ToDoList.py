from tkinter import *
from tkinter import messagebox


#now adding a spot to add a new task not already in it
def newT():
    task = my_entry.get()
    if task != "":
        listb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("WARNING", "Please enter a task.")
#now for deleting a task
def delT():
    listb.delete(ANCHOR)
    
    
#this creates the window pop up
#starting base for todolist creation
parentwindow = Tk()
#width x height + x-position + y-position
parentwindow.geometry('500x450+500+200')
#adds title to window
parentwindow.title('To Do List')
#config provides the background color
parentwindow.config(bg='#223442')
#if has this, cannot be resized
parentwindow.resizable(width=False, height= False)

#this section will work on creating the frames as first widget
#window over parent window
#pady10 means extra padding around the frame

framing = Frame(parentwindow)
framing.pack(pady=10)

#creating ListBox shown to user
listb = Listbox(
    framing, 
    width=25,
    height=8,
    font=('Times', 20),
    bd=0,
    fg='#464657',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
listb.pack(side=LEFT, fill=BOTH)


#Can create already filled in data that can be altered once window is up
filled_list = [
    'Drink water',
    'Work out #1',
    'Work out #2',
    'Eat breakfast',
    'Eat lunch',
    'Eat dinner',
    'Study language'
    ]
for item in filled_list:
    listb.insert(END, item)


#Now add scrollbars for listbox
scrollbar = Scrollbar(framing)
scrollbar.pack(side=RIGHT, fill=BOTH)

listb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listb.yview)


#this is for the user to enter more on the list
my_entry = Entry(
    parentwindow,
    font=('Times', 24)
    )

my_entry.pack(pady=20)


#frame for buttons and adding buttons
buttons = Frame(parentwindow)
buttons.pack(pady=20)

#This is for adding a new task
addTaskButton = Button(
    buttons,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newT
)
addTaskButton.pack(fill=BOTH, expand=True, side=LEFT)

#this is for deleting a task
delTaskButton = Button(
    buttons, 
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=delT
)
delTaskButton.pack(fill=BOTH, expand=True, side=LEFT)

#mainloop allows the window to be seen infinitely 
parentwindow.mainloop()