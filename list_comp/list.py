numbers = [1,2,3,4,5]
# square_numbers =[]
# #for loop 
# for num in numbers:
#   square_numbers.append(num*num)
# print(square_numbers)

#list comprehesion

square_numbers = [num * num for num in numbers]
print(square_numbers)