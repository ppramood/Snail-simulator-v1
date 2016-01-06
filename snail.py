import tkinter as tk
from tkinter import messagebox

# ---------- Fuction Area ---------#
def simulate(current_height=0,plant_height=30,number_days=0,snail_climb=3,snail_drop=2):
	while True:
		number_days+=1
		current_height+=snailclimbbox()
		if current_height >= plantheightbox():
			break
		current_height-=snaildropbox()
	remove=boxclear()
	outputlabel.insert(tk.END,number_days)

def plantheightbox(plant_height=30):
	if userentry2.get():
		return int(userentry2.get())
	else:
		return plant_height



def snailclimbbox(snail_climb=3):
	if userentry.get():
		return int(userentry.get())
	else:
		return snail_climb

def snaildropbox(snail_drop=2):
	if userentry1.get():
		return int(userentry1.get())
	else:
		return snail_drop

def boxclear():
	outputlabel.delete("1.0",tk.END)

#-----------End Of Fuction Area ------------#
#----------------GUI Area-------------------#


root = tk.Tk()
root.title('Snail Programe')
frame1 = tk.Frame(root)
label1= tk.Label(root,text="A snail climbs up 3 meters every day \n and climbs down 2 meters back down.\n How many days it takes to climb a 30 meter tree?")
label1.grid(row=0,column=1)

button1 = tk.Button(root,text="simulate",command=lambda :simulate() )
button1.grid(row =3,column=0)

infolabel3=tk.Label(root,text="Enter the Plant height (default is 30):").grid(row =2,column=1)

infolabel=tk.Label(root,text="Enter the climb rate (default is 3):").grid(row =3,column=1)

infolabel2=tk.Label(root,text="Enter the Drop rate (default is 2):").grid(row =4,column=1)


userentry = tk.Entry(root)
userentry.grid(row =3,column=2)

userentry1 = tk.Entry(root)
userentry1.grid(row =4,column=2)

userentry2 = tk.Entry(root)
userentry2.grid(row =2,column=2)


outputlabel=tk.Text(root,height =2,width=10)
outputlabel.grid(row =1,column=1)

messagebutton=tk.Button(root,text='info',command=lambda :messagebox.showinfo('info','Snail simulator v1 \ncreated By ppramood'))
messagebutton.grid(row=0,column=2)

root.mainloop()

#---------------End Of GUI------------------#