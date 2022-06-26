def getDataSets(dataSetName):
    if dataSetName == "light":
        return f"./data/dat_light.csv"
    elif dataSetName == "medium":
        return f"./data/dat_medium.csv"
    elif dataSetName == "heavy":
        return f"./data/dat_heavy.csv"
