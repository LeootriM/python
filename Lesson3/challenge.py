#imagine you're a loyalty program for a popular sotre, you need to check whether a specific costumer is a part of this program. If they are , you should grant them the benefits of the discount
#members of the program:
#Alice
#Bob
#Charlie
#Anna


loyal_customers={'Alice' , 'Bob' , 'Charlie' , 'Anna'}
costumer = 'Alice'

is_member = costumer in loyal_customers
print("this person is a loyal costumer", is_member)

