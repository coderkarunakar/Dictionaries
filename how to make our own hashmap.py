#how to make our own hashmap(Dictionary)
#our access and insert should be very fast so inorder to get that we can use array or a list 
#if you want to isert an particular index,for that index you have to convert the key to the integer,that index should be an integer
#convert key to an integer ,this function is called as an hash function
#key -> hash function ->Integer
#and  the array we are using is called as bucket array and it has keys
#Hash function is distributed into 2 parts 1.hash code 2.compresion function
#hashfunction:when we give an string it converts to  a byte code this compression fucntion is used to make the array into that particular size this is the use of the compression fucntion
#hash code:when you pass a key through a hash function it will give you a hash code ,the hash code can be a any integer,but to make sure that comes with in the limits i will pass through the hash compression function
#the perfect compression function size is modulo bucket size
