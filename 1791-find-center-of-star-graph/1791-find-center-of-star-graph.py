class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes_dict = {}
        for edge1, edge2 in edges:
            if edge1 not in nodes_dict:
                nodes_dict[edge1] = 1
            else:
                nodes_dict[edge1] += 1
            if edge2  not in nodes_dict:
                nodes_dict[edge2] = 1
            else:
                nodes_dict[edge2] += 1
                
        center = math.inf
        maxVal = -math.inf
        #print(nodes_dict)
        for key,value in nodes_dict.items():
            if value > maxVal:
                center = key
                maxVal = value
        return center
                
        