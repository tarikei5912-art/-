class Fenwick_tree:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("N","n","A","B")

    def __init__(self,N:int,A:list):#はじめにAリストを2^Nにゼロ埋めした配列からフェニ木を作る
        self.N=N
        self.n=1<<N
        self.A=[0]*(self.n+1)
        self.B=[]#以後Bは配列の値保存用に使う
        for a in range(len(A)):
            self.B.append(A[a])
        B=[0]*(self.n+1)#B[i]=Aの[0,i)の和(累積和)
        SUM=0
        while True:
            if len(self.B)<self.n:
                self.B.append(0)
            else:
                break
        for n in range(self.n):
            if n<len(A):
                SUM+=A[n]
            B[n+1]=SUM
        for n in range(1,self.n+1):
            self.A[n]=B[n]-B[(n-1)&(n)]


    def add(self,n:int,x):
        """
        外部から与えるのは0indexの添字である
        加算
        """
        self.B[n]+=x
        n+=1#これで1indexedになる
        while True:
            if n==self.n:
                break
            self.A[n]+=x
            n=n+(((~n)+1)&n)
        self.A[n]+=x

    def update(self,n:int,x):
        """
        外部から与えるのは0indexの添字である
        更新
        """
        dx=x-self.B[n]
        self.add(n,dx)

    def query(self,l:int,r:int):
        """
        [l,r]の区間合計を返す
        ここでlとrは0indexedである
        """
        r+=1
        SUM=0
        while True:
            if r==0:
                break
            SUM+=self.A[r]
            r=(r-1)&r
        while True:
            if l==0:
                break
            SUM-=self.A[l]
            l=(l-1)&l
        return SUM 

