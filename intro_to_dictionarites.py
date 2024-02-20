#To create a dictionary
#Note:list were created using []
#Tuples were created using ()
#Dictionary were created using {}

#here we are going to discuss how to create a dictionary in multiple methods,and check its type ,printing 
#syntax:a={key:value}
a= {}
print(type(a))
#Note:the key ,value can be string and integer as well
#Note:here we need to give values and keys as well
b = {"the":1, "a":5,1000:"abc"}
type(b)
print(b)
print(("thel lenght of the dict is ",(len(b))))


#Note:you can copy a dictionary as well
c = b.copy()
print(c)

#Another way of creating the dict is using a list and inside that using a list pair is used
d = dict([("the",3),("a",10),(2,3)])
print(d)

#Another way of creating ,but in this case all the values become none ,since we gave only keys
e = dict.fromkeys(["abc",32,4])
print(e)
#in this case all the for all the keys the  values will be 10 ,since we mentioned at the end
f = dict.fromkeys(["hii",3,5],10)
print(f)

#Note:Dictionaries are mutable ,we can change the values and keys   