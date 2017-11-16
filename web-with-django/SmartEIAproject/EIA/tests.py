from django.test import TestCase
f = open("U://类别及代码.txt", "r",encoding='utf-8')
for line in f:
    line = line[0:len(line) - 1]
    print("                    <option>"+line+"</option>")   # do something here
f.close()
# Create your tests here.
