from turtle import *#import all functions
from datetime import date,timedelta

import turtle
import pyttsx3

def text_to_speach(text="hi,its me",lang='english'):
    engine=pyttsx3.init()
    #rate=engine.getProperty('voice',lang)
    #engine.setProperty('rate',rate-40)
    #engine.setProperty('voice',lang)
    engine.say(text)
    engine.runAndWait()

lyrics="mostafa"
today=date.today()
dates=[]
for i in range(10):
  dates.append((today-timedelta(days=i)).strftime("%d-%m-%y"))

print(dates)
print('\U0001f600')#emojis in python
print('\U0001f6a0')
print('\U0001f6ff')
text_to_speach(text=lyrics)
pattern=turtle.Turtle()
scre=turtle.Screen()   
scre.bgcolor("white")
pattern.speed(5000)
len=len(scre.getshapes())
passs=scre.textinput("--password--","enter the password please :")
if passs in ["moha","2580","M","   "]:
  for i in range(180):
      pattern.shape(scre.getshapes()[i%len])
      pattern.pencolor("black")
      pattern.forward(50)
      pattern.pencolor("red")
      pattern.forward(50)
      pattern.right(30)
      pattern.forward(20)
      pattern.pencolor("blue")
      pattern.left(60)
      pattern.forward(50)
      pattern.right(30)

      pattern.penup()
      pattern.setposition(0,0)
      pattern.pendown()
      pattern.right(2)
  pattern.penup()
  turtle.done()
else:
 
  write("wrong", align="center", font=("Veradna", 90, "normal"),move=0)
  hideturtle()
  turtle.mainloop()