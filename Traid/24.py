import math
triad1=[]
triad2=[]
triad3=[]
triad4=[]
list1=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
len1=len(list1)
for j in range(0,len1,1):
    p1=list1[j]*list1[j]
    for i in range(0,len1,1):
        p2=list2[i]*list2[i]
        output1=math.sqrt(p1+p2)
        output2=int(output1)
        if output1==output2:
            triad1.append(list1[j])
            triad2.append(list2[i])
            triad3.append(output2)

triad33=set(triad3)
triad333=list(triad33)
triad333.sort()
len3=len(triad3)
for i in range(0,len3,1):
    triad4.append((triad1[i],triad2[i],triad3[i]))
print(triad4)
