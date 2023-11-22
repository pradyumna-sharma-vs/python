import mod_findlucky as mf
result=mf.findlucky(10)
print(result)
f1=open("lucky.txt","w")
s1="Honourable Prime MInister of India,The following are the lucky prisoner"
s2=""
for i in result:
    info1=str(i)
    s2=s2+","+info1
f1.write(s1+"\n")
f1.write(s2)
f1.close
