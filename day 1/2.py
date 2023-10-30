def reverse1(word1):
    s1=word1
    len1=len(s1)
    for i in range(1,len1+1,1):
        print(s1[len1-i],end="")
    print()
reverse1("Pradyumna is staying at Chitpady,Udupi with his family")
reverse1("Nidhi Prabhu is staying at Ajarkadu")
reverse1("Shivashankar is staying at Hosur near Bangaluru")
