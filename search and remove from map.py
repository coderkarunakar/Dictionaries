class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 10
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

m = Map()
m.insert("karunakar", 2)
print(m.getValue('Parikh'))
print(m.size())
m.insert("Rohan", 7)
print(m.size())
m.insert("karunakar", 3)
print(m.size())
print(m.getValue('Rohan'))
print(m.getValue('Parikh'))
m.remove('Rohan')
print(m.getValue('Rohan'))
