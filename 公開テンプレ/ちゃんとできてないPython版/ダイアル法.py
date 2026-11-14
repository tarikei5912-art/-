def dial(N:int,Edge:list,start:list):
    """
    https://github.com/tarikei5912-art/-
    """
    """
    Nは頂点の数
    Edgeは(始点,終点,重さ)
    始点,終点は0indexed
    """
    MAP=[]
    MAXW=0
    for _ in range(N):
        MAP.append([])
    for s,t,w in Edge:
        MAP[s].append((t,w))
        MAXW=max(MAXW,w)
    inf=10**18
    DMAP=[inf]*N
    D=[]
    for _ in range(MAXW+1):
        D.append([])
    count=0#残り処理していない移動
    for s in start:
        if DMAP[s]==inf:
            D[0].append(s)
            DMAP[s]=0
            count+=1
    d0=0
    nt=0
    while True:
        if count==0:
            break
        d1=0
        if len(D[d0])==0:
            d0=(d0+1)%(MAXW+1)
            nt+=1
            continue
        while True:
            np=D[d0][d1]
            if DMAP[np]==nt:
                for t,w in MAP[np]:
                    if DMAP[t]>DMAP[np]+w:
                        D[(d0+w)%(MAXW+1)].append(t)
                        count+=1
                        DMAP[t]=DMAP[np]+w
            d1+=1
            if d1==len(D[d0]):
                nt+=1
                D[d0]=[]
                count-=d1
                break
        d0=(d0+1)%(MAXW+1)
    return DMAP

    
