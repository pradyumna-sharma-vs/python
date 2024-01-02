def give_holidays():
    import csv
    list1 =[]
    holiday=[]
    name=input("enter the state ")
    with open("Holidays_2024.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            list1 .append([row[0],row[1], row[2], row[3].replace("\n", " ").replace('&',',')])
    for l in list1:
        if "name" in l[3]:
            if "except" not in l[3]:
                holiday.append(str(l[0]+" "+l[1]+", Occasion : "+l[2]+"\n")) 
        elif "National" in l[3] and "except" not in l[3]:
            holiday.append(str(l[0]+" "+l[1]+", Occasion : "+l[2]+"\n"))
    return holiday

holiday=give_holidays()
print(*(h for h in holiday))
