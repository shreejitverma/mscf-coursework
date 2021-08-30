
# breadth_first_search.py
# Author(s): Shreejit Verma (shreejiv@andrew.cmu.edu), YingTu(yingt@andrew.cmu.edu)
# Date: 08/13/2021

# 2.a (function definition)
def BFS(G, root, target):
    """
      def BFS(G, root, target): # Pythonish pseudocode
         S.add(root)
         T.add(root, None)      # value, parent
         Q = [root]
         while Q:
            cur = Q.pop(0)
            if cur is target:
               return cur parent list
            for v in G[cur]:
               if v not in S:
                  S.add(v)
                  T.add(v, cur)
                  Q += [v]
      """
    S = {root}
    T = {root: None}
    Q = [root]
    while Q:
        cur = Q.pop(0)
        if cur == target:
            result = [cur]
            while T[cur]:
                result = [T[cur]] + result
                cur = T[cur]
            return result
        for v in G[cur]:
            if v not in S:
                S.add(v)
                T[v] = cur
                Q += [v]

        # 2.c (function definitions)


def _BFS_con_comps(G, root):
    S = []
    Q = [root]

    while Q:
        node = Q.pop(0)
        if node not in S:
            S.append(node)
            neighbours = G[node]

            for neighbour in neighbours:
                Q.append(neighbour)
    return S


def BFS_con_comps(G):
    # return a list of connected components in G,
    # where each connected component is a sorted
    # list of nodes
    result = []
    S = []
    for k, v in G.items():
        if k not in S:
            S = list(set(S + _BFS_con_comps(G, k)))
            result += [_BFS_con_comps(G, k)]
    return result


def print_con_comps(G_cc):
    # display connected components
    print('graph contains', len(G_cc), 'connected components:')
    for i in range(len(G_cc)):
        print(f"{i+1}: {G_cc[i]}")

def main():
    # 2.a (test code)
    G = {'A': ['B', 'J', 'Me'],
         'B': ['A'],
         'C': ['D', 'P'],
         'D': ['C', 'O'],
         'E': ['F', 'J', 'K'],
         'F': ['E', 'M'],
         'G': ['K', 'S', 'Ed'],
         'H': ['O', 'U'],
         'Me': ['A', 'I', 'N', 'V'],
         'I': ['Me', 'Q'],
         'J': ['A', 'E', 'L', 'Q', 'W'],
         'K': ['E', 'G'],
         'L': ['J', 'W'],
         'M': ['E', 'S', 'T'],
         'N': ['Me', 'V'],
         'O': ['H', 'D'],
         'P': ['C', 'U'],
         'Q': ['I', 'J', 'X', 'Y'],
         'R': ['Ed'],
         'S': ['G', 'M', 'Y', 'Z'],
         'T': ['M'],
         'U': ['H', 'P'],
         'V': ['Me', 'N'],
         'W': ['J', 'L'],
         'X': ['Q', 'Y'],
         'Y': ['Q', 'S', 'X', 'Z'],
         'Ed': ['G', 'R', 'Z'],
         'Z': ['S', 'Y', 'Ed']}
    print('Shortest path from Me to Ed:', BFS(G, 'Me', 'Ed'))

    # 2.b (test code)
    print('Shortest path from A to I:  ', BFS(G, 'A', 'I'))
    print('Shortest path from B to R:  ', BFS(G, 'B', 'R'))
    print('Shortest path from C to H:  ', BFS(G, 'C', 'H'))
    print('Shortest path from M to T:  ', BFS(G, 'M', 'T'))

    # 2.c (test code)

    # connected components tests:
    G2 = {'A': ['B', 'C'],
          'C': ['A'],
          'E': ['F'],
          'D': [],
          'B': ['A'],
          'F': ['E']}
    G2_cc = BFS_con_comps(G2)
    print_con_comps(G2_cc)
    G_cc = BFS_con_comps(G)
    print_con_comps(G_cc)


if __name__ == '__main__':
    main()
