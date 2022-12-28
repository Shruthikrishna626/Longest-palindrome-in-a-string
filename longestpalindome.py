#program to print largest palindrome in a string
s=input("enter a string\n")
s1=s[::-1]
print(s,s1)
s3=""

for i in range(len(s)):
    if s[i]==s1[i] and s.find(s[i])==s1.find(s1[i]):
        s3=s3+s[i]
s3=set(s3)
for i in s3:
    print( ''.join(i),end="")



    

#just for understand logic

       # print(s[i])
    #else:
        #print("not match")
#if s[1]==s1[1]:
 #   print(s[1])
#else:
#   print("not match")
#if s[2]==s1[2]:
   # print(s1[2])
#else:
    #print("not match")
#if s[3]==s1[3]:
   # print(s[3])
#else:
    #print("not match")
