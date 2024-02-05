from FileParserPy import FileParser
from probabilityTheory import ProbabilityTheory
from MinMax import extremumsSearch

for i in range(0, 1):

    fileInfo = FileParser.Parse(i)

    values = fileInfo[0]
    timeStep = fileInfo[1]

    mat_ojid = ProbabilityTheory.calculate_mathematical_expectation(values)
    sred_qvad_otkl = ProbabilityTheory.calculate_square_deviation(values)

    extremumsSearch(values, timeStep, False)

    print(f'Математическое ожидание: {mat_ojid}')
    print(f'Среднеквадратическое отклонение: {sred_qvad_otkl}')
    
input("Нажмите Enter для выхода")