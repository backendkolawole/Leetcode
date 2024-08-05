// declare a stack variable that will be returned which is an empty list initially
// iterate through the asteroids
// if the current asteroid is going left
// if the stack is empty, push the current asteroid to the top of the stack and continue to the next iteration
// while the stack is not empty and the current asteroid is greater than or equal to the element at the top of the stack, pop elements from the stack
// else push the current asteroid to the stack
// return the stack 

var asteroidCollision = function(asteroids) {
    let stack = []

    for (let asteroid of asteroids) {
        if (!stack.length || asteroid > 0) {
            stack.push(asteroid)
            continue
        }

        while (stack.length) {
            peek = stack.at(-1)
            if (peek < 0) {
                stack.push(asteroid)
                break
            }
            else if (peek == -asteroid) {
                stack.pop()
                break
            }
            else if (peek > -asteroid) {
                break
            } 
            else {
                stack.pop()
                if (!stack.length) {
                    stack.push(asteroid)
                    break
                }
            }

        }
        
    }    
    return stack
};