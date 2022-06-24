rows = input("行数を入力してください:")
digits = input("桁数を入力してください:")

for A in range(1, int(rows)+1):
    for B in range(1, int(digits)+1):
        print(A * B, end=" ")
    print()
