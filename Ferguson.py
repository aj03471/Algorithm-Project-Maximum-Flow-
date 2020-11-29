#Ford-Fulkerson Algorithm

#Number of nodes = n
import time

#find path by using BFS
def dfs(C, F, s, t):
        print()
        print("source:",s,"sink:",t)
        
        stack = [s]
        paths={s:[]}
        if s == t:
                return paths[s]
        while(stack): # O(n)
                u = stack.pop()
                for v in range(len(C)): #O(n^2)
                        if(C[u][v]-F[u][v]>0) and v not in paths:
                                paths[v] = paths[u]+[(u,v)]
                                print(paths)
                                if v == t:
                                        print("F:",F)
                                        print("C:",C)
                                        print("Paths["+str(v)+"]:",paths[v])
                                        print("DFS: PATHS:",paths)
                                        return paths[v]
                                stack.append(v)
                print("stack:",stack)
                                
        return None

# number of paths = P
def max_flow(C, s, t):
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)]
        print("F:",F)
        path = dfs(C, F, s, t) #O(n^2)
        count = 0
        while path != None: # O (P) 
            print()
            count = count+1
            print("count:",count)
            print()
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path: #O(len(path))
                print("for u,v in path:",u,v,path)
                F[u][v] += flow
                F[v][u] -= flow
            path = dfs(C,F,s,t) #O(P * n^2)
            print("while: Path:",path)
        return sum(F[s][i] for i in range(n))

#PseudoPolynimial time complexity:
# O(P * n^2) + O(n^2) + O(len(path)) + O(1) = O(P * n^2)
    
# make a capacity graph
# node s  o  p  q  r  t
C1 = [[ 0, 3, 3, 0, 0, 0 ],  # s
     [ 0, 0, 2, 3, 0, 0 ],  # o
     [ 0, 0, 0, 0, 2, 0 ],  # p
     [ 0, 0, 0, 0, 4, 2 ],  # q
     [ 0, 0, 0, 0, 0, 2 ],  # r
     [ 0, 0, 0, 0, 0, 0 ]]  # t

C = [[ 0, 16, 13, 0, 0, 0 ],  # s
     [ 0, 0, 10, 12, 0, 0 ],  # o
     [ 0, 4, 0, 0, 14, 0 ],  # p
     [ 0, 0, 9, 0, 0, 20 ],  # q
     [ 0, 0, 0, 7, 0, 4 ],  # r
     [ 0, 0, 0, 0, 0, 0 ]]  # t

source = 0  # A
sink = 10    # F

print("Ford-Fulkerson algorithm")


start=time.time()
max_flow_value = max_flow(C, source, sink)
print("max_flow_value is: ", max_flow_value)
# using time() to show present time 
end=time.time()
print("Sigma/Diff:  ", end-start)
