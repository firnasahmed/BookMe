
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
			cur = con.cursor()

			cur.execute("select * from user_information where username=%s and password = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = win)
				close()
				deshboard()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)

#---------------------------------------------------------------End Login Function ---------------------------------

#---------------------------------------------------- DeshBoard Panel -----------------------------------------
def deshboard():

	def book():
		if vehicle_name.get() =="" or day.get() =="" or month.get() == "" or year.get() == "":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = des)

		else:
			con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
			cur = con.cursor()

			cur.execute("insert bookings set vehicle_name ='" + vehicle_name.get() + "', day ='" +  day.get() + "', month = '" + month.get() + "', year = '" + year.get() +"'")
			con.commit()	
			con.close()
			messagebox.showinfo("Success" , "Booked Vehicle " , parent = des)

	



	des = Tk()
	des.title("User Panel BookMe Cab Service")	
	des.maxsize(width=800 ,  height=500)
	des.minsize(width=800 ,  height=500)		

		#heading label
	heading = Label(des , text = f"User Name : {user_name.get()}" , font = 'Verdana 20 bold',bg='red')
	heading.place(x=220 , y=50)

	f=Frame(des,height=1,width=800,bg="green")
	f.place(x=0,y=95)

	con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
	cur = con.cursor()

	cur.execute("select * from user_information where username ='"+ user_name.get() + "'")
	row = cur.fetchall()

	a=Frame(des,height=1,width=400,bg="green")
	a.place(x=0,y=195)

	b=Frame(des,height=100,width=1,bg="green")
	b.place(x=400,y=97)

	for data in row: 
		first_name = Label(des, text= f"First Name : {data[1]}" , font='Verdana 10 bold')
		first_name.place(x=20,y=100)

		last_name = Label(des, text= f"Last Name : {data[2]}" , font='Verdana 10 bold')
		last_name.place(x=20,y=130)

		age = Label(des, text= f"Age : {data[3]}" , font='Verdana 10 bold')
		age.place(x=20,y=160)

		gender = Label(des, text= f"ID : {data[0]}" , font='Verdana 10 bold')
		gender.place(x=250,y=100)

		city = Label(des, text= f"City : {data[5]}" , font='Verdana 10 bold')
		city.place(x=250,y=130)

		add = Label(des, text= f"Address : {data[6]}" , font='Verdana 10 bold')
		add.place(x=250,y=160)

	# BookMe App
	heading = Label(des , text = "Book A Vehicle" , font = 'Verdana 20 bold')
	heading.place(x=30 , y=200)	

	# Book Vehicle 
	Vehicle= Label(des, text= "Vehicle:" , font='Verdana 10 bold')
	Vehicle.place(x=30,y=245)

	Day = Label(des, text= "Day (DD/MM/YYYY):" , font='Verdana 10 bold')
	Day.place(x=30,y=275)


	# Book Entry Box
	vehicle_name = tk.StringVar()
	day = StringVar()
	month = tk.StringVar()
	year = StringVar()

	vehicle_list= ttk.Combobox(des, width=30, textvariable= vehicle_name, state='readonly')
	car = 'Car'
	van = 'Van'
	threewheel = 'Three Wheel'
	lorry = 'Lorry'
	truck = 'Truck'
	vehicle_list['values']=(car,van,threewheel,lorry,truck)
	vehicle_list.current(0)
	vehicle_list.place(x=120,y=245)

	Day = Entry(des, width=5 , textvariable = day)
	Day.place(x=120 , y=300)

	Month_Box= ttk.Combobox(des, width=10, textvariable=month, state='readonly')
	Month_Box['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
	Month_Box.current(0)
	Month_Box.place(x=158,y=300)

	Year = Entry(des, width=10 , textvariable = year)
	Year.place(x=245 , y=300)
	

	# button 

	btn= Button(des, text = "Book" ,font='Verdana 10 bold', width = 20, command = book)
	btn.place(x=130, y=335)




	con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
	cur = con.cursor()

	cur.execute("select * from user_information where username ='"+ user_name.get() + "'")
	rows = cur.fetchall()


#--------------------------Available Vehicles------------------------------------------------

	con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
	cur = con.cursor()

	# Available Vehicle Details - Car
	cur.execute("select car_id,car_name,car_cooler,car_count from car")
	rows = cur.fetchall()

	heading = Label(des , text = f"Available Vehicles" , font = 'Verdana 15 bold')
	heading.place(x=460 , y=120)

	headingC = Label(des , text = f"Cars" , font = 'Verdana 12 bold')
	headingC.place(x=460 , y=160)

	for cr in rows:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=460,y=180)

		d2 = Label(des, text= f" | {cr[2]}" , font='Verdana 10 bold')
		d2.place(x=580,y=180)

		d3 = Label(des, text= f" | Passengers: {cr[3]}" , font='Verdana 10 bold')
		d3.place(x=640,y=180)


	# Available Vehicle Details - Van
	cur.execute("select van_id,van_name,van_cooler,van_count from van")
	rows2 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Vans" , font = 'Verdana 12 bold')
	headingC.place(x=460 , y=210)

	for cr in rows2:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=460,y=230)

		d2 = Label(des, text= f" | {cr[2]}" , font='Verdana 10 bold')
		d2.place(x=580,y=230)

		d3 = Label(des, text= f" | Passengers: {cr[3]}" , font='Verdana 10 bold')
		d3.place(x=640,y=230)


	# Available Vehicle Details - threewheel
	cur.execute("select tw_id,tw_name,tw_count from threewheel")
	rows3 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Three Wheels" , font = 'Verdana 12 bold')
	headingC.place(x=460 , y=260)

	for cr in rows3:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=460,y=280)

		d3 = Label(des, text= f" | Passengers: {cr[2]}" , font='Verdana 10 bold')
		d3.place(x=580,y=280)


	# Available Vehicle Details - Lorry
	cur.execute("select lorry_id,lorry_name,lorry_load from lorry")
	rows4 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Lorry" , font = 'Verdana 12 bold')
	headingC.place(x=460 , y=310)

	for cr in rows4:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=460,y=330)

		d3 = Label(des, text= f" | Load: {cr[2]}kg" , font='Verdana 10 bold')
		d3.place(x=580,y=330)


	# Available Vehicle Details - Truck
	cur.execute("select truck_id,truck_name,truck_size from truck")
	rows5 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Truck" , font = 'Verdana 12 bold')
	headingC.place(x=460 , y=360)

	for cr in rows5:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=460,y=380)

		d3 = Label(des, text= f" | Size: {cr[2]}ft" , font='Verdana 10 bold')
		d3.place(x=580,y=380)
	




					
#-----------------------------------------------------End Deshboard Panel -------------------------------------
#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
	# signup database connect 
	def action():
		if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
				cur = con.cursor()
				cur.execute("select * from user_information where username=%s",user_name.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
				else:
					cur.execute("insert into user_information(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						age.get(),
						var.get(),
						city.get(),
						add.get(),
						user_name.get(),
						password.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)

	# close signup function			
	def switch():
		winsignup.destroy()

	# clear data function
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		age.delete(0,END)
		var.set("Male")
		city.delete(0,END)
		add.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)


	# start Signup Window	

	winsignup = Tk()
	winsignup.title("User Signup - BookMe Cab Service")
	winsignup.maxsize(width=500 ,  height=600)
	winsignup.minsize(width=500 ,  height=600)


	#heading label
	heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
	heading.place(x=80 , y=60)

	# form data label
	first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold')
	first_name.place(x=80,y=130)

	last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold')
	last_name.place(x=80,y=160)

	age = Label(winsignup, text= "Age :" , font='Verdana 10 bold')
	age.place(x=80,y=190)

	Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
	Gender.place(x=80,y=220)

	city = Label(winsignup, text= "City :" , font='Verdana 10 bold')
	city.place(x=80,y=260)

	add = Label(winsignup, text= "Address :" , font='Verdana 10 bold')
	add.place(x=80,y=290)

	user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
	user_name.place(x=80,y=320)

	password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
	password.place(x=80,y=350)

	very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
	very_pass.place(x=80,y=380)

	# Entry Box ------------------------------------------------------------------

	first_name = StringVar()
	last_name = StringVar()
	age = IntVar(winsignup, value='0')
	var= StringVar()
	city= StringVar()
	add = StringVar()
	user_name = StringVar()
	password = StringVar()
	very_pass = StringVar()


	first_name = Entry(winsignup, width=40 , textvariable = first_name)
	first_name.place(x=200 , y=133)


	
	last_name = Entry(winsignup, width=40 , textvariable = last_name)
	last_name.place(x=200 , y=163)

	
	age = Entry(winsignup, width=40, textvariable=age)
	age.place(x=200 , y=193)

	
	Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
	Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)


	city = Entry(winsignup, width=40,textvariable = city)
	city.place(x=200 , y=263)


	
	add = Entry(winsignup, width=40 , textvariable = add)
	add.place(x=200 , y=293)

	
	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=200 , y=323)

	
	password = Entry(winsignup, width=40, show="*" , textvariable = password)
	password.place(x=200 , y=353)

	
	very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
	very_pass.place(x=200 , y=383)


	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
	btn_signup.place(x=200, y=413)


	btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=280, y=413)


	sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
	sign_up_btn.place(x=350 , y =20)


	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	


	

#------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("User Login - BookMe Cab Service")

# window size
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)


#heading label
heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win , text="Switch To Sign up" , command = signup )
sign_up_btn.place(x=350 , y =20)



win.mainloop()

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------