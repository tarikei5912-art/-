class WaveletMatrix:
    __slots__=("A","count0","MaxBit","N")
    def __init__(self,A:list,MaxBit:int):
        """
        機能
        count(L,R,U,D) 配列で[L,R)の間のD以上U以下にあるものの個数をかえす
        search(L,R,k) 配列で[L,R]をソートした時にk番目(0indexed)を返す
        """
        self.A=[]
        B=self.A
        self.MaxBit=MaxBit
        self.N=len(A)
        N=len(A)
        self.count0=[]#区間[0,n)で左に行った要素の数
        count0=self.count0
        for _ in range(MaxBit+1):
            B.append([])
            count0.append([0]*(N+1))
        B[0]=A
        for b in range(1,MaxBit+1):
            c=0#右に行くやつが現れるたびにカウントする
            L=[]#左に行くやつ
            R=[]#右に行くやつ
            for n in range(N):
                if B[b-1][n]&(1<<MaxBit-b)==0:#左にいく
                    L.append(B[b-1][n])
                    c+=1
                else:
                    R.append(B[b-1][n])
                count0[b-1][n+1]=c
            B[b]=L+R

    def count(self,L,R,U,D):
        """
        count(L,R,U,D) 配列で[L,R)の間のD以上U以下にあるものの個数をかえす
        """
        if D!=0:
            return self.COUNT(L,R,U)-self.COUNT(L,R,D-1)
        else:
            return self.COUNT(L,R,U)

    def COUNT(self,L,R,U):
        """
        この関数は普通外部から直接実行しない
        配列で[L,R]のU以下の数を返す
        """
        ANS=0
        count=self.count0
        l,r=L,R
        for n in range(self.MaxBit):
            if U&(1<<(self.MaxBit-n-1))==0:#左に進む
                l,r=count[n][l],count[n][r]
            else:#右に進む
                ANS+=count[n][r]-count[n][l]
                l,r=count[n][-1]+(l-count[n][l]),count[n][-1]+(r-count[n][r])


        return ANS+(r-l)
                

