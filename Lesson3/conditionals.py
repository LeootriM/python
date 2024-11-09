#Conditional
from tempfile import tempdir

age = 19

if age>=19:
    print("you can vote")
else:
    print("you cannot vote")

    #Temperature

    temperature = 28
    if temperature >30:
        print("is a hot day")
    elif 20<=temperature <=30:
        print("the weather is pleasant")
    else:
        print("it is a cold day today")