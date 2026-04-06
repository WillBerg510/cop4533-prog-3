def highest_value_lcs(values, a, b):
    OPT = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                OPT[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                OPT[i][j] = OPT[i - 1][j - 1] + values[a[i - 1]]
            else:
                OPT[i][j] = max(OPT[i - 1][j], OPT[i][j - 1])
    return OPT[len(a)][len(b)]


if __name__ == "__main__":
    file_name = input("Input file name without extension: ")

    with open(f"../data/{file_name}.in", "r") as file:
        k = int(file.readline())
        alphabet = {}

        for i in range(0, k):
            line = file.readline()
            line = line.split(" ")
            alphabet[line[0]] = int(line[1])

        A = file.readline().strip()
        B = file.readline().strip()

        print(highest_value_lcs(alphabet, A, B))
