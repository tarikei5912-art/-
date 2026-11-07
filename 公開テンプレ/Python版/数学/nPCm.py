class nPCm:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("nf","nfi","mod")

    def __init__(self,MAX_n,mod):#nの最大値を入れて前計算をする
        """
        modが素数かつMAX_n<modならただしく動く
        """
        self.mod=mod
        nf=[1]*(MAX_n+1)
        nfi=[1]*(MAX_n+1)
        for n in range(1,MAX_n+1):
            nf[n]=nf[n-1]*n%mod
        
        nfi[-1]=self.mod_inv(nf[-1])
        for n in range(MAX_n-1,0,-1):
            nfi[n]=(nfi[n+1]*(n+1))%mod
        self.nf=nf
        self.nfi=nfi

    def mod_inv(self,n):#modを法としたとき×nの逆元を見つける
        return pow(n,-1,self.mod)
    
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