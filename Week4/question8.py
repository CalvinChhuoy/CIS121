''''
total = 0 
sum = 0
while total >= 0:
    number = int(input("Enter a number: "))
if number >= 0:
    total += number
    print(f"{sum}")
'''''
'''''
num = int(input("Enter a number: "))
for x in range (1, num + 1):
    if num % x == 0:
        print(x)
'''''
'''''
def my_fctn (number):
    number += 2 
    number *= 4
    return(number)

result1 =my_fctn(10)
result2 = my_fctn(3)
print(result2)

print(my_fctn(my_fctn(10)))
'''''
'''''
def add_5(number):
    number += 5 
    return number

def times_2(number):
    number *= 2
    return number

x = times_2(add_5(10))
print(x)
#is x ==30 or x ==5
'''''
'''''
#write a power of 2 fctn calculate (3*2)^2 = 3^(2*3) ... 3^(2*10)
def power_2(number):
    number **= 2
    return number
result = power_2(power_2(3))
print(result)

#print(power_of_2(power_of_2(3)))

#using the times_2 function, muliple 5 by 2 a total of 10 times.
'''''
'''''
result = 5
def times_2(number):
    number *= 2
    return number
for i in range (0,10):
    result = times_2(result)
print(result)
'''''
'''''
#write a function that returns the product of two arguments.
def product (num1, num2):
    result = num1 * num2 
    return result

x = product (3, 4)
print(x)
'''''
#In python, a list start with [ and end with ]
#x = [ # this is a list with nothing in it.
lyst =["apple", "banana", 3, False, 4.5, "grapes"]
#write the code the prints the word banana from the list.

#print(lyst[1])

#write code that prints 3, False, 4.5

#print(lyst[2:5])

#write a code that only prints p from grapes in the list.

#print(lyst[5][3])

#print every element of the lyst one at a time.
#for element in lyst:
#    print (element)

#lyst.append( element ) will add the element to the end of the lyst.#
print(lyst)
lyst.append(12)
lyst.insert(3,12)
print(lyst)