def tsp_dfs(graph, start, visited, curr_cost, n):
    global nodes_visited_dfs, original_start
    if len(visited) == n:
        nodes_visited_dfs += 1
        return curr_cost + graph[start][original_start]
    min_dist = float("inf")
    for i in range(n):
        if i not in visited:
            visited.add(i)
            new_cost = curr_cost + graph[start][i]
            dist = tsp_dfs(graph, i, visited, new_cost, n)
            if dist < min_dist:
                min_dist = dist
            visited.remove(i)

    return min_dist


def tsp_dfs_pruning(graph, start, visited, curr_cost, n, curr_b_cost):
    global nodes_visited_pruning, original_start
    if curr_cost > curr_b_cost:
        return curr_b_cost
    if len(visited) == n:
        nodes_visited_pruning += 1
        return curr_cost + graph[start][original_start]
    min_dist = float("inf")
    for i in range(n):
        if i not in visited:
            visited.add(i)
            new_cost = curr_cost + graph[start][i]
            dist = curr_b_cost = tsp_dfs_pruning(graph, i, visited, new_cost, n, curr_b_cost)
            if dist < min_dist:
                min_dist = dist
            visited.remove(i)

    return min_dist


if __name__ == '__main__':
    graph = [[0, 400, 15, 20],
             [400, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    original_start = 2
    nodes_visited_dfs = 0
    nodes_visited_pruning = 0
    visited = set([original_start])
    curr_cost = 0
    n = 4
    visit = [False] * n
    curr_b_cost = 9999
    print(tsp_dfs_pruning(graph, original_start, visited, curr_cost, n, curr_b_cost))
    print(tsp_dfs(graph, original_start, visited, curr_cost, n))
    print(nodes_visited_dfs)
    print(nodes_visited_pruning)
