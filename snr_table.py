from tkinter import *
import sys
from tkinter import messagebox

def snr_table_pressed(event):
	messagebox.showinfo("Snr_Infomation","Your Table Is Ready! Lets Rock!")
	num = int(entry.get())
	snr_1=' Snr Table of ' + str(num) + '\n---------------\n'
	for i in range(1,11):
		snr_1 = snr_1 + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"

	snr_column.configure(text = snr_1, justify=LEFT)

def snr_table_enter():
	messagebox.showinfo("Snr_Infomation","Your Table Is Ready! Lets Rock!")
	num = int(entry.get())
	snr_1=' Snr Table of ' + str(num) + '\n---------------\n'
	for i in range(1,11):
		snr_1 = snr_1 + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"

	snr_column.configure(text = snr_1, justify=LEFT)

def snr_information():
	messagebox.showinfo("Welcome To Snr ", "Hello Guys, Welcome Back To Snr Multiplication Table's Generator. This was Devoloped By Snr_Sunny(User_ID:-Sunny_1177_143)")

def snr_help_inform():
	messagebox.showinfo("Snr_Infomation","Enter Your Number In The Text Field And Press Enter Or Click On Get Table Button.")

def Snr_quit():
	messagebox.showinfo("Snr_Infomation","Bye! Meet You Later")
	sys.exit()

Snr_root = Tk()

Snr_root.geometry("1200x650+650+650")

Snr_root.title("SNR MULTIPLICATION TABLE GENERATOR ")

Snr_root.iconbitmap(r'C:\Users\sai teja\Documents\—Pngtree—c4d cool black red gold_4581725.png')

Snr_root.configure(background="goldenrod1")

Snr_Message = Button(text= ' Enter a Number :- ',bg = "blue" ,  activebackground = "goldenrod1", font=( ' sens-serif ' , 20))

snr_label = Button(text='*WELCOME TO SNR*', bg = "blue",activebackground = 'goldenrod1', font =( ' sens-serif ' , 18), command = snr_information)

snr_column = Label(font=( ' sens-serif ' ,  18))

snr_quit_button = Button(text = "Quit",bg = "blue", font =( ' sens-serif ' , 18), command = Snr_quit , activebackground = 'goldenrod1')

entry = Entry(font=( ' sens-serif ' , 18), width=6 )

snr_button = Button(text= ' Get Table' ,bg = "blue", font=( ' sens-serif ', 18),activebackground = 'goldenrod1', command=snr_table_enter)

snr_help = Button(text ="Help", bg = "blue", font=( ' sens-serif ', 17),activebackground = 'goldenrod1',command =snr_help_inform)

Snr_root.bind("<Return>", snr_table_pressed)

Snr_Message.grid(row=1, column=2,padx=10, pady=10)

snr_quit_button.grid(row= 2, column= 3)

snr_label.grid(row=0, column=5,padx=10, pady=10)

entry.grid(row=1, column=3,padx=10, pady=10, ipady=10,  )

snr_button.grid(row=1, column=4,padx=10, pady=10)

snr_help.grid(row= 2, column=5,)

snr_column.grid(row=1, column=5, columnspan=3,padx=10, pady=10)

mainloop()