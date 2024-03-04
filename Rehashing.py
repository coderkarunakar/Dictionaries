#every thing is O(1)
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 5
        self.buckets = [None for _ in range(self.bucketSize)]
        self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hashcode):
        return abs(hashcode) % self.bucketSize

    def getValue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1  # Decrease count when a key is removed
                return head.value
            prev = head
            head = head.next
        return None
        #insert the new into the new bucket size
    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.bucketSize = 2*self.bucketSize
    
        #now i need to go to each element of the linked list
        self.count = 0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head = head.next
    def loadFactor(self):
        return self.count/self.bucketSize
    def insert(self, key, value):
        hashcode = hash(key)
        index = self.getBucketIndex(hashcode)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = self.buckets[index]
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.rehash()

        

m = Map()
for  i in range(10):
    m.insert('abc' + str(i) , i +1)
    print(m.loadFactor())

for i in range(10):
    print('abc' + str(i) + ':',    m.getValue('abc' + str(i)))




#Time complexity
# insert (key,value)
#first you get a key then you get a hash code to that,then you get an index corresponding to that ,you see through this linked list if that element is already present or not,if present then replace
#time which is taking is calculating the hash code  i.e O(l) ,and iterating on linked list O(n)
#so i say O(l) is very much lesser than O(n) because max lenght of the string will be 4 or 5 so o(l) is constant no
#so o(n) need to be improved

#if there are b boxes then n/b each entrie takes place,and this n/b should remain less thatn 0.7 (this factor is called as load factor) n->no of entries ,b->bucket size

#Rehashing: it initializes a new array of double size and what ever the previous element was,will try to store it in the new array whose size is the double of the previous size,increase the bucket size maintain n/b < 0.7


#Time complexity :
#Time Complexity for retrieving all keys from hashmap
#O(n)