from tkinter import *
import random
import time
import tkinter.messagebox as showinfo



# Configurations
Svanik = Tk()
Svanik.geometry("515x635")
Svanik.maxsize(615,635)
Svanik.minsize(615,635)
Svanik.iconbitmap("icon.ico")
Svanik.resizable(height=False,width=False)
Svanik.configure(bg="lightblue")
Svanik.title("Welcome to the sliding puzzle~Svanik Jain")
showinfo.showinfo("How to play the game",'''Instead of sliding the pieces, please click the pieces to move them You need to arrange the pieces in ascending order. The order of arranging the pieces is - 
		          ( 1 2 3
		            4 5 6
		            7 8  )''')

# Variabless
Num1 = StringVar()
Num2 = StringVar()
Num3 = StringVar()
Num4 = StringVar()
Num5 = StringVar()
Num6 = StringVar()
Num7 = StringVar()
Num8 = StringVar()
Num9 = StringVar()


Button_clicked = 0
N1Number = 0
N2Number = 0
N3Number = 0
N4Number = 0
N5Number = 0
N6Number = 0
N7Number = 0
N8Number = 0
N9Number = 0

Moves = IntVar()
Temp  = IntVar()
Moves.set(0)
Temp.set(1)

Start_Time = 0
End_Time = 0
Actual_Time = 0
Temp2 = IntVar()
Temp2.set(0)

numbers = 0
Random_Number_1 = 1
Random_Number_2 = 2
Random_Number_3	= 3
Random_Number_4 = 4
Random_Number_5	= 5
Random_Number_6 = 6
Random_Number_7	= 7
Random_Number_8 = 8

svanik = 70
jain = 60
svanikjainproductions = 0


# Functions
def randomNumberSet():
	global Random_Number_1
	global Random_Number_2
	global Random_Number_3	
	global Random_Number_4
	global Random_Number_5	
	global Random_Number_6
	global Random_Number_7	
	global Random_Number_8
	global Moves	
	global numbers

	numbers = [1,2,3,4,5,6,7,8]
	random.shuffle(numbers)
	numbers2 = []
	index = 1
	for x in numbers:
		if index % 2 == 0:
			numbers2.append(numbers[(numbers.index(x))-1:index])
		index = index + 1

	for j in numbers2:
		first_num = j[0]
		second_num = j[1]
		if first_num == 1:
			first_num = Random_Number_1

		if first_num == 2:
			first_num = Random_Number_2

		if first_num == 3:
			first_num = Random_Number_3

		if second_num == 4:
			second_num = Random_Number_4
 
		if second_num == 5:
			second_num = Random_Number_5
 
		if second_num == 6:
			second_num = Random_Number_6
 
		if second_num == 7:
			second_num = Random_Number_7

		if second_num == 8:
			second_num = Random_Number_8



		if first_num == 1:
			first_num = Random_Number_1

		if first_num == 2:
			first_num = Random_Number_2

		if first_num == 3:
			first_num = Random_Number_3

		if first_num == 4:
			first_num = Random_Number_4
 
		if first_num == 5:
			first_num = Random_Number_5
 
		if first_num == 6:
			first_num = Random_Number_6
 
		if first_num == 7:
			first_num = Random_Number_7

		if first_num == 8:
			first_num = Random_Number_8
 

		if first_num == 1:
			Random_Number_1 = second_num
			
		if first_num == 2:
			Random_Number_2 = second_num
			
		if first_num == 3:
			Random_Number_3 = second_num
			
		if first_num == 4:
			Random_Number_4 = second_num
			
		if first_num == 5:
			Random_Number_5 = second_num
			
		if first_num == 6:
			Random_Number_6 = second_num
			
		if first_num == 7:
			Random_Number_7 = second_num

		if first_num == 8:
			Random_Number_8 = second_num



		if second_num == 1:
			Random_Number_1 = first_num
			
		if second_num == 2:
			Random_Number_2 = first_num
			
		if second_num == 3:
			Random_Number_3 = first_num
			
		if second_num == 4:
			Random_Number_4 = first_num
			
		if second_num == 5:
			Random_Number_5 = first_num
			
		if second_num == 6:
			Random_Number_6 = first_num
			
		if second_num == 7:
			Random_Number_7 = first_num

		if second_num == 8:
			Random_Number_8 = first_num
	Set_Number()



def Set_Number():
	global Random_Number_1
	global Random_Number_2
	global Random_Number_3	
	global Random_Number_4
	global Random_Number_5	
	global Random_Number_6
	global Random_Number_7	
	global Random_Number_8
	global Start_Time


	for x in range(1,10):
		if Random_Number_1 == x:
			Num1.set(x)
		if Random_Number_2 == x:
			Num2.set(x)
		if Random_Number_3 == x:
			Num3.set(x)
		if Random_Number_4 == x:
			Num4.set(x)
		if Random_Number_5 == x:
			Num5.set(x)
		if Random_Number_6 == x:
			Num6.set(x)
		if Random_Number_7 == x:
			Num7.set(x)
		if Random_Number_8 == x:
			Num8.set(x)

	Num9.set("  ")
	Start_Time = time.time()

def Move(btn_Value):
	global Button_clicked
	global Random_Number_1
	global Random_Number_2
	global Random_Number_3	
	global Random_Number_4
	global Random_Number_5	
	global Random_Number_6
	global Random_Number_7	
	global Random_Number_8
	global svanikjainproductions
	global N1Number
	global N2Number
	global N3Number
	global N4Number
	global N5Number
	global N6Number
	global N7Number
	global N8Number
	global N9Number
	global Moves


	N1Number = Num1.get()
	N2Number = Num2.get()
	N3Number = Num3.get()
	N4Number = Num4.get()
	N5Number = Num5.get()
	N6Number = Num6.get()
	N7Number = Num7.get()
	N8Number = Num8.get()
	N9Number = Num9.get()
	Button_clicked = btn_Value
	if Button_clicked == 1:
		
		if N2Number == "  ":
			Num1.set(N2Number)
			Num2.set(N1Number)
			Moves.set(Moves.get() + Temp.get())

		elif N4Number == "  ":
			Num1.set(N4Number)
			Num4.set(N1Number)
			Moves.set(Moves.get() + Temp.get())
			
	if Button_clicked == 2:
		
		if N3Number == "  ":
			Num2.set(N3Number)
			Num3.set(N2Number)
			Moves.set(Moves.get() + Temp.get())

		elif N1Number == "  ":
			Num2.set(N1Number)
			Num1.set(N2Number)
			Moves.set(Moves.get() + Temp.get())

		elif N5Number == "  ":
			Num2.set(N5Number)
			Num5.set(N2Number)
			Moves.set(Moves.get() + Temp.get())
		    
	if Button_clicked == 3:
		
		if N2Number == "  ":
			Num3.set(N2Number)
			Num2.set(N3Number)
			Moves.set(Moves.get() + Temp.get())

		elif N6Number == "  ":
			Num3.set(N6Number)
			Num6.set(N3Number)
			Moves.set(Moves.get() + Temp.get())
	
	if Button_clicked == 4:
		
		if N1Number == "  ":
			Num4.set(N1Number)
			Num1.set(N4Number)
			Moves.set(Moves.get() + Temp.get())

		elif N5Number == "  ":
			Num4.set(N5Number)
			Num5.set(N4Number)
			Moves.set(Moves.get() + Temp.get())

		elif N7Number == "  ":
			Num4.set(N7Number)
			Num7.set(N4Number)
			Moves.set(Moves.get() + Temp.get())

	if Button_clicked == 5:
		
		if N2Number == "  ":
			Num5.set(N2Number)
			Num2.set(N5Number)
			Moves.set(Moves.get() + Temp.get())

		elif N4Number == "  ":
			Num5.set(N4Number)
			Num4.set(N5Number)
			Moves.set(Moves.get() + Temp.get())

		elif N6Number == "  ":
			Num5.set(N6Number)
			Num6.set(N5Number)	
			Moves.set(Moves.get() + Temp.get())

		elif N8Number == "  ":
			Num5.set(N8Number)
			Num8.set(N5Number)	
			Moves.set(Moves.get() + Temp.get())

	if Button_clicked == 6:
		
		if N3Number == "  ":
			Num6.set(N3Number)
			Num3.set(N6Number)
			Moves.set(Moves.get() + Temp.get())

		elif N9Number == "  ":
			Num6.set(N9Number)
			Num9.set(N6Number)
			Moves.set(Moves.get() + Temp.get())

		elif N5Number == "  ":
			Num6.set(N5Number)
			Num5.set(N6Number)
			Moves.set(Moves.get() + Temp.get())

	if Button_clicked == 7:
		
		if N4Number == "  ":
			Num7.set(N4Number)
			Num4.set(N7Number)
			Moves.set(Moves.get() + Temp.get())

		elif N8Number == "  ":
			Num7.set(N8Number)
			Num8.set(N7Number)
			Moves.set(Moves.get() + Temp.get())

	if Button_clicked == 8:
		
		if N9Number == "  ":
			Num8.set(N9Number)
			Num9.set(N8Number)
			Moves.set(Moves.get() + Temp.get())

		elif N5Number == "  ":
			Num8.set(N5Number)
			Num5.set(N8Number)
			Moves.set(Moves.get() + Temp.get())

		elif N7Number == "  ":
			Num8.set(N7Number)
			Num7.set(N8Number)
			Moves.set(Moves.get() + Temp.get())

	if Button_clicked == 9:
		
		if N6Number == "  ":
			Num9.set(N6Number)
			Num6.set(N9Number)
			Moves.set(Moves.get() + Temp.get())

		elif N8Number == "  ":
			Num9.set(N8Number)
			Num8.set(N9Number)
			Moves.set(Moves.get() + Temp.get())
	svanikjainproductions = 100
	Check_if_Won()
	
def Check_if_Won():
	global End_Time
	global Start_Time
	global Actual_Time
	global svanikjainproductions
	global Temp2
	End_Time = time.time()
	Actual_Time = End_Time - Start_Time
	Actual_Time = int(Actual_Time)
	Temp2.set(Actual_Time)
	global Moves
	if (Num1.get() == "1" and Num2.get() == "2" and Num3.get() == "3" and Num4.get() == "4" and Num5.get() == "5" and Num6.get() == "6" 
		and Num7.get() == "7" and Num8.get() == "8" and Num9.get() == "  "):
		time.sleep(0.001)
		Svanik.destroy()
		Jain  = Tk()
		Jain.geometry("530x180")
		Jain.maxsize(530,180)
		Jain.minsize(530,180)
		Jain.iconbitmap("icon.ico")
		Jain.resizable(height=False,width=False)
		svanikjainproductions = 0
		Jain.configure(bg="lightgreen")
		Moves2 = IntVar()
		Moves2.set(Moves.get())
		Jain.title("You Won!!!")
		Label2 = Label(Jain,text="You Won!!!",padx=150,font="Calbrai 20 bold",bg="lightgreen",fg="red")
		Label2.grid(row=0,column=0)

		Label9 = Label(Jain,text="",bg="lightgreen")
		Label9.grid(row=1,column=0)

		Label7 = Label(Jain,text="Moves in which you won: ",font="Calbrai 20 bold",bg="lightgreen",fg="red")
		Label7.grid(row=2,column=0)

		Label8 = Label(Jain,textvariable=Moves2,font="Calbrai 20 bold",bg="lightgreen",fg="red")
		Label8.grid(row=2,column=1)


		Label5 = Label(Jain,text="Seconds in which you won: ",font="Calbrai 20 bold",bg="lightgreen",fg="red")
		Label5.grid(row=3,column=0)

		Label6 = Label(Jain,text=Temp2.get(),font="Calbrai 20 bold",bg="lightgreen",fg="red")
		Label6.grid(row=3,column=1)
		Jain.mainloop()


# FunctionCall
randomNumberSet()

# frames
Title = Frame(Svanik,borderwidth=6,relief=RIDGE,bg="lightgreen",pady=2)
Title.pack(pady=5)

MoveFrame  = Frame(Svanik,borderwidth=6,relief=RIDGE,padx=30,bg="orange",pady=10)
MoveFrame.pack(pady=5)

BtnFrame = Frame(Svanik,borderwidth=6,relief=RIDGE,padx=30,bg="orange",pady=10)
BtnFrame.pack(pady=5)

# Title
TitleLabel = Label(Title,text="Welcome to the square game ~Svanik Jain",padx=100,font="Calbrai 10 bold",bg="lightgreen",fg="red")
TitleLabel.pack()

# Moves
MoveLabel = Label(MoveFrame,text="Moves: ",padx=100,font="Calbrai 12 bold",bg="lightgreen",fg="red")
MoveLabel.pack(side=LEFT)

MoveLabel2 = Label(MoveFrame,textvar=Moves,padx=100,font="Calbrai 12 bold",bg="lightgreen",fg="red")
MoveLabel2.pack(side=LEFT)
# Buttons
btn1 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num1,font="Ubuntu 14 bold",bg="blue",fg="orange" , command= lambda: Move(1))
btn2 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num2,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(2))
btn3 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num3,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(3))
btn4 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num4,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(4))
btn5 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num5,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(5))
btn6 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num6,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(6))
btn7 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num7,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(7))
btn8 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num8,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(8))
btn9 = Button(BtnFrame,padx=svanik,pady=jain,textvar=Num9,font="Ubuntu 14 bold",bg="blue",fg="orange", command= lambda: Move(9))


btn1.grid(row=0,column=0,padx=5,pady=2)
btn2.grid(row=0,column=1,padx=5,pady=2)
btn3.grid(row=0,column=2,padx=5,pady=2)

btn4.grid(row=1,column=0,padx=5,pady=2)
btn5.grid(row=1,column=1,padx=5,pady=2)
btn6.grid(row=1,column=2,padx=5,pady=2)

btn7.grid(row=2,column=0,padx=5,pady=2)
btn8.grid(row=2,column=1,padx=5,pady=2)
btn9.grid(row=2,column=2,padx=5,pady=2)

Svanik.mainloop()