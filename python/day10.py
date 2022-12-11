

data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def solve(data):
    reg = 1
    cycles = 0

    ans = 0
    vals = []
    while cycles < 240:
        for i in data.splitlines():
            print(i, reg, cycles)
            vals.append(reg)
            if i == "noop":
                cycles += 1
                if (cycles + 20) % 40 == 0:
                    ans += cycles * reg
                    #print(cycles, reg, "HERE")
                    if cycles == 240:
                        vals.append(reg)
                        break
                continue
            #reg += int(i.split()[1])
            cycles += 1
            vals.append(reg)

            #print(cycles, reg)
            if (cycles+20)%40==0:
                ans += cycles*reg
                print(cycles, reg)
                if cycles == 240:
                    vals.append(reg)
                    break

            cycles += 1
            if (cycles+20)%40==0:
                ans += cycles*reg
                print(cycles, reg)
                if cycles == 240:
                    vals.append(reg)
                    break
            reg += int(i.split()[1])
    print(ans)
    print(vals)


    spos = 1
    grid = [["." for i in range(40)] for j in range(6)]
    print(len(vals))

    for pixel in range(240):
        spos = vals.pop(0)
        prow = pixel%40

        if spos-1 <= prow <= spos+1:
            grid[pixel//40][pixel%40] = "#"



    for i in grid:
        print(*i)







data = """addx 1
addx 4
addx 1
noop
noop
addx 4
addx 1
addx 4
noop
noop
addx 5
noop
noop
noop
addx -3
addx 9
addx -1
addx 5
addx -28
addx 29
addx 2
addx -28
addx -7
addx 10
noop
noop
noop
noop
noop
addx -2
addx 2
addx 25
addx -18
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 2
addx 3
noop
addx -15
addx 8
addx -28
noop
noop
noop
addx 7
addx -2
noop
addx 5
noop
noop
noop
addx 3
noop
addx 3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 3
addx -31
addx 37
addx -28
addx -9
noop
noop
noop
addx 37
addx -29
addx 4
noop
addx -2
noop
noop
noop
addx 7
noop
noop
noop
addx 5
noop
noop
noop
addx 4
addx 2
addx 4
addx 2
addx 3
addx -2
noop
noop
addx -34
addx 6
noop
noop
noop
addx -4
addx 9
noop
addx 5
noop
noop
addx -2
noop
addx 7
noop
addx 2
addx 15
addx -14
addx 5
addx 2
addx 2
addx -32
addx 33
addx -31
addx -2
noop
noop
addx 1
addx 3
addx 2
noop
addx 2
noop
addx 7
noop
addx 5
addx -6
addx 4
addx 5
addx 2
addx -14
addx 15
addx 2
noop
addx 3
addx 4
noop
addx 1
noop
noop"""
test = """noop
addx 3
addx -5"""
solve(data)