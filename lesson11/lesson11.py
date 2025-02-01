import datetime

current_time = datetime.datetime.now()

print("year: ", current_time.year)
print("month: " ,current_time.month)
print("day: ", current_time.day)
print("hour: ", current_time.hour)
print("minute: " ,current_time.minute)



current_timenow = datetime.datetime.now().date()

print(current_timenow)

print("year: " , current_timenow.year)
print("day: " , current_timenow.day)



settime = datetime.datetime.now()

specific_time = datetime.datetime.now().time()
specific_time = datetime.datetime(2000,1,4)



future_time = current_time + datetime.deltatime(days = 100)

print(future_time)

print(future_time.year)


teksti = "this is what i/n want to write"

with open ("example.txt" , "w")as file:
    file.write(teksti)


file_path = "example.txt"
file = open(file_path , "r")

content = file.read()
print(content)
file.close()

with open("example.txt" , "r") as file:
    lines = file.readLines()
    print(lines)

    with open("example.txt", "r") as file:
        line = file.readLine()
        print(line)

        if os.path.exists("example.txt")
            print("file exists")




