import numpy as np

from src.Open_Close.Logical_Operators import LogicalOp as logOp

class DilateandErode:

    def dilate(self, image, window):
        newimage = np.zeros(image.shape())

        for i in range(0, image.size(0)):
            for j in range(0 , image.size(1)):
                window = [image[i, j-1], image[i, j], image[i, j+1]]
                newimage[i, j] = logOp.logicalOR(self.multiply(window * image(i, j)))

    @classmethod
    def multiply(self,vector, scalar):
        for i in range(len(vector)):
            vector[i] *= scalar
        return vector




