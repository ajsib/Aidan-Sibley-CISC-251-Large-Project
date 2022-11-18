#!/usr/bin/python
import os

d1={}
# opening the same file twice
f1 = open("drugsamples.csv", "r")
f2= open("drugsamples.csv", "r")
for line1 in f1:
    d1[line1[0:9]]=[] #  initialize dictionary
f1.close()
for line2 in f2:
    d1[line2[0:9]].append(line2) #  add each line
f2.close()
# overwrite/create file
script = """
> results.csv
         """
f3 = open("results.csv", "w") #  open created file
os.system("bash -c '%s'" % script)
# user input minimum number of seizures
t1 = input("Please Enter the minimum number of seizures: ")
for key in d1:
    if len(d1[key]) > int(t1):
        for line in d1[key]:
            f3.write(line)
f3.close()



        


        
        
