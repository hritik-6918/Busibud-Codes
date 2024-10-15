Searching Challenge

Have the function SearchingChallenge (strArr) take the array of strings stored in strArr, which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix. A contiguous region is one where there is a connected group of 0's going in one or more of four directions: up, down, left, or right. For example: if strArr is ("10111", "10101", "11101", "11111"], then this looks like the following matrix:

10111

10101

11101

11111

For the input above, your program should return 2 because there are two separate contiguous regions of 0's, which create "holes" in the matrix .You can assume the input will not be empty.

Examples

Input: ["01111", "01101", "00011", "11110"]

Output: 3

4

Input: ["1011", "0010"]

Output: 2

My Solution:-

def SearchingChallenge(strArr):
matrix = [list(row) for row in strArr]
rows = len(matrix)
cols = len(matrix[0])

    def dfs(r,c):
      if r<0 or r>=rows or c<0 or c>=cols or matrix[r][c] != '0':
          return

      matrix[r][c] = '1'

      dfs(r+1,c)
      dfs(r-1,c)
      dfs(r,c+1)
      dfs(r,c-1)

    hole_count = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '0':
                dfs(r,c)
                hole_count += 1

    return hole_count

# keep this function call here

print(SearchingChallenge(input()))
