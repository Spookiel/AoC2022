


test = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


data = """Monkey 0:
  Starting items: 54, 61, 97, 63, 74
  Operation: new = old * 7
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 1:
  Starting items: 61, 70, 97, 64, 99, 83, 52, 87
  Operation: new = old + 8
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 2:
  Starting items: 60, 67, 80, 65
  Operation: new = old * 13
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 3:
  Starting items: 61, 70, 76, 69, 82, 56
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 4:
  Starting items: 79, 98
  Operation: new = old + 2
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 72, 79, 55
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 6:
  Starting items: 63
  Operation: new = old + 4
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 7:
  Starting items: 72, 51, 93, 63, 80, 86, 81
  Operation: new = old * old
  Test: divisible by 11
    If true: throw to monkey 0
    If false: throw to monkey 4"""



import re
pat =  r"\d+"
mval = 1

import dataclasses

@dataclasses.dataclass
class Monkey:
    citems: [int]
    optype: str
    opval: int
    tval: int
    ift: int
    iff: int
    inspected: int  = 0


    def proc_op(self, val):
        if self.optype == "square":
            return val*val
        if self.optype == "*":
            return val*self.opval
        if self.optype == "+":
            return val + self.opval
        if self.optype == "-":
            return val - self.opval

    def test_item(self, val):
        return val%self.tval == 0

    def proc_turn(self):
        ### Return list of (ind, obj)
        #print(self.citems)
        ans = []
        while self.citems:
            ne = self.citems.pop(0)
            self.inspected += 1

            nval = self.proc_op(ne)
            #nval //= 3

            res = self.test_item(nval)

            if res:
                ans.append((self.ift, nval))
            else:
                ans.append((self.iff, nval))
        return ans

    def add_item(self, val):
        self.citems.append(val%mval)



from math import gcd

def solve(data):
    global mval

    oppat = r"[-+*/]"

    mlist = []

    monkeys = [[i for i in m.splitlines()] for m in data.split("\n\n")]

    lines = [[list(map(int, re.findall(pat, line))) for line in monk.splitlines()] for monk in data.split("\n\n")]



    for ind, monk in enumerate(monkeys):
        ### Need operation type
        cline = lines[ind]
        optype = re.findall(oppat, monk[2])
        digs = re.findall(r"-?\d+", monk[2])
        if not digs:
            optype = ["square"]
        #print(optype, lines[ind], cline)
        optype = optype[0]
        if optype == "square":
            mlist.append(Monkey(cline[1], optype, 0, cline[3][0], cline[4][0], cline[5][0]))
        else:
            mlist.append(Monkey(cline[1], optype, cline[2][0], cline[3][0], cline[4][0], cline[5][0]))

    mval =mlist[0].tval

    for i in range(1, len(mlist)):
        mval = (mlist[i].tval*mval) // gcd(mlist[i].tval, mval)
    print(mval)
    for round in range(10000):
        #print(round)
        for m in mlist:
            rlist = m.proc_turn()

            for (ind, obj) in rlist:
                mlist[ind].add_item(obj)



    a,b = sorted(mlist, key=lambda m: m.inspected, reverse=True)[:2]

    print(a.inspected, b.inspected)
    print(a.inspected*b.inspected)



solve(data)