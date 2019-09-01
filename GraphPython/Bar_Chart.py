from turtle import *
from random import shuffle
from sys import argv
#list of colors to be used for the graph
List_Color = ['Red','lightBlue','Cyan','Green','Yellow','Brown','Purple','lightPink','Maroon','White']
shuffle(List_Color)     #shuffling the colours
#setting up the turtle and screen objects
cursor = Turtle()
screen = Screen()
screen.setworldcoordinates(-300, -300, 300, 300)    #screen size
screen.bgcolor('black')     #screen background
Origin = (-280, -280)       #origin as a tuple
cursor.hideturtle()         
File = argv[1]           #file for data to be extracted from
name_x = argv[2]         #name of the x bar   
#getting the data from the file
def data_extract(FileName):
    try:    # checking whether the file is found in the directory
        object_file = open(FileName,'r')    #reading in data from origin
    except FileNotFoundError:
        print('File not found please try adding the file to the current repository')
        exit()  #exiting program if file is not found
    data=[]
    finaldata=[]
    line=0
    while line!='':     #reading in data from the file
        line=object_file.readline()
        data.append(line)
    object_file.close()
    for i in data:      #converting data from the file into floating numbers
        try:
            finaldata.append(float(i))
        except ValueError:
            pass
    return finaldata
#generating intervals to be plotted
def interval_gen(DataList):
    minimum=min(DataList)   #minimum value of the rawdata
    maximum=max(DataList)   #maximum value of the rawdata
    Range=maximum-minimum   #range of values
    interval=Range/10       #segments of the graph
    interval_list=[round(minimum + i*interval,2) for i in range(11) ]
    return interval_list
#counting the occurances of data between the intervals
def frequency_gen(RawData,interval_list):
    frequency_list=[0 for i in range(10)]       #list of frequencies
    for i in RawData:
        for j in range(10):
            if interval_list[j]<=i<interval_list[j+1]:# incrementing the values if rawdata lies between certain range
                frequency_list[j]+=1
    frequency_list[-1]+=RawData.count(max(RawData))
    return (frequency_list)
#function to draw individual bars
def BarsDraw(x,colour,step):
    cursor.color('white')   # setting the colour of the cursor
    cursor.fillcolor(colour)
    cursor.begin_fill() #starting the fill colour of the bars
    cursor.seth(90)
    cursor.fd((40/step)*x)  
    cursor.right(90)
    cursor.fd(20)
    cursor.lt(90)
    cursor.penup()
    cursor.fd(5)
    cursor.write(str(x), align= 'center',font = ('Arial',10,'normal'))  #writng the value of the bars on top of the bar 
    cursor.bk(5)
    cursor.pendown()
    cursor.rt(90)
    cursor.fd(20)
    cursor.right(90)
    cursor.fd((40/step)*x)
    cursor.right(90)
    cursor.fd(40)
    cursor.end_fill()   #ending the fill of the colour of the bars
    cursor.penup()
    cursor.seth(0)
    cursor.forward(40)
    cursor.pendown()
#function to draw the axis
def Axis(List,max):
    #setting the colour of the cursor to white and moving it to the origin
    cursor.color('white')
    cursor.penup()
    cursor.goto(Origin)
    cursor.pendown()
    #drawing the x axis
    cursor.seth(0)
    for i in List:
        cursor.seth(0)
        cursor.forward(40)
        cursor.dot()
        cursor.seth(270)
        cursor.penup()
        cursor.forward(15)
        cursor.write(i)
        cursor.backward(15)
        cursor.pendown()
    cursor.seth(0)
    cursor.forward(40)
    cursor.stamp()
    cursor.penup()
    cursor.forward(20)
    cursor.write(name_x,align='center',font=('Arial',12,'normal'))
    #resetting to the origin
    cursor.penup()
    cursor.goto(Origin)
    cursor.seth(90)
    #drawing the y axis
    cursor.pendown()
    for i in range((max-1)//13+1, max+(max-1)//13+1, (max-1)//13+1):
        cursor.seth(90)
        cursor.forward(40)
        cursor.dot()
        cursor.seth(180)
        cursor.penup()
        cursor.forward(15)
        cursor.write(i)
        cursor.backward(15)
        cursor.pendown()
    cursor.seth(90)
    cursor.forward(40)
    cursor.stamp()
    cursor.penup()
    cursor.forward(10)
    cursor.right(90)
    cursor.forward(20)
    cursor.write('frequency',align='center',font=('Arial',12,'normal'))
#function to draw the scale on the top right of the screen using lists as the parameters
def Scale(Ylist,Xlist):
    cursor.penup()
    cursor.goto(160,200)
    cursor.write('Scale:\nX axis- 1 unit: {:.2f}\nY axis- 1unit: {}'.format((Xlist[1]-Xlist[0]), max(Ylist)//13+1))
#main part of the function
RawDataList = data_extract(File)
IntervalList = interval_gen(RawDataList)
FrequencyList = frequency_gen(RawDataList,IntervalList)
Axis(IntervalList,max(FrequencyList))
Scale(FrequencyList,IntervalList)
#starting to draw the bars
cursor.penup()
cursor.goto(Origin[0]+40,Origin[1])
cursor.pendown()
for i in range(len(FrequencyList)):
    BarsDraw(FrequencyList[i],List_Color[i%len(List_Color)],(max(FrequencyList)-1)//13+1)
screen.mainloop()