
#very important and most common interview question
#How to insert in map i.e Key value pair
#here doing only insert function
#map node is similar to linked list node but just not only data but a key ,value
class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

#defines a class named map
class Map:
    #defines constructor method for the map class
    def __init__(self) :
        #setting initial size of the bucket array to 10
        self.bucketSize = 10
        #initializes the buckets attribute as a list of size bucketsize with each element initialized to none
        self.bukets = [None for i in range(self.bucketSize)]
#initialzes the count of elements in  the map  to 0
        self.count = 0
        #defines a method size which returns the count of the elements in the map
    def size(self):
        #its count will be the size of the map
        return self.count
        #defines a method getbucketindex which takes a hash code as input and returns the index in the bucket array where the element should be inserted based on the hashcode
    def getBucketIndex(self,hashcode):
        return (abs(hashcode)%(self.bucketSize))
        #defines a method insert a key value pair into the map,it calculates the  hashcode for the key.gets the index for the hashcode using getbucket index method and initializes head with the bucket at the calculated index
    def insert(self,key,value):
        #calculating index
        #here we are using a hash function
        hashcode = hash(key)
        index = self.getBucketIndex(hashcode)
        #getting the head corresponding to that index
        head = self.bukets  [index]
#iterates through the linked list at the bucket index. if a node with the same key is found, it updates its value and returns
        while head is not None:
            #if anypoint our head key becomes to our key then replace that element
            if head.key == key:
                head.value = value
                return
                #this is to move to next step
            head = head.next
        head = self.bukets[index]
#creates a new map node with the given key value pair.inserts the new node at the begining of the linked list at the calculated index increments the count of the elements in the map
        newNode = MapNode(key,value)
        #at that particular index creating a head
        newNode.next = head
        self.bukets[index] = newNode
        self.count += 1

m = Map()
m.insert("karunakar",2)
print(m.size())
m.insert("Rohan",7)
print(m.size())
m.insert("karunakar",3)
print(m.size())

# overview:first we will try to find out the element if am able to find out the element then i just replace that value if am not able to find out the element then i will create a new element and i will point its next to be head at that linked list and i will insert that new node at that index and i will increase my count


        