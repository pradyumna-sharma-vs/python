master=[
    ["apple", "add"], ["bat", "ball"], ["cat", "camera"], ["dirty", "domestic"],
    ["elephant", "ear"], ["friend", "famous"], ["goat", "gun", "Ground"],
    ["horse", "hat", "humble"], ["important", "indication"], ["jewelry", "joke"],
    ["key", "kilogram"], ["light", "lemon"], ["man", "mat"], ["nest", "nature"],
    ["orange", "owl", "origin", "omission"], ["pen", "paper", "person"],
    ["queue", "quiz"], ["red", "rainbow"], ["strong", "smile"], ["train", "tea"],
    ["umbrella", "ugly"], ["violin", "victory"], ["water", "waste", "watch", "war"],
    ["xmas", "xerox"], ["yellow", "yak"], ["zebra", "zero", "zoo"]
]
s1="smile"
len1=len(s1)
char1=s1[len1-1]
print(char1)
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(0,10,1):
    s1 = input()
    len1 = len(s1)
    char1 = s1[len1 - 1]
    position = alpha.index(char1)
    s2=master[position][0]
    
    print("Round "+str(i),"-",s1,"-",s2)
