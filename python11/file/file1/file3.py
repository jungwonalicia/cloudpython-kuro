# with open("../data1.txt", "r") as fileInput:

import os

print(os.path.exists("data1.txt"))

if os.path.exists("data1.txt"):
    fileInput = open("data1.txt", "r")
    total_line = fileInput.readlines()
    print(total_line)

    for x in total_line:
        print(x)


        fileInput.close()
else:
    print("해당 파일이 없습니다.다시 확인해주세요.")       
