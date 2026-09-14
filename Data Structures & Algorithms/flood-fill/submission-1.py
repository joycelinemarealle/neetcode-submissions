class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #store original color first
        origImage = image[sr][sc]

        #do nothing if color same
        if image[sr][sc] == color:
                return image
        
        def dfs(r, c):
            ROWS, COLUMNS = len(image), len(image[0])

            #base case 
            if (r < 0 or c < 0 or r == ROWS or c == COLUMNS or  image[r][c] != origImage)  :
                return
            #changing color is how we keep track if visited
            image[r][c] = color

            #recursive
            dfs( r + 1 , c)
            dfs( r - 1 , c)
            dfs( r, c + 1 )
            dfs( r, c - 1)
            
        dfs( sr, sc)
        return image




            
           

        #store original image color
        #if color at sr,sc is same do nothing no need to chang3 return
        #if not then need to check out of bounds <0, max grid or color not match orig
        #move recursively r+1, r-1, c+1, c-1
        #modify color Image[sr][sc] = color
        #return image after fille