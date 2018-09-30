class Histogram:
    #An array A contains N integers having values between 0 and n-1 (inclusive). The histogram of
    #A is an array H of size n for which the entry i contains the number of occurences of element i in
    #A.
    #My updated approach of the algorithm with O(n) complexity as opposed to O(n^2)

    
    def histogramSolve(self, numberOfElements, uniqueElements, histogramArray):
        storedHistogram = [0] * (uniqueElements + 1)
        for i in range(numberOfElements):
            location = histogramArray[i]
            currentValue = storedHistogram[location]
            updatedValue = currentValue + 1
            storedHistogram[location] = updatedValue
        for y in range(uniqueElements + 1):
            print(storedHistogram[y])
           
            

histogram = Histogram()
histogramArray = [0,1,2,3,3,4,5,5,1,2,3,3,3,3,3,4,5,6,6,7,8,9]
histogram.histogramSolve(len(histogramArray), 9, histogramArray)
