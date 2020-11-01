from turtle import *
import turtle
from datetime import datetime
import time
from tkinter import *
import os

def get_time():
	time_str=time.strftime("%A, %B %d, %G | %r ")
	clock.config(text=time_str)
	clock.after(200,get_time)

def moving(distance, angle=0):
	penup()
	right(angle)
	forward(distance)
	pendown()

def layout(lenght, vast):
	fd(lenght*1.15)
	rt(90)
	fd(vast/2.0)
	lt(120)
	fd(vast)
	lt(120)
	fd(vast)
	lt(120)
	fd(vast/2.0)

def timer_hands(name, lenght, vast):
	reset()
	moving(-lenght*0.15)
	begin_poly()
	layout(lenght, vast)
	end_poly()
	clock_labellings = get_poly()
	register_shape(name, clock_labellings)

def clockface(radius):
	reset()
	pensize(7)
	for i in range(60):
		moving(radius)
		if i % 5 == 0:
			fd(25)
			moving(-radius-25)
		else:
			dot(3)
			moving(-radius)
		rt(6)

def settings():
	global second_hand, minute_hand, hour_hand
	timer_hands("second_hand", 125, 25)
	timer_hands("minute_hand", 130, 25)
	timer_hands("hour_hand", 90, 25)
	clockface(160)
	second_hand = Turtle()
	second_hand.shape("second_hand")
	second_hand.color("gray40", "black")
	minute_hand = Turtle()
	minute_hand.shape("minute_hand")
	minute_hand.color("red", "orange")
	hour_hand = Turtle()
	hour_hand.shape("second_hand")
	hour_hand.color("red", "orange")
	for hand in second_hand, minute_hand, hour_hand:
		hand.resizemode("user")
		hand.shapesize(1,1,3)
		hand.speed(0)
	ht()

def tick():
	t = datetime.today()
	secondTimer = t.second + t.microsecond*0.000001
	minute = t.minute + secondTimer/60.0
	onTheHour = t.hour + minute/60.0
	try:
		tracer(False)
		second_hand.setheading(6*secondTimer)
		minute_hand.setheading(6*minute)
		hour_hand.setheading(6*onTheHour)
		tracer(True)
		ontimer(tick, 100)
	except Terminator:
		pass

def main():
	tracer(False)
	settings()
	tracer(True)
	tick()
	wn = turtle.Screen()
	wn.title('''Real O'Clock > By: David H. Pham''')

	return "DONE"

if __name__ == "__main__":
	mode("logo")
	msg = main()
	print(msg)
	root=Tk()
	root.title('DIGITAL CLOCK | Real Time > By: David H. Pham')
	clock=Label(root,font='times 30 normal', bg='#4d4d4d', foreground='light blue')
	clock.pack()
	get_time()
	root.mainloop()
	wn.mainloop()
	#mainloop()
