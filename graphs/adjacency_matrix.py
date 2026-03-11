def create_graph(v, edges):
    matrix= [[0 for i in range(v)] for i in range(v)]

    for i in edges:
        u= i[0]
        v= i[1]
        matrix[u][v] = 1

        # matrix[v][u]=1

    return matrix

if __name__ == "__main__":
    v= 3
    edges= [[0,1],[0,2],[1,2]]

    resp= create_graph(v, edges)
    for i in range(v):
        for j in range(v):
            print(resp[i][j],end=" ")
        print()           