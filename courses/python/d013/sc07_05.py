myList = [30, 10, 20]
print("list :", myList)
myList.append(40)
print("after append(40) :", myList)
print("using pop() :", myList.pop())
print("after pop :", myList)
myList.sort()
print("sort :", myList)
myList.reverse()
print("reverse :", myList)
print("index(20) :", myList.index(20))
myList.insert(2, 222)
print("insert 222 at index 2 :", myList)
myList.remove(222)
print("after removing 222 :", myList)
myList.extend([77, 88, 77])
print("after extend([77, 88, 77]) :", myList)
print("counting 77 :", myList)
