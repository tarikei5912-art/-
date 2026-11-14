"""
https://github.com/tarikei5912-art/-
"""
import math
def gcd(a,b):
    return math.gcd(a,b)
    
def lcm(a,b):
    return math.lcm(a,b)

def pow_mod(n,m,mod):#modを法としたときのn^mを返す
    return pow(n,m,mod)

def mod_inv(n,mod):#modを法としたとき×nの逆元を見つける
    return pow(n,-1,mod)

