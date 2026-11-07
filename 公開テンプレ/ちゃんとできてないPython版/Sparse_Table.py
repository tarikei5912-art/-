class Sparse_Table:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("n","A","B")
    def __init__(self,N:int,A:list):#大きさ
        """
        A[N][1<<N]の配列を作る
        使う時の注意点
        ・単位元の設定は関数によって変わる
        """
        identity_element=0
        self.A=[]
        self.n=1<<N
        if N==0:
            self.A=[[identity_element]]
        for n in range(N):
            self.A.append([])
            for _ in range(self.n):
                self.A[n].append(identity_element)

        for a in range(len(A)):
            self.A[0][a]=A[a]

        for n in range(N-1):
            p=1<<n
            for m in range(self.n):
                if m+p>=self.n:
                    self.A[n+1][m]=self.A[n][m]
                else:
                    self.A[n+1][m]=self.function(self.A[n][m],self.A[n][m+p])

        self.B=[0]
        for n in range(N):
            for a in range(1<<n):
                self.B.append(n)



    def function(self,a,b):
        return max(a,b)


    def query(self,l:int,r:int):
        """
        区間[l,r]の区間クエリを返す
        """
        q=self.B[r-l]
        return self.function(self.A[q][l],self.A[q][r-(1<<q)+1])


    