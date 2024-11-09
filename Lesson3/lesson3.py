#Create a set using curly braskets

#my_set={1,2,3}

#print(my_set)


#Creating a set from a list using the set() function

#my_set=([4,5,6])
#print(my_set)

#Create an empty set using the set() fuction

#my_set= set()
#print(my_set)

my_set = {1,1,2,3,4,5,6,3,4}

print(my_set)#Set will automaticlly remove duplicates

###################
set1={1,2,3}
set2={3,4,5}

#Union between set1 and set2 using the union() method

union_method = set1.union(set2)

#Compute  union between set1 and set2 using the | operator

union_operator = set1 | set2

print("union of set1 and 2 using method: ",union_method)
print("union of set 1 and set 2 using operator", union_operator)

# Compute intersection between set1 and set2 using the intersection method

intersection_method=set1.intersection(set2)

#computing intersection betweeen set1 and 2 using operator

intersection_operator = set1 & set2

print("intersection of set 1 and 2 using the intersection method" , intersection_method)
print("intersection of set 1 and 2 using the intersection operator" , intersection_operator)


#Computing the elements that are unique to set1 using the difference method

difference_method = set1.difference(set2)

#Computing elements that are unique to set1 using the - operator
difference_operator = set1-set2

print("difference of set1 and set2 using the difference method: " ,difference_method)
print("difference of set 1 and set 2 using the - operator:" ,difference_operator)


#computing the elements that are in set1 and in set 2 but not in their intersection

symemtric_difference_method = set1.symmetric_difference(set2)

#computing the elements that are in set1 and set 2 but not in their intersection using the ^ operator
symmetric_operator= set1 ^ set2

print("symmetric difference of set 1 and set2 using the symmetric difference method: " , symemtric_difference_method)
print("symmetric difference of set 1 and set 2 using the ^ operator" , symmetric_operator)

#SET METHODS

#create a set

my_sett = {1,2,3}

#add number 7 at the end of the set

my_sett.add(7)#add method

#removing number 3 from my set
my_sett.remove(3)#remove method


#removing 8 from the set without throwing an error if 8 is in now in the set

my_sett.discard(8)
print(my_sett)

#removing all the numbers from the set
my_sett.clear()

print(my_sett)


#remove duplications from a list

#Create a list that contains duplication

my_list=[1,2,3,4,4,55,7,6,4,5,4,6,10]

#convert this list to a set to remove duplications

unique_set=set(my_list)

print(unique_set)

#convert this set to a list

unique_list = list(unique_set)
print(unique_list)

#Checking for common elements

blertas_interest = {"music" , "movies" , "travel"}
drilonis_interest={"movies" , "games" , "football"}

common_intrests=blertas_interest.intersection(drilonis_interest)

print(common_intrests)

#IN operator

colors={"Green" , "red" , "purple" , "black"}
color = "blue"

print(color in colors)













