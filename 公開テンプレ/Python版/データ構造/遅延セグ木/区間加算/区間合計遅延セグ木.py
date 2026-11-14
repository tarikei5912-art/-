class AddSumLazySegmentTree:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("A","Lazy","N","n")
    def __init__(self,N:int,A=[],initial=0):
        """
        引数
        N 長さが2^Nの配列ができる
        A 配列の初期値
        initial 配列の不足分を埋めるやつ
        
        機能
        add(L,R,X) セグ木のLからRの間をXに加算
        get(N) セグ木のn番目の要素を取得する
        query(L,R) セグ木のLからRの合計を求める
        """
        self.N=N
        self.n=(1<<N)
        temp=self.n
        self.A=[initial]*(temp)+A+[initial]*(temp-len(A))
        A=self.A
        for n in range(temp-1,0,-1):
            A[n]=A[2*n]+A[2*n+1]
        self.Lazy=[0]*(temp*2)

    def add(self,l:int,r:int,X):
        """
        add(L,R,X) セグ木のLからRの間にXを加算
        """
        self.ADD(l,r,X,1,0,self.n-1)

    def ADD(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        """
        M=(L+R+1)//2
        if L==l and R==r:
            self.A[np]+=X*(R-L+1)
            self.Lazy[np]+=X
            return
        if M<=l:#右側にあるなら
            self.A[np]+=X*(r-l+1)
            self.ADD(self,l,r,X,2*np+1,M,R)
            return
        if r<=M-1:#左側にあるなら
            self.A[np]+=X*(r-l+1)
            self.ADD(self,l,r,X,2*np,L,M-1)
            return
        self.A[np]+=X*(r-l+1)
        self.LADD(self,l,M-1,X,2*np,L,M-1)
        self.RADD(self,M,r,X,2*np+1,M,R)

    def LADD(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        R==rの時に使用する
        """
        if L==l and R==r:
            self.A[np]+=X*(R-L+1)
            self.Lazy[np]+=X
            return
        M=(L+R+1)//2
        if M<=l:#右部分木に収まるなら
            self.A[np]+=X*(r-l+1)
            self.LADD(l,r,X,2*np+1,M,R)
        else:
            self.A[np]+=X*(r-l+1)
            self.Lazy[2*np+1]+=X
            self.A[2*np+1]+=X*(R-M+1)
            self.LADD(l,M-1,X,2*np,L,M-1)


    def RADD(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        L==lの時に使用する
        """
        if L==l and R==r:
            self.A[np]+=X*(R-L+1)
            self.Lazy[np]+=X
            return
        M=(L+R+1)//2
        if r<=M-1:#左部分木に収まるなら
            self.A[np]+=X*(r-l+1)
            self.RADD(l,r,X,2*np,L,M-1)
        else:
            self.A[np]+=X*(r-l+1)
            self.Lazy[2*np]+=X
            self.A[2*np]+=X*(M-L)
            self.RADD(M,r,X,2*np+1,M,R)

    def get(self,n:int):
        """
        get(N) セグ木のn番目の要素を取得する
        """
        np=n+self.n
        ans=self.A[np]
        np//=2
        Lazy=self.Lazy
        for _ in range(self.N):
            ans+=Lazy[np]
            np//=2
        return ans

    def query(self,L:int,R:int):
        """
        query(L,R) セグ木のLからRの合計を求める
        """
        return self.QUERY(L,R,1,0,self.n-1)

    def QUERY(self,l,r,np,L,R):
        """
        この関数は普通外部から実行しない
        """
        M=(L+R+1)//2
        if l==L and r==R:
            return self.A[np]
        ln=np*2
        rn=ln+1

        A=self.A
        Lazy=self.Lazy
        temp=Lazy[np]
        if temp!=0:
            count=M-L
            A[ln]+=temp*count
            A[rn]+=temp*count
            Lazy[ln]+=temp
            Lazy[rn]+=temp
            Lazy[np]=0
        if r<=M-1:#左の木にいるなら
            return self.QUERY(l,r,ln,L,M-1)
        if M<=l:#右の木にいるなら
            return self.QUERY(l,r,rn,M,R)
        return self.QUERY(l,M-1,ln,L,M-1)+self.QUERY(M,r,rn,M,R)
                


