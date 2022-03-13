1.	Create a program that asks the user to enter their name and their age. Print out a message that tells them the year that they will turn 100 years old
username = input("Enter username:")
age = input("Enter  age: ")
print('Hi %s turn into 97 years old on %s' %(username, age))

O/P ==> 
C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
Enter username:mani
Enter  age: 23
Hi mani turn into 97 years old on 23
=================
2.	What is pandas groupby? Demonstrate with your own example
import pandas as pd

metro_city_data = {'city': ['Chennai', 'Chennai', 'Mumbai', 'Mumbai', 'Kolkatta',
   'Kolkatta', 'Kolkatta', 'Kolkatta', 'Chennai', 'Royals', 'Royals', 'Chennai'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876000,789000,86300,6735600,7410052,8120045,7560045,7880054,694562,7014587,80424587,69024587]}
df = pd.DataFrame(metro_city_data)
df_grouped = df.groupby(['city', 'Year']).groups
print(df_grouped)

O/P 
C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
{('Chennai', 2014): [0], ('Chennai', 2015): [1], ('Chennai', 2016): [8], ('Chennai', 2017): [11], ('Kolkatta', 2014): [4], ('Kolkatta', 2015): [5], ('Kolkatta', 2016): [6], ('Kolkatta', 2017): [7], ('Mumbai', 2014): [2], ('Mumbai', 2015): [3], ('Royals', 2014): [9], ('Royals', 2015): [10]}

Process finished with exit code 0
====================================
3.	How to create a dataframe from list?
import pandas as pd

metro_city_data = {'city': ['Chennai', 'Chennai', 'Mumbai', 'Mumbai', 'Kolkatta',
   'Kolkatta', 'Kolkatta', 'Kolkatta', 'Chennai', 'Royals', 'Royals', 'Chennai'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876000,789000,86300,6735600,7410052,8120045,7560045,7880054,694562,7014587,80424587,69024587]}
df = pd.DataFrame(metro_city_data)
cityList= df['city'].tolist()
print(cityList)

O/P 

C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
['Chennai', 'Chennai', 'Mumbai', 'Mumbai', 'Kolkatta', 'Kolkatta', 'Kolkatta', 'Kolkatta', 'Chennai', 'Royals', 'Royals', 'Chennai']

Process finished with exit code 0
=====================================================
4.	What are the ways to combine the dataframe in pandas. Give an example for each
import pandas as pd

metro_city_data = {'city': ['Chennai', 'Chennai', 'Mumbai', 'Mumbai', 'Kolkatta',
   'Kolkatta', 'Kolkatta', 'Kolkatta', 'Chennai', 'Royals', 'Royals', 'Chennai'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876000,789000,86300,6735600,7410052,8120045,7560045,7880054,694562,7014587,80424587,69024587]}

metro_city_data1 = {'city': ['Chennai1', 'Chennai1', 'Mumbai1', 'Mumbai1', 'Kolkatta1',
   'Kolkatta1', 'Kolkatta1', 'Kolkatta1', 'Chennai1', 'Royals1', 'Royals1', 'Chennai1'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876000,789000,86300,6735600,7410052,8120045,7560045,7880054,694562,7014587,80424587,69024587]}
df = pd.DataFrame(metro_city_data)
df1 = pd.DataFrame(metro_city_data1)
join = [df, df1]
res1 = pd.concat(join)

print(res1)

O/P 

C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
         city  Rank  Year    Points
0     Chennai     1  2014    876000
1     Chennai     2  2015    789000
2      Mumbai     2  2014     86300
3      Mumbai     3  2015   6735600
4    Kolkatta     3  2014   7410052
5    Kolkatta     4  2015   8120045
6    Kolkatta     1  2016   7560045
7    Kolkatta     1  2017   7880054
8     Chennai     2  2016    694562
9      Royals     4  2014   7014587
10     Royals     1  2015  80424587
11    Chennai     2  2017  69024587
0    Chennai1     1  2014    876000
1    Chennai1     2  2015    789000
2     Mumbai1     2  2014     86300
3     Mumbai1     3  2015   6735600
4   Kolkatta1     3  2014   7410052
5   Kolkatta1     4  2015   8120045
6   Kolkatta1     1  2016   7560045
7   Kolkatta1     1  2017   7880054
8    Chennai1     2  2016    694562
9     Royals1     4  2014   7014587
10    Royals1     1  2015  80424587
11   Chennai1     2  2017  69024587

Process finished with exit code 0

-------------------------- 
df = pd.DataFrame(metro_city_data)

df1 = pd.DataFrame(metro_city_data1)


res2 = pd.merge(df, df1, on= ['city', 'Rank', 'Year', 'Points'])
#print(res1)
print(res2)

=====================================
Q 5 What is the difference between list and tuples in Python 
Key   List	                            Tuple
1     List is mutable                   tuple is immutable 
2.    List represents []                tuple represents ()
3.    consume more memory               Less Memory 

============================================
Q6 Find out the mean, median and standard deviation of this numpy array -> np.array([1,5,3,100,4,48])

import numpy as np

print('=========================================================')
num_array = np.array([1,5,3,100,4,48])
print('Given Array = ', num_array)
mean_value = np.mean(num_array)
print('Mean Value = ', mean_value)
median_value = np.median(num_array)
print('Median Value = ', median_value)
std_dev_Value = np.std(num_array)
print('Standard Deviation Value = ', std_dev_Value)

----------------------
O/P
-------------
C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
=========================================================
Given Array =  [  1   5   3 100   4  48]
Mean Value =  26.833333333333332
Median Value =  4.5
Standard Deviation Value =  36.59424666377065

Process finished with exit code 0
=======================================================================================================
Q7. 7.	How will you remove duplicate elements from a list?

print('=========================================================')
num_list = [1, 5, 3, 6, 3, 5, 6, 1, 45, 56 , 45 , 56, 100, 101 , 100]
print("The original list is : " + str(num_list))
cln_list = list(set(num_list))
print( 'List after removing duplicate through set = ', cln_list)
# to remove duplicated from list
result = []
[result.append(x) for x in num_list if x not in result]
print('Duplicate removed through for list iteration check and append = ',result)

---------------------------------------
O/P
----------------------
C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
=========================================================
The original list is : [1, 5, 3, 6, 3, 5, 6, 1, 45, 56, 45, 56, 100, 101, 100]
List after removing duplicate through set =  [1, 3, 100, 5, 6, 101, 45, 56]
Duplicate removed through for list iteration check and append =  [1, 5, 3, 6, 45, 56, 100, 101]

Process finished with exit code 0
==========================================================================================================

Q8.	What is a map() function in Python? Give an example

   Map function retunrs a map object [Which is an iterator]   of the result after applying the given function to each item of a given iteratable (list , tuple etc.]
   
 map(fun, iter)
 
 Parameters :
    fun : It is a function to which map passes each element of given iterable.
    iter : It is a iterable which is to be mapped.
 
 Ex: 
    def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
print('Given List = ',numbers)
result = map(addition, numbers)
print('Processed List = ', list(result))
------------------------------------------ 
O/P 
-------------
C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
Given List =  (1, 2, 3, 4)
Processed List =  [2, 4, 6, 8]

Process finished with exit code 0
=========================================================================================================
Q9.	What is pass in Python?

The pass statement is generally used as a placeholder i.e. when the user does not know what code to write. So user simply places pass at that line.
-----------------
Ex: 
  li = ['a', 'b', 'c', 'd']
print('List Given = ',li)
for i in li:
    if (i == 'a'):
        pass
    else:
        print(i)
        
----------
O/P
--------
   C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
List Given =  ['a', 'b', 'c', 'd']
b
c
d

Process finished with exit code 0
====================================================================
10.	What is vstack() in numpy? Give an example

   numpy.vstack() function is used to stack the sequence of input arrays vertically to make a single array.
   
--------------------------------
import numpy as np

in_array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
in_array2 = np.array([[11, 12, 13, 14], [15, 16, 17, 18]])
out_array = np.vstack((in_array1, in_array2))
print(' Array List1 = \n', in_array1)
print(' \n Array List2 = \n', in_array2)
print(' \n putput Array  = \n', out_array)
-----------------
O/P
----------------
C:\Users\manikandan\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/manikandan/PycharmProjects/pythonProject/test.py
 Array List1 = 
 [[1 2 3 4]
 [5 6 7 8]]
 
 Array List2 = 
 [[11 12 13 14]
 [15 16 17 18]]
 
 putput Array  = 
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [11 12 13 14]
 [15 16 17 18]]

Process finished with exit code 0

======================================================================