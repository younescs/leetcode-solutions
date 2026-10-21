
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
            if graph.get(course, []) ==[] or course in safe_list:
                return True
            visited.add(course)
            for neighbor in graph.get(course):
                if not search_for_cycle(neighbor, visited):
                    return False
            safe_list.add(course)
            visited.remove(course)
            graph[course] = []
            return True


        safe_list = set()
        for course in graph:
            if course in safe_list:
                continue
            if not (search_for_cycle(course, set())):
                return False
        
        return True

            
            
        
              



            
