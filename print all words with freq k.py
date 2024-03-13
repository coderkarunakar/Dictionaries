#print all the words with the frequency k
#example:"this is a word string having many many words"
#we need to print only the frequency 1 i.e in this case we will be getting output as this is a word string having words 
#here we wont be getting the many in the output because it has frequency 2 so it wont be printed ,rest all other is having frequency 1 so this will be printed
s = "this is a word string having many many word"
k = 2
#approach:split the string into single single word
words = s.split()
print(words)
#this is to get the frequency of the each word
#create a dictionary
# d = {}
# #go through all the words in the list
# for w in words:
#     #corresponding to this word my dictionary should have a key and the value should be the frequency,
#     #when ever i see a word increase that words frequency by 1
#     #if word is in dictionary,then increase its frequency
#     if  w in d:
#         d[w] = d[w] + 1
#         #if it is not in the dicitonary then makes its frequency to be one
#     else:
#         d[w] = 1

# print(d)


#more consice method
#created an empty dictionary
d = {}
#loop through the all words
for w in words:
    #if the word is there then give me the value stored corresponding to it,if the word is not there then give me the 2nd argument i.e 0 in this case
    #if the value is not there in the dictionary d then it returns 0  and +1 to it
    d[w] = d.get(w,0) + 1
print(d)

#Now dictionary contains all words  and its frequency
#Actual logic print according to the frequency i.e k
#loop through each word in the dictionary
for w in d:
    #here words in dictionary is equal to k then print that particular word
    #if the index words value is  equal to the freq of k then it get printed else no ,here the k
    # s frequency is equal to 2
    if d[w] == k:
        print(w)



# #Another Approach
#     #printing using a function another approach
# def printkfreqwords(s,k):
#     words = s.split()
#     d = {} 
#     for w in words:
#         d[w] = d.get(w,0) + 1
#     for w in d:
#     #here words in dictionary is equal to k then print that particular word
#         if d[w] == k:
#                 print(w)
# printkfreqwords(s,1)