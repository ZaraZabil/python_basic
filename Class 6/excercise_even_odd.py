# The program takes a list and puts the even and odd elements in it into two separate lists.
#
# Problem Solution
# 1. Take in the number of elements and store it in a variable.
# 2. Take in the elements of the list one by one.
# 3. Use a for loop to traverse through the elements of the list and an if statement to check if the element is even or odd.
# 4. If the element is even, append it to a separate list and if it is odd, append it to a different one.
# 5. Display the elements in both the lists.
enter=int(input("Enter umber of elements: "))
a=[]
for num in list(range(1,enter+1)):
    num=int(input("Enter number"))
    a.append(num)
print(a)
even=[]
odd=[]
for num in a:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)