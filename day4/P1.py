import mod_rule2
import mod_rule3
import mod_rule4 as mr4

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word_done = []
man_sum = 0
Computer_sum = 0 

def transform1(file):
        f1 = open(file,'r')
        list1 = f1.read()
        list2 = []
        for j in range(0,26,1):
            templist = []
            for i in range(0,len(list1),1):
                if list1[i][0] == alpha[j]:
                    templist.append (list1[i])
            list2.append(templist) 
        return list2

last_word = ""
list1 = transform1('D:/SangamOne/Python/day4/dictionary_of_words.txt')
lastchar="a"
print("Input word starting from",lastchar)
input1=input()
result=mod_rule2.rule2(lastchar, input1)
isdisqualified=result
if(isdisqualified):
    print("Player is disqualified")
else:
    print("Player has entered",input1)

used=["apple","banana","carrot","drumstick","egg","fish"]
result=mod_rule3.rule3(used)
input1=result[1]
if(result[0]):
    print("Player disqualified")
else:
    print("Player has entered",input1)

s1="Enter a word within seconds "
s2="Player is disqualified due to Rule4"
s3="Player has entered the word "
timeout=5
result=mr4.rule4(s1,timeout)
time1=result[0]
input1=result[1]
if(time1>timeout):
    print(s2)
else:
    print(s3,input1)



