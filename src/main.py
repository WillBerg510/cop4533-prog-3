import time

def find_solution_sequence(m, a, b, i, j):
    if i == 0 or j == 0:
        return ""

    # if the characters at this location match, add to sequence and go back 1 character for both strings
    if a[i-1] == b[j-1]:
        return find_solution_sequence(m, a, b, i-1, j-1) + a[i-1]
    # if the characters don't match, go backwards 1 character on each string and check the OPT with the higher value
    elif m[i-1][j] > m[i][j-1]:
        return find_solution_sequence(m, a, b, i-1, j)
    else:
        return find_solution_sequence(m, a, b, i, j-1)


def highest_value_lcs(values, a, b):
    # initialize empty 2d array
    OPT = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

    # recursion to find optimal solution through tabulation
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            # if there are matching characters, add value of that character to OPT
            if a[i - 1] == b[j - 1]:
                OPT[i][j] = OPT[i - 1][j - 1] + values[a[i - 1]]
            # otherwise move forward 1 character on each string and choose the OPT with the greater value
            else:
                OPT[i][j] = max(OPT[i - 1][j], OPT[i][j - 1])

    # find solution
    seq = find_solution_sequence(OPT, a, b, len(a), len(b))

    return [seq, str(OPT[len(a)][len(b)])]


if __name__ == "__main__":
    file_name = input("Input file name without extension: ")

    # start recording runtime
    start_time = time.perf_counter()

    # read file
    with open(f"../data/input/{file_name}.in", "r") as file:
        k = int(file.readline())
        alphabet = {}

        # go through k lines and put value of each letter into a dictionary
        for i in range(0, k):
            line = file.readline()
            line = line.split(" ")
            alphabet[line[0]] = int(line[1])

        # read strings A and B and remove any whitespace
        A = file.readline().strip()
        B = file.readline().strip()

        # compute solution
        output = highest_value_lcs(alphabet, A, B)

        # write solution to output file
        with open(f"../data/output/{file_name}.out", "w") as output_file:
            output_file.write(f"{output[0]}\n")
            output_file.write(output[1])

            print(f"Output file data/{file_name}.out created.")

            end_time = time.perf_counter()
            print(f"Runtime: {(end_time - start_time) * 1000:.3f} ms.")


