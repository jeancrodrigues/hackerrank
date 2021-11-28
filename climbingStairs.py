def climbing_stairs(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 2
        
    climbing = [ 0 for i in range(n)]
    climbing[0] = 1
    climbing[1] = 2

    for i in range(2,n):
        climbing[i] = climbing[i-1] + climbing[i-2]
        
    return climbing[n-1]

if __name__ == "__main__":
    print(climbing_stairs(2))#2
    print(climbing_stairs(3))#3
    print(climbing_stairs(4))#5
    print(climbing_stairs(26)) # 196418