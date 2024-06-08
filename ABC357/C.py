def generate_carpet(N):
    if N == 0:
        return ["#"]

    prev_carpet = generate_carpet(N - 1)
    size = len(prev_carpet)
    new_carpet = []

    for i in range(3 * size):
        if size <= i < 2 * size:
            #こうすることで、リストの要素を繰り返すことができる。添え字を循環させることができる。
            new_carpet.append(prev_carpet[i % size] + "." * size + prev_carpet[i % size])
        else:
            new_carpet.append(prev_carpet[i % size] * 3)

    return new_carpet

N = int(input())
carpet = generate_carpet(N)
for line in carpet:
    print(line)




#########
#.##.##.#
#########
###...###
#.#...#.#
###...###
#########
#.##.##.#
#########
