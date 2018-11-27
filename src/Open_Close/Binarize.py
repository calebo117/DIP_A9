import numpy as np


class Binarize:

    def calculateExpectedValue(self, start, end, hist):
        total = 0
        expect_val = 0
        for i in range(start, end):
            total += hist[i]
        for i in range(start, end):
            expect_val += (i + 1) * (hist[i] / total)
        return expect_val

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        hist = [0]*256
        w = np.size(image,0)
        h = np.size(image,1)

        for i in range(w):
            for j in range(h):
                I = image[i, j]
                hist[I] += 1
        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        threshold = len(hist)/2
        expect_val1 = float(0)
        expect_val2 = float(0)

        while True:
            temp1 = self.calculateExpectedValue(0, int(threshold), hist)
            temp2 = self.calculateExpectedValue(int(threshold), len(hist), hist)
            if (expect_val1 == temp1) & (expect_val2 == temp2):
                break
            expect_val1 = temp1
            expect_val2 = temp2
            threshold = (expect_val1+expect_val2)/2
        print(threshold)
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        bin_img = image.copy()
        hist = self.compute_histogram(bin_img)
        threshold = self.find_optimal_threshold(hist)
        h = np.size(bin_img, 0)
        w = np.size(bin_img, 1)
        for i in range(h):
            for j in range(w):
                if bin_img[i,j] >= threshold:
                    bin_img[i,j] = 255#white
                else:
                    bin_img[i,j] = 1 #black
        return bin_img


