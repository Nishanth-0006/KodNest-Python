# lists == Lists are mutable , ordered , and allow duplictaes values and can be accesed using index, []
nums = [1,2,3,4,2]
print(nums)
print(type(nums))
print(nums[2])
# 
names2 = ["nishanth", "nishath2", "nishath3"]
names2[1] = "yashwanth"
print(names2)
# 

# Lists Methods
names = ["nesha" , "nishanth", "vihani"]
names.append("liki")
print(names)
names.insert(2, "yashwanth")
print(names)
names.pop()
print(names)
names.remove("nishanth")
print(names)
names.clear()
del names

# Lists constructors list()
nums = list((1,2,3,4,5,6,7,8))
print(nums)
print(type(nums))


n1 = ["dhanush", "chetan"]
n2 = ["Naresh", "nishanth"]
# list1 = n1.extend(n2)
# print(list1)
print(n1.extend(n2))
print(n1)

n = [ 2,1,4,8,3]
print(n)
n.sort()
print(n)
n.reverse()
print(n)


colors = ["red", "green", "yellow", "purple"]
colors[1:2] = ["black", "white"]
print(colors)