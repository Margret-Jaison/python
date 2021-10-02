# filter, map,reduce


from functools import reduce
num=[1,5,7,4,8,6,9]
even=list(filter(lambda a:a%2==0,num))
double=list(map(lambda a:a*2,even))
sum=reduce(lambda a,b: a+b,double)
print(even)
print(double)
print(sum)
