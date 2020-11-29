G =  [[ 0, 3, 3, 0, 0, 0 ],  # s
     [ 0, 0, 2, 3, 0, 0 ],  # o
     [ 0, 0, 0, 0, 2, 0 ],  # p
     [ 0, 0, 0, 0, 4, 2 ],  # q
     [ 0, 0, 0, 0, 0, 2 ],  # r
     [ 0, 0, 0, 0, 0, 0 ]]  # t
F =  [[ 0, 0, 0, 0, 0, 0 ],  # s
     [ 0, 0, 0, 0, 0, 0 ],  # o
     [ 0, 0, 0, 0, 0, 0 ],  # p
     [ 0, 0, 0, 0, 0, 0 ],  # q
     [ 0, 0, 0, 0, 0, 0 ],  # r
     [ 0, 0, 0, 0, 0, 0 ]]  # t
import time

def dfs(G,F,s,t):
    stack = [s]
    path = {s:[]}
    

    while(stack):
       
        u = stack.pop()
        for v in range(len(G)):
           
            if (F[u][v] < G[u][v]) and v not in path:
                path[v] = path[u]+[(u,v)]
                if v==t:
                    
                    
                    return path[v]
                stack.append(v)
                
    return None

def main(G,F,s,t):
   
    path = dfs(G,F,s,t)
   
    max_flow = 0
    while (path!=None):
        flow = min(G[u][v] - F[u][v] for u,v in path)
        for u,v in path:
                      
            F[u][v]+=flow
        path = dfs(G,F,s,t)
        
    return sum(F[s][i] for i in range(len(G)))

# using time() to show present time 
start=time.time()
print(main(G,F,0,5))
# using time() to show present time 
end=time.time()
print("Sigma/Diff:  ", end-start)

    
    
