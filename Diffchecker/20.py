def diff1(fname1,fname2):
    f1 = open(fname1,"r")
    f2 = open(fname2,"r")
    difflines = []
    for i in range(0,4,1):
        info1 = f1.readline()
        info2 = f2.readline()
        if info1!= info2:
            difflines.append(i)
    return difflines

result = diff1("file1.txt","file2.txt")
print(result)
