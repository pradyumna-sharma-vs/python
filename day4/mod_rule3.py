def rule3(list1):
    used=list1
    len1=len(used)
    input1=input("Enter a word: ")
    isdisqualified=False
    if input1 in used:
        isdisqualified=True 
    else:
        print()
    return(isdisqualified,input1)

        




