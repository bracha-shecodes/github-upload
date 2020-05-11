from itertools import permutations
from itertools import  combinations


def main():

    with open('letters.dat', 'r', encoding='utf-8') as f:
        for letter in f:
            letters = letter.strip().split(',')
            print(letter)
        perm = permutations(letters, 5)
#        perm = combinations(letters, 5)
        with open('res.dat', 'w', encoding='utf-8', newline='') as o1:
            inx = 0
            for i in list(perm):
                inx += 1
                o1.write("%s\r\n" % conv_tup_to_str(i))
#                o1.write("\n\r")
#                o1.write(i)
            print(inx)


def conv_tup_to_str(tup):
    str1 = ','.join(tup)
    return str1


if __name__ == "__main__":
    main()

#','.join(str(x)
# q = []
# >>> for x in range(3):
#     q.append("%s")
# >>> "".join(q)