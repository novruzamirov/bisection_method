#Novruz Amirov id: 150200903
import random

#a
a = 0
b = 0
it = 0
for i in range(10000):
    x = random.random()
    y = random.random()
    z = random.random()

    if (x+y)*z == x*z + y*z:
        a = a + 1
    elif it == 0:
        print("\na) A set of 3 numbers the Distributive Law failed: ")
        print("x:", x, " y:", y, " z:", z)
        it = it + 1
        b = b + 1
    else:
        b = b + 1

c = a + b
print("Percentage of fails in Distributive Law: ", (b / c) * 100, "\n")

#b
it = 0
a = 0
b = 0
for i in range(10000):
    x = random.random()
    y = random.random()
    z = random.random()

    if (x+y)+z == x+(y+z):
        a = a + 1
    elif it == 0:
        print("b) A set of 3 numbers the Associative Law failed: ")
        print("x:", x, " y:", y, " z:", z)
        it = it + 1
        b = b + 1
    else:
        b = b + 1

d = a + b
print("Percentage of fails in Associative Law: ", (b / d) * 100, "\n")

#c
it = 0
a = 0
b = 0
for i in range(10000):
    x = random.random()
    y = random.random()
    z = random.random()

    if x+y == y+x:
        a = a + 1
    elif it == 0:
        print("A set of 2 numbers the Commutative Law failed: ")
        print("x:", x, " y:", y)
        it = it + 1
        b = b + 1
    else:
        b = b + 1

e = a + b
print("c) Percentage of fails for Commutative Law: ", (b / e) * 100, "\n")

#d1
it = 0
a = 0
b = 0
for i in range(10000):
    x = random.random()
    y = random.random()
    z = random.random()

    if (x*y)*z == x*(y*z):
        a = a + 1
    elif it == 0:
        print("d1) A set of 3 numbers the Associative Law for Multiplication failed: ")
        print("x:", x, " y:", y, " z:", z)
        it = it + 1
        b = b + 1
    else:
        b = b + 1

e = a + b
print("Percentage of fails for Associative Law for Multiplication: ", (b / e) * 100)

#d2
it = 0
a = 0
b = 0
for i in range(10000):
    x = random.random()
    y = random.random()
    z = random.random()

    if x*y == y*x:
        a = a + 1
    elif it == 0:
        print("A set of 2 numbers the Commutative Law for Multiplication failed: ")
        print("x:", x, " y:", y)
        it = it + 1
        b = b + 1
    else:
        b = b + 1

e = a + b
print("d2) Percentage of fails for Commutative Law for Multiplication: ", (b / e) * 100, "\n")


