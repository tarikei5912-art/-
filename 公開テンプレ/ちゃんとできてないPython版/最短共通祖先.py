

class LCA:
    """
    https://github.com/tarikei5912-art/-
    """
    """
    自動的に頂点0を根とする
    """
    __slots__=("Dict","A","H","B","n")
    def __init__(self,N:int,MAP:list):
        """
        MAPはちゃんと双方向に移動できる木にしてから入れること
        MAP[i]=地点iから移動できる地点のリスト
        """
        self.Dict={0:0}
        Euler_Tour=[0]
        self.H=[None]*N
        self.H[0]=0
        DFS=[0]
        h=0
        while True:
            if len(MAP[DFS[-1]])==0:#いく先がないなら
                DFS.pop()
                h-=1
            else:
                if self.H[MAP[DFS[-1]][-1]] is not None:#上に戻るやつなら
                    MAP[DFS[-1]].pop()
                    continue

                else:
                    DFS.append(MAP[DFS[-1]].pop())
                    h+=1
                    self.H[DFS[-1]]=h
            if len(DFS)==0:
                break
            else:
                if DFS[-1] not in self.Dict:
                    self.Dict[DFS[-1]]=len(Euler_Tour)
                Euler_Tour.append(DFS[-1])
        p=len(Euler_Tour)
        N=0
        while p!=0:
            N+=1
            p=p>>1



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

        for a in range(len(Euler_Tour)):
            self.A[0][a]=Euler_Tour[a]

        for n in range(N-1):
            p=1<<n
            for m in range(self.n):
                if m+p>=self.n:
                    self.A[n+1][m]=self.A[n][m]
                else:
                    if self.H[self.A[n][m]]<self.H[self.A[n][m+p]]:
                        self.A[n+1][m]=self.A[n][m]
                    else:
                        self.A[n+1][m]=self.A[n][m+p]

        self.B=[0]
        for n in range(N):
            for a in range(1<<n):
                self.B.append(n)

    def LCA(self,l:int,r:int):
        l=self.Dict[l]
        r=self.Dict[r]
        if l>r:
            l,r=r,l
        q=self.B[r-l]
        
        if self.H[self.A[q][l]]<self.H[self.A[q][r-(1<<q)+1]]:
            return self.A[q][l]
        else:
            return self.A[q][r-(1<<q)+1]
        

        