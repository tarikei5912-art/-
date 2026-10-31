"""
https://github.com/tarikei5912-art/-
"""
def gcd(a,b):
    while True:
        if a%b==0:
            return b
        else:
            a,b=b,a%b
    
def lcm(a,b):
    return a*b//gcd(a,b)

def pow_mod(n,m,mod):#modを法としたときのn^mを返す
    n=n%mod
    q=n#現状はnを入れておくがこれが繰り返し二乗法に使うやつ
    ANS=1
    while m>=1:
        if m%2==1:
            ANS=(ANS*q)%mod
        m=m>>1
        q=(q*q)%mod
    return ANS

def mod_inv(n,mod):#modを法としたとき×nの逆元を見つける
    return pow_mod(n,mod-2,mod)
