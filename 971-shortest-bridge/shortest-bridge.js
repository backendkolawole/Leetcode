var shortestBridge = function(grid) {
    let directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
    let n = grid.length;

    function isValid(i, j) {
        if (i < 0 || j < 0 || i === n || j === n || visited.has(i + ',' + j)) return false;
        return true;
    }

    let visited = new Set();
    let queue = [];

    function dfs(i, j) {
        if (!isValid(i, j) || grid[i][j] !== 1) return;
        visited.add(i + ',' + j);
        queue.push([i, j]);
        dfs(i - 1, j);
        dfs(i, j + 1);
        dfs(i + 1, j);
        dfs(i, j - 1);
    }

    function bfs() {
        let bridge = 0;
        while (queue.length) {
            let size = queue.length;
            for (let i = 0; i < size; i++) {
                let [x, y] = queue.shift();

                for (let [a, b] of directions) {
                    let newX = x + a;
                    let newY = y + b;
                    if (!isValid(newX, newY)) {
                        continue;
                    }
                    if (grid[newX][newY] === 1) return bridge;
                    queue.push([newX, newY]);
                    visited.add(newX + ',' + newY);
                }
            }
            bridge += 1;
        }
        return -1; // Return -1 if no bridge found (optional)
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            let cell = grid[i][j];

            if (cell === 1) {
                dfs(i, j);
                return bfs();
            }
        }
    }
};