from fileParser import FileParser
from probabilityTheory import ProbabilityTheory
from dataAnalyser import DataAnalyzer
from excelManager import ExcelManager

print("Enter the number of files to analyze:")
filesNumber = int(input())

print("Show graphs for each file? (y/n)")
isShowPlot = input()
if(isShowPlot.lower() == "y"):
        isShowPlot = True
else:
    isShowPlot = False
print("Save graphs for each file? (y/n)")
isSavePlot = input()
if(isSavePlot.lower() == "y"):
    isSavePlot = True
else:
    isSavePlot = False

for i in range(0, filesNumber):

    fileInfo = FileParser.Parse(i)

    values = fileInfo[0]
    timeStep = fileInfo[1]

    mathematical_expectation = ProbabilityTheory.calculate_mathematical_expectation(values)
    square_deviation = ProbabilityTheory.calculate_square_deviation(values)

    truncateValues = DataAnalyzer.truncatData(values, mathematical_expectation, square_deviation, timeStep)
    
    values = truncateValues[0]
    startTime = truncateValues[1]
    endTime = truncateValues[2]

    extremumsIndexes = DataAnalyzer.extremumsIndexSearch(values)
    minsIndexes = extremumsIndexes[0]
    maxIndexes = extremumsIndexes[1]
    
    minmax = DataAnalyzer.getExtremumsValues(values, minsIndexes, maxIndexes)
    minsValues = minmax[0]
    maxsValues = minmax[1]
    
    minmaxTimes = DataAnalyzer.getExtremumsTimes(minsIndexes, maxIndexes, timeStep, startTime)
    minsTimes = minmaxTimes[0]
    maxsTimes = minmaxTimes[1]

    DataAnalyzer.drawPlot(values, timeStep, drawMin=True, drawMax=True, minsIndexes=minsIndexes, maxesIndexes=maxIndexes, showPlot = isShowPlot, savePlot = isSavePlot, fileName = f"Plot{i}")
    
    wb = ExcelManager.CreateBook(f"Result{i}")
    ExcelManager.write_to_excel(f"Result{i}", "Математическое ожидание", [mathematical_expectation], 1)
    ExcelManager.write_to_excel(f"Result{i}", "Среднеквадратическое отклонение", [square_deviation], 2)
    ExcelManager.write_to_excel(f"Result{i}", "Время начала переходного процесса", [startTime], 3)
    ExcelManager.write_to_excel(f"Result{i}", "Время окончания переходного процесса", [endTime], 4)
    ExcelManager.write_to_excel(f"Result{i}", "Длительность переходного процесса", [endTime - startTime], 5)
    ExcelManager.write_to_excel(f"Result{i}", "Локальные минимумы процесса", minsValues, 6)
    ExcelManager.write_to_excel(f"Result{i}", "Время локальных минимумов процесса", minsTimes, 7)
    ExcelManager.write_to_excel(f"Result{i}", "Локальные максимумы процесса", maxsValues, 8)
    ExcelManager.write_to_excel(f"Result{i}", "Время локальных максимумов процесса", maxsTimes, 9)
    print(f"Data has been successfully uploaded to Excels/Result{i}.xlsx") 

input("Press Enter to exit")