class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        print(prerequisites)

        # get all prerequisites for each course
        preMap = { i : [] for i in range(numCourses) }
        for course, pre in prerequisites:
            preMap[course].append(pre)

        print(preMap)

        # this is actually a stack. dfs uses a stack / bfs uses a queue
        # visitSet = set()
        visitSet = []
        def dfs(course):
            # loop, exit
            if course in visitSet:
                return False
            # no prereq for course
            if preMap[course] == []:
                return True

            # visitSet.add(course)
            visitSet.append(course)
            # if course has prereqs we can't do, return false
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            # visitSet.remove(course)
            visitSet.pop()

            # set its prereq to an empty list because we can take course
            preMap[course] = []

            return True

        # check if all courses can be completed
        # loop required because the nodes might not be connected and dfs won't work
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
