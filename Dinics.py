#Dinic Algorithm
import time

#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix,flow matrix,source and sink
        n = len(C)
        queue = []
        queue.append(s)# //append the source
        global level
        level = n * [0]  # initialization
        #print(level)
        level[s] = 1  
        while queue:
            k = queue.pop(0)
            for i in range(n):
                    if (F[k][i] < C[k][i]) and (level[i] == 0): # not visited
                            level[i] = level[k] + 1
                            print(level[i])
                            queue.append(i)
                            print(queue)
        return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(C)):
            if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
                f = Dfs(C,F,i,min(tmp,C[k][i] - F[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp

#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)] # F is the flow matrix
       # print(F)
        flow = 0
        while(Bfs(C,F,s,t)):
               
               flow = flow + Dfs(C,F,s,10000)
        
        return flow

#-------------------------------------
# make a capacity graph
# node   s   A   B   C   D   t
C =     [[ 0, 10, 10, 0, 0, 0 ],  # s
        [ 0, 0, 1, 4, 8, 0 ],  # A
        [ 0, 0, 0, 2, 9, 0 ],  # B
        [ 0, 0, 0, 0, 0, 10 ],  # C
        [ 0, 0, 0, 0, 0, 10 ],  # D
        [ 0, 0, 0, 0, 0, 0 ]]  # t

source = 0  # A
sink = 5   # F
print ("Dinic's Algorithm")


start=time.time()
max_flow_value = MaxFlow(C, source, sink)
print ("max_flow_value is", max_flow_value)
# using time() to show present time 
end=time.time()
print("Sigma/Diff:  ", end-start)



