"""
動作確認はまだ
"""
class cycle_check:#有向グラフのサイクルチェック
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("MAP","N")
    def __init__(self,N):
        self.MAP=[]
        self.N=N
        for _ in range(N):
            self.MAP.append([])

    def add(self,i,j):#vからiへの有向辺を追加
        self.MAP[i].append(j)

    def cycle_C(self,start:list):#startの集合の任意の頂点から辿り着けるサイクルが存在するか
        """
        startのリストを与えるとそのスタートの集合の任意の頂点から辿り着けるサイクルが存在するかを判定する
        """
        DMAP=[0]*self.N#0未探索,1探索中,2探索終了
        P=[0]*self.N
        for s in start:
            if DMAP[s]==0:
                D=[s]
                while True:
                    if len(self.MAP[D[-1]])==P[D[-1]]:
                        DMAP[D.pop()]=2
                        if len(D)==0:
                            break
                    else:
                        if DMAP[self.MAP[P[D[-1]]]]==0:#未探索なら
                            D.append(self.MAP[P[D[-1]]])
                            P[D[-2]]+=1
                            DMAP[self.MAP[P[D[-1]]]]=1
                        elif DMAP[self.MAP[P[D[-1]]]]==1:#探索中なら
                            return True
                        else:
                            P[D[-1]]+=1
        return False

    def return_cycle(self,start:list):
        """
        startのリストを与えるとそのスタートの集合の任意の頂点から辿り着けるサイクルを一つ返す
        """
        DMAP=[0]*self.N#0未探索,1探索中,2探索終了
        P=[0]*self.N
        for s in start:
            if DMAP[s]==0:
                D=[s]
                while True:
                    if len(self.MAP[D[-1]])==P[D[-1]]:
                        DMAP[D.pop()]=2
                        if len(D)==0:
                            break
                    else:
                        if DMAP[self.MAP[P[D[-1]]]]==0:#未探索なら
                            D.append(self.MAP[P[D[-1]]])
                            P[D[-2]]+=1
                            DMAP[self.MAP[P[D[-1]]]]=1
                        elif DMAP[self.MAP[P[D[-1]]]]==1:#探索中なら
                            RANS=[self.MAP[P[D[-1]]]]
                            while True:
                                if D[-1]==RANS[0]:
                                    return RANS.reverse()
                                else:
                                    RANS.append(D.pop())

                        else:
                            P[D[-1]]+=1
        return None
    
                            

                    
