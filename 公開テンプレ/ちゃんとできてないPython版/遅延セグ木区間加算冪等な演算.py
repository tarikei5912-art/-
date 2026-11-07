class Lazy_Segment_Tree:#区間加算
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__ = ("A", "Lazy", "N", "L", "R","ZERO")
    def __init__(self,N:int,A:list):
        if A is None:
            A=[]
        self.A=[0]*(2<<N)
        self.Lazy=[0]*(2<<N)
        self.N=N
        self.L=[0]*(2<<N)
        self.R=[(1<<N)-1]*(2<<N)
        for n in range(1,1<<N):
            self.L[2*n]=self.L[n]
            self.R[2*n]=(self.L[n]+self.R[n])//2
            self.L[2*n+1]=(self.L[n]+self.R[n])//2+1
            self.R[2*n+1]=self.R[n]
        self.ZERO=float("inf")
        for a in range(len(A)):
            self.A[(1<<N)+a]=A[a]
        for n in range((1<<self.N)-1,0,-1):
            self.A[n]=self.F(self.A[2*n]+self.Lazy[2*n],self.A[2*n+1]+self.Lazy[2*n+1])

    def add(self,L:int,R:int,X:int):
        STACK=[(L,R,X,1)]
        RE=[]
        while len(STACK):
            l,r,x,n=STACK.pop()
            if l==self.L[n] and r==self.R[n]:
                self.Lazy[n]+=x
                continue
            elif r<=self.R[n*2]:
                STACK.append((l,r,x,n*2))
            elif self.L[n*2+1]<=l:
                STACK.append((l,r,x,n*2+1))
            else:
                STACK.append((l,self.R[n*2],x,n*2))
                STACK.append((self.L[n*2+1],r,x,n*2+1))
            RE.append(n)
        for a in range(len(RE)):
            n=RE[-a-1]
            self.A[n]=self.F(self.A[2*n]+self.Lazy[2*n],self.A[2*n+1]+self.Lazy[2*n+1])

    def F(self,a,b):#ここをいじることでminとmaxを切り替えることができる
        return min(a,b)

    def query(self,L:int,R:int):
        STACK=[(L,R,1)]
        RE=[]
        ANS=self.ZERO
        while len(STACK):
            l,r,n=STACK.pop()
            if l==self.L[n] and r==self.R[n]:
                ANS=self.F(ANS,self.A[n]+self.Lazy[n])
                continue
            elif r<=self.R[n*2]:
                STACK.append((l,r,n*2))
            elif self.L[n*2+1]<=l:
                STACK.append((l,r,n*2+1))
            else:
                STACK.append((l,self.R[n*2],n*2))
                STACK.append((self.L[n*2+1],r,n*2+1))
            if self.Lazy[n]!=0:
                self.Lazy[2*n]+=self.Lazy[n]
                self.Lazy[2*n+1]+=self.Lazy[n]
                self.Lazy[n]=0
            RE.append(n)
        for a in range(len(RE)):
            n=RE[-a-1]
            self.A[n]=self.F(self.A[2*n]+self.Lazy[2*n],self.A[2*n+1]+self.Lazy[2*n+1])
        return ANS