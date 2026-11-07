N=int(input())
MAP=[]
DFS=[0]
IN=[-1]*N#入ってくるタイミング
OUT=[-1]*N#出ていくタイミング
incount=1
IN[0]=0
outcount=0
D=[0]*N

def E():
    global DFS,incount,outcount,IN,OUT,D
    np=DFS[-1]
    for to in MAP[np]:
        #print(np,to)
        if IN[to]==-1:
            IN[to]=incount
            incount+=1
            DFS.append(to)
            E()
    DFS.pop()
    OUT[np]=outcount
    outcount+=1
    D[np]=len(DFS)
    if len(DFS)==0:
        return

E()
print(IN)
print(OUT)
print(D)