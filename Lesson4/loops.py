#Create a list

names= ["blerta" , "erosi" , "driloni" , "brikena" , "ylli"]

#iterate in the names list and print every name

for name in names:
    print(name)


    ###

    sentence = "hello world"

    for character in sentence:
        if character.isalpha(): #check if the character is a letter
            print(character)



#range function

for number in range(1,6):#print number from the number 1 to 5 or more intail n to n-1
    print(number)


#######

numbers = [12,45,6,72,21,8,94,65]

#initialize a variable maxmimum with hte first value from the lsit numbers

maximum =  number[0]

for num in numbers: #begin a loop iterating through each lement in the list numbers
    if num > maximum: # check i f the current element num is bigger than the current maximum value
        maximum = num #if so , update the maximun value to be the current element in sum
        print(" the maximumn value in the list is : " ,maximum)



