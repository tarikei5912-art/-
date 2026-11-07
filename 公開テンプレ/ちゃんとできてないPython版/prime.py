class prime:
    """
    https://github.com/tarikei5912-art/-
    """
    __slots__=("prime_list","prime_list2","N")
    def __init__(self,N):#Nまでの素数を全て求める
        self.prime_list=[True]*(N+1)
        self.prime_list[0]=False
        self.prime_list[1]=False
        self.prime_list2=[]
        self.N=N
        for n in range(2,N+1):
            if n**2>N:
                break
            if self.prime_list[n]:
                for m in range(n*n,N+1,n):
                    self.prime_list[m]=False
        for n in range(2,N+1):
            if self.prime_list[n]:
                self.prime_list2.append(n)
    
    def check_prime(self,n):#nが素数であるかどうかを判定する
        #注：事前に決定したNより大きい場合O(N/logN)かかる
        if n <=self.N:
            return self.prime_list[n]
        elif n <=self.N**2:
            p=0
            while True:
                if self.prime_list2[p]**2>n:
                    break
                if n%self.prime_list2[p]==0:
                    p+=1
                else:
                    return False
            return True
        else:
            return None

    def return_prime_list(self):
        return self.prime_list

#これはさらに改良することができそう