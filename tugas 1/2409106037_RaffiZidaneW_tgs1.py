def pattern(n):
    print(f"{'*':<3}", end=" ")
    for i in range(1, n+1):
        print(f"{i:<3}", end=" ")
    print()

    for j in range(1, n+1):
        print()
        print(f"{j:<3}", end=" ")
        for k in range(1, n+1):
            kali = j * k
            print(f"{kali:<3}", end=" ")
        print()              

pattern(5)