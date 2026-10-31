class UpdateSumLazySegmentTree:
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
        update(L,R,X) セグ木のLからRの間をXに更新
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
        self.Lazy=[None]*(temp*2)

    def update(self,l:int,r:int,X):
        """
        update(L,R,X) セグ木のLからRの間をXに更新
        """
        self.UPDATE(l,r,X,1,0,self.n-1)

    def UPDATE(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        """
        Lazy=self.Lazy
        A=self.A
        if (l==L and r==R):
            Lazy[np]=X
            A[np]=X*(R-L+1)
        else:
            ln=2*np
            rn=2*np+1
            if Lazy[np] is not None:
                temp=Lazy[np]
                Lazy[ln]=temp
                Lazy[rn]=temp
                Lazy[np]=None
                A[ln]=temp*((R-L+1)//2)
                A[rn]=temp*((R-L+1)//2)
            M=(L+R)//2#正確には左の子の右端
            if (l<=M):#左に触れている場合
                if (M+1<=r):#右にも触れている場合
                    self.LUPDATE(l,M,X,ln,L,M)
                    self.RUPDATE(M+1,r,X,rn,M+1,R)
                else:
                    self.UPDATE(l,r,X,ln,L,M)
            else:
                self.UPDATE(l,r,X,rn,M+1,R)
            A[np]=A[ln]+A[rn]

    def LUPDATE(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        R==rの時に使用する
        """
        Lazy=self.Lazy
        A=self.A
        if (l==L and r==R):
            Lazy[np]=X
            A[np]=X*(R-L+1)
        else:
            ln=2*np
            rn=2*np+1
            if Lazy[np] is not None:
                temp=Lazy[np]
                Lazy[ln]=temp
                Lazy[rn]=temp
                Lazy[np]=None
                A[ln]=temp*((R-L+1)//2)
                A[rn]=temp*((R-L+1)//2)
            M=(L+R)//2#正確には左の子の右端
            if (l<=M):#左に触れている場合
                self.LUPDATE(l,M,X,ln,L,M)
                Lazy[rn]=X
                A[rn]=X*((R-L+1)//2)
            else:
                self.LUPDATE(l,r,X,rn,M+1,R)
            A[np]=A[ln]+A[rn]

    def RUPDATE(self,l,r,X,np,L,R):
        """
        この関数は普通外部から使用しない
        L==lの時に使用する
        """
        Lazy=self.Lazy
        A=self.A
        if (l==L and r==R):
            Lazy[np]=X
            A[np]=X*(R-L+1)
        else:
            ln=2*np
            rn=2*np+1
            if Lazy[np] is not None:
                temp=Lazy[np]
                Lazy[ln]=temp
                Lazy[rn]=temp
                Lazy[np]=None
                A[ln]=temp*((R-L+1)//2)
                A[rn]=temp*((R-L+1)//2)
            M=(L+R)//2#正確には左の子の右端
            if (M+1<=r):#右に触れている場合
                self.RUPDATE(M+1,r,X,rn,M+1,R)
                Lazy[ln]=X
                A[ln]=X*((R-L+1)//2)
            else:
                self.RUPDATE(l,r,X,ln,L,M)
            A[np]=A[ln]+A[rn]

    def get(self,n:int):
        """
        get(N) セグ木のn番目の要素を取得する
        """
        return self.GET(n,1,0,self.n-1)

    def GET(self,n,np,L,R):
        """
        この関数は普通外部から実行しない
        """
        if self.Lazy[np] is None:
            if (L==n and R==n):
                return self.A[np]
            else:
                M=(L+R)//2#正確には左の子の右端
                if(n<=M):#左の子なら
                    return self.GET(n,2*np,L,M)
                else:
                    return self.GET(n,2*np+1,M+1,R)
        else:
            return self.Lazy[np]

    def query(self,L:int,R:int):
        """
        query(L,R) セグ木のLからRの最大値を求める
        """
        return self.QUERY(L,R,1,0,self.n-1)

    def QUERY(self,l:int,r:int,np,L,R):
        """
        この関数は普通外部から実行しない
        """
        if (L==l and R==r):
            return self.A[np]
        if self.Lazy[np] is not None:
            return self.Lazy[np]*(r-l+1)
        M=(L+R)//2#正確には左の子の右端
        if l<=M:#左に触れているなら
            if M+1<=r:#右にも触れているなら
                return self.QUERY(l,M,2*np,L,M)+self.QUERY(M+1,r,2*np+1,M+1,R)
            else:
                return self.QUERY(l,r,2*np,L,M)
        else:
            return self.QUERY(l,r,2*np+1,M+1,R)
            
