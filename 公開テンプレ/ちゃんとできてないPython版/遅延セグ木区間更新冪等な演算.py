class Lazy_Segment_Tree:
    """
    https://github.com/tarikei5912-art/-
    """
    """
    区間更新の遅延セグ木
    """
    __slots__ = ("A", "Lazy", "N","n", "L", "R","ZERO")
    def __init__(self,N:int,A:list):
        if A is None:
            A=[]
        self.A=[0]*(2<<N)
        self.Lazy=[None]*(2<<N)
        self.N=N
        self.n=1<<N
        self.L=[0]*(2<<N)
        self.R=[(1<<N)-1]*(2<<N)
        for n in range(1,1<<N):
            self.L[2*n]=self.L[n]
            self.R[2*n]=(self.L[n]+self.R[n])//2
            self.L[2*n+1]=(self.L[n]+self.R[n])//2+1
            self.R[2*n+1]=self.R[n]
        self.ZERO=0
        for a in range(len(A)):
            self.A[(1<<N)+a]=A[a]
        for n in range((1<<self.N)-1,0,-1):
            self.A[n]=self.F(self.A[2*n],self.A[2*n+1])


    def Lazy_inheritance(self,n):
        self.Lazy[2*n]=self.Lazy[n]
        self.Lazy[2*n+1]=self.Lazy[n]
        self.A[2*n]=self.Lazy[n]
        self.A[2*n+1]=self.Lazy[n]
        self.Lazy[n]=None


    def update(self,L:int,R:int,X):
        """
        区間[L,R]をXに更新する
        """
        STACK=[(L,R,1)]
        RE=[]
        while len(STACK):
            l,r,n=STACK.pop()
            if l==self.L[n] and r==self.R[n]:
                self.Lazy[n]=X
                self.A[n]=X

            elif r<=self.R[n*2]:#更新区間が今の地点の左の子の場合
                RE.append(n)
                if self.Lazy[n] is not None:
                    self.A[n]=self.Lazy[n]
                    self.Lazy_inheritance(n)
                STACK.append((l,r,n*2))
            elif self.L[n*2+1]<=l:
                RE.append(n)
                if self.Lazy[n] is not None:
                    self.A[n]=self.Lazy[n]
                    self.Lazy_inheritance(n)
                STACK.append((l,r,n*2+1))
            else:
                RE.append(n)
                if self.Lazy[n] is not None:
                    self.A[n]=self.Lazy[n]
                    self.Lazy_inheritance(n)
                    
                STACK.append((l,self.R[n*2],n*2))
                STACK.append((self.L[n*2+1],r,n*2+1))
        # 子から親の順に再計算

        for n in reversed(RE):

            self.A[n] = self.F(
            
            self.A[2*n],

            self.A[2*n+1])

    def F(self,a,b):#ここをいじることでminとmaxを切り替えることができる
        return sum(a,b)

    def query(self,L:int,R:int):
        STACK=[(L,R,1)]
        ANS=self.ZERO
        while len(STACK):
            l,r,n=STACK.pop()
            if l==self.L[n] and r==self.R[n]:
                if self.Lazy[n] is not None:
                    if n>=self.n:#一番下なら
                        self.A[n]=self.Lazy[n]
                        self.Lazy[n]=None
                    else:
                        self.A[n]=self.Lazy[n]
                        self.Lazy_inheritance(n)
                ANS=self.F(ANS,self.A[n])
            elif r<=self.R[n*2]:#区間[L,R]が左の子にいる場合
                if self.Lazy[n] is not None:
                    self.A[n]=self.Lazy[n]
                    self.Lazy_inheritance(n)
                STACK.append((l,r,2*n))
            elif self.L[n*2+1]<=l:#区間[L,R]が右の子の場合
                if self.Lazy[n] is not None:
                    self.A[n]=self.Lazy[n]
                    self.Lazy_inheritance(n)
                STACK.append((l,r,2*n+1))
            else:
                if self.Lazy[n] is not None:
                    self.A[n]=self.Lazy[n]
                    self.Lazy_inheritance(n)
                STACK.append((l,self.R[2*n],2*n))
                STACK.append((self.L[2*n+1],r,2*n+1))
        return ANS