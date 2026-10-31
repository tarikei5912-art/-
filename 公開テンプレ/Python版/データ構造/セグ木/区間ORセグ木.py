class OrSegmentTree:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("A","N","N2")
    def __init__(self,N:int,A:list=[],a=0):
        """
        引数
        N セグ木の配列の大きさは2**N
        A 配列の初期値 与えない場合は空の配列となる
        a 配列の長さが足りていない場合の埋めるやつ 指定なしの場合は0埋めされる
        機能
        get(n) セグ木のn番目の値を参照する
        update(n,x) セグ木のn番目の要素の数をxに変更する
        add(n,x) セグ木のn番目の要素にxを足す
        time(n,x) セグ木のn番目の要素にxを掛ける
        bitwise_xor(n,x) セグ木のn番目の要素にxビット単位のxorをする
        bitwise_and(n,x) セグ木のn番目の要素にxビット単位のandをする
        bitwise_or(n,x) セグ木のn番目の要素にxビット単位のorをする
        query(L,R) 閉区間の総orを返す
        """
        self.N=N
        self.N2=1<<N
        self.A=[a]*(1<<(N+1))
        self.A[self.N2:self.N2+len(A)]=A
        A=self.A

        for n in range(self.N2-1,0,-1):
            A[n]=A[2*n]|A[2*n+1]

    def get(self,n:int):
        """
        get(n) セグ木のn番目の値を参照する
        """
        return self.A[self.N2+n]

    def update(self,n:int,x):
        """
        update(n,x) セグ木のn番目の要素の数をxに変更する
        """
        np=self.N2+n
        self.A[np]=x
        while np!=1:
            np//=2
            self.A[np]=self.A[np*2]|self.A[np*2+1]

    def add(self,n:int,x):
        """
        add(n,x) セグ木のn番目の要素にxを足す
        """
        temp=self.get(n)
        x+=temp
        np=self.N2+n
        self.A[np]=x
        while np!=1:
            np//=2
            self.A[np]=self.A[np*2]|self.A[np*2+1]

    def times(self,n:int,x):
        """
        times(n,x) セグ木のn番目の要素にxを掛ける
        """
        temp=self.get(n)
        x*=temp
        np=self.N2+n
        self.A[np]=x
        while np!=1:
            np//=2
            self.A[np]=self.A[np*2]|self.A[np*2+1]

    def bitwise_xor(self,n:int,x:int):
        """
        bitwise_xor(n,x) セグ木のn番目の要素にxビット単位のxorをする
        """
        temp=self.get(n)
        x^=temp
        np=self.N2+n
        self.A[np]=x
        while np!=1:
            np//=2
            self.A[np]=self.A[np*2]|self.A[np*2+1]

    def bitwise_and(self,n:int,x:int):
        """
        bitwise_xor(n,x) セグ木のn番目の要素にxビット単位のxorをする
        """
        temp=self.get(n)
        x&=temp
        np=self.N2+n
        self.A[np]=x
        while np!=1:
            np//=2
            self.A[np]=self.A[np*2]|self.A[np*2+1]

    def bitwise_or(self,n:int,x:int):
        """
        bitwise_or(n,x) セグ木のn番目の要素にxビット単位のxorをする
        """
        temp=self.get(n)
        x|=temp
        np=self.N2+n
        self.A[np]=x
        while np!=1:
            np//=2
            self.A[np]=self.A[np*2]|self.A[np*2+1]

    def query(self,L:int,R:int):
        """
        query(L,R) 閉区間[L,R]の総orを返す
        """
        A=self.A
        ANS=0
        L+=self.N2
        R+=self.N2
        while L<=R:
            if L&1:
                ANS|=A[L]
                L+=1
            if R&1==0:
                ANS|=A[R]
                R-=1
            L//=2
            R//=2
        return ANS
