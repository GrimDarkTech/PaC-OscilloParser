import matplotlib.pyplot as plot
import matplotlib

matplotlib.use('TkAgg')

class DataAnalyzer:
    """Сlass that implements methods for processing arrays of data"""

    @staticmethod
    def extremumsIndexSearch(values: list) -> tuple:
        """Returns tuple of list of local minima indexes and a list of local maxima indexes of float array"""
        maxesIndexes = [0]
        minsIndexes = [0]

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
    def drawPlot(dataValues: list, timeStep: float, drawMin: bool, drawMax: bool, **kargs):
        """Draws plot of array of function values with fixed time step"""
        minsIndexes = kargs.get('minsIndexes', [])
        maxesIndexes = kargs.get('maxesIndexes', [])
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
        plot.show()

