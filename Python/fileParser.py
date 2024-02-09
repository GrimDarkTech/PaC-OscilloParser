class FileParser: 
    
    @staticmethod
    def parse(file_number) -> tuple:
        """Returns tuple of list of values readed from CSV-file and float value of time step between values"""
        values = []
        file_number = str(file_number)
        
        #Fill filename with zeros to 4-symbols
        while(len(file_number) < 4):
            file_number = "0" + file_number

        #Opening CSV-file
        csv = open(f"Data/ALL{file_number}/F{file_number}CH2.CSV", "r")

        lines = csv.readlines()
        
        #Getting time step value
        time_step = lines[1].split(",")[1]
        time_step = float(time_step)
        
        for i in range(18):
            lines.pop(0)
        
        for line in lines:
            values.append(float(line.split(",")[4]))

        csv.close()

        print(f"File opened {file_number}CH2.CSV")
        return (values, time_step)