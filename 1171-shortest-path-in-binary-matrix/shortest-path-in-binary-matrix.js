var shortestPathBinaryMatrix = function(grid) {
    let n = grid.length;
    let visited = new Set();
    if (grid[0][0] !== 0 || grid[n - 1][n - 1] !== 0) return -1;
    let queue = [[0, 0, 1]]; // Initialize with starting point and path length

    function isValid(i, j) {
        // Correct the bounds checking and the visited check
        return i >= 0 && j >= 0 && i < n && j < n && !visited.has(i + ',' + j);
    }

    let directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]];

    while (queue.length) {
        let size = queue.length;

        for (let i = 0; i < size; i++) {
            let [x, y, path] = queue.shift();
            if (x === n - 1 && y === n - 1) return path; // Found the end point
            for (let [a, b] of directions) {
                let new_x = a + x;
                let new_y = b + y;

                if (isValid(new_x, new_y) && grid[new_x][new_y] !== 1) {
                    visited.add(new_x + ',' + new_y); // Use new_x and new_y
                    queue.push([new_x, new_y, path + 1]); // Push the new coordinates and updated path length
                }
            }
        }
    }
    return -1; // No path found
};