# Q7 - 럭키 스트라이크

n = input()

size = len(n)

left = right = 0

for x in range(0, size//2):
    left += int(n[x])
for y in range(size//2, size):
    right += int(n[y])  
    
print('LUCKY' if left == right else 'READY')