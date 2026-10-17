import random

"""
テスト
add(random.randint(-10**9,10**9))を40万回
random_access(n)を40万回
search(random.randint(-10**9,10**9))を40万回実行
100個のランダムテストケース
平均2s
最大3.10s
"""
class Treap():#現状二秒で4.0×10**5個要素を追加するのが限界
    """
    https://github.com/tarikei5912-art/-
    """
    def __init__(self):#初期化
        self.key=[]#値を保存する
        self.priority=[]#ランダム優先度 数字が高いほうが優先度が高い
        self.left=[]#左のノードのアドレス
        self.right=[]#右のノードのアドレス
        self.left_len=[]#そのノードにあるものの部分木の要素の数(そのノードを含む)
        self.right_len=[]#そのノードにあるものの部分木の要素の数(そのノードを含む)
        self.parent=[]#そのノードの親のアドレスを保存
        self.root=None#最上位の番号を決める
        self.attribute=[]
    
    def add(self,a):#要素を追加するO(logN)
        #print("a",a)
        if self.root is None:#初めての追加なら
            self.key.append(a)
            self.priority.append(random.randint(0,10**9))
            self.left.append(-1)
            self.right.append(-1)
            self.left_len.append(0)
            self.right_len.append(0)
            self.parent.append(-1)
            self.root=0
            self.attribute.append(-1)#属性親の左についてる子なら0,親の右についてる子なら1,根なら-1
        else:
            np=self.root
            priority=random.randint(0,10**9)
            n=len(self.key)
            
            while True:
                if self.key[np]>a:#左側に配置するなら
                    if self.left[np]==-1:#左に子がないなら
                        self.left[np]=n
                        self.key.append(a)
                        self.priority.append(priority)
                        self.left.append(-1)
                        self.right.append(-1)
                        self.parent.append(np)
                        self.left_len.append(0)
                        self.right_len.append(0)
                        self.left_len[np]+=1
                        self.attribute.append(0)
                        break
                    else:
                        self.left_len[np]+=1
                        np=self.left[np]
                else:#右側に配置するなら
                    if self.right[np]==-1:#右に子がないなら
                        self.right[np]=n
                        self.key.append(a)
                        self.priority.append(priority)
                        self.left.append(-1)
                        self.right.append(-1)
                        self.parent.append(np)
                        self.left_len.append(0)
                        self.right_len.append(0)
                        self.right_len[np]+=1
                        self.attribute.append(1)
                        break
                    else:
                        self.right_len[np]+=1
                        np=self.right[np]
            #ここから右回転や左回転で上手いことしないといけない
            np=n
            while True:
                if np==self.root:
                    break
                parent=self.parent[np]#元々の親
                right=self.right[np]#元々の右
                right_len=self.right_len[np]
                left=self.left[np]#元々の右
                left_len=self.left_len[np]
                grandparent=self.parent[parent]#こいつが-1の場合若干話が変わる
                
                if self.priority[parent]>=self.priority[np]:#親の優先度が高ければ(回転の必要がない)
                    break
                else:#回転する必要があるなら
                    if self.attribute[np]==0:#右回転の必要があるなら
                        #親の乗っ取り
                        self.attribute[np]=self.attribute[parent]#親の属性を引き継ぎ
                        self.parent[np]=self.parent[parent]#親の親を引き継ぐ
                        if grandparent==-1:#新たな親が存在しない場合
                            self.root=np
                        else:#新たな親が存在する場合
                            if self.attribute[np]==0:#新たな親のどちらの子であるかによって処理がかわる
                                self.left[grandparent]=np
                            else:
                                self.right[grandparent]=np
                        #元親の子化
                        self.parent[parent]=np
                        self.attribute[parent]=1
                        self.right[np]=parent
                        #親の元子供の枠への押し付け
                        self.left[parent]=right#元々持ってた右の子を元親の左の空いた枠に押し付ける
                        if right==-1:#そもそも子供が存在しないなら
                            self.left_len[parent]=0
                        else:#子供が存在するなら
                            self.left[parent]=right
                            self.left_len[parent]=self.left_len[right]+1+self.right_len[right]
                            self.parent[right]=parent
                            self.attribute[right]=0
                        self.right_len[np]=self.left_len[parent]+1+self.right_len[parent]

                    elif self.attribute[np]==1:#左回転の必要があるなら
                        #親の乗っ取り
                        self.attribute[np]=self.attribute[parent]#親の属性を引き継ぎ
                        self.parent[np]=self.parent[parent]#親の親を引き継ぐ
                        if grandparent==-1:#新たな親が存在しない場合
                            self.root=np
                        else:#新たな親が存在する場合
                            if self.attribute[np]==0:#新たな親のどちらの子であるかによって処理がかわる
                                self.left[grandparent]=np
                            else:
                                self.right[grandparent]=np
                        #元親の子化
                        self.parent[parent]=np
                        self.attribute[parent]=0
                        self.left[np]=parent
                        #親の元子供の枠への押し付け
                        self.right[parent]=left#元々持ってた右の子を元親の左の空いた枠に押し付ける
                        if left==-1:#そもそも子供が存在しないなら
                            self.right_len[parent]=0
                        else:#子供が存在するなら
                            self.right[parent]=left
                            self.right_len[parent]=self.left_len[left]+1+self.right_len[left]
                            self.parent[left]=parent
                            self.attribute[left]=1
                        self.left_len[np]=self.left_len[parent]+1+self.right_len[parent]

                
    def debag(self):#デバッグ用
        print("parent",self.parent)
        print("left",self.left)
        print("right",self.right)
        print("left_len",self.left_len)
        print("right_len",self.right_len)
        print("key",self.key)
        print("priority",self.priority)

        
    def remove(self,n):#要素を削除する工事中
        #結構難しそう
        pass

    def random_access(self,n):#ランダムアクセスO(logN)
        if n<0 or len(self.key)<=n:#範囲外アクセスなら
            return None
        else:
            np=self.root
            while True:
                if n==self.left_len[np]:#今いる地点がnなら
                    return self.key[np]
                elif n>self.left_len[np]:#左の配列に用事はない場合
                    n-=(self.left_len[np]+1)
                    np=self.right[np]
                else:#右の配列に用事はない場合
                    np=self.left[np]

        
    def search(self,N):#要素がNの配列番号を返す、ないなら-1を返す,O(logN)
        if len(self.key)==0:
            return -1
        elif len(self.key)==1:
            if self.key[0]==N:
                return 0
            else:
                return -1
        else:
            np=self.root
            while True:
                if self.key[np]==N:
                    return np
                elif self.key[np]<N:#右側にありそう
                    if self.right[np]==-1:#右側がないなら
                        return -1
                    else:
                        np=self.right[np]
                else:#左側にありそう
                    if self.left[np]==-1:#左側がないなら
                        return -1
                    else:
                        np=self.left[np]
    
    def return_deep(self):#計算量が深すぎじゃないかのチェックO(N)
        return self.return_deep2(self.root)
    
    def return_deep2(self,np):
        ans=1
        if self.right[np]==-1:#右側が存在しないなら
            pass
        else:
            ans=self.return_deep2(self.right[np])+1
        if self.left[np]==-1:#左側が存在しないなら
            pass
        else:
            ans=max(ans,self.return_deep2(self.left[np])+1)
        return ans