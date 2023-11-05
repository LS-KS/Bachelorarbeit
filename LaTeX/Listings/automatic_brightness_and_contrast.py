    def _automatic_brightness_and_contrast(self,image,  clip_hist_percent):
        """
        Private method. 
        Automatic brightness and contrast optimization with
        (optional) histogram clipping.
        First calculates Histogram of submitted image. 
        Then calculates cumulative distribution of histogram.
        Then calculates left and right cut of histogram based
        on submitted clip_hist_percent and cumulative 
        distribution.
        Then calculates alpha and beta values for 
        cv2.convertScaleAbs() function.
        Finally calculates new histogram with desired range 
        and shows histogram.
        If an error occurs, the submitted image without 
        adjustment is returned.
        :param image: input image
        :type image: grayscale image
        :param clip_hist_percent: percent of histogram to clip
        :type clip_hist_percent: float
        """

        # Calculate grayscale histogram
        hist = cv2.calcHist(image, [0], None, [256], [0,256])
        hist_size = len(hist)

        # Calculate cumulativ distribution from the histogram
        # It is calculated by summing all values from the 
        # beginning up to the current index
        accumulator = []
        accumulator.append(float(hist[0]))
        for index in range(1, hist_size):
            accumulator.append(accumulator[index-1]+float(hist[index]))

        # Locate points to clip
        maximum = accumulator[-1]
        clip_hist_percent *= (maximum/100)/2

        # Locate left cut
        minimum_gray = 0

        while accumulator[minimum_gray] < clip_hist_percent:
            minimum_gray +=1

        # Locate right cut
        maximum_gray = hist_size-1
        while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
            maximum_gray -= 1

        # Calculate alpha and beta values
        if maximum_gray -minimum_gray !=0:
            alpha = 255/(maximum_gray - minimum_gray)
            beta = -minimum_gray * alpha
            img = cv2.convertScaleAbs(image, alpha= alpha, beta=beta)
            cv2.imwrite("processed_before_detection.png", img)
            return img
        else:
            if self.eventlogService is not None:
                self.eventlogService.writeEvent(
                    "Stocktaker._automatic_brightness_and_contrast", 
                    "Error while calculating alpha and beta values." 
                    +"Image is not adjusted."
                    )
            return image