class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseGraph = defaultdict(list)

        for a, b in prerequisites: 
            courseGraph[a].append(b)
        
        UNVISITED = 0 
        VISITING = 1 
        VISITED = 2

        courseStates = [UNVISITED] * numCourses 

        def dfs(courseNum: int): 
            if courseStates[courseNum] == VISITED: return True
            if courseStates[courseNum] == VISITING: return False 
            
            courseStates[courseNum] = VISITING
            prerecs = courseGraph[courseNum]
            for prerec in prerecs: 
                if not dfs(prerec): return False 
            
            courseStates[courseNum] = VISITED
            return True 
        
        for course in range(0, numCourses): 
            if not dfs(course): return False 
        
        return True 
