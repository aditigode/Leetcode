class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search for row
        def binarySearchRow(target, low, high):
            while high >= low:
                mid = (low + high) // 2
                #print(mid,low,high)

                if matrix[mid][0] > target:
                    high = mid - 1
                elif matrix[mid][len(matrix[0])-1] < target:
                    low = mid + 1
                else:
                    return mid
            return -1

        row = binarySearchRow(target, 0, len(matrix)-1)
        print(row)
        if row == -1:
            return False
        
        #binary search for column
        def binary_search(target,low,high,row):
            while high >= low:
                
                mid = (low+ high) //2
                #print(mid,low, high, row)
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return False

        return binary_search(target, 0, len(matrix[0])-1, row)

        