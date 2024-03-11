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

# to get all the keys
print(a.keys())

# to get all the values
print(a.values())

# to get key-value pairs
print(a.items())

# iterating through keys
for i in a:

    #(printed only list)
    print(i,a[i])
   
#incase i dont want to get through all the values and i just want to pass through all the values
for i in a.values():
    #here printing only the dictionary 
    print(i)

#check if a key exist in dict or not
#this will tell you if the key exist in dict or not
print("list" in a)
print("dict" in a)
print("li" in a)