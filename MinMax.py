import matplotlib.pyplot as plot
import matplotlib

matplotlib.use('TkAgg')

#serachs extremums values
def extremumsSearch(dataY, timeStep, drawPlot):

    extMaxesIndexes = [0]
    extMinsIndexes = [0]

    if(dataY[0]>=dataY[1]):
        extMaxesIndexes.append(0)
    else:
        extMinsIndexes.append(0)
    
    if(dataY[len(dataY) - 1]>=dataY[len(dataY) - 2]):
        extMaxesIndexes.append(len(dataY) - 1)
    else:
        extMinsIndexes.append(len(dataY) - 1)
    
    for i in range(1, len(dataY) - 1):
        if(dataY[i] >= dataY[i+1] and dataY[i] >= dataY[i-1]):
            extMaxesIndexes.append(i)
        elif (dataY[i] <= dataY[i+1] and dataY[i] <= dataY[i-1]):
            extMinsIndexes.append(i)

    print('-----------Максимумы------------------')
    for i in extMaxesIndexes:
        print(dataY[i])

    print()
    print('--------------------------------------')

    print('-----------Минимумы-----------------')
    for i in extMinsIndexes:
        print(dataY[i])

    print()
    print('------------------------------------')

    print("Количество максимумов")
    print(len(extMaxesIndexes))
    print("Количество минимумов")
    print(len(extMinsIndexes))

    if(drawPlot):
        dataT = []
        for i in range(0, len(dataY)):
            dataT.append(i * timeStep)


        plot.plot(dataT, dataY, '-b', markevery=extMinsIndexes, marker=8, markerfacecolor='green', markeredgecolor='green')
        plot.plot(dataT, dataY, '-b', markevery=extMaxesIndexes, marker=8, markerfacecolor='red', markeredgecolor='red')
        plot.show()

