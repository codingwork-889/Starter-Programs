# print Hello
print("Hello Programmers ")


# if Demo with input method
#x1=int(input("Enter First Variable "))
x1=20
#y1=int(input("Enter Second Variable "))
y1=10
if x1>y1:
    print("x is greater than y")

#if else demo
if x1<y1:
    print("y is greater than x")
else:
    print("x is greater than y")

# if else with OR operator
#gen=input("Are you a male(y/n)")
gen='Y'
if gen=='y' or gen=='Y':
    print("Gender Male")
else:
    print("Gender Female")

#if else with AND operator
age=20
if age>=18 and age<=120:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
    
# if elif demo1
marks=75
if marks<35:
    print("Grade 'F':Fail")
elif marks>=35 and marks<=40:
    print("Grade 'D' ")
elif marks>=40 and marks<=50:
    print("Grade 'C'")
elif marks>=50 and marks<=60:
    print("Grade 'B'")
elif marks>=60 and marks<=70:
    print("Grade 'B+'")
elif marks >=70 and marks<=80:
    print("Grade 'A'")
else:
    print("Grade A+")
    
# if elif demo2
bill_amt=3900
if bill_amt>=5000:
    bill_amt=bill_amt-500
elif bill_amt>=4000 and bill_amt<=4999:
    bill_amt=bill_amt-400
elif bill_amt>=3000 and bill_amt<=3999:
    bill_amt=bill_amt-300
elif bill_amt>2000 and bill_amt<=2999:
    bill_amt-=200
elif bill_amt>1000 and bill_amt<=1999:
    bill_amt-=100
print("Final bill amount after discount is:",bill_amt)


#nested if
n=8
if n >10:
    print("Number is greater than to 10")
    if n%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Number is smaller than or equal to 10")
    
# Switch Case alternative (using dictionary)
myswitch={
1:"ONE",
2:"TWO",
3:"THREE",
4:"FOUR",
5:"FIVE"
    }
num=3
print("You enter:",myswitch.get(num,"invalid number"))

#for loop accessing element
print("for loop accessing element")
os=["Windows","mac os","unix","Linux"]
for x in os:
    print(x)

#demo 2
for x in 'Python':
    print(x)

#demo 3    
for x in range(1,11):
    print("Square of ",x*x)

#demo 4
print("even numbers between 1 to 25")
for x in range(1,26):
    if x%2==0:
        print(x)
#demo 5
print("for loop demo 5 multiplicative table")
n=5
for i in range(1,11):
    print(n*i)

# for else demo
for x in range(6):
    print(x)
else:
    print("end of loop")
    
#range function(demo 1)
print("demo 1")
for x in range(6):
    print(x)

#range function (demo 2)
print("demo 2")
for x in range(5,10):
    print(x)

#demo 3
print("demo 3")
for x in range(10,0,-2):
    print(x)
#while loop (demo 1)
print("while loop demo 1")
n=0
while n!=1:
    print("You are inside the while loop")
    print("Press 1 to exit from the loop:")
    n=1
print("You are out of the wile loop.")

#demo 2
print("while loop demo 2")
n=1
while n<=10:
    print(n)
    n+=1

#demo 3
print("while loop Square of number")
n=1
i=5
while n!=i:
    print("square of the number is :",i*i)
    break
print("end of program")

# while else demo
print("while else demo")
num=1
while num<=5:
    print(num,"is less than 5")
    num+=1
else:
    print("We reached to 5")

#nested loop demo
for x in range(1,11):
    for y in range(1,11):
        print("{0:02d}".format(x*y),end="")
    print()

#break demo
print("break demo")
for x in range(5):
    if x==3:
        break
    print("Number is ",x)

#continue demo
print("continue demo")
for x in range(5):
    if x==3:
        continue
    print("Number is ",x)

