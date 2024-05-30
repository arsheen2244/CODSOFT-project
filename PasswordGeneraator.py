from tkinter import *
import string
import random
import pyperclip

root=Tk()
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')

def generate():
    lowerCase=string.ascii_lowercase
    UpperCase=string.ascii_uppercase
    numbers=string.digits
    special_Characters=string.punctuation

    sumUp=lowerCase+UpperCase+numbers+special_Characters
    password_length=int(length_box.get())
    password = random.sample(sumUp,password_length)
   

    if choice.get()==1:
        entry.insert(0,random.sample(lowerCase,password_length))
    
    if choice.get()==2:
        entry.insert(0,random.sample(lowerCase+UpperCase+numbers,password_length))
    
    if choice.get()==3:
        entry.insert(0,random.sample(sumUp,password_length))
    
    
def copy():
    random_password=entry.get()
    pyperclip.copy(random_password)


passwordLabel=Label(root,text= "Password Generator",font=("times new roman",20,'bold'),bg='gray20',fg="white")
passwordLabel.grid(pady=8)

weakrodioButton=Radiobutton(root,text="Weak",value=1,variable=choice,font=Font)
weakrodioButton.grid(pady=5)

MediumrodioButton=Radiobutton(root,text="Medium",value=2,variable=choice,font=Font)
MediumrodioButton.grid(pady=5)

StrongrodioButton=Radiobutton(root,text="Strong",value=3,variable=choice,font=Font)
StrongrodioButton.grid(pady=5)

lengthLabel=Label(root,text='Password length',font=Font ,bg='gray20',fg='white')
lengthLabel.grid(pady=5)

length_box=Spinbox(root,from_=5 ,to_=18, width=5 ,font=Font)
length_box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generate)
generateButton.grid(pady=5)

entry=Entry(root,width=17,bd=4,font=Font)
entry.grid(pady=5)

copyButton=Button(root,text='Copy the Password',font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()