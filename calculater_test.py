m1 = int(input("Please enter one of the two numbers you'd like to know the multiplication to: "))
m2 = int(input("Please enter the other of the two numbers you'd like to know the multiplication to:"))

d1 = int(input("Please enter one of the two numbers you'd like to know the division to: "))
d2 = int(input("Please enter the other of the two numbers you'd like to know the division to: "))

a1 = int(input("Please enter one of the two numbers you'd like to know the addition to: "))
a2 = int(input("Please enter the other of the two numbers you'd like to know the addition to: "))

s1 = int(input("Please enter one of the two numbers you'd like to know the subtraction to: "))
s2 = int(input("Please enter the other of the two numbers you'd like to know the subtraction to: "))

while ValueError:
    print("One of the numbers you have entered is not an integer!")
    continue

while ZeroDivisionError:
    print ("You have encountered an ZeroDivisionError!")
    continue


print ("Here is your multiplication answer: ", m1*m2)
print ("Here is your division answer: ", d1/d2)
print ("Here is your addition answer: ", a1+a2)
print ("Here is your subtraction answer: ", s1 - s2)
