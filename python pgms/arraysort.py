from array import*

a=array('i',[2,8,13,7])
print(sorted(a))
new=array(a.typecode,(v*v for v in a))
for e in new:
    print(e)
