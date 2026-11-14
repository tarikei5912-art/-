
def SCC(N:int,Edges:list):
    """
    https://github.com/tarikei5912-art/-
    """
    """
    Nは頂点の数
    Edgesは辺の数
    Edges[i]は[i本目の辺のスタート地点,i本目の辺のゴール地点]
    #なお頂点番号は0indexedで与えるので気をつけること
    """
    MAP=[]
    RMAP=[]
    for _ in range(N):
        MAP.append([])
        RMAP.append([])
    for m in range(len(Edges)):
        FROM,TO=Edges[m]
        MAP[FROM].append(TO)
        RMAP[TO].append(FROM)
    
    order=[]
    DMAP=[0]*N
    CMAP=[0]*N
    for n in range(N):
        if DMAP[n]!=0:
            continue
        D=[n]
        DMAP[n]=1
        while True:
            if len(D)==0:
                break
            np=D[-1]
            if len(MAP[np])==CMAP[np]:
                DMAP[np]=2
                order.append(np)
                D.pop()
            else:   
                if DMAP[MAP[np][CMAP[np]]]==0:
                    D.append(MAP[np][CMAP[np]])
                    DMAP[MAP[np][CMAP[np]]]=1
                CMAP[np]+=1

    SCCNodes=[-1]*N
    SCCEdges=[]
    DMAP=[0]*N
    NodesCount=0
    for n in range(len(order)-1,-1,-1):
        if SCCNodes[order[n]]!=-1:
            continue
        D=[order[n]]
        DMAP[order[n]]=1
        SCCNodes[order[n]]=NodesCount
        d=0
        while True:
            for x in RMAP[D[d]]:
                if DMAP[x]!=1:
                    DMAP[x]=1
                    D.append(x)
                    SCCNodes[x]=NodesCount
            d+=1
            if len(D)==d:
                break
        NodesCount+=1
    REMAP=[]
    for _ in range(NodesCount):
        REMAP.append(set([]))
    for FROM,TO in Edges:
        if SCCNodes[FROM]!=SCCNodes[TO]:
            REMAP[SCCNodes[FROM]].add(SCCNodes[TO])
    for a in range(NodesCount):
        SCCEdges.append(list(REMAP[a]))
    return SCCNodes,SCCEdges



    





        
