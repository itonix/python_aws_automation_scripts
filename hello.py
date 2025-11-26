# import math
# # for i in range(101):
# #     if math.remainder(i, 7) == 0:
# #         print(i)
# #     else:
# #         continue
# i = 0

# # while i < 101:
# #     if (math.remainder(i,7) == 0):
# #         print(i)
# #     i += 1
# #=========================================#
# # items = ["milk","cat","rat","pan","ran"]

# # for i in items:
# #     if (i == "rat"):
# #         print("found {}".format(i))
# #         continue
    
# #     print("not found{}".format(i))
# #     #=========================================#



# # shopping_list = ["cat","rat","jeans","pan","eggs"]
# # found_at = None
# # item_needed = "eggs"
# # numb =  len(shopping_list)

# # for item in shopping_list:

# # for item_nu in range(numb):
# #     if (shopping_list[item_nu] == item_needed):
# #         found_at = item_nu + 1
# #         print("found item  {} at {}".format(shopping_list[item_nu],found_at))


# #========================================================#
# for i in range(0,21):
#     if (i % 3 == 0 or i % 5 == 0 ):
#         continue
#     else:
#         print(i)
###-------------------------------------appending list##################
# mylist = ["cat","rat","jeans","pan","eggs"]

# a = b = c = mylist
# c.append("car")
# print(a)

# f = ["jam"]

# a.clear()

# print(a)

################################################################################


#available_list = ["ex-it", "mo-use", "key-board", "cp-u", "cab-le", "lap-top"]

# item_selected = []
# x = len(available_list)

# while True:
#     print("\nAvailable items:")
#     for i in range(x):
#         print(f"{i}: {available_list[i]}")

#     choose_item = int(input("Enter the number representing item (0 to exit): "))

#     if choose_item == 0:
#         break

#     if choose_item < x:
#         item_selected.append(available_list[choose_item])
#     else:
#         print("Invalid choice! Try again.")

# print("\nThe Items you selected: {}".format(item_selected))

###########################################string split###################

# x = "test-string"
# y = str(x.partition('-'))
# z = str(x.rsplit('-'))
# print(y)
# print(z)
#########################################



##############################split

# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]

# x = None
# flowers = []
# shrubs = []

# for number,name in enumerate(data):
#     x = name.rsplit(' - ')
#     if (x[1] == "Flower"):
#         flowers.append(x[0])
#     else:
#         shrubs.append(x[0])
# print(flowers)
# print(shrubs)





#######################################


# n = int(input("Enter number:"))
# t = input("Enter the value 'o' for odd and 'e' for even:")


# def sum_ofeven(evensum):
#     sum = 0
#     for i in range(evensum):
#         if (i % 2 == 0):
#             sum = sum + i
#     return sum
        
# def sum_ofodd(evensum):
#     sum = 0
#     for i in range(evensum):
#         if (i % 2 != 0):
#             sum = sum + i
#     return sum
    



# def sum_eo(n , t):
#     if ( t == 'e'):
#         return sum_ofeven(n)
#     elif ( t == 'o'):
#         return sum_ofodd(n) 
#     else:
#         return -1
         
  



# answer = sum_eo(n,t.lower())
# print(answer)

###############################################3




# def arguments(*valueofargs):
#     for i in valueofargs:
#         print(i)


# item = arguments(0,1,2,3,4)

############







# def sum_numbers(*args):
#     sum = 0
#     """ enter the values:"""
#     for i in args:
#         sum = sum + i
#     return sum



# print(sum_numbers(12.5, 3.147, 98.1))

###########################


# while open('hello.py',"r") as test:
#  for line in test:
#   print(line)


#############################################


