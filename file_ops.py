#methods to read in and save a .CSV file
import csv
import os
import pandas as pd

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
    current_dir = os.getcwd()
    resultspath = os.path.join(current_dir,"results")
    if not os.path.isdir(resultspath): #if the results folder does not exist
        os.mkdir(resultspath) #creates folder in current directory
    savefilepath = os.path.join(resultspath,savefilepath+".csv")
    with open(savefilepath, 'w', newline='') as f: #writes listofitems to that file path
        writer = csv.writer(f)
        for each in listofitems:
            writer.writerow(each)

def savelist(listofitems, message="Enter the file name."):
    #requests name of file to be saved, writes to CSV file in data-lists
    savefilepath = input(message+"\n")
    if savefilepath=='':#if empty input, does not save file
        return None
    current_dir = os.getcwd()
    listspath = os.path.join(current_dir,"data-lists")
    if not os.path.isdir(listspath): #if the data-lists folder does not exist
        os.mkdir(listspath) #creates folder in current directory
    savefilepath = os.path.join(listspath,savefilepath+".csv")
    with open(savefilepath, 'w', newline='') as f: #writes listofitems to that file path
        writer = csv.writer(f)
        writer.writerow(listofitems)
        
def savepdcsv(itemdict, message="Enter the file name."):
    #takes in dictionary with each key having a three-item list for its value
    #first item in that list is a number
    #requests name of file to be saved, saves writing to CSV file in results
    savefilepath = input(message+"\n")
    if savefilepath=='':#if empty input, does not save file
        return None
    current_dir = os.getcwd()
    resultspath = os.path.join(current_dir,"results")
    if not os.path.isdir(resultspath): #if the results folder does not exist
        os.mkdir(resultspath) #creates folder in current directory
    savefilepath = os.path.join(resultspath,savefilepath+".csv")
    
    #convert dictionary to pandas DataFrame
    tempdf = pd.DataFrame(data=itemdict)
    datadf = tempdf.T #now index is the item names
    datadf.reset_index(inplace=True) #reset index to be numbers, item names become a column
    coldict = {"index":"Items",0:"Total",1:"Above",2:"Below"}
    datadf.rename(columns=coldict, inplace=True) #rename columns
    #sort by Total, from highest to lowest
    datadf.sort_values("Total",inplace=True,ascending=False)
    #save datadf, sorted, as CSV
    datadf.to_csv(savefilepath,index_label="Index")