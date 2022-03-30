import tkinter
import random
import math
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import time

g = {}

nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def addNodes(G, nodes):
    for i in nodes:
        G[i]=[]
    return G

g = addNodes(g,nodes)

def addEges(G, edges, directed = False):
    if directed:
        for i in edges:
            G[i[0]].append((i[1], i[2]))
    else:
        for i in edges:
            if (i[1],i[2]) not in G[i[0]]:
                G[i[0]].append((i[1], i[2]))
            if (i[0],i[2]) not in G[i[1]]:
                G[i[1]].append((i[0], i[2]))
    return G

edges = [(10,1,5),(1,2,10),(4,3,6),(2,3,5),(6,3,5),(3,5,4),(15,12,4),(9,12,3),(6,9,3),(9,14,3),(9,8,8),(5,8,3),(8,7,7),(7,13,5),(13,11,10)]

g = addEges(g,edges)

print(g)

def dijkstra(G, f):
    d={}
    v=[]    
    for n in G:
        if n == f:d[n] = [n, 0]
        else:d[n] = ['',math.inf]
    while len(v)<len(G):
        cN= ''
        s = math.inf
        for node in d:
            if node not in v and d[node][1] < s:
                s = d[node][1]
                cN = node
        v.append(cN)
        for n in G[cN]:
            node=n[0]
            if node not in v:
                w = n[1]
                if d[node][1] > s + w:
                    d[node][1] = s + w
                    d[node][0] = cN
    return d

def getweight(e,edges):
    for i in edges:
        if((e[0]==i[0] and  e[1]==i[1]) or (e[0]==i[1] and  e[1]==i[0])):
            return i[2]

def getShortestPath(G,f,t):
    d = dijkstra(G,f)
    lst = []
    while t!=f:
        lst.append((d[t][0],t))
        t = d[t][0]

    return lst[::-1]

def pathweight(p,edges):
    w=0
    for i in p:
        w += getweight(i,edges)
    return w


def getPaths(g, startpoint, intermediatepoints):
    fnl=[]
    while(len(intermediatepoints)!=0):
        minpw=999
        minp=[]
        for i in intermediatepoints:
            if(pathweight(getShortestPath(g,startpoint,i),edges)<minpw):
                minp = getShortestPath(g,startpoint,i)
        startpoint=minp[-1][1]
        intermediatepoints.remove(startpoint)
        fnl.extend(minp)
    return fnl
        

ovalColor = "#0f0"
lineColor = "red"

master = Tk()
master.title("Greedy Path")
w = Canvas(master, width=1000, height=500,bd=0,highlightthickness=0)
w.configure(bg="white")
w.pack()


dictForNodeCoordinates = {
    "A": (50, 200),
    "B":(200, 50),
    "C":(50, 50),
    "D":(300, 150),
    "E":(400, 50),
    "F":(400, 250),
    "G":(500, 150),
    "H":(450, 350),
    "I":(250, 350),
    "J":(400, 400),
    "K":(500, 35),
    "L":(600, 50),
    "M":(600, 50),
    "N":(600, 250),
    "O":(550, 400),
}



def createoval(oColor, Lcolor, dest=False):
    if (dest==True):
        w.destroy
    else: 

        # Point 10
        w.create_oval(30, 30, 70, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(50, 50,text="B", fill="black")
        #point 1
        w.create_oval(30, 180, 70, 220, outline=oColor,fill=oColor, width=1)
        w.create_text(50, 200,text="A", fill="black")
        #point 2
        w.create_oval(180, 30, 220, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(200, 50,text="B", fill="black")
        #point 4
        w.create_oval(30, 30, 70, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(50, 50,text="C", fill="black")
        #point 3
        w.create_oval(280, 130, 320, 170, outline=oColor,fill=oColor, width=1)
        w.create_text(300, 150,text="D", fill="black")
        #point 6
        w.create_oval(380, 30, 420, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(400, 50,text="E", fill="black")
        #point 5
        w.create_oval(380, 230, 420, 270, outline=oColor,fill=oColor, width=1)
        w.create_text(400, 250,text="F", fill="black")
        #point 9
        w.create_oval(480, 130, 520, 170, outline=oColor,fill=oColor, width=1)
        w.create_text(500, 150,text="G", fill="black")
        #point 8
        w.create_oval(430, 330, 470, 370, outline=oColor,fill=oColor, width=1)
        w.create_text(450, 350,text="H", fill="black")
        #point 7
        w.create_oval(230, 330, 270, 370, outline=oColor,fill=oColor, width=1)
        w.create_text(250, 350,text="I", fill="black")
        #point 13
        w.create_oval(380, 380, 420, 420, outline=oColor,fill=oColor, width=1)
        w.create_text(400, 400,text="J", fill="black")
        #point 15
        w.create_oval(480, 15, 520, 55, outline=oColor,fill=oColor, width=1)
        w.create_text(500, 35,text="K", fill="black")
        #point 15
        w.create_oval(580, 30, 620, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(600, 50,text="L", fill="black")
        #point 12
        w.create_oval(580, 30, 620, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(600, 50,text="M", fill="black")
        #point 14
        w.create_oval(580, 230, 620, 270, outline=oColor,fill=oColor, width=1)
        w.create_text(600, 250,text="N", fill="black")
        #point 11
        w.create_oval(530, 380, 570, 420, outline=oColor,fill=oColor, width=1)
        w.create_text(550, 400,text="O", fill="black")
    

createoval("#0f0", "red")

def colorSelectedNode(nodeName, oColor="#00f"):
    if (nodeName == "A"):
        w.create_oval(30, 180, 70, 220, outline=oColor,fill=oColor, width=1)
        w.create_text(50, 200,text="A", fill="black")
    elif (nodeName == "B"):
        w.create_oval(180, 30, 220, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(200, 50,text="B", fill="black")
    elif (nodeName == "C"):
        w.create_oval(30, 30, 70, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(50, 50,text="C", fill="black")
    elif (nodeName == "D"):
        w.create_oval(280, 130, 320, 170, outline=oColor,fill=oColor, width=1)
        w.create_text(300, 150,text="D", fill="black")
    elif (nodeName == "E"):
        w.create_oval(380, 30, 420, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(400, 50,text="E", fill="black")
    elif (nodeName == "G"):
        w.create_oval(480, 130, 520, 170, outline=oColor,fill=oColor, width=1)
        w.create_text(500, 150,text="G", fill="black")
    elif (nodeName == "F"):
        w.create_oval(380, 230, 420, 270, outline=oColor,fill=oColor, width=1)
        w.create_text(400, 250,text="F", fill="black")
    elif (nodeName == "H"):
        w.create_oval(430, 330, 470, 370, outline=oColor,fill=oColor, width=1)
        w.create_text(450, 350,text="H", fill="black")
    elif (nodeName == "I"):
        w.create_oval(230, 330, 270, 370, outline=oColor,fill=oColor, width=1)
        w.create_text(250, 350,text="I", fill="black")
    elif (nodeName == "J"):
        w.create_oval(380, 380, 420, 420, outline=oColor,fill=oColor, width=1)
        w.create_text(400, 400,text="J", fill="black")
    elif (nodeName == "K"):
        w.create_oval(480, 15, 520, 55, outline=oColor,fill=oColor, width=1)
        w.create_text(500, 35,text="K", fill="black")
    elif (nodeName == "L"):
        w.create_oval(580, 30, 620, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(600, 50,text="L", fill="black")
    elif (nodeName == "M"):
        w.create_oval(580, 30, 620, 70, outline=oColor,fill=oColor, width=1)
        w.create_text(600, 50,text="M", fill="black")
    elif (nodeName == "N"):
        w.create_oval(580, 230, 620, 270, outline=oColor,fill=oColor, width=1)
        w.create_text(600, 250,text="N", fill="black")
    elif (nodeName == "O"):
        w.create_oval(530, 380, 570, 420, outline=oColor,fill=oColor, width=1)
        w.create_text(550, 400,text="O", fill="black")


def inputDialog(prmpt):
    uIn = simpledialog.askstring(title="Input Required",prompt=prmpt)
    return uIn

    
selectToColor = ""
NumberToLetterMap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
startingNode = (inputDialog("Enter the starting node? "))
mustIncludeStops = list(inputDialog("Enter Stops that must be visited? (comma separated) ").split(","))
print(mustIncludeStops)
stopsInInteger = []
for y in mustIncludeStops:
    stopsInInteger.append(NumberToLetterMap.index(y)+1)


finalPath = getPaths(g, NumberToLetterMap.index(startingNode)+1, stopsInInteger)

x = 0

def proceedFinding(event):
    global x

    if (x < len(finalPath)):
        index = finalPath[x]
        weight = getweight((index[0],index[1]),edges)
        print(NumberToLetterMap[index[0]-1] +" --> "+NumberToLetterMap[index[1]-1] + "  weight = " + str(weight))
        colorSelectedNode(NumberToLetterMap[index[0]-1],oColor="#00f")
        colorSelectedNode(NumberToLetterMap[index[1]-1],oColor="#00f")

        w.create_line(
            dictForNodeCoordinates[NumberToLetterMap[index[0]-1]][0], 
            dictForNodeCoordinates[NumberToLetterMap[index[0]-1]][1], 
            dictForNodeCoordinates[NumberToLetterMap[index[1]-1]][0], 
            dictForNodeCoordinates[NumberToLetterMap[index[1]-1]][1], 
            fill="#f00")
        x+=1
    else:
        print("Done")
    

master.bind('<Button-1>', func=proceedFinding)
master.mainloop()