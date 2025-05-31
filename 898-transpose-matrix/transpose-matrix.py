import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(sam) for sam in zip(*matrix)]