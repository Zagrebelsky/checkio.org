def safe_pawns(pawns):

pawns_indexes = {}
for p in pawns:
    print "p =", p
    row = int(p[1]) - 1
    print "row =", row
    col = ord(p[0]) - 97
    print "col =", col
    pawns_indexes[col] = row
    print pawns_indexes


for i in pawns_indexes:
    if i+1 in pawns_indexes and pawns_indexes[i] == pawns_indexes[i+1]-1 or pawns_indexes[i] == pawns_indexes[i+1]+1:
        print i



    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"b4", "d4", "f4", "c3", "e3", "g5", "d2"
1:3, 3:3,
pawns_indexes[i+1]+1
