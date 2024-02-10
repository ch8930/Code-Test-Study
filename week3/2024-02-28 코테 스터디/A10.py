import numpy as np
import copy

def new_key(key,k):
    r = 0
    change = [[0]*k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            change[i][k-j-1] = key[j][i]       
    return change        

def check(tmp, k, l):
    for i in range(k,k+l):
        for j in range(k,k+l):
            if tmp[i][j] != 1:
                return False
    return True        

def solution(key, lock):
    
    if 0 not in np.array(lock):
        return True
    
    k = len(key)
    l = len(lock)
    new = 2*(k-1)+l
    search = [[0]*new for _ in range(new)]
    s = len(search)
    
    for i in range(l):
        for j in range(l):
            search[k-1+i][k-1+j] = lock[i][j]
    for i in search:
        for j in i:
            print(j, end =' ')
        print()    
    # 탐색
    for i in range(0, k+l-1):
        for j in range(0, k+l-1):
            # 회전해보면서 검사
            for _ in range(4):
                tmp = copy.deepcopy(search)
                # 회전된 키 할당
                key = new_key(key,k)                        
                for x in range(k):
                    for y in range(k):
                        tmp[i+x][j+y] += key[x][y]
                print(tmp)
                
                if check(tmp,k,l) == True:
                    return True
                    
    return False

key=[[0,0,0],[0,0,0],[0,0,0]]
lock=[[1,1,0],[1,1,1],[1,1,1]]

a = solution(key, lock)
print(a)        