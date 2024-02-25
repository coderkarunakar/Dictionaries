#Collision handling in maps:
#you had a bucket and you had a hash function through which a key goes  and you get an index corresponding to that and you store that key and value pair
#Collision handling means multiple keys are going in to  the same index and handling this is known as Collision handling
#For handling Collosion we have 2 ways 1.Closed Hashing 2.Open Addresing
#1.Closed Hashing :if you get the multiple same index,then store in the same index only but store it as a form of Linked List it is also known as seperate chaining
#Open Addresing:here if you get multiple value in the same index it will not store in the same place it will find 
#to store key a  at some index we will first calculate the hash function of a and sum function of i
#Condition:for function of  i ,the f(0) should be 0
#the different f(i)(function of i) is 
#1.Linear Probing:here f(i) will be f(i) and here i will be 0,1,2,3..... and it moves linear ,it moves till it find an empty position
#2.Quadratic Probing :our f(i) will be i^2  here i =0^2,1^2,2^2,3^2... till you get some empty postion but this is bit faster than the Linear Probing
#3.double Hashing:here f(i) will be i * h(a),  for f(0) it will be 0,for f(1) it will be 1*h(a)
#for f(2) it will be 2*h(a)


#in this 3 techniques we are not storing the values in the same index we are actually storing in the different places ,only in Closed Hashing we are storing in the same index

#But in real scenario sepearate chaining works absoulutely fine,in terms of Time complexity it is as good,and it is quite easy 
#Seperate chaining is the best 