class SumFenwickTree:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("A","N","n")
    def __init__(self,N:int,A:list=[],a=0):
        """
        機能
        add(n,x) n番目にxを加算
        update(n,x) n番目をxに更新
        query(L,R) L番目からR番目の合計を出力 
        """
        self.N=N
        self.n=1<<N
        self.A=[0]*(self.n+1)
        
