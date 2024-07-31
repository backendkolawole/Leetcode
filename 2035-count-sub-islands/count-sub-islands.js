var countSubIslands = function(grid1, grid2) {
    let rows = grid1.length;
    let columns = grid1[0].length;

    let visited = new Set();
    let count = 0;

    function dfs(i, j) {
        if (i < 0 || j < 0 || i === rows || j === columns || grid2[i][j] === 0 || visited.has(`${i},${j}`)) {
            return true;
        }

        // if (visited.has(`${i},${j}`)) {
        //     return true
        // }

        visited.add(`${i},${j}`);

        let isSubIsland = grid1[i][j] === 1;
        isSubIsland = dfs(i - 1, j) && isSubIsland;
        isSubIsland = dfs(i, j + 1) && isSubIsland;
        isSubIsland = dfs(i + 1, j) && isSubIsland;
        isSubIsland = dfs(i, j - 1) && isSubIsland;

        return isSubIsland;
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if (grid2[i][j] === 1 && !visited.has(`${i},${j}`) && dfs(i, j)) {
                count++;
            }
        }
    }

    return count;
};