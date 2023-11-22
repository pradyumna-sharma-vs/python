def findlucky(num1):
    count=num1
    prison=["c"]*count
    lucky=[]
    unlucky=[]
    
    for i in range (0,count,1):
        prison[i]="0"

    for i in range(1,count,2):
        prison[i]="c"

    for j in range(2,count,1):
        for i in range(j,count,j+1):
            if prison[i]=="c":
                prison[i]="0"

            else:
                prison[i]="c"

    for i in range(0,count,1):
        if prison[i]=="0":
            lucky.append(i+1)
        else:
            unlucky.append(i+1)
    return lucky
findlucky(10)
findlucky(100)
