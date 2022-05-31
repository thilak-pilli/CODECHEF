my_list=[]
f=open('numbers.txt',"r")
for line in f:
        my_list.append((line.strip('\n')))
print(my_list)
f.close()
e= open("even.txt","a")
o= open("odd.txt","a")
for ele in my_list:
  if(int(ele)%2==0):
    e.write(ele+"\n")
  else:
    o.write(ele+"\n")
e.close()
o.close()
