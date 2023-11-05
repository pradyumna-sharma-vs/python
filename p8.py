def perm3(word3):
    word3=word3
    list3=[]
    s1=word3[0:1]
    s2=word3[1:2]
    s3=word3[2:3]
    list3.append(s1+s2+s3)
    list3.append(s1+s3+s2)
    list3.append(s2+s1+s3)
    list3.append(s2+s3+s1)
    list3.append(s3+s1+s2)
    list3.append(s3+s2+s1)
    return list3

def perm4(word4):
    word4=word4
    list4=[]
    s1=word4[0:1]
    s2=word4[1:2]
    s3=word4[2:3]
    s4=word4[3:4]
    part1=s1
    part2=s2+s3+s4
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    part1=s2
    part2=s1+s3+s4
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    part1=s3
    part2=s1+s2+s4
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    part1=s4
    part2=s1+s2+s3
    result=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+result[i])
    print(list4)
word4="FAST"
perm4(word4)
