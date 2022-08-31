n = int(input())
number_bytes = (n).to_bytes(2, 'little')
count = 0
for i in number_bytes:
    count += i
print(count)
