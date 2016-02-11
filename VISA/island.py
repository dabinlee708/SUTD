def isSafe(M,row,col,ROW,COL,visited):
	return (col >= 0) and (col < COL) and (row >= 0) and (row < ROW) and M[row][col]==1 and (False==visited[row][col])
def dfs(M,row,col, ROW, COL, visited):
	travelR=[-1,-1,-1,0,0,1,1,1]
	travelC=[-1,0,1,-1,1,-1,0,1]
	visited[row][col]=True
	for i in range(8):
		if (isSafe(M, row + travelR[i], col + travelC[i], ROW, COL, visited)):
			dfs(M, row + travelR[i], col + travelC[i], ROW, COL, visited)
def islandCount(m, ROW, COL, visited):
	count = 0
	for a in range(ROW):
		for b in range(COL):
			if ((m[a][b]) == 1) and False==visited[a][b]:
				dfs(m,a,b, ROW, COL, visited)
				count+=1
	return count
def solver(c):
	ROW=len(c)
	COL=len(c[0])
	visited=[]
	for i in range(ROW):
		visited.append([])
		for j in range(COL):
			visited[i].append(False)
	print "Islands: ",islandCount(c, ROW, COL, visited)

m=	[	
	[1,1,0,0,0],
	[0,1,0,0,1],
	[1,0,0,1,1],
	[0,0,0,0,0],
	[1,0,1,0,1]
	]
solver(m)