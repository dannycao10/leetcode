class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1
        row = 0
        
        while lr <= rr:
            mid = (rr + lr) // 2
            if target < matrix[mid][0]:
                rr = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                lr = mid + 1
            else:
                row = mid
                break

        if not lr <= rr:
            return False

        lc, rc = 0, len(matrix[0]) - 1
        while lc <= rc:
            mid = (rc + lc) // 2
            if target < matrix[row][mid]:
                rc = mid - 1
            elif target > matrix[row][mid]:
                lc = mid + 1
            else:
                return True

        return False

        # Empty array with no rows or cols
        # Single row multiple col (false, true)
        # Single col mulitple rows (false, true)
        # 4 x 4 with a true result
        # 4 x 4 with false result

                