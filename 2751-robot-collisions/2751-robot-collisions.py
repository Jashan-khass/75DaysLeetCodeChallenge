class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots.sort()
        
        stack = []
        healths = list(healths)
        
        for pos, h, d, i in robots:
            if d == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack[-1]
                    if healths[j] < healths[i]:
                        healths[j] = 0
                        healths[i] -= 1
                        stack.pop()
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                        break
                    else:
                        healths[j] = 0
                        healths[i] = 0
                        stack.pop()
                        break
        
        result = []
        for i in range(len(positions)):
            if healths[i] > 0:
                result.append(healths[i])
        
        return result


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"))
    print(sol.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"))
    print(sol.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"))