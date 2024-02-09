import matplotlib.pyplot as plot
import matplotlib

matplotlib.use('TkAgg')

class DataAnalyzer:
    """Сlass that implements methods for processing arrays of data"""

    @staticmethod
    def extremumsIndexSearch(values: list) -> tuple:
        """Returns tuple of list of local minima indexes and a list of local maxima indexes of float array"""
        maxesIndexes = []
        minsIndexes = []

        #Checking first value of array
        if(values[0] >= values[1]):
            maxesIndexes.append(0)
        else:
            minsIndexes.append(0)

        #Checking last value of array
        if(values[len(values) - 1] >= values[len(values) - 2]):
            maxesIndexes.append(len(values) - 1)
        else:
            minsIndexes.append(len(values) - 1)
        
        #Checking values from 1 to n - 1
        for i in range(1, len(values) - 1):
            if(values[i] >= values[i+1] and values[i] >= values[i-1]):
                maxesIndexes.append(i)
            elif (values[i] <= values[i+1] and values[i] <= values[i-1]):
                minsIndexes.append(i)
        return (minsIndexes, maxesIndexes)
    
    @staticmethod
    def getExtremumsValues(values: list, minsIndexes: list, maxsIndexes: list) -> tuple:
        """Returns tuple of list of minima values and list of maxima values"""
        minsValues = []
        for i in range(0, len(minsIndexes)):
            minsValues.append(values[i])
            maxsValues = []
        for i in range(0, len(maxsIndexes)):
            maxsValues.append(values[i])
        return(minsValues, maxsValues)

    @staticmethod
    def getExtremumsTimes(minsIndexes: list, maxsIndexes: list, timeStep: float, startTime: float) -> tuple:
        """Returns tuple of list of minima times and list of maxima times"""
        minsTimes = []
        for i in range(0, len(minsIndexes)):
            minsTimes.append(startTime + minsIndexes[i] * timeStep)
        maxsTimes = []
        for i in range(0, len(maxsIndexes)):
            maxsTimes.append(startTime + maxsIndexes[i] * timeStep)
        return(minsTimes, maxsTimes)

    @staticmethod
    def drawPlot(dataValues: list, timeStep: float, drawMin: bool, drawMax: bool, **kargs):
        """Draws plot of array of function values with fixed time step"""
        minsIndexes = kargs.get('minsIndexes', [])
        maxesIndexes = kargs.get('maxesIndexes', [])
        showPlot = kargs.get('showPlot', [])
        savePlot = kargs.get('savePlot', [])
        fileName = kargs.get('fileName', [])
        #Calculate time 
        dataTime = []
        for i in range(0, len(dataValues)):
            dataTime.append(i * timeStep)

        #Draw maxima
        if(drawMin):
            plot.plot(dataTime, dataValues, '-b', markevery=minsIndexes, marker=8, markerfacecolor='green', markeredgecolor='green')
        #Draw minima
        if(drawMax):
            plot.plot(dataTime, dataValues, '-b', markevery=maxesIndexes, marker=8, markerfacecolor='red', markeredgecolor='red')
        #Drawing plot
        if(savePlot):
            plot.savefig(f"Plots/{fileName}.pdf")
            print(f"Plot image has been successfully uploaded to Plots/{fileName}.pdf") 
        if(showPlot):
            plot.show()
        
    @staticmethod
    def truncatData(values:list,mathematical_expectation:float,square_deviation:float, timeStep: float) -> tuple:
        """Returns truncated list of values that go beyond the mathematical expectation of the +-square deviation"""
        indexs = []
        for i in range (0, len(values)):
            if values[i] > mathematical_expectation + square_deviation or values[i] < mathematical_expectation - square_deviation:
                indexs.append(i)
        for i in range (0, len(indexs)):
            if indexs[1]-indexs[0] > 5:
                indexs.pop(0)
        cutValues = []
        for i in range (indexs[0], indexs[len(indexs)-1]):
            cutValues.append(values[i])
        startTime = indexs[0] * timeStep
        endTime = indexs[len(indexs)-1] * timeStep
        return (cutValues, startTime, endTime)

