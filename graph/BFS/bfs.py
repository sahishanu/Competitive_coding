#Building graph using Adjecency list

class graph:
	def __init__(self):
		self.g=dict()
	def addedge(self,v,u):
		try:
			self.g[v].append(u)
		except:
			self.g[v]=[u]
		try:
			self.g[u].append(v)
		except:
			self.g[u]=[v]
	def __str__(self):
		return(str(self.g))
g=graph()
g.addedge(1,2)
g.addedge(2,3)
g.addedge(5,4)
g.addedge(1,5)
g.addedge(5,3)

print(g)

# BFS treversal in graph from v to all the nodes


def bfs_all(g,v,visited,dist):
	print("inside bfs_all")
	q=[]
	print(v,end=" ")
	visited[v]=True
	dist[v]=0
	for i in g[v]:
		dist[i]=1
		q.append(i)
	while(len(q)!=0):
		x=q.pop(0)
		if(not(visited[x])):
			print(x,end=" ")
			visited[x]=True
			for u in g[x]:
				if(not visited[u]):
					q.append(u)
					dist[u]=dist[x]+1
	print("")



visited=[False for i in range(6)]
dist=["" for i in range(6)]


gp=g.g


bfs_all(gp,1,visited,dist)
print("distance of each node :")
print(dist)



