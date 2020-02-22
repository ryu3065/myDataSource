graph = {}
graph['a'] = {}
graph['a']['b'] = 5
graph['a']['c'] = 2
graph['b'] = {}
graph['b']['d'] = 4
graph['b']['e'] = 2
graph['c'] = {}
graph['c']['b'] = 8
graph['c']['e'] = 7
graph['d'] = {}
graph['d']['fin'] = 3
graph['d']['e'] = 6
graph['e'] = {}
graph['e']['fin'] = 1
graph['fin'] = {}

print(graph)

parents = {}
parents['b'] = 'a'
parents['c'] = 'a'
parents['d'] = None
parents['e'] = None
parents['fin'] = None

print(parents)

costs = {}
costs['b'] = 5
costs['c'] = 2
costs['d'] = float('inf')
costs['e'] = float('inf')
costs['fin'] = float('inf')

print(costs)

visited = []
how = []

def low_cost_node(costs):
  lowCost = float('inf')
  lowCostNode = None
  for i in costs:
    print("i :",i)
    print("visited :", visited)
    #cost = costs[i]
    if lowCost > costs[i] and i not in visited:
      lowCost = costs[i]
      lowCostNode = i
  print("lowCostNode :", lowCostNode)
  return lowCostNode

def dijkstra(graph, parents, costs):
  node = low_cost_node(costs)
  print("node: ", node)
  while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    print("neighbors : ", neighbors)

    for n in neighbors.keys():
      new_cost = cost + neighbors[n]
      if costs[n] > new_cost:
        costs[n] = new_cost
        parents[n] = node
        how.append(node)
    visited.append(node)
    node = low_cost_node(costs)
  return print("result :", costs)

dijkstra(graph,parents,costs)

