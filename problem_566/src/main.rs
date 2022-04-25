use std::collections::{HashMap, HashSet};

// This problem was asked by Facebook.
//
// A graph is minimally-connected if it is connected and there is no edge that
// can be removed while still leaving the graph connected. For example, any
// binary tree is minimally-connected.
//
// Given an undirected graph, check if the graph is minimally-connected. You
// can choose to represent the graph as either an adjacency matrix or adjacency
// list.

// For an undirected graph, this also implies that there is only one path to
// reach each node. So if a simple D/BFS ever comes upon a node that we have
// seen, then we know that there is a link that can be removed.

type AdjacencyList = HashMap<usize, Vec<usize>>;

fn is_minimially_connected(graph: &AdjacencyList) -> bool {
    let mut seen: HashSet<usize> = HashSet::new();
    fn dfs(node: usize, parent: Option<usize>, graph: &AdjacencyList, seen: &mut HashSet<usize>) -> bool {
        seen.insert(node);
        for &n in graph[&node].iter() {
            if let Some(parent) = parent {
                if n == parent {
                    continue;
                }
            }
            if seen.contains(&n) {
                return false;
            }
            if !dfs(n, Some(node), graph, seen) {
                return false;
            }
        }
        true
    }
    if let Some(&first) = graph.keys().next() {
        let val = dfs(first, None, graph, &mut seen);
        val
    } else {
        true  // A graph with no nodes is minimally connected.
    }
}

fn main() {
    let tree = HashMap::from([
        (0, vec![1, 2]),
        (1, vec![0, 3, 4]),
        (2, vec![0, 5, 6]),
        (3, vec![1, 7, 8]),
        (4, vec![1]),  // Only link to parent
        (5, vec![2]),
        (6, vec![2]),
        (7, vec![3]),
        (8, vec![3]),
    ]);
    assert!(is_minimially_connected(&tree));
    let tree = HashMap::from([
        (0, vec![1, 2]),
        (1, vec![0, 3, 4]),
        (2, vec![0, 5, 6]),
        (3, vec![1, 7, 8]),
        (4, vec![1]),  // Only link to parent
        (5, vec![2]),
        (6, vec![2, 0]),  // Loop
        (7, vec![3]),
        (8, vec![3]),
    ]);
    assert!(!is_minimially_connected(&tree));
}
