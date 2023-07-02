import sys

def can_divide(mid):
    res = 0
    sum_so_far = [0] * (n+1)
    mn_so_far = [i for i in range(n+1)]
    
    for i in range(1, n+1):
        sum_so_far[i] += sum_so_far[i-1] + a[i-1] - mid
        
        if i >= k:
            mn_so_far[i] = min(mn_so_far[i], mn_so_far[i-k])
            if sum_so_far[i]-sum_so_far[mn_so_far[i]] >= 0:
                res |= True
            
        if res == True and i >= k:
            break
    
    return res

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    a = []
    
    while len(a) < n:
        a.extend(list(map(int, input().strip().split())))
        
#     print('Data read from stdin:', file=sys.stderr)
#     print("N: ", n)
#     print("K: ", k)
#     print("List of soldiers:", a)

    
    l ,r= min(a), max(a)+10**9