#bacanya 0,1,2,3,4,5,6,7,8
# list1 = [1,2,3,4,5,6,7,8,9]
#bacanya -8 -7 -6 -5 -4 -3 -2 -1

#print dari list1 pada index ke-2
#print(list1[2])

#print dari list1 pada index ke-(-3)
#print(list1[-3])

# print(list1[1:]) #print dari index 1 sampai selesai
# print(list1[1:5]) #print dari index 1 sampai ke 5
# print(list1[:5]) #print semua sampai index ke 5

# #manipulasi list
# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)

# list1[8] = "Pelatihan 3"
# print(list1)

# del list1[8]
# print(list1)

# list1.clear()
# print(list1)

# list1.append("Desktop")
# print(list1)

# list1.extend(["Programming","AMCC",2020,2021])
# print(list1)
#------------------------------------------------#

# my_tuple = ('Hallo sayang')
# print(my_tuple[1])
# print(my_tuple[-1])
# print(my_tuple[:5])
# print(my_tuple[5:])
# print(my_tuple[1:4])

# my_tuple = (1,2,3,[6,5])
# print(my_tuple[3][0])

# my_tuple = (5,6,7)
# print(my_tuple)

# del my_tuple
# print(my_tuple)

# my_tuple = ('Hallo sayang')
# print(my_tuple.index('s'))
#-----------------------------------------------#

# list1 = [1,2,3,4,5]
# set1 = set(list1)
# print(set1)

# set2 = {1,2,3,4,5}
# print(set2)

# set2.add(8)
# print(set2)

# set2.update([5,6,7,8])
# print(set2)
# #data yang di remove, kalo diremove lagi ga error
# set2.discard(7)
# set2.discard(7)
# print(set2)
# # #data yang udah di remove, kalo diremove lagi bakal eror
# # set2.remove(8)
# # set2.remove(8)
# # print(set2)

# set2.clear()
# print(set2)

# set3 = {10,11,12,13,14}
# set4 = {21,22,23,24,10}

# print(set3 | set4)
# print(set4.union(set3))
#-----------------------------------------------#

dict1 = {1:"Salsabila",2:"Klaten",3:19}
# print("Hai namaku", dict1[1])
# print("Asalku dari", dict1.get(2))

dict1[5] = "Informatika"
print(dict1)

dict1[5] = "Geografi"
print(dict1)

del dict1[3]
print(dict1)

dict1.clear()
print(dict1)