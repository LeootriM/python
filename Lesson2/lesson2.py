#  Creating a tuple with person details


person = ("Leotrim" , 16, "Programmer")
name,age,profession=person
print(name, "'s" , "is" , age , "years old" , "and he is a" , "profession")


#Creating dictionary

my_dictionary={
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"

    #more keys more values pairs
}

contact_info={
    "blerta": "234-34245",
    "drini" : "145-05325"
}

#Create a variable called kreative's phone and use [] we can specify which key we eant to acces

kreative_phone = contact_info["blerta"]

print(kreative_phone)

print(contact_info)


#Change the key value
contact_info["drini"] = "0252525"
print(contact_info)

#we want to add another friend to contact_info

contact_info["Eros"] = "888833"

print(contact_info)

#delete a contact info

del contact_info["blerta"]
print(contact_info)



#print only te keys of the dictionary

keys = contact_info.keys()

print(keys)

#print the values
values = contact_info.values()
print(values)

#print items

items = contact_info.items()
print(items)
















