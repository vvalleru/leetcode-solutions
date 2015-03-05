class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        result = [[0]*n for x in xrange(n)]

        left_margin = top_margin = 0
        right_margin = bottom_margin = n - 1
        current_elem = 1
    
        while left_margin <= right_margin:
            current_row_index = top_margin
            current_col_index = left_margin
            while current_col_index <= right_margin:
                result[current_row_index][current_col_index] = current_elem
                current_elem += 1
                current_col_index += 1
                
            current_col_index -= 1
            current_row_index += 1
            while current_row_index <= bottom_margin:
                result[current_row_index][current_col_index] = current_elem
                current_elem += 1
                current_row_index += 1
                
            current_col_index -= 1
            current_row_index -= 1
            while current_col_index >= left_margin:
                result[current_row_index][current_col_index] = current_elem
                current_elem += 1
                current_col_index -= 1
                
            current_col_index += 1
            current_row_index -= 1
            while current_row_index > top_margin:
                result[current_row_index][current_col_index] = current_elem
                current_elem += 1
                current_row_index -= 1
                
            top_margin += 1
            bottom_margin -= 1
            left_margin += 1
            right_margin -= 1
        return result