
data = []
data2 = []
array = []
count = 0
count2 = 0
count3 = 0
count4 = 0
latvia = "Latvia"
ocount = 0
a = -1
with open ("data.txt", "r") as f:
    for row in f:
        data = row
        text = data.find("Latvia")
        data2 = row.rstrip().split(",")
        array = row
        omana = data.find("Omana")
        if text != a:
            length = len(data2)
            people = data2[length-1]
            people = int(people)
            count = count + people
            text2 = data.find("Telecommunication")
            text3 = data.find("https://")
            text4 = data.find(".org")
            if text4 != -1:
                count4= count4 + 1
            if text3 != -1:
                count3 = count3 + 1
                
            if text2 != -1:
                count2 = count2 + 1
        
            
            
print(count4)
print(count3)
print(count2)
print(count)
print(latvia)
print(data2)
print(array)