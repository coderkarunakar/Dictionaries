#what is hashcode
#for integer the hashcode will be the same integer only
#in case of strings  sum of asci values for all the characters in case of strings
#ex:for abc ->asci(a)+asci(b)+asci(c)
#but for strings the above one is not correct because for abc,bac,cab all will be similar so the best approach will be
#Approach is :Number base power like 0,1,2,3,4.... it goes on
#ex:abc -->10^2(asci(a)) + 10^1(asci(b))+10^0(asci(c))
#ex:bac -->10^2(asci(b)) + 10^1(asci(a))+10^0(asci(c))
#ex:cab -->10^2(asci(c)) + 10^1(asci(a))+10^0(asci(b))
#for compression we will be using modulo bucket size(%bucket size)

#Collision handling:after getting a hashcode ,after compressing we got the same index this is actually called as collision handling
#we can use inbuilt has() function,compression handler is %bucket size

