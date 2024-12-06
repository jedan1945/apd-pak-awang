def pattern(n):
    print(f"{'*':<3}", end=" ")
    for i in range(n, 0, -1):
        print(f"{i:<3}", end=" ")
    print()

    for j in range(n, 0, -1):
        print()
        print(f"{j:<3}", end=" ")
        for k in range(n, 0, -1):
            kali = j * k
            print(f"{kali:<3}", end=" ")
        print()              

pattern(5)