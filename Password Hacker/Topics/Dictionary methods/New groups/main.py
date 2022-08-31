# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
n = int(input())
stu_dict = {k: None for k in groups}
for i in range(n):
    stu_dict[groups[i]] = int(input())
print(stu_dict)