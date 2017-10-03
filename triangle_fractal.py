#triangular fractal program

#i once wrote this to run on a calculator when i was in sixth form
#a long time ago

#it starts at a point of (0,0) then randomly picks between (0,0) (1,0) and (0.5,1)
#moves halfway and plots a point - then repeats



#ol.penney@gmail.com
#2/10/17

import random
import numpy as np
import pylab as pl

print("fractal")
x=0.0
y=0.0

xx=list()
yy=list()

for i in range(0, 50000):
    r=random.randint(0,2)
    #print(r)
    if r==0:
        #print("first point")
        x=(x+0)/2
        y=(y+0)/2
    else:
        if r==1:
            #print("second point")
            x=(x+1)/2
            y=(y+0)/2
        else:
            #print("third point")
            x=(x+0.5)/2
            y=(y+1.0)/2
    #print(str(x) + " " + str(y))
    xx.append(x);
    yy.append(y);
#print("end")
pl.scatter(xx,yy, s=.1)
pl.show()
