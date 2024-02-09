class FileParser: 
    
    @staticmethod
    def Parse(fileNumber) -> tuple:
        """Returns tuple of list of values readed from CSV-file and float value of time step between values"""
        values = []
        fileNumber = str(fileNumber)
        
        #Fill filename with zeros to 4-symbols
        while(len(fileNumber) < 4):
            fileNumber = "0" + fileNumber

        #Opening CSV-file
        csv = open(f"Data/ALL{fileNumber}/F{fileNumber}CH2.CSV", "r")

        lines = csv.readlines()
        
        #Getting time step value
        timeStep = lines[1].split(",")[1]
        timeStep = float(timeStep)
        
        for i in range(18):
            lines.pop(0)
        
        for line in lines:
            values.append(float(line.split(",")[4]))

        csv.close()

        print(f"File opened {fileNumber}CH2.CSV")
        return (values, timeStep)