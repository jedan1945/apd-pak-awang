def simbol(simbol, jmlh):
    for i in range(1, jmlh):
        print(simbol, end="")

def pattern(n):
    print(f"{'*':<3}", end=" ")
    for i in range(1, n+1):
        print(f"{i:<3}", end=" ")
    print()
    simbol("-", 30)
    
    for j in range(1, n+1):
        print()
        print(f"{j:<3}", end=" ")
        for k in range(1, n+1):
            kali = j*k
            print(f"{kali:<3}", end=" ")
        print()
        
        if j % 2 == 1:
            simbol("&", 20)
        elif j % 2 == 0:
            simbol("@", 20)             

pattern(5)