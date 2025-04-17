list1 = ["kyalo ","kevin","maryanne"]
list2 = ["ian","douglas","simon"]
list3 = list1 + list2
print(list3)
list1 += list2
print(list1)
list1 = list1 + list2
print(list1)
# appending the other list
for item in list2:
    list1.append(item)
print(list1)
# create list one = data science
# create list 2  = graphic design
# create list 3 = students
data_science = ["ian","maryanne","kevin"]
graphic_design = [ "douglas","john","papitoh"]
students = data_science + graphic_design
print(students)
backup = data_science.copy()
data_science.clear()
print(data_science)
print(backup)
#slicing list
