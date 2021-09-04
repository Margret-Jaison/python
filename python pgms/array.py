from array import*

a=array('i',[])
n=int(input("enter the range"))

for i in range(n):
    x=int(input("enter the value"))
    a.append(x)
print(a)
print(sorted(a))
k=int(input("enter the key to be searched"))
c=0
for e in a:
     if(e==k):
       print(c)
       break
     c+=1
print("builtin function of search is")
print(a.index(k))