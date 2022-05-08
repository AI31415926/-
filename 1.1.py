a=[1 for i in range(300)];
a[0:2]=[0,0];
for i in range(2,300):
    if a[i] ==1:
        for j in range(i+1,300):
            if a[j]!=0 and j%i==0:
                a[j]=0
for i in range(300):
    if a[i] ==1:
        print(i,end=' ')
