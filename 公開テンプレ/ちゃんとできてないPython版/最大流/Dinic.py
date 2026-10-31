def Dinic(N:int,Edges:list,resource:list,sink:list):
    """
    https://github.com/tarikei5912-art/-
    """
    """
    N頂点の数
    Edges[m] [出発点,到着点,流せる量]
    """
    FMAP=[]#フローマップ
    inf=10**20
    MAP=[]
    for n in range(N+2):
        FMAP.append([])
        MAP.append(set([]))
        for _ in range(N+2):
            FMAP[n].append(0)
    
    for u,v,w in Edges:
        FMAP[u+1][v+1]+=w
        MAP[u+1].add(v+1)
        MAP[v+1].add(u+1)
    for n in range(N+2):
        MAP[n]=list(MAP[n])

    for r in resource:
        FMAP[0][r+1]=inf
        MAP[0].append(r+1)
        MAP[r+1].append(0)


    for s in sink:
        FMAP[s+1][N+1]=inf
        MAP[s+1].append(N+1)
        MAP[N+1].append(s+1)

    ANS=0
    RBFSC=0
    while True:
        #はじめにBFSを行う
        BFS=[-1]*(N+2)
        BFS[0]=0
        D=[0]
        d=0
        while True:
            np=D[d]
            if np==N+1:
                break
            for to in MAP[np]:
                if FMAP[np][to]>0 and BFS[to]==-1:
                    BFS[to]=BFS[np]+1
                    D.append(to)
            d+=1
            if d==len(D):
                break

        if BFS[-1]==-1:
            break


        #次に逆順にBFSをして関係ない通路を切る
        BFS2=[0]*(N+2)
        BFS2[N+1]=1
        D=[N+1]
        d=0
        while True:
            np=D[d]
            if np==0:
                break
            for to in MAP[np]:
                if FMAP[to][np]>0 and BFS[np]==BFS[to]+1 and BFS2[to]==0:
                    BFS2[to]=1
                    D.append(to)
            d+=1
            if d==len(D):
                break   

        for d in D:
            BFS[d]+=N+5
        RBFSC+=1

        #DFSを行う

        DFS=[0]#今まで通ったノード 
        CDFS=[0]
        WMAP=[0]#i番目にいる頂点より前は全てWMAP[i]を流す
        TEMP=[[inf+1,0]]#i番目の頂点を見ているときは流す量(仮)はTEMP[i]
        temp=inf+1
        TEMP2=0#このフェーズで流した水の量
        while True:
            np=DFS[-1]
            if np==N+1:
                WMAP[-1],count=TEMP[-1][0]-TEMP2,TEMP[-1][1]
                TEMP2=TEMP[-1][0]
                ANS+=WMAP[-1]
                for _ in range(count):
                    w=WMAP[-1]
                    WMAP.pop()
                    to=DFS.pop()
                    np=DFS[-1]
                    FMAP[np][to]-=w
                    FMAP[to][np]+=w
                    WMAP[-1]+=w
                    CDFS.pop()
                    TEMP.pop()
                count=TEMP[-1][1]
            if CDFS[-1]==len(MAP[np]):
                CDFS.pop()
                to=DFS.pop()
                w=WMAP.pop()
                TEMP.pop()
                if len(DFS)==0:
                    break
                np=DFS[-1]
                temp,count=TEMP[-1]
                FMAP[np][to]-=w
                FMAP[to][np]+=w
                WMAP[-1]+=w
            else:
                CDFS[-1]+=1
                to=MAP[np][CDFS[-1]-1]
                if BFS[to]==BFS[np]+1 and FMAP[np][to]>0:
                    if TEMP[-1][0]-TEMP2>FMAP[np][to]:
                        temp=FMAP[np][to]+TEMP2
                        count=0
                    count+=1
                    TEMP.append([temp,count])
                    DFS.append(to)
                    CDFS.append(0)
                    WMAP.append(0)
    return ANS
                

            
            


    