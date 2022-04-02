use std::result::Result;
// This problem was asked by Google.
//
// Given an undirected graph represented as an adjacency matrix and an integer
// k, write a function to determine whether each vertex in the graph can be
// colored such that no two adjacent vertices share the same color using at
// most k colors. 


fn color_graph(adj: &Vec<Vec<bool>>, num_colors: usize) -> Result<Vec<usize>, Vec<usize>> 
{
    assert!(num_colors > 0);
    let mut colors = vec![0; adj.len()];

    // Assign groups whenever we find a conflict to the current coloring.
    for i in 0..adj.len() {
        for j in 0..adj[i].len() {
            if adj[i][j] && colors[i] == colors[j] {
                colors[j] += 1;
            }
        }
    }

    let colors_needed = colors.iter().max().unwrap() + 1;
    if colors_needed > num_colors {
        Ok(colors)
    } else {
        Err(colors)
    }
}

fn main() {
    let mat: Vec<Vec<bool>> = 
    vec![
        vec![false, true,  false, false, true],
        vec![true,  false, true,  false, false],
        vec![false, true,  false, true,  false],
        vec![false, false, true,  false, true],
        vec![true,  false, false, true,  false]
    ];
    color_graph(&mat, 2);
    color_graph(&mat, 3);
}
