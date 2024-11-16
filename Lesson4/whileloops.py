from Lesson4.loops import number

count = 1 #initialize  the loop control variable

while count <= 10 : #the condition if count is less than or equal to 10
    print("iteration" , count)
    count+=1 #increment the loop control variable



# do while loop
# infinite loop

while True:
    #prompt user to enter a positive number

    user_input = input("enter a positive number: ")

#check if the input is a numeric

    if user_input.isnumeric():
    number = int(user_input)


    if number > 0:
        break

        #print the error message for valid input

        print("error please try again")

        #print the valid positive number entered by the user

        print("you have enetered a valid positive number: " ,number)



######
#break

    listofnumber = [1,2,3,4,5,6,7]
    target = 4

    for number in listofnumber:
        print(number) #print the current element that is being iterated
        if number == target #check if the current element is equal to the target value
            print("target found")
            break #end the loop immediatly after finding the target