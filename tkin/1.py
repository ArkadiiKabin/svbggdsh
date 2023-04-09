from tkinter import *

root = Tk()

btn=[]
v=[0]*9
c=0

def click(i,j):
    print(i,j)
    global c

    index1=i*3+j
    if v[index1]==0:
        c+=1
        
        if c%2==1:
            v[index1]=1
            mesLbl.config(text="Ход красных!")
            btn[index1].config(background="blue",state="disabled")
        else:
            v[index1]=2
            mesLbl.config(text="Ход синих!")
            btn[index1].config(background="red",state="disabled")

    if win():
        mesLbl.config(text="!")

     
def win():
    if v[0]==v[1]==v[2] !=0:
        return True
    
    elif v[3]==v[4]==v[5] !=0:
        return True
    
    elif v[6]==v[7]==v[8] !=0:
        return True
    
    elif v[0]==v[3]==v[6] !=0:
        return True
    
    elif v[1]==v[4]==v[7] !=0:
        return True
    
    elif v[2]==v[5]==v[8] !=0:
        return True
    
    else:
        return False
   




    
    


for i in range(3):
    for j in range(3):
        b=Button(root,width=20,height=10,command=lambda r=i, c=j:click(r,c))
        btn.append(b)
        b.grid(row=i,column=j)
        

mesLbl=Label(root,text="Ход синих")
mesLbl.grid(row=3,column=0,columnspan=3)

root.mainloop()