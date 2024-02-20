from fileParser import FileParser
from probabilityTheory import ProbabilityTheory
from dataAnalyser import DataAnalyzer
from excelManager import ExcelManager
from threadsManager import ThreadManager

dataForPlots = []

def AnalyzeFiles(file_number):
    
    #Reading data from CSV file
    file_info = FileParser.parse(file_number)

    values = file_info[0]
    time_step = file_info[1]

    #Calculating mathematical expectation and square_deviation for data
    mathematical_expectation = ProbabilityTheory.calculate_mathematical_expectation(values)
    square_deviation = ProbabilityTheory.calculate_square_deviation(values)

    #Truncating data to async event
    truncate_values = DataAnalyzer.truncat_data(values, mathematical_expectation, square_deviation, time_step)
    
    values = truncate_values[0]
    start_time = truncate_values[1]
    end_time = truncate_values[2]

    #Searching for extremum indexes
    extremums_indexes = DataAnalyzer.extremums_index_search(values)
    mins_indexes = extremums_indexes[0]
    maxes_indexes = extremums_indexes[1]

    #Getting extremum values
    minmax = DataAnalyzer.get_extremums_values(values, mins_indexes, maxes_indexes)
    mins_values = minmax[0]
    maxs_values = minmax[1]
    
    #Getting time argument values for extremum values
    minmaxTimes = DataAnalyzer.get_extremums_times(mins_indexes, maxes_indexes, time_step, start_time)
    minsTimes = minmaxTimes[0]
    maxsTimes = minmaxTimes[1]

    #Saving data to draw plots
    dataForPlots.append((values, time_step, mins_indexes, maxes_indexes, f"Plot{file_number}"))

    #Writing result  with excel table
    wb = ExcelManager.create_book(f"Result{file_number}")
    ExcelManager.write_to_excel(f"Result{file_number}", "Математическое ожидание", [mathematical_expectation], 1)
    ExcelManager.write_to_excel(f"Result{file_number}", "Среднеквадратическое отклонение", [square_deviation], 2)
    ExcelManager.write_to_excel(f"Result{file_number}", "Время начала переходного процесса", [start_time], 3)
    ExcelManager.write_to_excel(f"Result{file_number}", "Время окончания переходного процесса", [end_time], 4)
    ExcelManager.write_to_excel(f"Result{file_number}", "Длительность переходного процесса", [end_time - start_time], 5)
    ExcelManager.write_to_excel(f"Result{file_number}", "Локальные минимумы процесса", mins_values, 6)
    ExcelManager.write_to_excel(f"Result{file_number}", "Время локальных минимумов процесса", minsTimes, 7)
    ExcelManager.write_to_excel(f"Result{file_number}", "Локальные максимумы процесса", maxs_values, 8)
    ExcelManager.write_to_excel(f"Result{file_number}", "Время локальных максимумов процесса", maxsTimes, 9)
    print(f"Data has been successfully uploaded to Excels/Result{file_number}.xlsx") 

#Entry point

def main():

    print("Enter the number of files to analyze:")
    number_of_files = int(input())

    print("Show graphs for each file? (y/n)")
    is_show_plot = input()
    if(is_show_plot.lower() == "y"):
            DataAnalyzer.set_plot_backend("TkAgg")
            is_show_plot = True
    else:
        is_show_plot = False
        
    print("Save graphs for each file? (y/n)")
    is_save_plot = input()
    if(is_save_plot.lower() == "y"):
        is_save_plot = True
    else:
        is_save_plot = False
    
    
    for i in range(0, number_of_files):
        ThreadManager.create_thread(AnalyzeFiles, file_number = i)
        
    ThreadManager.start_threads()

    ThreadManager.wait_for_threads()

    for plot in dataForPlots:
        DataAnalyzer.draw_plot(plot[0], time_step = plot[1], mins_indexes=plot[2], maxes_indexes=plot[3], is_show_plot=is_show_plot, is_save_plot=is_save_plot, file_name=plot[4])
        

    input("Press Enter to exit")

if __name__ == "__main__":
    main()