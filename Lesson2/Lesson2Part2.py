from Lesson2.lesson2 import contact_info

contact_information={

    "Trimi": {
"phone_number": "402351548",
"email": "haha@gmail.com",
"address": "prishtina"
    },

    "VP": {
"phone_number": "2232321",
"email": "vp@gmail.com",
"address": "Vranjevc"
    },

    "BL": {
"phone_number": "777777",
"email": "bl@hotmail.com",
"address": "Llukar"
    }
}

#Change someones detail
contact_information["Trimi"]["email"]="trimbaba@gmail.com"
print(contact_information)