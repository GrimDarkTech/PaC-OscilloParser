import collections
from math import *

class ProbabilityTheory:
        
        @staticmethod
        def calculate_mathematical_expectation(values:list[float]) -> float:
            variance = 0.0
            for i in range(0, len(values)):
                variance += values[i]
            variance = variance / len(values)
            return variance
        
        @staticmethod
        def calculate_median(values:list[float]) -> float:
            median = 0.0
            values.sort()
            if(len(values) // 2 == 0):
                median = (values[len(values) // 2]  + values[len(values) // 2 + 1]) / 2
            else:
                median = values[len(values) // 2]
            return median
        
        @staticmethod
        def calculate_variance(values:list[float]) -> float:
            variance = 0.0
            mathematical_expectation = ProbabilityTheory.calculate_mathematical_expectation(values)
            for i in range(0, len(values)):
                    variance += pow((values[i] - mathematical_expectation), 2)
            if(len(values) <= 30):
                variance = variance / (len(values) - 1)
            else:
                 variance = variance / len(values)
            return variance
        
        @staticmethod
        def calculate_square_deviation(values:list[float]) -> float:
            square_deviation = ProbabilityTheory.calculate_variance(values)
            square_deviation = pow(square_deviation, 0.5)
            return square_deviation

        @staticmethod
        def check_for_normal_distribution(values:list[float]) -> float:
            x_square = 0.0
            mathematical_expectation = ProbabilityTheory.calculate_mathematical_expectation(values)
            square_deviation = ProbabilityTheory.calculate_square_deviation(values)
            for i in range(0, len(values)):
                t = (values[i] - mathematical_expectation) / square_deviation
                с = (2 * square_deviation) / (pow(len(values), 0.5))
                frequency_theoretical = (len(values) * с * exp(-(t * t) / 2)) / (square_deviation * pow(2 * pi, 0.5))
                count_frequency = collections.Counter(values) 
                x_square += (count_frequency[values[i]] - frequency_theoretical) / frequency_theoretical
            return x_square