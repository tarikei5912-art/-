class Rolling_Hash:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("S","Mod1","Mod2")
    def __init__(self,S):
        self.S=S
        self.Mod1=18446744073709551533#素数
        self.Mod2=18446744073709551557#素数
        
        
    
    def search(self,S):#self.Sの中にSが入っているかをチェックする,入っているならはじめの入っている場所を返す
        Pow1=self.pow_mod(4649,len(S),self.Mod1)#67^len(S)%Mod1
        Pow2=self.pow_mod(4649,len(S),self.Mod2)#67^len(S)%Mod2
        h1=0
        h2=0
        Hash1=0
        Hash2=0
        for s in range(len(S)):
            Hash1=(Hash1*4649+ord(S[s]))%self.Mod1
        for s in range(len(S)):
            Hash2=(Hash2*4649+ord(S[s]))%self.Mod2
        for s in range(len(self.S)):
            h1=(h1*4649+ord(self.S[s]))%self.Mod1
            if s>=len(S):
                h1=(h1-Pow1*ord(self.S[s-len(S)]))%self.Mod1
            h2=(h2*4649+ord(self.S[s]))%self.Mod2
            if s>=len(S):
                h2=(h2-Pow2*ord(self.S[s-len(S)]))%self.Mod2
            if h1==Hash1 and h2==Hash2:
                return s-len(S)+1
        return -1
    
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
    