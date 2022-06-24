rows = input("行数を入力してください:")
digits = input("桁数を入力してください:")

for A in range(1, int(rows) + 1):
    for B in range(1, int(digits) + 1):
        if len(str(A * B)) < 2:
            print(A, "x", B, "=", " ", A * B, "|", end="")  # 半角スペースにならない
        else:
            print(A, "x", B, "=", A * B, "|", end="")
    print()
