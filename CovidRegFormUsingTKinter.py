# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
from tkinter import font
from tkinter import ttk,messagebox
win =Tk()
win.geometry('1200x%d'%(win.winfo_screenheight()))
win.title('covid-19 vaccine registration')
v1=IntVar(win)
v2=IntVar(win)
v3=IntVar(win)
win.config(borderwidth=3,relief='raised')

Label(win,text='COVID-19 Vaccine Registration Form',font=(font.ITALIC,20,'bold'),fg='blue').place(x=300,y=10)
Label(win,text='Please read below carefully and ask for help if you need',font=(font.NORMAL,10,'bold'),fg='grey').place(x=350,y=40)
ttk.Separator(win,orient='horizontal').place(x=0,y=60,relheight=1,relwidth=1)

ttk.Separator(win,orient='horizontal').place(x=0,y=90,relheight=1,relwidth=1)
Label(win,text='Medical history',font=(font.BOLD,12,'bold'),fg='purple').place(x=30,y=82)
Label(win,text='Yes',font=(font.ITALIC,10,'bold'),fg='grey').place(x=500,y=100)
Label(win,text='No',font=(font.ITALIC,10,'bold'),fg='grey').place(x=600,y=100)
Label(win,text="Don't know",font=(font.BOLD,10,'bold'),fg='grey').place(x=700,y=100)
Label(win,text='*Do you have allergies to latex, food, medications, or vaccine\n components? (such as eggs, thimerosal, gelatin, neomycin, phenol, \n or bovine protein)?',font=(font.BOLD,10,'italic','bold')).place(x=30,y=120)
Label(win,text='*Did you ever experience any serious reaction after getting a vaccine?',font=(font.BOLD,10,'bold','italic')).place(x=30,y=180)
Label(win,text='*In the past year, did you receive a transfusion of blood or blood\n products, or get injected immune (gamma) globulin\n or any antiviral drug?',font=(font.BOLD,10,'bold','italic')).place(x=30,y=210)

Radiobutton(win,height=1,width=2,variable=v1,value=1).place(x=500,y=130)
Radiobutton(win,height=1,width=2,variable=v1,value=2).place(x=600,y=130)
Radiobutton(win,height=1,width=4,variable=v1,value=3).place(x=700,y=130)

Radiobutton(win,height=1,width=2,variable=v2,value=1).place(x=500,y=180)
Radiobutton(win,height=1,width=2,variable=v2,value=2).place(x=600,y=180)
Radiobutton(win,height=1,width=4,variable=v2,value=3).place(x=700,y=180)

Radiobutton(win,height=1,width=2,variable=v3,value=1).place(x=500,y=230)
Radiobutton(win,height=1,width=2,variable=v3,value=2).place(x=600,y=230)
Radiobutton(win,height=1,width=4,variable=v3,value=3).place(x=700,y=230)

ttk.Separator(win,orient='horizontal').place(x=0,y=300,relheight=1,relwidth=1)
Label(win,text='Do you have any of the followings? (select all that apply)',font=(font.BOLD,12,'bold'),fg='purple').place(x=30,y=292)
Checkbutton(win,text='Lung disease',font=(font.BOLD,10,'bold','italic')).place(x=30,y=320)
Checkbutton(win,text='Heart disease',font=(font.BOLD,10,'bold','italic')).place(x=150,y=320)
Checkbutton(win,text='Asthma',font=(font.BOLD,10,'bold','italic')).place(x=270,y=320)
Checkbutton(win,text='Kidney Disease',font=(font.BOLD,10,'bold','italic')).place(x=360,y=320)
Checkbutton(win,text='Diabetes',font=(font.BOLD,10,'bold','italic')).place(x=490,y=320)
Checkbutton(win,text='Anemia',font=(font.BOLD,10,'bold','italic')).place(x=590,y=320)
Checkbutton(win,text='Blood disorder',font=(font.BOLD,10,'bold','italic')).place(x=690,y=320)

ttk.Separator(win,orient='horizontal').place(x=0,y=390,relheight=1,relwidth=1)
Label(win,text='Do you have immunocompromised condition? (select all that apply)',font=(font.BOLD,12,'bold'),fg='purple').place(x=30,y=382)
Label(win,text='Do you have any of the followings? (select all that apply)',font=(font.BOLD,12,'bold'),fg='purple').place(x=30,y=292)
Checkbutton(win,text='Cancer',font=(font.BOLD,10,'bold','italic')).place(x=30,y=420)
Checkbutton(win,text='Leukemia',font=(font.BOLD,10,'bold','italic')).place(x=150,y=420)
Checkbutton(win,text='Lymphoma',font=(font.BOLD,10,'bold','italic')).place(x=270,y=420)
Checkbutton(win,text='HIV/AIDS',font=(font.BOLD,10,'bold','italic')).place(x=370,y=420)
Checkbutton(win,text='Transplant',font=(font.BOLD,10,'bold','italic')).place(x=490,y=420)
Checkbutton(win,text='Asplenia',font=(font.BOLD,10,'bold','italic')).place(x=590,y=420)
Checkbutton(win,text='CSF leak',font=(font.BOLD,10,'bold','italic')).place(x=690,y=420)
Checkbutton(win,text='Cochlear implant',font=(font.BOLD,10,'bold','italic')).place(x=800,y=420)

v4=IntVar(win)
ttk.Separator(win,orient='horizontal').place(x=0,y=472,relheight=1,relwidth=1)
Label(win,text='Have you ever tested positive for COVID-19?',font=(font.BOLD,12,'bold','italic'),fg='purple').place(x=30,y=462)
Radiobutton(win,height=1,width=2,variable=v4,value=1,text='Yes',font=(font.BOLD,10,'bold','italic')).place(x=50,y=490)
Radiobutton(win,height=1,width=2,variable=v4,value=2,text='No',font=(font.BOLD,10,'bold','italic')).place(x=180,y=490)

ttk.Separator(win,orient='horizontal').place(x=0,y=540,relheight=1,relwidth=1)
Label(win,text='In the last 14 days(mark if you have),',font=(font.BOLD,12,'bold','italic'),fg='purple').place(x=30,y=532)
Checkbutton(win,text='travelled internationally',font=(font.BOLD,10,'bold','italic')).place(x=50,y=560)
Checkbutton(win,text='contacted with a person who was confirmed to have COVID-19',font=(font.BOLD,10,'bold','italic')).place(x=300,y=560)

ttk.Separator(win,orient='horizontal').place(x=0,y=600,relheight=1,relwidth=1)
Label(win,text='Do you have any of the followings?',font=(font.BOLD,12,'bold','italic'),fg='purple').place(x=30,y=592)
Checkbutton(win,text='Cough',font=(font.BOLD,10,'bold','italic')).place(x=30,y=630)
Checkbutton(win,text='Cold',font=(font.BOLD,10,'bold','italic')).place(x=110,y=630)
Checkbutton(win,text='Fever',font=(font.BOLD,10,'bold','italic')).place(x=190,y=630)
Checkbutton(win,text='Shortness of breath',font=(font.BOLD,10,'bold','italic')).place(x=665,y=630)
Checkbutton(win,text='Sore throat',font=(font.BOLD,10,'bold','italic')).place(x=565,y=630)
Checkbutton(win,text='Loss of smell/taste',font=(font.BOLD,10,'bold','italic')).place(x=820,y=630)
Checkbutton(win,text='Abdominal pain\n/diarrhea',font=(font.BOLD,10,'bold','italic')).place(x=260,y=630)
Checkbutton(win,text='Abnormal bruising or \nbleeding/eye redness',font=(font.BOLD,10,'bold','italic')).place(x=400,y=630)
def np():
    file=Toplevel(win)
   
    file.geometry('1200x%d'%(win.winfo_screenheight()))
    file.title('covid-19 vaccine registration')
    Label(file,text='COVID-19 Vaccine Registration Form',font=(font.ITALIC,20,'bold'),fg='blue').place(x=300,y=10)
    Label(file,text='Please read below carefully and ask for help if you need',font=(font.NORMAL,10,'bold'),fg='grey').place(x=350,y=40)
    ttk.Separator(file,orient='horizontal').place(x=0,y=60,relheight=1,relwidth=1)
    
    ttk.Separator(file,orient='horizontal').place(x=0,y=90,relheight=1,relwidth=1)
    Label(file,text='Personal Information',font=(font.BOLD,14,'bold'),fg='purple').place(x=30,y=82)
    
    Label(file,text='Name',font=(font.BOLD,12,'bold'),fg='black').place(x=40,y=120)
    Label(file,text='First Name',font=(font.BOLD,8,'bold'),fg='gray').place(x=40,y=160)
    Label(file,text='Last Name',font=(font.BOLD,8,'bold'),fg='gray').place(x=350,y=160)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=40,y=190)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=350,y=190)
    
    Label(file,text='Address',font=(font.BOLD,12,'bold'),fg='black').place(x=40,y=250)
    Label(file,text='street address',font=(font.BOLD,8,'bold'),fg='gray').place(x=40,y=290)
    Entry(file,width=50,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=40,y=320)
    Label(file,text='street address line 2',font=(font.BOLD,8,'bold'),fg='gray').place(x=40,y=350)
    Entry(file,width=50,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=40,y=380)
    Label(file,text='City',font=(font.BOLD,8,'bold'),fg='gray').place(x=40,y=410)
    Label(file,text='State',font=(font.BOLD,8,'bold'),fg='gray').place(x=350,y=410)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=40,y=440)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=350,y=440)
    Label(file,text='Postal / Zip Code',font=(font.BOLD,8,'bold'),fg='gray').place(x=40,y=470)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=40,y=500)
    
    Label(file,text='Email',font=(font.BOLD,12,'bold'),fg='black').place(x=680,y=120)
    Label(file,text='example@example.com',font=(font.BOLD,8,'bold'),fg='gray').place(x=680,y=160)
    Entry(file,width=50,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=680,y=190)
    
    Label(file,text='Phone Number',font=(font.BOLD,12,'bold'),fg='black').place(x=680,y=240)
    Label(file,text="Please enter a valid phone number '(000) 000-0000'",font=(font.BOLD,8,'bold'),fg='gray').place(x=680,y=280)
    Entry(file,width=50,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=680,y=320)
    
    ttk.Separator(file,orient='horizontal').place(x=0,y=550,relheight=1,relwidth=1)
    Label(file,text='Emergency Contact Information',font=(font.BOLD,14,'bold'),fg='purple').place(x=30,y=542)
    
    Label(file,text='Name',font=(font.BOLD,12,'bold'),fg='black').place(x=40,y=580)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=40,y=640)
    Label(file,text='Phone',font=(font.BOLD,12,'bold'),fg='black').place(x=350,y=580)
    Label(file,text="Please enter a valid phone number '(000) 000-0000'",font=(font.BOLD,8,'bold'),fg='gray').place(x=350,y=610)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=350,y=640)
    Label(file,text='Relation',font=(font.BOLD,12,'bold'),fg='black').place(x=660,y=580)
    Entry(file,width=30,font=(font.BOLD,12,'bold','italic'),bg='#e0ffff',fg='#2b3856').place(x=660,y=640)
    def end():
        if messagebox.askquestion('registration','Are you sure to submit?'):
            win.destroy()
    Button(file,text='Submit',activeforeground='yellow',command=end,activebackground='black',bg='blue',fg='white',padx=40,font=(font.BOLD,15,'bold'),wraplength=-1).place(x=1000,y=630)
    

Button(win,text='Next   >',activeforeground='yellow',command=np,activebackground='black',bg='blue',fg='white',padx=40,font=(font.BOLD,15,'bold'),wraplength=-1).place(x=1000,y=630)
win.mainloop()