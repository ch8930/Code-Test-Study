# Q8 - 문자열 재정리

s = input()
n = len(s)
sum = 0
arr = []
'''for i in s:
    arr.append(ord(i))
arr.sort()
print(arr)
count = 0
for x in arr:
    if x >= 65:
        count += 1

sorted_char = ''
for x in arr[n-count:]:
    sorted_char += chr(x)
for x in arr[:n-count]:
    print(x)
    sum += int(x-48)
str_sum = f'{sum}'
print(sorted_char+str_sum)'''

for x in s:
    if x.isalpha():
        arr.append(x)
    else:
        sum += int(x)

arr.sort()

if sum != 0:
    arr.append(str(sum))
    
print(''.join(arr))    