#Adding or removing data in dictionary
#Access looping elements in dictionary
#Note:a dictionary can have a value as a dictionary
a = {1:2, 3:4, "list":[1,23],"dict":{1:2}}
print(a)
#Note:here there is no indexing ,here you can use actual key
#you can access the data by using 
print(a[1])
print(a[3])
print(a["list"])
print(a['dict'])

#Another way of accesing the data is 
print(a.get(1))
#here actually the key li is not present but this gives you the output as None
print(a.get("li"))
#but instead of getting output as none you can make what ever you want if the value is not present,i.e it will return the value associated with it ,incase the value is presetnt,other wise it will return the second argument
print(a.get('li',0))
a = {1: 2, 3: 4, 'list': [1, 23], 'dict': {1: 2}}

# to get all the keys(it gves you no of keys)
print(a.keys())

# to get all the values(it gives you no of  values)
print(a.values())

# to get key-value pairs(it gives you the list )
print(a.items())

# iterating through keys(list)
for i in a:
    print(i,a[i])
   
#incase i dont want to get through all the values and i just want to pass through all the values(dict)
for i in a.values():
#it  is just printing the no of values
    print(i)

#check if a key exist in dict or not
#this will tell you if the key exist in dict or not
print("list" in a)
print("dict" in a)
print("li" in a)


###Adding removing data in dict

#Adding
#i want to add and tuple into the dictionary
a['t'] = (1,2,3)
print(a)

#we can update the data as well since it is mutable
#updating
a[1]=10
print(a)
#we can update by creating a new dict as well in this case what we create in b will be updated to a ,in this case any thing which is similar will be updated as per b ,and differ one will be simply added
b = {3:5, 'the':4, 2:100}
a.update(b)
print(a)

#Remove
#here also we can remove the key value pair by using its key ,
#using a pop method but here u need to give the key 
a.pop('t')
print(a)

#Note:in pop if the key is not there then you will be getting the key error
#or instead of pop you can use delete on a particular key
#but here also u need to give the key
del a[1]
print(a)


#using clear also we can remove every thing:this removes everything and it makes dictionary empty
a.clear()
print(a)

#incase if you want to delete the dictionary it self then simply use ,now
del a
#now if you try to search a then you will be getting the error since there is no element with name a since the data a is not there here you will be getting the error
print(a)
