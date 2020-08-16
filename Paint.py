from tkinter import *
from tkinter.colorchooser import askcolor


r=Tk()
r.title("Paint")

w, h = r.winfo_screenwidth(), r.winfo_screenheight()
r.geometry("%dx%d+0+0" % (w, h))


L1=Label(r,text="Welcome to paint",font=("Castellar",22,"underline"),fg="red",bg="yellow")
L1.grid(row=0,column=1)
e1=Entry(r)
e1.grid(row=0,column=3,pady=10,sticky=N)
e2=Entry(r)
e2.grid(row=0,column=3,pady=30,sticky=N)



L2=Label(r,text="1)Please enter first\n and second dimension\n 2)Select any shape \n 3)Hold and drag the \n mouse until desired \n result \n 4)Note: Don't get feared by \n multiple shapes \n They are for your help \n At the end onlyone \n shape will be made",
         font=("Monotype Corsiva",15,"italic"),fg="green",bg="yellow")
L2.grid(row=1,column=3,sticky=N)
Label(r,text="Made by Anshuman Gupta",font=("Chiller",15,"bold"),fg="red",bg="yellow").grid(row=1,column=1,sticky=N)

def createcanvas():
    c=Canvas(r,height=float(e1.get()),width=float(e2.get()),bg="white")
    c.grid(row=1,column=1,sticky=N,pady=50)
    def val():
        global result
        result=None
        return result
    val()
    
    def colour_choose():
        global result
        result="black"
        res=askcolor(color=None,
                        title="Colour chooser")
        def colourchange():
            global result
            result=res[1]
            return result
        colourchange()
    
    def rect():
        def getfirst_loc(e):
            m=(e.x)
            n=(e.y)
            def getfake(evnt):
                o=(evnt.x)
                p=(evnt.y)
                sq=c.create_rectangle(m,n,o,p)
                c.itemconfig(sq,tags="sq")
                def getsecond_loc(event):
                    o=(event.x)
                    p=(event.y)
                    c.create_rectangle(m,n,o,p,fill=result)
                    c.delete("sq")
                c.bind("<ButtonRelease-1>",getsecond_loc)
                
            c.bind("<B1-Motion>",getfake)
            
        c.bind("<Button-1>",getfirst_loc)
        
    def line():
        def getfirst_loc(e):
            m=(e.x)
            n=(e.y)
            def getfake(evnt):
                o=(evnt.x)
                p=(evnt.y)
                l=c.create_line(m,n,o,p)
                c.itemconfig(l,tags="l")
                def getsecond_loc(event):
                    o=(event.x)
                    p=(event.y)
                    c.create_line(m,n,o,p,fill=result)
                    c.delete("l")
                c.bind("<ButtonRelease-1>",getsecond_loc)
                
            c.bind("<B1-Motion>",getfake)
            
        c.bind("<Button-1>",getfirst_loc)
        
    def circle():
        def getfirst_loc(e):
            m=(e.x)
            n=(e.y)
            
            def getfake(evnt):
                o=(evnt.x)
                p=(evnt.y)
                cir=c.create_oval(m,n,o,p)
                c.itemconfig(cir,tags="circ")
                def getsecond_loc(event):
                    o=(event.x)
                    p=(event.y)
                    c.create_oval(m,n,o,p,fill=result)
                    c.delete("circ")
                c.bind("<ButtonRelease-1>",getsecond_loc)
                
            c.bind("<B1-Motion>",getfake)
            
        c.bind("<Button-1>",getfirst_loc)
    def fillingcircle():
        def getfirst_loc(e):
            m=(e.x)
            n=(e.y)
            
            def getfake(evnt):
                o=(evnt.x)
                p=(evnt.y)
                cir=c.create_oval(m,n,o,p,width=0,fill=result)
                
                def getsecond_loc(event):
                    o=(event.x)
                    p=(event.y)
                    c.create_oval(m,n,o,p,fill=result,width=0)
                    
                c.bind("<ButtonRelease-1>",getsecond_loc)
                
            c.bind("<B1-Motion>",getfake)
            
        c.bind("<Button-1>",getfirst_loc)
    def eraser():
        
        def createdot(s):
            m=(s.x-1)
            n=(s.y-1)
            o=(s.x+10)
            p=(s.y+10)
            c.create_oval(m,n,o,p,fill="white",width=0)
        c.bind("<Button-1>",createdot)
        c.bind("<B1-Motion>",createdot)
        c.bind("<ButtonRelease-1>",createdot)
    def quitting():
        r.destroy()
    def clearall():
        c.destroy()
    def pencil():
        def createdot(s):
            m=(s.x-1)
            n=(s.y-1)
            o=(s.x+5)
            p=(s.y+5)
            c.create_oval(m,n,o,p,fill=result,width=0)
        c.bind("<Button-1>",createdot)
        c.bind("<B1-Motion>",createdot)
        c.bind("<ButtonRelease-1>",createdot)
    
        

        
    b1=Button(r,text="rectangle",command=rect)
    b1.grid(row=1,column=2,pady=50,sticky=N)
    b2=Button(r,text="Line",command=line)
    b2.grid(row=1,column=2,pady=100,sticky=N)
    b3=Button(r,text="Circle",command=circle)
    b3.grid(row=1,column=2,pady=150,sticky=N)
    b4=Button(r,text="clear",command=clearall)
    b4.grid(row=1,column=2,pady=200,sticky=N)
    b5=Button(r,text="Exit",command=quitting)
    b5.grid(row=1,column=2,pady=250,sticky=N)
    b6=Button(r,text="Fillingcircle",command=fillingcircle)
    b6.grid(row=1,column=2,pady=300,sticky=N)
    b7=Button(r,text="Eraser",command=eraser)
    b7.grid(row=1,column=2,pady=350,sticky=N)
    b9=Button(r,text="pencil",command=pencil)
    b9.grid(row=1,column=2,pady=400,sticky=N)
    b10=Button(r,text="choose colour",command=colour_choose)
    b10.grid(row=1,column=3,pady=300,sticky=N)
    
b8=Button(text="Create \n Canvas",command=createcanvas)
b8.grid(row=1,column=2,pady=1,sticky=N)



mainloop()

