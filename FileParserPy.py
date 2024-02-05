class FileParser: 
    
    @staticmethod
    def Parse(fileNumber) -> tuple:
        values = []
        fileNumber = str(fileNumber)
        
        while(len(fileNumber) < 4):
            fileNumber = "0" + fileNumber

        csv = open(f"24_01/ALL{fileNumber}/F{fileNumber}CH2.CSV", "r")

        lines = csv.readlines()
        
        timeStep = lines[1].split(",")[1]
        timeStep = float(timeStep)
        
        for i in range(18):
            lines.pop(0)

        for line in lines:
            values.append(float(line.split(",")[4]))

        csv.close()

        print(f"File opened {fileNumber}CH2.CSV")
        return (values, timeStep)