
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

			cur.execute("select * from admin_information where username=%s and password = %s",(user_name.get(),password.get()))
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

	des = Tk()
	des.title("Admin Panel BookMe Cab Service")
	des.maxsize(width=800 ,  height=500)
	des.minsize(width=800 ,  height=500)

		#heading label
	heading = Label(des , text = f"User Name : {user_name.get()}" , font = 'Verdana 20 bold',bg='green')
	heading.place(x=240 , y=50)

	f=Frame(des,height=1,width=800,bg="green")
	f.place(x=0,y=95)

	con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
	cur = con.cursor()

	cur.execute("select * from admin_information where username ='"+ user_name.get() + "'")
	row = cur.fetchall()


	for data in row:
		name = Label(des, text= f"Name : {data[1]}" , font='Verdana 10 bold')
		name.place(x=20,y=50)


	# Add Vehicle
	heading = Label(des , text = "Add A Vehicles" , font = 'Verdana 20 bold')
	heading.place(x=470 , y=100)

	def AddCar():
		selcar = Tk()
		selcar.title("Add Car")
		selcar.maxsize(width=400 ,  height=300)
		selcar.minsize(width=400 ,  height=300)

		def AddCar2():
			if car_name.get() =="" or car_cooler.get() =="" or car_count.get() == "":
				messagebox.showerror("Error" , "All Fields Are Required" , parent = selcar)

			else:
				con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
				cur = con.cursor()

				cur.execute("insert car set car_name ='" + car_name.get() + "', car_cooler ='" +  car_cooler.get() + "', car_count = '" + car_count.get()+"'")
				con.commit()	
				con.close()
				messagebox.showinfo("Success" , "Added Vehicle " , parent = selcar)
		
		#heading label
		heading = Label(selcar , text = "Add Car" , font = 'Verdana 20 bold')
		heading.place(x=20 , y=60)

		# form data label
		car_name = Label(selcar, text= "Car Name :" , font='Verdana 10 bold')
		car_name.place(x=20,y=130)


		car_cooler = Label(selcar, text= "Car Cooler Type :" , font='Verdana 10 bold')
		car_cooler.place(x=20,y=160)

		car_count = Label(selcar, text= "Passengers Count :" , font='Verdana 10 bold')
		car_count.place(x=20,y=190)

		# Entry Box ------------------------------------------------------------------

		car_name = StringVar()
		car_cooler = IntVar()
		car_count = IntVar()

		car_name = Entry(selcar, width=30 , textvariable = car_name)
		car_name.place(x=170 , y=133)

		car_cooler = Entry(selcar, width=30,textvariable = car_cooler)
		car_cooler.place(x=170 , y=163)

		car_count = Entry(selcar, width=30, textvariable = car_count)
		car_count.place(x=170 , y=193)

		# button Add Car

		btn_signup = Button(selcar, text = "Add Car" ,font='Verdana 10 bold', command = AddCar2)
		btn_signup.place(x=200, y=253)


	def AddVan():
		selvan = Tk()
		selvan.title("Add Van")
		selvan.maxsize(width=400 ,  height=300)
		selvan.minsize(width=400 ,  height=300)

		def AddVan2():
			if van_name.get() =="" or van_cooler.get() =="" or van_count.get() == "":
				messagebox.showerror("Error" , "All Fields Are Required" , parent = selvan)

			else:
				con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
				cur = con.cursor()

				cur.execute("insert van set van_name ='" + van_name.get() + "', van_cooler ='" +  van_cooler.get() + "', van_count = '" + van_count.get()+"'")
				con.commit()	
				con.close()
				messagebox.showinfo("Success" , "Added Vehicle " , parent = selvan)
		
		#heading label
		heading = Label(selvan , text = "Add Van" , font = 'Verdana 20 bold')
		heading.place(x=20 , y=60)

		# form data label
		van_name = Label(selvan, text= "Van Name :" , font='Verdana 10 bold')
		van_name.place(x=20,y=130)


		van_cooler = Label(selvan, text= "Van Cooler Type :" , font='Verdana 10 bold')
		van_cooler.place(x=20,y=160)

		van_count = Label(selvan, text= "Passengers Count :" , font='Verdana 10 bold')
		van_count.place(x=20,y=190)

		# Entry Box ------------------------------------------------------------------

		van_name = StringVar()
		van_cooler = IntVar()
		van_count = IntVar()

		van_name = Entry(selvan, width=30 , textvariable = van_name)
		van_name.place(x=170 , y=133)

		van_cooler = Entry(selvan, width=30,textvariable = van_cooler)
		van_cooler.place(x=170 , y=163)

		van_count = Entry(selvan, width=30, textvariable = van_count)
		van_count.place(x=170 , y=193)

		# button Add Car

		btn_signup = Button(selvan, text = "Add Van" ,font='Verdana 10 bold', command = AddVan2)
		btn_signup.place(x=200, y=253)


	def AddTw():
		seltw = Tk()
		seltw.title("Add Threewheel")
		seltw.maxsize(width=400 ,  height=300)
		seltw.minsize(width=400 ,  height=300)


		def AddTW2():
			if tw_name.get() =="":
				messagebox.showerror("Error" , "All Fields Are Required" , parent = seltw)

			else:
				con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
				cur = con.cursor()

				cur.execute("insert threewheel set tw_name ='" + tw_name.get() +"'")
				con.commit()	
				con.close()
				messagebox.showinfo("Success" , "Added Vehicle " , parent = seltw)
		
		#heading label
		heading = Label(seltw , text = "Add Threewheel" , font = 'Verdana 20 bold')
		heading.place(x=20 , y=60)

		# form data label
		tw_name = Label(seltw, text= "Threewheel Name :" , font='Verdana 10 bold')
		tw_name.place(x=20,y=130)


		# Entry Box ------------------------------------------------------------------

		tw_name = StringVar()

		tw_name = Entry(seltw, width=30 , textvariable = tw_name)
		tw_name.place(x=170 , y=133)

		# button Add Car

		btn_signup = Button(seltw, text = "Add Threewheel" ,font='Verdana 10 bold', command = AddTW2)
		btn_signup.place(x=200, y=253)

	def AddLorry():
		sellorry = Tk()
		sellorry.title("Add Lorry")
		sellorry.maxsize(width=400 ,  height=300)
		sellorry.minsize(width=400 ,  height=300)

		def AddLorry2():
			if lorry_name.get() =="" or lorry_load.get() =="":
				messagebox.showerror("Error" , "All Fields Are Required" , parent = sellorry)

			else:
				con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
				cur = con.cursor()

				cur.execute("insert lorry set lorry_name ='" + lorry_name.get() + "', lorry_load ='" +  lorry_load.get() +"'")
				con.commit()	
				con.close()
				messagebox.showinfo("Success" , "Added Vehicle " , parent = sellorry)
		
		#heading label
		heading = Label(sellorry , text = "Add Lorry" , font = 'Verdana 20 bold')
		heading.place(x=20 , y=60)

		# form data label
		lorry_name = Label(sellorry, text= "Lorry Name :" , font='Verdana 10 bold')
		lorry_name.place(x=20,y=130)


		lorry_load = Label(sellorry, text= "Lorry Load (kg) :" , font='Verdana 10 bold')
		lorry_load.place(x=20,y=160)


		# Entry Box ------------------------------------------------------------------

		lorry_name = StringVar()
		lorry_load = IntVar()

		lorry_name = Entry(sellorry, width=30 , textvariable = lorry_name)
		lorry_name.place(x=170 , y=133)

		lorry_load = Entry(sellorry, width=30,textvariable = lorry_load)
		lorry_load.place(x=170 , y=163)

		# button Add Car

		btn_signup = Button(sellorry, text = "Add Lorry" ,font='Verdana 10 bold', command = AddLorry2)
		btn_signup.place(x=200, y=253)


	def AddTruck():
		seltruck = Tk()
		seltruck.title("Add Truck")
		seltruck.maxsize(width=400 ,  height=300)
		seltruck.minsize(width=400 ,  height=300)

		def AddTruck2():
			if truck_name.get() =="" or truck_size.get() =="":
				messagebox.showerror("Error" , "All Fields Are Required" , parent = seltruck)

			else:
				con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
				cur = con.cursor()

				cur.execute("insert truck set truck_name ='" + truck_name.get() + "', truck_size ='" +  truck_size.get() +"'")
				con.commit()	
				con.close()
				messagebox.showinfo("Success" , "Added Vehicle " , parent = seltruck)
		
		#heading label
		heading = Label(seltruck , text = "Add Truck" , font = 'Verdana 20 bold')
		heading.place(x=20 , y=60)

		# form data label
		truck_name = Label(seltruck, text= "Truck Name :" , font='Verdana 10 bold')
		truck_name.place(x=20,y=130)


		truck_size = Label(seltruck, text= "Truck Size (7Ft/12Ft) :" , font='Verdana 10 bold')
		truck_size.place(x=20,y=160)


		# Entry Box ------------------------------------------------------------------

		truck_name = StringVar()
		truck_size = IntVar()

		truck_name = Entry(seltruck, width=30 , textvariable = truck_name)
		truck_name.place(x=190 , y=133)

		truck_size = Entry(seltruck, width=30,textvariable = truck_size)
		truck_size.place(x=190 , y=163)

		# button Add Car

		btn_signup = Button(seltruck, text = "Add Lorry" ,font='Verdana 10 bold', command = AddTruck2)
		btn_signup.place(x=200, y=253)


	# buttons
	btn= Button(des, text = "Add Car" ,font='Verdana 10 bold', width = 20, command = AddCar)
	btn.place(x=553, y=150)

	btn= Button(des, text = "Add Van" ,font='Verdana 10 bold', width = 20, command = AddVan)
	btn.place(x=553, y=190)

	btn= Button(des, text = "Add Threewheel" ,font='Verdana 10 bold', width = 20, command = AddTw)
	btn.place(x=553, y=230)

	btn= Button(des, text = "Add Lorry" ,font='Verdana 10 bold', width = 20, command = AddLorry)
	btn.place(x=553, y=270)

	btn= Button(des, text = "Add Truck" ,font='Verdana 10 bold', width = 20, command = AddTruck)
	btn.place(x=553, y=310)



	con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
	cur = con.cursor()

	# Available Vehicle Details - Car
	cur.execute("select car_id,car_name,car_cooler,car_count from car")
	rows = cur.fetchall()

	heading = Label(des , text = f"Available Vehicles" , font = 'Verdana 15 bold')
	heading.place(x=20 , y=120)

	headingC = Label(des , text = f"Cars" , font = 'Verdana 12 bold')
	headingC.place(x=20 , y=160)

	for cr in rows:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=20,y=180)

		d2 = Label(des, text= f" | {cr[2]}" , font='Verdana 10 bold')
		d2.place(x=140,y=180)

		d3 = Label(des, text= f" | Passengers: {cr[3]}" , font='Verdana 10 bold')
		d3.place(x=220,y=180)


	# Available Vehicle Details - Van
	cur.execute("select van_id,van_name,van_cooler,van_count from van")
	rows2 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Vans" , font = 'Verdana 12 bold')
	headingC.place(x=20 , y=210)

	for cr in rows2:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=20,y=230)

		d2 = Label(des, text= f" | {cr[2]}" , font='Verdana 10 bold')
		d2.place(x=140,y=230)

		d3 = Label(des, text= f" | Passengers: {cr[3]}" , font='Verdana 10 bold')
		d3.place(x=220,y=230)


	# Available Vehicle Details - threewheel
	cur.execute("select tw_id,tw_name,tw_count from threewheel")
	rows3 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Three Wheels" , font = 'Verdana 12 bold')
	headingC.place(x=20 , y=260)

	for cr in rows3:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=20,y=280)

		d3 = Label(des, text= f" | Passengers: {cr[2]}" , font='Verdana 10 bold')
		d3.place(x=220,y=280)


	# Available Vehicle Details - Lorry
	cur.execute("select lorry_id,lorry_name,lorry_load from lorry")
	rows4 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Lorry" , font = 'Verdana 12 bold')
	headingC.place(x=20 , y=310)

	for cr in rows4:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=20,y=330)

		d3 = Label(des, text= f" | Load: {cr[2]}kg" , font='Verdana 10 bold')
		d3.place(x=220,y=330)


	# Available Vehicle Details - Truck
	cur.execute("select truck_id,truck_name,truck_size from truck")
	rows5 = cur.fetchmany(size=1)

	headingC = Label(des , text = f"Truck" , font = 'Verdana 12 bold')
	headingC.place(x=20 , y=360)

	for cr in rows5:
		d1 = Label(des, text= f"* {cr[1]}" , font='Verdana 10 bold')
		d1.place(x=20,y=380)

		d3 = Label(des, text= f" | Size: {cr[2]}ft" , font='Verdana 10 bold')
		d3.place(x=220,y=380)




#-----------------------------------------------------End Deshboard Panel -------------------------------------
#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
	# signup database connect
	def action():
		if name.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="bookme")
				cur = con.cursor()
				cur.execute("select * from admin_information where username=%s",user_name.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
				else:
					cur.execute("insert into admin_information(name,username,password) values(%s,%s,%s)",
						(
						name.get(),
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
		name.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)


	# start Signup Window

	winsignup = Tk()
	winsignup.title("Admin SignUp - BookMe Cab Service")
	winsignup.maxsize(width=500 ,  height=600)
	winsignup.minsize(width=500 ,  height=600)


	#heading label
	heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
	heading.place(x=80 , y=60)

	# form data label
	name = Label(winsignup, text= "Name :" , font='Verdana 10 bold')
	name.place(x=80,y=130)


	user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
	user_name.place(x=80,y=160)

	password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
	password.place(x=80,y=190)

	very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
	very_pass.place(x=80,y=220)

	# Entry Box ------------------------------------------------------------------

	name = StringVar()
	user_name = StringVar()
	password = StringVar()
	very_pass = StringVar()


	name = Entry(winsignup, width=40 , textvariable = name)
	name.place(x=200 , y=133)


	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=200 , y=163)


	password = Entry(winsignup, width=40, show="*" , textvariable = password)
	password.place(x=200 , y=193)


	very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
	very_pass.place(x=200 , y=223)


	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
	btn_signup.place(x=200, y=253)


	btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=280, y=253)


	sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
	sign_up_btn.place(x=350 , y =20)


	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------




#------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("Admin Login - BookMe Cab Service")

# window size
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)


#heading label
heading = Label(win , text = "Admin Login" , font = 'Verdana 25 bold')
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
