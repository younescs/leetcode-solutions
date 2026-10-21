
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        num_preq = len(prerequisites)
        if num_preq == 0:
            return True

        graph = dict()
        for course, prereq in prerequisites:
            if course in graph:
                graph[course].append(prereq)
            else:
                graph[course] = [prereq]
        print(graph)

        def search_for_cycle(course, visited):
            if course in visited:
                return False
            if graph.get(course, []) ==[]:
                return True
            visited.add(course)
            for neighbor in graph.get(course):
                if not search_for_cycle(neighbor, visited):
                    return False
            visited.remove(course)
            graph[course] = []
            return True


        for course in graph:
            if not (search_for_cycle(course, set())):
                return False
        
        return True

            
            
        
              



            
