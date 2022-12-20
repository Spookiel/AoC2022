

test = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

data = """Valve SY has flow rate=0; tunnels lead to valves GW, LW
Valve TS has flow rate=0; tunnels lead to valves CC, OP
Valve LU has flow rate=0; tunnels lead to valves PS, XJ
Valve ND has flow rate=0; tunnels lead to valves EN, TL
Valve PD has flow rate=0; tunnels lead to valves TL, LI
Valve VF has flow rate=0; tunnels lead to valves LW, RX
Valve LD has flow rate=0; tunnels lead to valves AD, LP
Valve DG has flow rate=0; tunnels lead to valves DR, SS
Valve IG has flow rate=8; tunnels lead to valves AN, YA, GA
Valve LK has flow rate=0; tunnels lead to valves HQ, LW
Valve TD has flow rate=14; tunnels lead to valves BG, CQ
Valve CQ has flow rate=0; tunnels lead to valves TD, HD
Valve AZ has flow rate=0; tunnels lead to valves AD, XW
Valve ZU has flow rate=0; tunnels lead to valves TL, AN
Valve HD has flow rate=0; tunnels lead to valves BP, CQ
Valve FX has flow rate=0; tunnels lead to valves LW, XM
Valve CU has flow rate=18; tunnels lead to valves BX, VA, RX, DF
Valve SS has flow rate=17; tunnels lead to valves DG, ZD, ZG
Valve BP has flow rate=19; tunnels lead to valves HD, ZD
Valve DZ has flow rate=0; tunnels lead to valves XS, CC
Valve PS has flow rate=0; tunnels lead to valves GH, LU
Valve TA has flow rate=0; tunnels lead to valves LI, AA
Valve BG has flow rate=0; tunnels lead to valves TD, ZG
Valve WP has flow rate=0; tunnels lead to valves OB, AA
Valve XS has flow rate=9; tunnels lead to valves EN, DZ
Valve AA has flow rate=0; tunnels lead to valves WG, GA, VO, WP, TA
Valve LW has flow rate=25; tunnels lead to valves LK, FX, SY, VF
Valve AD has flow rate=23; tunnels lead to valves DF, GW, AZ, LD, FM
Valve EN has flow rate=0; tunnels lead to valves ND, XS
Valve ZG has flow rate=0; tunnels lead to valves SS, BG
Valve LI has flow rate=11; tunnels lead to valves YA, XM, TA, PD
Valve VO has flow rate=0; tunnels lead to valves AA, OD
Valve AN has flow rate=0; tunnels lead to valves IG, ZU
Valve GH has flow rate=15; tunnels lead to valves VA, PS
Valve OP has flow rate=4; tunnels lead to valves AJ, TS, FM, BX, NM
Valve BX has flow rate=0; tunnels lead to valves OP, CU
Valve RX has flow rate=0; tunnels lead to valves CU, VF
Valve FM has flow rate=0; tunnels lead to valves OP, AD
Valve OB has flow rate=0; tunnels lead to valves WP, XW
Valve CC has flow rate=3; tunnels lead to valves QS, LP, DZ, OD, TS
Valve LP has flow rate=0; tunnels lead to valves LD, CC
Valve NM has flow rate=0; tunnels lead to valves WH, OP
Valve HQ has flow rate=0; tunnels lead to valves XW, LK
Valve GW has flow rate=0; tunnels lead to valves SY, AD
Valve QS has flow rate=0; tunnels lead to valves CC, XW
Valve DF has flow rate=0; tunnels lead to valves AD, CU
Valve XM has flow rate=0; tunnels lead to valves LI, FX
Valve VA has flow rate=0; tunnels lead to valves CU, GH
Valve GA has flow rate=0; tunnels lead to valves IG, AA
Valve YA has flow rate=0; tunnels lead to valves LI, IG
Valve XW has flow rate=20; tunnels lead to valves OB, HQ, QS, WH, AZ
Valve XJ has flow rate=24; tunnel leads to valve LU
Valve AJ has flow rate=0; tunnels lead to valves WG, OP
Valve WH has flow rate=0; tunnels lead to valves XW, NM
Valve TL has flow rate=13; tunnels lead to valves PD, DR, ZU, ND
Valve OD has flow rate=0; tunnels lead to valves CC, VO
Valve ZD has flow rate=0; tunnels lead to valves SS, BP
Valve DR has flow rate=0; tunnels lead to valves DG, TL
Valve WG has flow rate=0; tunnels lead to valves AJ, AA"""


import re
import heapq as hp
from collections import defaultdict

flows = []
graph = []
df = defaultdict(int)
def score(state):
    global flows, graph, df

    ### Calculate expected score
    #print(state, "HERE")
    exp = 0
    for l in graph:
        if l[0] not in state[3]:
            #print("FOUND", l[0], df[l[0]])
            exp += 1.5*(30-state[1])*df[l[0]]
    return -(exp+state[0]*3)

def add(state):
    return (score(state), state[0], state[1], state[2], state[3])
from functools import lru_cache
def solve(data):
    global flows, graph,df
    lines = [i for i in data.splitlines()]

    d = defaultdict(list)
    df = defaultdict(int)

    pat = r"[A-Z][A-Z]"
    pat2 = r"\d+"

    flows = [int(re.findall(pat2, line)[0]) for line in lines]
    graph = [re.findall(pat, line) for line in lines]
    names = [line[0] for line in graph]
    dists = defaultdict(lambda: 9999999)

    for ind, l in enumerate(graph):
        a = l[0]
        df[a] = flows[ind]
        dists[(a,a)] = 0
        for edge in l[1:]:
            d[a].append(edge)
            d[edge].append(a)
            dists[(a, edge)] = 1
            dists[(edge, a)] = 1



    poi = [i for i in names if df[i] > 0]
    ### Run floyd on these


    for k in range(len(names)):
        for i in range(len(names)):
            for j in range(len(names)):
                if dists[(names[i], names[j])] > dists[(names[i], names[k])]+dists[(names[k], names[j])]:
                    dists[(names[i], names[j])] =  dists[(names[i], names[k])]+dists[(names[k], names[j])]

    print(poi)

    print(dists[("IG", "OP")])

    def gi(name):
        return poi.index(name)
    #@lru_cache(maxsize=None)
    def rec(cn, mask, tleft):
        if tleft < 0:
            return 0

        #print(cn, mask, tleft)
        #input()
        best = 0

        if cn in poi and not mask[gi(cn)]:
            ### Can open this node
            val = (tleft-1)*df[cn]
            #print("CAN TURN ON", cn, "FOR SCORE", val, tleft, df[cn])
            nmask = list(mask)
            nmask[gi(cn)] = 1
            val += rec(cn, tuple(nmask), tleft-1)
            best = max(best, val)

        for adj in poi:
            #aind = gi(adj)
            if adj != cn:
                best = max(best, rec(adj, mask, tleft-dists[(cn, adj)]))

        return best

    @lru_cache(maxsize=None)
    def rec2(cn, mask, tleft, e=False):
        #print(cn, mask, tleft)
        if tleft < 0:
            if e:
                return 0
            else:
                #print("STARTING ELEPHANT")
                return rec2("AA", mask, 26, True)

        #print(cn, mask, tleft)
        #input()
        best = 0

        if cn in poi and not mask[gi(cn)]:
            ### Can open this node
            val = (tleft-1)*df[cn]
            #print("CAN TURN ON", cn, "FOR SCORE", val, tleft, df[cn])
            nmask = list(mask)
            nmask[gi(cn)] = 1
            val += rec2(cn, tuple(nmask), tleft-1, e)
            best = max(best, val)

        for adj in poi:
            #aind = gi(adj)
            if adj != cn:
                best = max(best, rec2(adj, mask, tleft-dists[(cn, adj)], e))

        return best



    #print(rec("AA", tuple([0]*len(poi)), 30))
    print(rec2("AA", tuple([0] * len(poi)), 26))






    ### Precompute distances with flow > 0
    ### Do DP on these?
    ###






solve(data)
