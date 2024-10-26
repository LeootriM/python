#Declaring a variable

#variable_name=value

tenperature = 22.0

name = "Leotrim"

print(type(tenperature))
print(type(name))

age =16

x = 5
y=9

result = x*y

print(result)

#update value
age=age+1
print(age)

#combine value

first_name ="trimi"
last_name="sylejmani"

full_name= first_name + " " +last_name
print(full_name)

#Lists

name_of_the_list=['item1' , 'item2' , 'item3']

#example of a list

shopping_list=["apples" , "banana" , "milk" , "bread", 15]

print(shopping_list)

#indekximi mbrenda nje liste

homework =["math" , "psikologji" , "biologji" , "anglisht"]
print(homework[0])
print(homework[3])
print(homework[1])
print(homework[2])


to_do_list=["teach 11d" , "go shopping" , "create an app" , "watch the game"]
first_item=to_do_list[0] #this is accessing the first item at index 0 which is teach11d
second_item=to_do_list[1]

favorite_subject=["psikologji" , "ed.fizike" , "sociologji"  ]
forth_subject = favorite_subject[1]
print(forth_subject)



#adding data to a list we do sot by using append() method

#i want to add strawberries to the shopping list

shopping_list.append("strawberries")

print(shopping_list)

#insert method lets us specify where we want to add our element

shopping_list.insert(2, "lemons")
print(shopping_list)



#remove() methods help use remove items from the list

to_do_list.remove("create an app")
print(to_do_list)

del to_do_list[2]


#updateing data, ypu can change the value of an item by assigning a new value

to_do_list[0]="teach 1g"
print(to_do_list)

