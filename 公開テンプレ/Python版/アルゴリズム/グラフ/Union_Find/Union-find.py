class Union_Find:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("N","A","C")
    def __init__(self,N:int):
        """
        引数
        N 頂点の数
        機能
        find(v) 頂点vから辿れる一番上の頂点番号を返す
        union(v,u) 頂点vと頂点uを結合する 返り値は新たに結合したならTrue 元々結合していたならFalse
        count(v) 頂点vと連結している頂点の数
        """
        self.A=list(range(N))
        self.N=N
        self.C=[1]*N

    def find(self,v:int):
        """
        find(v) 頂点vから辿れる一番上の頂点番号を返す
        """
        A=self.A
        if A[v]==v:
            return v
        else:
            u=self.find(A[v])
            A[v]=u
            return u

    def union(self,v:int,u:int):
        """
        union(v,u) 頂点vと頂点uを結合する
        返り値
        新たに結合したならTrue
        元々結合していたならFalse
        """
        v=self.find(v)
        u=self.find(u)
        A=self.A
        C=self.C
        if v==u:
            return False
        else:
            if C[v]>C[u]:
                pass
            else:
                v,u=u,v
            A[u]=v
            C[v]+=C[u]
            C[u]=0
            return True

    def count(self,v:int):
        """
        count(v) 頂点vと連結している頂点の数
        """
        v=self.find(v)
        return self.C[v]