# Q10 - 자물쇠와 열쇠
# 00 01 02 -> 20 10 00
# 10 11 12 -> 21 11 01
# key 반시계방향 90도 회전
def rotate_key(key):
    size = len(key)
    new_key = [[0]*size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            new_key[size - 1 - y][x] = key[x][y]
    return new_key        
            
            
    
    
def right_key(key, lock):    
    sk = len(key)
    sl = len(lock)
    
    for x in range(sl):
        for y in range(sl):
            