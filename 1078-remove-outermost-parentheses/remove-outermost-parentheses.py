# declare a variable count with initial value 0
# declare a variable flag with initial value true
# iterate through string s
# if the current char is equal to an opening string increment count
# else if the current char is equal to a closing string decrement count
# if count is equal to 1 and the flag is true
# set the flag equal to false and continue
# else add the current char to the result string
# else if the count is equal to 0 and flag is false
# set the flag to true and continue
# else add the char to result string

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0
        flag = True

        for char in s:
            if char == "(":
                count +=1
            elif char == ")":
                count -=1

            if count == 1 and flag:
                flag = False
                continue
            elif count == 0 and not flag:
                flag = True
                continue
            result += char
        
        return result
