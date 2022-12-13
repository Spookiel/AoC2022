


test = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

data = """abccccccccaaaaaaaccaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccaaaaaa
abccccccccaaaaaaaccaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccaaaaaa
abccccccccccaaaaaaccaaaaaaaaaaaaaaaaccccccccccccccccacccccccccccccccccccaaaaa
abcccccaaaacaaaaaaccaaaaaaaaaaaaaaaaacccccccccccccccaaaccccaccccccccccccccaaa
abccccaaaaacaaccccccaaaaaacaaacaacaaaaaaacccccccccccaaaacccaacccccccccccccaaa
abaaccaaaaaaccccaaacaaaacacaaacaaccaaaaaacccccccccccaklaccccccccccccccccccaac
abaaccaaaaaaccaaaaaacccccccaaacccaaaaaaaccccccccccckkkllllccccccccccccccccccc
abaaccaaaaaaccaaaaaacccccccaaaaacaaaaaaacccccccccckkkklllllcccccccaaaccaccccc
abacccccaacccccaaaaacccccccaaaaaccaaaaaaacccccccckkkkpppllllccccccaaaaaaccccc
abacccccccccccaaaaacccccccccaaaacccaaaaaaccccccckkkkpppppplllccccddddaaaccccc
abccccccccccccaaaaaccccccccccaaaccaaaccccccccccckkkppppppppllllldddddddaccccc
abccacccccccccccccccccccccccccccccaaccccccccccckkkopppupppplllmmmmdddddaacccc
abccaaacaaaccccccccccccccccccccaaaaaaaaccccccckkkkopuuuuupppllmmmmmmddddacccc
abccaaaaaaaccccccccccccccccccccaaaaaaaacccccjjkkkooouuuuuuppqqqqqmmmmddddcccc
abccaaaaaacccccccccccccccaaccccccaaaacccccjjjjjjoooouuxuuuppqqqqqqmmmmdddcccc
abcaaaaaaaacccccccccccccaaacccccaaaaaccccjjjjoooooouuuxxuuvvvvvqqqqmmmdddcccc
abaaaaaaaaaacccccccaaaaaaacaacccaacaaacccjjjooooouuuuxxxxvvvvvvvqqqmmmdddcccc
abaaaaaaaaaacccaaacaaaaaaaaaacccacccaaccjjjooootttuuuxxxyyvyyvvvqqqmmmeeecccc
abcccaaacaaacccaaaaaaacaaaaaccccccccccccjjjooottttxxxxxxyyyyyyvvqqqmmmeeccccc
abcccaaacccccccaaaaaacaaaaaccccaaccaacccjjjnnntttxxxxxxxyyyyyvvvqqqnneeeccccc
SbccccaacccccccaaaaaaaaacaaacccaaaaaacccjjjnnntttxxxEzzzzyyyyvvqqqnnneeeccccc
abcccccccccccccaaaaaaaaacaaccccaaaaaccccjjjnnnttttxxxxyyyyyvvvrrrnnneeecccccc
abcccaacccccccaaaaaaaaaccccccccaaaaaacccciiinnnttttxxxyyyyywvvrrrnnneeecccccc
abcccaaaaaaccaaaaaaaacccccccccaaaaaaaaccciiiinnnttttxyyywyyywvrrrnnneeecccccc
abcccaaaaaaccaaaaaaaacccccccccaaaaaaaacccciiinnnntttxwywwyyywwwrrnnneeecccccc
abcaaaaaaaccaaaaaaaaaccccccccccccaacccccccciiinnnttwwwwwwwwwwwwrrnnneeecccccc
abcaaaaaaaccaaaaaacccccccccccccccaaccccccaaiiiinnttwwwwwwwwwwwrrrnnnffecccccc
abcccaaaaaaccaaaaaccccccccccccccccccccaaaaaciiinnssswwwssssrwwrrrnnnfffcccccc
abaacaaccaaccaaaccccccccaacccccccccccccaaaaaiiinnssssssssssrrrrrronnfffcccccc
abaccaaccaacccccccccaaacaacccccccccccccaaaaaiiimmmssssssmoosrrrrooonffaaacccc
abaaaccccaaaaaaccccccaaaaaccccccccccccaaaaaccihmmmmsssmmmoooooooooofffaaacccc
abaaaccccaaaaaacccccccaaaaaacccccccccccccaacchhhmmmmmmmmmoooooooooffffaaccccc
abaacccaaaaaaaccccccaaaaaaaaccccaaccccccccccchhhhmmmmmmmgggggooofffffaaaccccc
abaacccaaaaaaaccccccaaaaaaaccccaaaaccccccccccchhhhmmmmhggggggggfffffaaaaccccc
abccccccaaaaaaacccccaacaaaaacccaaaaccccccccccchhhhhhhhggggggggggfffaacaaccccc
abccaacccaaaaaaccccccccaaaaaccaaaaacccccccccccchhhhhhhggaaaaaaccccccccccccccc
abccaaaccaaccccccccccccccaaaaaaaaaccccccccccccccchhhhaaaccaaaacccccccccccccaa
abaaaaaaaccccccccccccccccaaaaaaaaccccccccccccccccccccaaaccccaaccccccccccccaaa
abaaaaaaaccccccccaaaccccacaaaaaacccccccccccccccccccccaaaccccccccccccccccccaaa
abaaaaaacccccccaaaaacaaaaaaaaaaacccccccccccccccccccccaaccccccccccccccccaaaaaa
abaaaaaacccccccaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccccccaaaaaa"""

from collections import defaultdict
from string import ascii_lowercase

def solve(data):
    print(ascii_lowercase)
    dlines = data.splitlines()
    lines = [[ascii_lowercase.index(j) if j in ascii_lowercase else j for j in i if j in ascii_lowercase] for i in data.splitlines()]

    spos = None
    epos =None

    lines = []
    for i in data.splitlines():
        l = []
        for j in i:
            try:
                l.append(ascii_lowercase.index(j))
            except:
                l.append(0)
        lines.append(l)



    for i in range(len(dlines)):
        for j in range(len(dlines[0])):
            if dlines[i][j] == "S":
                spos = j,i
            elif dlines[i][j] == "E":
                epos = j,i
    print(spos, epos)




    lines[epos[1]][epos[0]] = 25


    for l in lines:
        print(l, len(l))

    adj4 = [[0,1], [1,0], [-1,0], [0,-1]]


    best = defaultdict(lambda: 9999999)


    q = [(0, spos)]

    while q:
        dist, ne = q.pop(0)
        #print(dist, ne, ne==epos)
        x,y = ne

        if dist >= best[(x,y)]:
            continue



        #print("FOUND NODE", x, y, dist)
        for dx,dy in adj4:
            nx, ny = dx+x, dy+y

            if (nx, ny) not in [spos, epos]:

                if 0 <= ny < len(lines) and 0 <= nx < len(lines[ny]):
                    #print("CONSIDERING", nx, ny, lines[ny][nx], lines[y][x], ascii_lowercase[lines[ny][nx]])
                    if lines[ny][nx]-lines[y][x] <= 1:
                        if dist+1 < best[(nx, ny)]:

                            best[(nx,ny)] = dist+1
                            q.append((dist+1, (nx, ny)))
            else:
                if (nx, ny) == epos:
                    print("REACHED", epos, dist+1)
                    best[epos] = min(best[epos], dist+1)
                #print((nx, ny), dist+1)
    print(best[epos])


def solve2(data):
    print(ascii_lowercase)
    dlines = data.splitlines()
    lines = [[ascii_lowercase.index(j) if j in ascii_lowercase else j for j in i] for i in data.splitlines()]

    spos = None
    epos =None

    lines = []
    for i in data.splitlines():
        l = []
        for j in i:
            try:
                l.append(ascii_lowercase.index(j))
            except:
                l.append(0)
        lines.append(l)


    sposs = []
    for i in range(len(dlines)):
        for j in range(len(dlines[0])):
            if dlines[i][j] == "S":
                spos = j,i
            elif dlines[i][j] == "E":
                epos = j,i

            if lines[i][j] == 0 and dlines[i][j] != "E":
                sposs.append((0, (j, i)))
    print(spos, epos)




    lines[epos[1]][epos[0]] = 25


    for l in lines:
        print(l, len(l))

    adj4 = [[0,1], [1,0], [-1,0], [0,-1]]


    best = defaultdict(lambda: 9999999)


    q = sposs

    while q:
        dist, ne = q.pop(0)
        #print(dist, ne, ne==epos)
        x,y = ne

        if dist > best[(x,y)]:
            continue



        #print("FOUND NODE", x, y, dist)
        for dx,dy in adj4:
            nx, ny = dx+x, dy+y

            if (nx, ny) not in [spos, epos]:

                if 0 <= ny < len(lines) and 0 <= nx < len(lines[ny]):
                    #print("CONSIDERING", nx, ny, lines[ny][nx], lines[y][x], ascii_lowercase[lines[ny][nx]])
                    if lines[ny][nx]-lines[y][x] <= 1:
                        if dist+1 < best[(nx, ny)]:

                            best[(nx,ny)] = dist+1
                            q.append((dist+1, (nx, ny)))
            else:
                if (nx, ny) == epos:
                    print("REACHED", epos, dist+1)
                    best[epos] = min(best[epos], dist+1)
                #print((nx, ny), dist+1)
    print(best[epos])



solve2(data)