class nPCm:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("nf","nfi","mod")

    def __init__(self,MAX_n,mod):#nの最大値を入れて前計算をする
        self.mod=mod
        self.nf=[1]*(MAX_n+1)
        self.nfi=[1]*(MAX_n+1)
        for n in range(1,MAX_n+1):
            self.nf[n]=self.nf[n-1]*n%self.mod
        
        self.nfi[-1]=self.mod_inv(self.nf[-1])
        for n in range(MAX_n-1,0,-1):
            self.nfi[n]=(self.nfi[n+1]*(n+1))%mod

    def pow_mod(self,n,m,mod):#modを法としたときのn^mを返す
        n=n%mod
        q=n#現状はnを入れておくがこれが繰り返し二乗法に使うやつ
        ANS=1

        while m>=1:
            if m%2==1:
                ANS=(ANS*q)%mod
            m=m>>1
            q=(q*q)%mod
        return ANS

    def mod_inv(self,n):#modを法としたとき×nの逆元を見つける
        return self.pow_mod(n,self.mod-2,self.mod)
    
    def nCm(self,n,m):
        if n<m:
            return 0
        else:
            return (self.nf[n]*self.nfi[m]*self.nfi[n-m])%self.mod
    
    def nPm(self,n,m):
        if n<m:
            return 0
        else:
            return (self.nf[n]*self.nfi[n-m])%self.mod

#改良ポイントlucasの定理を利用してpが小さいけどnがでかい時のコードも書いた方がいい
#また法が素数でないときに使えない