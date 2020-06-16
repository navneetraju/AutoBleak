import json
import copy 

start="/hotel/admin/roomreservation.php"
loop_size = 4

with open('guess.json') as json_file:
    data = json.load(json_file)

"""
graph = {}
for item in data:
    s={}
    total = item["exits"]
    for next in item["nextPages"]:
        total += next["pageviews"]
    for next in item["nextPages"]:
        s[next["pagePath"]] = next["pageviews"]/total
    s["exits"] = item["exits"] / total
    graph[item["pagePath"]] = s

print(json.dumps(graph, sort_keys=True, indent=4))
"""

pages=[]
graph=[]
for item in data:
    pages.append(item["pagePath"])

pages.append("exit")

for item in data:
    s=[]
    for j in range(len(pages)):
        s.append(0.0)
    total = item["exits"]
    for next in item["nextPages"]:
        total += next["pageviews"]
    for next in item["nextPages"]:
        for j in range(len(pages)):
            if(pages[j] == next["pagePath"]):
                s[j] = next["pageviews"]/total
    s[len(s)-1]=item["exits"] / total
    graph.append(s)

def max_TSP_fixed(graph, vertex, start, max_path): 
    max_vertex=[]
    while True: 
        if vertex[0]!=start and vertex[len(vertex)-1]!=start:
            k = start
            current_pathweight = 1.0
            for i in range(len(vertex)): 
                current_pathweight *= graph[k][vertex[i]] 
                k = vertex[i] 
            current_pathweight *= graph[k][start] 
    
            if current_pathweight>max_path:
                max_path=current_pathweight
                max_vertex=vertex
                max_vertex = copy.deepcopy(vertex) 
  
        if not next_permutation(vertex): 
                break 
    return [max_vertex,max_path]

def max_TSP(graph, vertex, max_path): 
    max_vertex=[]
    while True: 
        if vertex[0]==vertex[len(vertex)-1]:
            k = vertex[0]
            current_pathweight = 1.0
            for i in range(1,len(vertex)): 
                current_pathweight *= graph[k][vertex[i]] 
                k = vertex[i]  
            if current_pathweight>max_path:
                max_path=current_pathweight
                max_vertex=vertex
                max_vertex = copy.deepcopy(vertex) 
  
        if not next_permutation(vertex): 
                break 
    return [max_vertex,max_path]

def int_to_base_n(i, base):
    digits = []
    while i:
        i, d = divmod(i, base)
        digits.append(str(d))
    if not digits:
        return '0'
    return ''.join(digits[::-1])

def my_sort(l):
    i = 1
    while i < len(l): 
        if(l[i] <= l[i-1]): 
            return 0
        i += 1
    return 1

def get_Loop_fixed(graph, start, path_length):
    max_path=0.0
    max_vertex=[]
    n=len(graph)
    plen=path_length-1
    for i in range(n**n):
        num=int_to_base_n(i, n)
        l=[int(i) for i in str(num)]
        if(len(l)>plen):
            break
        while len(l)<plen:
            l=[0]+l
        if(my_sort(l)): 
            new=max_TSP_fixed(graph, l, start, max_path)
            if new[1]>max_path:
                max_vertex=new[0]
                max_path=new[1]
    max_vertex.insert(0, start) 
    max_vertex.append(start)
    return [max_vertex,max_path]

def get_Loop(graph, path_length):
    max_path=0.0
    max_vertex=[]
    n=len(graph)
    plen=path_length+1
    for i in range(n**n):
        num=int_to_base_n(i, n)
        l=[int(i) for i in str(num)]
        if(len(l)>plen):
            break
        while len(l)<plen:
            l=[0]+l
        if(not any(i==j for i,j in zip(l, l[1:]))): 
            new=max_TSP(graph, l, max_path)
            if new[1]>max_path:
                max_vertex=new[0]
                max_path=new[1]
    return [max_vertex,max_path]

def next_permutation(L): 
    n = len(L) 
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]: 
        i -= 1
    if i == -1: 
        return False
    j = i + 1
    while j < n and L[j] > L[i]: 
        j += 1
    j -= 1
    L[i], L[j] = L[j], L[i] 
    left = i + 1
    right = n - 1
    while left < right: 
        L[left], L[right] = L[right], L[left] 
        left += 1
        right -= 1
    return True

#print(pages)
#for i in graph:
    #print(i)

for i in range(len(pages)):
    if(pages[i]==start):
        s=i
  
res = get_Loop_fixed(graph, s, loop_size-1)
#res = get_Loop(graph, loop_size-1)

loop = res[0]
prob = res[1]
loop = [pages[i] for i in range(len(loop))]

print(json.dumps(loop))