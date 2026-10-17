class Update_Max_LazySegmentTree:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("A","N","N2","Lazy","L","R","X")
    def __init__(self,N:int,A:list=[],a=0):
        """
        引数
        N セグ木の配列の大きさは2**N
        A 配列の初期値 与えない場合は空の配列となる
        a 配列の長さが足りていない場合の埋めるやつ 指定なしの場合は-inf埋めされる
        機能
        get(n) セグ木のn番目の値を参照する
        update(L,R,x) セグ木の閉区間[L,R]の要素の数をxに変更する
        query(L,R) 閉区間[L,R]の最大値を返す
        """
        self.N=N
        self.N2=1<<N
        self.A=[a]*(self.N2*2)
        self.Lazy=[None]*(self.N2*2)
        self.A[self.N2:self.N2+len(A)]=A
        A=self.A
        for n in range(self.N2-1,0,-1):
            A[n]=max(A[n*2],A[n*2+1])
        self.L=list(range(-self.N2,self.N2))
        self.R=list(range(-self.N2,self.N2))
        L=self.L
        R=self.R
        for n in range(self.N2-1,0,-1):
            L[n]=min(L[2*n],L[2*n+1])
            R[n]=max(R[2*n],R[2*n+1])
            

    def get(self,n:int):
        """
        get(n) セグ木のn番目の値を参照する
        """
        n+=self.N2
        ANS=self.A[n]
        Lazy=self.Lazy
        while n>0:
            if Lazy[n] is not None:
                ANS=Lazy[n]
            n//=2
        return ANS

    def update(self,l:int,r:int,x):
        """
        update(l,r,x) セグ木の閉区間[L,R]の要素の数をxに変更する
        """
        self.UPDATE(1,l,r,x)

    def UPDATE(self,np:int,l:int,r:int,x):
        """
        この関数は基本外側から実行しない
        """
        Lazy=self.Lazy
        A=self.A
        L=self.L
        R=self.R
        #実装途中
        


    def query(self,l:int,r:int):
        """
        query(l,r) 閉区間[l,r]の最大値を返す
        """
        return self.QUERY(1,l,r)

    def QUERY(self,np,l:int,r:int):
        """
        この関数は基本外部から実行しない
        """
        L=self.L
        R=self.R
        Lazy=self.Lazy
        A=self.A
        #実装途中


            


        


    
        

    
