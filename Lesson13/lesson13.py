import numpy as np
import pandas as pd

arr_2d = np.array([[1,2,3,4,5] , [6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

dimension = arr_2d.ndim
print(dimension)

size = arr_2d.size
print(size)

products=['apples' , 'bananas' , 'oranges' , 'pear']

sales = [200 , 300 ,400 ,100]

sales.series = pd.Series(sales , index=products)

total_sales = sales_series.sum()

best_selling_product = sales.series.idxmax()

highest_number = sales.series.max()

print(f"best sellin product is: " {best_selling_product} , "with" , {highest_number})