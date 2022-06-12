class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''
        for i, v in enumerate(matrix):
            # print(i)
            for j, v in enumerate(matrix[i]):
                # print(j)
                if matrix[i][j] == target:
                    return True
        '''
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True

        return False
        '''


        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:

            cur = matrix[row][col]

            if target == cur:
                return True
            elif target < cur:
                col -= 1
            elif target > cur:
                row += 1

        return False
