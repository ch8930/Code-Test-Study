# Q2 - 곱하기 혹은 더하기

def check_zero(result, a):
    if result == 0 or a == 0 :
        return result+a
    else :
        return result*a
    
s = input()

result = int(s[0])

for i in s[1:]:
    result = check_zero(result, int(i))
    
print(result)    