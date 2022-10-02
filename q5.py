#Novruz Amirov id: 150200903
import math
def a_func(c):
    return (3*c - ((math.e)**c))

def b_func(c):
    return (c + 3 * (math.cos(c)) - ((math.e) ** c))

def c_func(c):
    return (c**2 - 4*c + 4 - math.log(c))

def d_func(c):
    return (c + 1 - 2*math.sin(c*math.pi))

#a
a = 1
b = 2
p = (a+b) / 2
result = round(a_func(p), 5)

while result != 0:
    p = (a+b) / 2
    result = round(a_func(p), 5)
    
    if a_func(a) * result < 0:
        b = p
    elif a_func(a) * result > 0:
        a = p
    else:
        result = round(a_func(p), 5)
        print("A) p is:", p)  

#b
a = 0
b = 1
p = (a+b) / 2
result = round(b_func(p), 5)

while result != 0:
    p = (a+b) / 2
    result = round(b_func(p), 5)
    
    if b_func(a) * result < 0:
        b = p
    elif b_func(a) * result > 0:
        a = p
    else:
        result = round(b_func(p), 5)
        print("B) p is:", p) 

#c1
a = 1
b = 2
p = (a+b) / 2
result = round(b_func(p), 5)

while result != 0:
    p = (a+b) / 2
    result = round(c_func(p), 5)
    
    if c_func(a) * result < 0:
        b = p
    elif c_func(a) * result > 0:
        a = p
    else:
        result = round(c_func(p), 5)
        print("C1) p is:", p)  

#c2
a = 2
b = 4
p = (a+b) / 2
result = round(c_func(p), 5)

while result != 0:
    p = (a+b) / 2
    result = round(c_func(p), 5)
    
    if c_func(a) * result < 0:
        b = p
    elif c_func(a) * result > 0:
        a = p
    else:
        result = round(c_func(p), 5)
        print("C2) p is:", p)  

#d1
a = 0
b = 0.5
p = (a+b) / 2
result = round(d_func(p), 5)

while result != 0:
    p = (a+b) / 2
    result = round(d_func(p), 5)
    
    if d_func(a) * result < 0:
        b = p
    elif d_func(a) * result > 0:
        a = p
    else:
        result = round(d_func(p), 5)
        print("D1) p is:", p)  

#d2
a = 0.5
b = 1
p = (a+b) / 2
result = round(d_func(p), 5)

while result != 0:
    p = (a+b) / 2
    result = round(d_func(p), 5)
    
    if d_func(a) * result < 0:
        b = p
    elif d_func(a) * result > 0:
        a = p
    else:
        result = round(d_func(p), 5)
        print("D2) p is:", p)  


    

    


