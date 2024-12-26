l=[3,2,5,4,8,6,7]
n=len(l)

for i in range(n-1):
    if l[i]>l[i+1]:
    
        l[i],l[i+1]=l[i+1],l[i]
    
    
  
print(l)
