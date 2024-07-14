# 인접리스트

graph = [[] for _ in range(3)]
print(graph)

graph[0] = [(0, 7), (1, 5)]  # (note, edge)
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)
