s=0
for n in range(1,21):
    i=2
    c=0
    for i in range(2,n):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        s=s+n

print(s)
            
