print("FLA LAB1 EX1")
list1 = ["Math", "English", "History", "Chemistry", "Biology"]
#1
print(list1[1])
#2
print(len(list1))
#3
print(list1[1:4])
#4
print(list1[-4])
#5
list2 = list1.copy()
list2.pop(3)
print(list2)
#6
list3 = list1.copy()
list3.insert(2, "Geography")
print(list3)
#7
list4 = list1.copy()
list4.remove("English")
list4.insert(1, "Romanian")
print(list4)

print("\n")
print("FLA LAB1 EX2")
dict1 = {"Fname" : "Jane", "Lname" : "Doe", "age" : 23}
#1
print(dict1.get("Lname"))
#2
dict2 = dict1.copy()
dict2.update({"age" : 21})
print(dict2)
#3
dict1.update({"occupation" : "student"})
print(dict1)
#4
dict3 = dict1.copy()
dict3.pop("Fname")
print(dict3)
#5
mylist11 = list(dict1)
print(mylist11)
#6
for i in dict1:
    print(dict1.get(i))
#7
dict1.setdefault("hobby", "chess")
print(dict1)
dict1.clear()
