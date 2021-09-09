#methods to read in and save a .CSV file
import csv

def getfile(message="Enter the file name."):
    #get CSV file name from user text input
    filepath = input(message+"\n")
    if filepath == None or filepath=='': #if empty input
        return None, None #exit the function and return None
    else:
    #try: #read in CSV file to list of lists
        readlist = []
        with open(filepath,'r') as f:
            reading = csv.reader(f)
            for row in reading:
                readlist.append(row)
    #except: # if not a CSV file
    #    input(f"File does not appear to be a CSV. Check file name and try again.")
    #    return filepath, None #return input file name and null
    return filepath, readlist

def savecsv(listofitems, message="Enter the file name."):
    #requests name of file to be saved, saves writing to CSV file in results
    savefilepath = input(message+"\n")
    if savefilepath=='':#if empty input, does not save file
        return None
    savefilepath = "./results/"+savefilepath+".csv"
    with open(savefilepath, 'w', newline='') as f: #writes listofitems to that file path
        writer = csv.writer(f)
        for each in listofitems:
            writer.writerow(each)

def savelist(listofitems, message="Enter the file name."):
    #requests name of file to be saved, saves writing to CSV file in data-lists
    savefilepath = input(message+"\n")
    if savefilepath=='':#if empty input, does not save file
        return None
    savefilepath = "./data-lists/"+savefilepath+".csv"
    with open(savefilepath, 'w', newline='') as f: #writes listofitems to that file path
        writer = csv.writer(f)
        writer.writerow(listofitems)