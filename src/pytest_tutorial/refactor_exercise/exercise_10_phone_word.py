# Courtesy of Phupha
# for
def phoneWord2Num(word):
    if word[0] is not None:
        if word[0] == 'A' or word[0] == 'B' or word[0] == 'C' or word[0] == 'a' or word[0] == 'b' or word[0] == 'c':
            x = '2'
        elif word[0] == 'D' or word[0] == 'E' or word[0] == 'F' or word[0] == 'd' or word[0] == 'e' or word[0] == 'f':
            x = '3'
        elif word[0] == 'G' or word[0] == 'H' or word[0] == 'I' or word[0] == 'g' or word[0] == 'h' or word[0] == 'i':
            x = '4'
        elif word[0] == 'J' or word[0] == 'K' or word[0] == 'L' or word[0] == 'j' or word[0] == 'k' or word[0] == 'l':
            x = '5'
        elif word[0] == 'M' or word[0] == 'N' or word[0] == 'O' or word[0] == 'm' or word[0] == 'n' or word[0] == 'o':
            x = '6'
        elif word[0] == 'P' or word[0] == 'Q' or word[0] == 'R' or word[0] == 'S' or word[0] == 'p' or word[0] == 'q' or \
                word[0] == 'r' or word[0] == 's':
            x = '7'
        elif word[0] == 'T' or word[0] == 'U' or word[0] == 'V' or word[0] == 't' or word[0] == 'u' or word[0] == 'v':
            x = '8'
        elif word[0] == 'W' or word[0] == 'X' or word[0] == 'Y' or word[0] == 'Z' or word[0] == 'w' or word[0] == 'x' or \
                word[0] == 'y' or word[0] == 'z':
            x = '9'
    if word[1] is not None:
        if word[1] == 'A' or word[1] == 'B' or word[1] == 'C' or word[1] == 'a' or word[1] == 'b' or word[1] == 'c':
            y = '2'
        elif word[1] == 'D' or word[1] == 'E' or word[1] == 'F' or word[1] == 'd' or word[1] == 'e' or word[1] == 'f':
            y = '3'
        elif word[1] == 'G' or word[1] == 'H' or word[1] == 'I' or word[1] == 'g' or word[1] == 'h' or word[1] == 'i':
            y = '4'
        elif word[1] == 'J' or word[1] == 'K' or word[1] == 'L' or word[1] == 'j' or word[1] == 'k' or word[1] == 'l':
            y = '5'
        elif word[1] == 'M' or word[1] == 'N' or word[1] == 'O' or word[1] == 'm' or word[1] == 'n' or word[1] == 'o':
            y = '6'
        elif word[1] == 'P' or word[1] == 'Q' or word[1] == 'R' or word[1] == 'S' or word[1] == 'p' or word[1] == 'q' or \
                word[1] == 'r' or word[1] == 's':
            y = '7'
        elif word[1] == 'T' or word[1] == 'U' or word[1] == 'V' or word[1] == 't' or word[1] == 'u' or word[1] == 'v':
            y = '8'
        elif word[1] == 'W' or word[1] == 'X' or word[1] == 'Y' or word[1] == 'Z' or word[1] == 'w' or word[1] == 'x' or \
                word[1] == 'y' or word[1] == 'z':
            y = '9'
    if word[2] is not None:
        if word[2] == 'A' or word[2] == 'B' or word[2] == 'C' or word[2] == 'a' or word[2] == 'b' or word[2] == 'c':
            z = '2'
        elif word[2] == 'D' or word[2] == 'E' or word[2] == 'F' or word[2] == 'd' or word[2] == 'e' or word[2] == 'f':
            z = '3'
        elif word[2] == 'G' or word[2] == 'H' or word[2] == 'I' or word[2] == 'g' or word[2] == 'h' or word[2] == 'i':
            z = '4'
        elif word[2] == 'J' or word[2] == 'K' or word[2] == 'L' or word[2] == 'j' or word[2] == 'k' or word[2] == 'l':
            z = '5'
        elif word[2] == 'M' or word[2] == 'N' or word[2] == 'O' or word[2] == 'm' or word[2] == 'n' or word[2] == 'o':
            z = '6'
        elif word[2] == 'P' or word[2] == 'Q' or word[2] == 'R' or word[2] == 'S' or word[2] == 'p' or word[2] == 'q' or \
                word[2] == 'r' or word[2] == 's':
            z = '7'
        elif word[2] == 'T' or word[2] == 'U' or word[3] == 'V' or word[2] == 't' or word[2] == 'u' or word[2] == 'v':
            z = '8'
        elif word[2] == 'W' or word[2] == 'X' or word[3] == 'Y' or word[2] == 'Z' or word[2] == 'w' or word[2] == 'x' or \
                word[2] == 'y' or word[2] == 'z':
            z = '9'
    if word[3] is not None:
        if word[3] == 'A' or word[3] == 'B' or word[3] == 'C' or word[3] == 'a' or word[3] == 'b' or word[3] == 'c':
            a = '2'
        elif word[3] == 'D' or word[3] == 'E' or word[3] == 'F' or word[3] == 'd' or word[3] == 'e' or word[3] == 'f':
            a = '3'
        elif word[3] == 'G' or word[3] == 'H' or word[3] == 'I' or word[3] == 'g' or word[3] == 'h' or word[3] == 'i':
            a = '4'
        elif word[3] == 'J' or word[3] == 'K' or word[3] == 'L' or word[3] == 'j' or word[3] == 'k' or word[3] == 'l':
            a = '5'
        elif word[3] == 'M' or word[3] == 'N' or word[3] == 'O' or word[3] == 'm' or word[3] == 'n' or word[3] == 'o':
            a = '6'
        elif word[3] == 'P' or word[3] == 'Q' or word[3] == 'R' or word[3] == 'S' or word[3] == 'p' or word[3] == 'q' or \
                word[3] == 'r' or word[3] == 's':
            a = '7'
        elif word[3] == 'T' or word[3] == 'U' or word[3] == 'V' or word[3] == 't' or word[3] == 'u' or word[3] == 'v':
            a = '8'
        elif word[3] == 'W' or word[3] == 'X' or word[3] == 'Y' or word[3] == 'Z' or word[3] == 'w' or word[3] == 'x' or \
                word[3] == 'y' or word[3] == 'z':
            a = '9'
    if word[4] is not None:
        if word[4] == 'A' or word[4] == 'B' or word[4] == 'C' or word[4] == 'a' or word[4] == 'b' or word[4] == 'c':
            f = '2'
        elif word[4] == 'D' or word[4] == 'E' or word[4] == 'F' or word[4] == 'd' or word[4] == 'e' or word[4] == 'f':
            f = '3'
        elif word[4] == 'G' or word[4] == 'H' or word[4] == 'I' or word[4] == 'g' or word[4] == 'h' or word[4] == 'i':
            f = '4'
        elif word[4] == 'J' or word[4] == 'K' or word[4] == 'L' or word[4] == 'j' or word[4] == 'k' or word[4] == 'l':
            f = '5'
        elif word[4] == 'M' or word[4] == 'N' or word[4] == 'O' or word[4] == 'm' or word[4] == 'n' or word[4] == 'o':
            f = '6'
        elif word[4] == 'P' or word[4] == 'Q' or word[4] == 'R' or word[4] == 'S' or word[4] == 'p' or word[4] == 'q' or \
                word[4] == 'r' or word[4] == 's':
            f = '7'
        elif word[4] == 'T' or word[4] == 'U' or word[4] == 'V' or word[4] == 't' or word[4] == 'u' or word[4] == 'v':
            f = '8'
        elif word[4] == 'W' or word[4] == 'X' or word[4] == 'Y' or word[4] == 'Z' or word[4] == 'w' or word[4] == 'x' or \
                word[4] == 'y' or word[4] == 'z':
            f = '9'
    if word[5] is not None:
        if word[5] == 'A' or word[5] == 'B' or word[5] == 'C' or word[5] == 'a' or word[5] == 'b' or word[5] == 'c':
            b = '2'
        elif word[5] == 'D' or word[5] == 'E' or word[5] == 'F' or word[5] == 'd' or word[5] == 'e' or word[5] == 'f':
            b = '3'
        elif word[5] == 'G' or word[5] == 'H' or word[5] == 'I' or word[5] == 'g' or word[5] == 'h' or word[5] == 'i':
            b = '4'
        elif word[5] == 'J' or word[5] == 'K' or word[5] == 'L' or word[5] == 'j' or word[5] == 'k' or word[5] == 'l':
            b = '5'
        elif word[5] == 'M' or word[5] == 'N' or word[5] == 'O' or word[5] == 'm' or word[5] == 'n' or word[5] == 'o':
            b = '6'
        elif word[5] == 'P' or word[5] == 'Q' or word[5] == 'R' or word[5] == 'S' or word[5] == 'p' or word[5] == 'q' or \
                word[5] == 'r' or word[5] == 's':
            b = '7'
        elif word[5] == 'T' or word[5] == 'U' or word[5] == 'V' or word[5] == 't' or word[5] == 'u' or word[5] == 'v':
            b = '8'
        elif word[5] == 'W' or word[5] == 'X' or word[5] == 'Y' or word[5] == 'Z' or word[5] == 'w' or word[5] == 'x' or \
                word[5] == 'y' or word[5] == 'z':
            b = '9'
    if word[6] is not None:
        if word[6] == 'A' or word[6] == 'B' or word[6] == 'C' or word[6] == 'a' or word[6] == 'b' or word[6] == 'c':
            l = '2'
        elif word[6] == 'D' or word[6] == 'E' or word[6] == 'F' or word[6] == 'd' or word[6] == 'e' or word[6] == 'f':
            l = '3'
        elif word[6] == 'G' or word[6] == 'H' or word[6] == 'I' or word[6] == 'g' or word[6] == 'h' or word[6] == 'i':
            l = '4'
        elif word[6] == 'J' or word[6] == 'K' or word[6] == 'L' or word[6] == 'j' or word[6] == 'k' or word[6] == 'l':
            l = '5'
        elif word[6] == 'M' or word[6] == 'N' or word[6] == 'O' or word[6] == 'm' or word[6] == 'n' or word[6] == 'o':
            l = '6'
        elif word[6] == 'P' or word[6] == 'Q' or word[6] == 'R' or word[6] == 'S' or word[6] == 'p' or word[6] == 'q' or \
                word[6] == 'r' or word[6] == 's':
            l = '7'
        elif word[6] == 'T' or word[6] == 'U' or word[6] == 'V' or word[6] == 't' or word[6] == 'u' or word[6] == 'v':
            l = '8'
        elif word[6] == 'W' or word[6] == 'X' or word[6] == 'Y' or word[6] == 'Z' or word[6] == 'w' or word[6] == 'x' or \
                word[6] == 'y' or word[6] == 'z':
            l = '9'
        return int(x + y + z + a + f + b + l)
