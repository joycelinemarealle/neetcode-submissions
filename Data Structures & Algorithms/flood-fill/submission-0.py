class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        origImage = image[sr][sc]
        #no work needed if same
        if origImage == color:
            return image

        ROWS , COLUMNS = len(image), len(image[0])
        
        def dfs(r,c):
            #base case
            if r < 0 or c < 0 or r == ROWS or c == COLUMNS or image[r][c] != origImage:
                return

            image[r][c] = color #mark it as visited by changing color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image



        
     #store orignal collor
     #check base case , if color equal to ori no wokr needed so return
     #dfs recruved row and col
     #base case out of bonds, or pixel doesnot match 
     #call dfs on all four direction
        

        