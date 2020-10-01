#num_list=[1,2,3,4,5]
#for num in num_list:
   # print(num*num)
#my_empty_list=[]
#num_list=[1,2,3,4,5]
#for num in num_list:
  #  square=num**2
   # my_empty_list.append(square)
#print(my_empty_list)
my_empty_list=[]
user_num=int(input("For how many numbers you wat to square"))
for num in list(range(1,user_num+1)):
    square=num**2
    my_empty_list.append(square)
print(my_empty_list)