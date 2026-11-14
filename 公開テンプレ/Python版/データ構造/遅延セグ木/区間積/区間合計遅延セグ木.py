class TimeSumLazySegmentTree:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("A","Lazy","N","n","mod")
    def __init__(self,N:int,A=[],initial=1,mod:int=10**9+7):
        """
        引数
        N 長さが2^Nの配列ができる
        A 配列の初期値
        initial 配列の不足分を埋めるやつ
        mod 法
        
        機能
        time(L,R,X) セグ木のLからRの間にXをかける
        get(N) セグ木のn番目の要素を取得する
        query(L,R) セグ木のLからRの合計を求める
        """
        self.N=N
        self.n=(1<<N)
        temp=self.n
        self.mod=mod
        self.A=[initial]*(temp)+A+[initial]*(temp-len(A))
        A=self.A
        for n in range(temp-1,0,-1):
            A[n]=(A[2*n]+A[2*n+1])%mod
        self.Lazy=[1]*(temp*2)

    def time(self,l,r,X):
        """
        time(L,R,X) LからRの間にXをかける
        """
        self.TIME(l,r,X,1,0,self.n-1)



    def TIME(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        """
        M=(L+R+1)//2
        Lazy=self.Lazy
        A=self.A
        mod=self.mod
        if L==l and R==r:
            A[np]*=X
            A[np]%=mod
            Lazy[np]*=X
            Lazy[np]%=mod
            return
        if Lazy[np]!=1:
            Lazy[2*np]=(Lazy[2*np]*Lazy[np])%mod
            Lazy[2*np+1]=(Lazy[2*np+1]*Lazy[np])%mod
            A[2*np]=(A[2*np]*Lazy[np])%mod
            A[2*np+1]=(A[2*np+1]*Lazy[np])%mod
            Lazy[np]=1
        if M<=l:#右側にあるなら
            self.TIME(l,r,X,2*np+1,M,R)
            A[np]=(A[2*np]+A[2*np+1])%mod
            return 
        if r<=M-1:#左側にあるなら
            self.TIME(l,r,X,2*np,L,M-1)
            A[np]=(A[2*np]+A[2*np+1])%mod
            return
        self.LTIME(l,M-1,X,2*np,L,M-1)
        self.RTIME(M,r,X,2*np+1,M,R)
        A[np]=(A[2*np]+A[2*np+1])%mod

    def LTIME(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        R==rの時に使用する
        """
        A=self.A
        Lazy=self.Lazy
        mod=self.mod
        if L==l and R==r:
            A[np]=(A[np]*X)%mod
            Lazy[np]=(Lazy[np]*X)%mod
            return
        if Lazy[np]!=1:
            Lazy[2*np]=(Lazy[2*np]*Lazy[np])%mod
            Lazy[2*np+1]=(Lazy[2*np+1]*Lazy[np])%mod
            A[2*np]=(A[2*np]*Lazy[np])%mod
            A[2*np+1]=(A[2*np+1]*Lazy[np])%mod
            Lazy[np]=1
        M=(L+R+1)//2
        if M<=l:#右部分木に収まるなら
            self.LTIME(l,r,X,2*np+1,M,R)
            A[np]=(A[2*np]+A[2*np+1])%mod
        else:
            A[2*np+1]=(A[2*np+1]*X)%mod
            Lazy[2*np+1]=(Lazy[2*np+1]*X)%mod
            self.LTIME(l,M-1,X,2*np,L,M-1)
            A[np]=(A[2*np]+A[2*np+1])%mod

    def RTIME(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        L==lの時に使用する
        """
        A=self.A
        Lazy=self.Lazy
        mod=self.mod
        if L==l and R==r:
            A[np]=(A[np]*X)%mod
            Lazy[np]=(Lazy[np]*X)%mod
            return
        if Lazy[np]!=1:
            Lazy[2*np]=(Lazy[2*np]*Lazy[np])%mod
            Lazy[2*np+1]=(Lazy[2*np+1]*Lazy[np])%mod
            A[2*np]=(A[2*np]*Lazy[np])%mod
            A[2*np+1]=(A[2*np+1]*Lazy[np])%mod
            Lazy[np]=1
        M=(L+R+1)//2
        if r<=M-1:#左部分木に収まるなら
            self.RTIME(l,r,X,2*np,L,M-1)
            A[np]=(A[2*np]+A[2*np+1])%mod
            return 
        else:
            Lazy[2*np]=(Lazy[2*np]*X)%mod
            A[2*np]=(A[2*np]*X)%mod
            self.RTIME(M,r,X,2*np+1,M,R)
            A[np]=(A[2*np]+A[2*np+1])%mod

    def get(self,n:int):
        np=n+self.n
        ans=self.A[np]
        np//=2
        Lazy=self.Lazy
        for _ in range(self.N):
            ans=(ans*Lazy[np])%self.mod
            np//=2
        return ans

    def query(self,L,R):
        """
        query(L,R) LからRまでの合計を求める
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
        if r<=M-1:#左の木にいるなら
            return (temp*self.QUERY(l,r,ln,L,M-1))%self.mod
        if M<=l:#右の木にいるなら
            return (temp*self.QUERY(l,r,rn,M,R))%self.mod
        return (temp*(self.QUERY(l,M-1,ln,L,M-1)+self.QUERY(M,r,rn,M,R)))%self.mod