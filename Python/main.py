from FileParserPy import FileParser
from probabilityTheory import ProbabilityTheory
from MinMax import DataAnalyzer
from CutGrapf import Cut

for i in range(0, 2):

    fileInfo = FileParser.Parse(i)

    values = fileInfo[0]
    timeStep = fileInfo[1]

    mathematical_expectation = ProbabilityTheory.calculate_mathematical_expectation(values)
    square_deviation = ProbabilityTheory.calculate_square_deviation(values)

    cutValues = Cut(values,mathematical_expectation,square_deviation)

    extremumsIndexes = DataAnalyzer.extremumsIndexSearch(cutValues)
    minsIndexes = extremumsIndexes[0]
    maxIndexes = extremumsIndexes[1]

    DataAnalyzer.drawPlot(cutValues, timeStep, drawMin=True, drawMax=True, minsIndexes=minsIndexes, maxesIndexes=maxIndexes)

    print(f'Математическое ожидание: {mathematical_expectation}')
    print(f'Среднеквадратическое отклонение: {square_deviation}')
    
input("Нажмите Enter для выхода")