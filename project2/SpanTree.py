
def SpanTree(N):
    edge_left = GetEdge()
    edges_in_tree = { }
    chosen_edges = []
    for i in range(1, N-1):
        k = GetShortestEdge(edge_left)
        edge_left.del(k)
        if !((k.first in edges_in_tree) and (k.second in edges_in_tree)):
            chosen_edges.append(k)
