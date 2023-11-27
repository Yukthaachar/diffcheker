import re

s1 = 'Dear $1salutation $2name ,You are kindly requested to make a payment of $3amount by $4date'
list4=[]
list3=[]
f1 = open('list1.txt', 'r')
list5 = f1.readlines()
length=len(list5)

for k in range(0,length,1):
    res = re.findall(r"\$\d\w+", s1)
    lenr = len(res)
    list1 = s1.split(' ')
    len1 = len(list1)
    list2 = list5[k].split(", ")
    for i in range(len1):
        if list1[i] in res:
            index_in_List2 = res.index(list1[i])
            list1[i] = list2[index_in_List2]
            if list1[1] == 'M':
                list1.remove(list1[1])
                list1.insert(1, "Mr.")
            if list1[1] == 'F':
                list1.remove(list1[1])
                list1.insert(1, "Ms.")
        list3 = " ".join(list1)
    print(list3)


