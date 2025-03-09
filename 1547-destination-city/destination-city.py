class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start =[paths[i][0] for i in range(len(paths))]
        destination =[paths[i][1] for i in range (len (paths))]
        for i in range(len(paths)):
            if (paths[i][1] not in start):
                return paths[i][1]
        return "Sam"
