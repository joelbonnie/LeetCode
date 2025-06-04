class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        if  originalColor == color:
            return image 
        else: 
            image[sr][sc] = color 
            # Modify adjacent pixels: 

            # Up 
            if sr - 1 >= 0 and image[sr - 1][sc] == originalColor:
                image = self.floodFill(image, sr - 1, sc, color)

            # Down 
            if sr + 1 < len(image) and image[sr + 1][sc] == originalColor:
                image = self.floodFill(image, sr + 1, sc, color)

            # Left 
            if sc - 1 >= 0 and image[sr][sc - 1] == originalColor:
                image = self.floodFill(image, sr, sc - 1, color)

            # Right 
            if sc + 1 < len(image[0]) and image[sr][sc + 1] == originalColor:
                image = self.floodFill(image, sr, sc + 1, color)

            return image
