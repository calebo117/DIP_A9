import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256

        row, col = image.shape

        for i in range(row):
            for j in range(col):
                hist[image[i][j]] += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0

        mid = len(hist)/2

        # Add up first half total
        total_1 = 0
        for i in range(int(mid)):
            if hist[i] != 0:
                total_1 += hist[i]

        # Add up second half total
        total_2 = 0
        for i in range(int(mid), int(len(hist))):
            if hist[i] != 0:
                total_2 += hist[i]

        threshold_1 = 0
        for i in range(int(mid)):
            if hist[i] != 0:
                probability_1 = hist[i] / total_1
                probDist_1 = i * probability_1
                threshold_1 += probDist_1

        threshold_2 = 0

        for i in range(int(mid), int(len(hist))):
            if hist[i] != 0:
                probability_2 = hist[i] / total_2
                probDist_2 = i * probability_2
                threshold_2 += probDist_2

        threshold = (threshold_1 + threshold_2) / 2

        return threshold

    def binarize(self, image):
        """Computes the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        row, col = bin_img.shape
        threshold = self.find_optimal_threshold(self.compute_histogram(image))

        for i in range(row):
            for j in range(col):
                if bin_img[i][j] > threshold:
                    bin_img[i][j] = 255
                else:
                    bin_img[i][j] = 0

        return bin_img


