import random
class Treap:
    __slots__=("A","LA","RA","LC","RC","PA","Root")
    def __init__(self):
        self.A=[]
        self.LA=[]
        self.RA=[]
        self.PA=[]
        self.LC=[]
        self.RC=[]
        self.Root=None

    def add(self,X):
        """
        Xを追加
        引数
        X 追加する数
        """
        if self.Root==None:
            """
            現在根が存在しない場合
            """
            self.Root=0
            self.A.append(X)
            self.LA.append(-1)
            self.RA.append(-1)
            self.PA.append(-1)
            self.LC.append(0)
            self.RC.append(0)

    def random_access(self,n:int):
        """
        random_access ランダムアクセス
        引数
        n 添字
        """

    

    
        

        

        

