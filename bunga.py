import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('#262626')
t.pencolor('magenta')
t.speed(100)

col = ('cyan', 'yellow', 'red')
for i in range(3):
	for x in range(8):
		t.speed(x+10)
		for n in range(2):
			t.pensize(2)
			t.circle(80+i*20, 90)
			t.lt(90)
		t.lt(45)
	t.pencolor(col[i % 3])

t.color("purple")
t.penup()
t.goto(0, -300)
style = ('Berlin Sans FB', 90, 'normal')
t.hideturtle()
t.write('MY LOVE', font=style, align='center')

s.exitonclick()