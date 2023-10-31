master=[]
s1="smile"
len1=len(s1)
char1=s1[len1-1]
print(char1)
listA = ["apple","add"]
listB = ["bat","ball"]
listC = ["cat","camera"]
listD = ["dirty","domestic"]
listE=["elephant","ear"]
listF=["friend", "famous"]
listG=["goat","gun","Ground"]
listH=["horse","hat","humble"]
listI=["important","indication"]
listJ=["jewellry","joke"]
listK=["key","kilogram"]
listL=["light","lemon"]
listM=["man","mat"]
listN=["nest","nature"]
listO=["orange","owl","origin","omission"]
listP=["pen","paper","person"]
listQ=["queue","quiz"]
listR=["red","rainbow"]
listS=["strong","smile"]
listT=["train","tea"]
listU=["umbrella","ugly"]
listV=["voilin","victory"]
listW=["water","waste","watch","war"]
listX=["xmas","xerox"]
listY=["yellow","yak"]
listZ=["zebra","zero","zoo"]
master.append(listA)
master.append(listB)
master.append(listC)
master.append(listD)
master.append(listE)
master.append(listF)
master.append(listG)
master.append(listH)
master.append(listI)
master.append(listJ)
master.append(listK)
master.append(listL)
master.append(listM)
master.append(listN)
master.append(listO)
master.append(listP)
master.append(listQ)
master.append(listR)
master.append(listS)
master.append(listT)
master.append(listU)
master.append(listV)
master.append(listW)
master.append(listX)
master.append(listY)
master.append(listZ)
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(0,10,1):
    s1 = input()
    len1 = len(s1)
    char1 = s1[len1 - 1]
    position = alpha.index(char1)
    s2=master[position][0]
    
    print("Round "+str(i),"-",s1,"-",s2)
