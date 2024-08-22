
#Unordered,Unchangeable,Duplicates Not Allowed
# set1={"apple","mango","cherry"}
# print(set1) 



# set1={"apple","mango","cherry","apple"}
# print(set1)

# thisset = {"apple", "banana", "cherry", True,3, 1, 2}
# print(thisset)

# thisset = {True,2,1}
# print(thisset)

# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# this_set={'apple','banana','mango','cherry'}
# print(this_set)

# this_set=set(('apple','banana','mango','cherry'))
# print(this_set)



# Access Items

#loop
# this_set={'apple','banana','mango','cherry'}
# for w in this_set:
#     print(w) 


#true_false
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)
# print("jackfruit" in thisset)

# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset)
# print("jackfruit" not in thisset)




#Add set items {add(),update()}

# this_set={'apple','banana','mango','cherry','orange'}
# this_set.add('kiwi')
# this_set.add('pine apple')
# print(this_set)


# this_set_1={'apple','banana','mango'}
# this_set_2={'cherry','pineapple','kiwi'}
# this_set_1.update(this_set_2)
# print(this_set_1)
# print(this_set_2)

# this_set={'apple','banana','mango'}
# this_list=['cherry','pineapple','kiwi']
# this_set.update(this_list)
# print(this_set)

# this_list=['apple','banan','mango']
# this_set={'cherry','pine apple','kiwi'}
# this_list.extend(this_set)
# print(this_list)

#Remove Items {remove(),discard(),pop(),clear(),}


# this_set={'apple','banana','mango','cherry','orange'}
# this_set.remove('apple')
# this_set.remove('banana')
# this_set.remove('orange')
# this_set.remove('cherry')
# this_set.remove('mango')
# print(this_set)

# this_set={'apple','banana','mango','cherry','orange'}
# this_set.discard('apple')
# print(this_set)

# this_set={'apple','banana','mango','cherry','orange'}
# this_set.clear()
# print(this_set)


# this_set={'apple','banana','mango','cherry','orange'}
# this_set.pop()
# print(this_set)





#Join Sets
#union(),difference(),intersection(),difference_update(),



# this_set_1={'apple','banana','mango'}
# this_set_2={'cherry','pineapple','kiwi'}
# this_set=this_set_2.union(this_set_1)
# print(this_set)


# this_set_1={'apple','banana','mango'}
# this_set_2={'cherry','pineapple','kiwi'}
# this_set_3={34,3,4,7,9,8}
# this_set_4={45,22,75,755}
# this_set=this_set_1.union(this_set_2,this_set_2,this_set_3,this_set_4)
# print(this_set)

# this_set_1={'apple','banana','mango','kiwi','cherry'}
# this_set_2={'cherry','pineapple','kiwi','apple'}
# this_set__1=this_set_1.difference(this_set_2)
# this_set__2=this_set_2.difference(this_set_1)
# print(this_set__1)
# print(this_set__2)


# set1 = {"apple", "banana", "cherry","google"}
# set2 = {"microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

# this_set_1={1,2,4,5,6,7,3}
# this_set_2={4,5,6,7,8,9,10}
# this_set_3=this_set_1-this_set_2
# print(this_set_3)

# this_set_1={1,2,3,4,5,6,7}
# this_set_2={4,5,6,7,8,9,10}
# this_set_3=this_set_2-this_set_1
# print(this_set_3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple","banana"}
# set1.difference_update(set2)
# print(set1)


# this_set_1={1,2,3,4,5,6,7}
# this_set_2={4,5,6,7,8,9,10}
# this_set_1.difference_update(this_set_2)
# print(this_set_1)



# this_set_1={1,2,3,4,5,6,7}
# this_set_2={4,5,6,7,8,9,10}
# this_set_2.difference_update(this_set_1)
# print(this_set_2)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
