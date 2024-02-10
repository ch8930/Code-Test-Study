# Q3 - 문자열 뒤집기
import sys

input = sys.stdin.readline()

s = input
check =[0]*2

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            check[0] += 1
        else:
            check[1] += 1
    else:
        continue    
    
print(min(check))