f = open("file2.csv", "r")

name, year, location, total, avg = [], [], [], [], []

for line in range(0, 5):
    line = f.readline()
    print(line)
    # 공백 문자를 제거한다. 
    line = line.strip()

    # 줄을 단어로 분리한다. 
    words = line.split(",")
    
    name.append(words[0])
    year.append(words[1])
    location.append(words[2])
    total.append(int(words[3]))
    avg.append(float(words[4]))
    
print(name)
print(year)
print(location)
print(total)
print(avg)

sum = 0
for x in total:
    sum = sum + x
print("total평균: " , sum/5)





