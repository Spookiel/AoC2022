


test = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


data = """Sensor at x=3291456, y=3143280: closest beacon is at x=3008934, y=2768339
Sensor at x=3807352, y=3409566: closest beacon is at x=3730410, y=3774311
Sensor at x=1953670, y=1674873: closest beacon is at x=2528182, y=2000000
Sensor at x=2820269, y=2810878: closest beacon is at x=2796608, y=2942369
Sensor at x=3773264, y=3992829: closest beacon is at x=3730410, y=3774311
Sensor at x=2913793, y=2629579: closest beacon is at x=3008934, y=2768339
Sensor at x=1224826, y=2484735: closest beacon is at x=2528182, y=2000000
Sensor at x=1866102, y=3047750: closest beacon is at x=1809319, y=3712572
Sensor at x=3123635, y=118421: closest beacon is at x=1453587, y=-207584
Sensor at x=2530789, y=2254773: closest beacon is at x=2528182, y=2000000
Sensor at x=230755, y=3415342: closest beacon is at x=1809319, y=3712572
Sensor at x=846048, y=51145: closest beacon is at x=1453587, y=-207584
Sensor at x=3505756, y=3999126: closest beacon is at x=3730410, y=3774311
Sensor at x=2506301, y=3745758: closest beacon is at x=1809319, y=3712572
Sensor at x=1389843, y=957209: closest beacon is at x=1453587, y=-207584
Sensor at x=3226352, y=3670258: closest beacon is at x=3730410, y=3774311
Sensor at x=3902053, y=3680654: closest beacon is at x=3730410, y=3774311
Sensor at x=2573020, y=3217129: closest beacon is at x=2796608, y=2942369
Sensor at x=3976945, y=3871511: closest beacon is at x=3730410, y=3774311
Sensor at x=107050, y=209321: closest beacon is at x=1453587, y=-207584
Sensor at x=3931251, y=1787536: closest beacon is at x=2528182, y=2000000
Sensor at x=1637093, y=3976664: closest beacon is at x=1809319, y=3712572
Sensor at x=2881987, y=1923522: closest beacon is at x=2528182, y=2000000
Sensor at x=3059723, y=2540501: closest beacon is at x=3008934, y=2768339"""

import time
import re

pat = r"-?\d+"


def check_point(x, y, scanners):
    ### Returns if x,y is in range of any of the scanners
    for ind, (a, b, c, d) in enumerate(scanners):

        # print("DIST FROM THIS POINT TO SENSOR", dist(a,b,x,y), di)

        if dist(a,b,c,d) >= dist(a, b, x, y):
            return True
    return False


def dist(a,b,c,d):
    return abs(a-c)+abs(b-d)

def in_reg(man):

    return 2*(man*(man+1))




def solve(data):
    lines = [list(map(int, re.findall(pat, line))) for line in data.splitlines()]

    ans = 0
    dists = []
    for (a,b,c,d) in lines:
        md = abs(a-c)+abs(b-d)
        dists.append(md)
        ans += in_reg(md-1)

    y = 2000000

    ans = 0
    s = time.time()
    for x in range(-4000000,40000000):
        #print(ind)
        f = False

        for ind, (a, b, c, d) in enumerate(lines):


            if dists[ind] >= dist(a,b, x, y):
                print("DIST FROM THIS POINT TO SENSOR", dist(a, b, x, y), di)

                f = True
                break
        if f:
            #print(x,y, "CAN")
            ans += 1

        if time.time()-s > 5:
            print(ans-1, x)
            s = time.time()
            #print(ans+1)
    print(ans-1, "DONE")


def check_single(x,y,dist, scanners):
    dist += 1


    #cases = [[x+dist, y, 1,1],[x+dist, y, 1,1],[x-dist, y, 1,1],[x-dist, y, 1,1]]

    checked = 0
    sx = x+dist
    sy = y
    while sx > x:

        if sx < 0 or sy < 0:
            break

        res = check_point(sx, sy, scanners)

        if not res:
            print("CHECKED", checked)
            return sx,sy

        sx -= 1
        sy -= 1
        checked += 1
    sx = x + dist
    sy = y
    while sx > x:

        if sx < 0 or sy > 4000000:
            break

        res = check_point(sx, sy, scanners)

        if not res:
            print("CHECKED", checked)
            return sx, sy

        sx -= 1
        sy += 1
        checked += 1


    sx = x-dist
    sy = y
    while sx < x:

        if sx > 4000000 or sy > 4000000:
            break

        res = check_point(sx, sy, scanners)

        if not res:
            print("CHECKED", checked)
            return sx, sy

        sx += 1
        sy += 1
        checked += 1

    sx = x-dist
    sy = y
    while sx < x:

        if sx > 4000000 or sy < 0:
            break
        res = check_point(sx, sy, scanners)

        if not res:
            print("CHECKED", checked)
            return sx, sy

        sx += 1
        sy -= 1
        checked += 1






def solve2(data):
    lines = [list(map(int, re.findall(pat, line))) for line in data.splitlines()]

    for (a,b,c,d) in lines:
        md = abs(a-c)+abs(b-d)
        found = check_single(a,b, md, lines)
        if found:
            x,y = found
            print(x*4000000+y)
            break


solve2(data)
#solve(data)