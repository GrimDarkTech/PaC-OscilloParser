import matplotlib.pyplot as plot
import matplotlib


class DataAnalyzer:
    """Сlass that implements methods for processing arrays of data"""

    @staticmethod
    def extremums_index_search(values: list) -> tuple:
        """Returns tuple of list of local minima indexes and a list of local maxima indexes of float array"""
        maxes_indexes = []
        mins_indexes = []

        #Checking first value of array
        if(values[0] >= values[1]):
            maxes_indexes.append(0)
        else:
            mins_indexes.append(0)

        #Checking last value of array
        if(values[len(values) - 1] >= values[len(values) - 2]):
            maxes_indexes.append(len(values) - 1)
        else:
            mins_indexes.append(len(values) - 1)
        
        #Checking values from 1 to n - 1
        for i in range(1, len(values) - 1):
            if(values[i] >= values[i+1] and values[i] >= values[i-1]):
                maxes_indexes.append(i)
            elif (values[i] <= values[i+1] and values[i] <= values[i-1]):
                mins_indexes.append(i)
        return (mins_indexes, maxes_indexes)
    
    @staticmethod
    def get_extremums_values(values: list, mins_indexes: list, maxs_indexes: list) -> tuple:
        """Returns tuple of list of minima values and list of maxima values"""
        mins_values = []
        for i in range(0, len(mins_indexes)):
            mins_values.append(values[i])

            maxs_values = []
        for i in range(0, len(maxs_indexes)):
            maxs_values.append(values[i])

        return(mins_values, maxs_values)

    @staticmethod
    def get_extremums_times(mins_indexes: list, maxs_indexes: list, time_step: float, start_time: float) -> tuple:
        """Returns tuple of list of minima times and list of maxima times"""
        mins_times = []
        for i in range(0, len(mins_indexes)):
            mins_times.append(start_time + mins_indexes[i] * time_step)

        maxs_times = []
        for i in range(0, len(maxs_indexes)):
            maxs_times.append(start_time + maxs_indexes[i] * time_step)

        return(mins_times, maxs_times)
    
    @staticmethod
    def set_plot_backend(backend_name: str):
        matplotlib.use(backend_name)

    @staticmethod
    def draw_plot(data_values: list, time_step: float, **kargs):
        """Draws plot of array of function values with fixed time step"""
        mins_indexes = kargs.get('mins_indexes', [])
        maxes_indexes = kargs.get('maxes_indexes', [])
        is_show_plot = kargs.get('is_show_plot', False)
        is_save_plot = kargs.get('is_save_plot', False)
        file_name = kargs.get('file_name', "0")

        #Calculate time 
        data_time = []
        for i in range(0, len(data_values)):
            data_time.append(i * time_step)

        #Draw maxina and minima
        plot.figure()
        plot.plot(data_time, data_values, '-b', markevery=mins_indexes, marker=8, markerfacecolor='green', markeredgecolor='green')
        plot.plot(data_time, data_values, '-b', markevery=maxes_indexes, marker=8, markerfacecolor='red', markeredgecolor='red')
        #Saving plot to PDF
        if(is_save_plot):
            plot.title(file_name)
            plot.savefig(f"Plots/{file_name}.pdf")
            plot.close()
            print(f"Plot image has been successfully uploaded to Plots/{file_name}.pdf") 
        #Showing plot
        if(is_show_plot):
            plot.show()
        
    @staticmethod
    def truncat_data(values:list,mathematical_expectation:float,square_deviation:float, time_step: float) -> tuple:
        """Returns truncated list of values that go beyond the mathematical expectation of the +-square deviation"""
        #Search for indexes of values beyond the standard deviation
        indexs = []
        for i in range (0, len(values)):
            if values[i] > mathematical_expectation + square_deviation or values[i] < mathematical_expectation - square_deviation:
                indexs.append(i)
        #Removing values that are remote from the cluster
        for i in range (0, len(indexs)):
            if indexs[1]-indexs[0] > 5:
                indexs.pop(0)

        trunced_values = []
        for i in range (indexs[0], indexs[len(indexs)-1]):
            trunced_values.append(values[i])
        start_time = indexs[0] * time_step
        end_time = indexs[len(indexs)-1] * time_step
        return (trunced_values, start_time, end_time)

