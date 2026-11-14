import sys
sys.setrecursionlimit(10**6)
def cycle_check(MAP,starts):
    """
    隣接リスト表現のMAPとstartのリストを渡すとサイクルの有無を返す
    https://github.com/tarikei5912-art/-
    """
    DMAP=[0]*len(MAP)#0 未探索,1 探索中,2 探索済み
    ANS=False
    def solve(np):
        nonlocal ANS
        for to in MAP[np]:
            if DMAP[to]==1:
                ANS=True
                return
            elif DMAP[to]==0:
                DMAP[to]=1
                solve(to)
                if ANS:
                    return
        DMAP[np]=2
        return 
    for s in starts:
        if DMAP[s]==0:
            DMAP[s]=1
            solve(s)
    return ANS