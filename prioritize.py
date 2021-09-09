# This Python program ranks a list by asking the user to choose
# one out of a pair at a time from the command line
import csv
import numpy as np
import os, sys
import file_ops
import combine
import comparing

#determine whether to use existing data from csv file
#if so, call file_ops.getfile()
#if not, ask for information and create equivalent list of lists
# and later, save that listoflists to csv

#extend list of lists into each list item being a key in a dictionary
#create combination pairs from all keys in dictionary
#ask user for input to select one option from each pair
#and add 1 to dictionary value for that key, creating frequency dictionary
#as it continues to loop through the pairs, it also checks against
#previous user selection to infer a ranking relationship
#between the current pair

def get_one_choice(choices=["Item1","Item2"]):
    #choices is a list of two items that can be converted to strings
    #put choices into an input message, returns the selected item
    choices_str = f"Select one of the below options by entering the corresponding number.\n"
    for num, choice in enumerate(choices):
        choices_str = choices_str+f"{num+1}. {choice}\n"
    #end loop adding choices to msg_str
    num_selection = int(input(choices_str))
    return choices[num_selection-1]


def increm(val):
    #increment to 1 if null val
    if val == None:
        return 1
    else: #otherwise, increment by 1
        return val+1
#end function


def main():
    #use existing data or enter input
    useprior = input("Are you using data from an existing CSV file? Y/N\n")
    datadict = {}
    if useprior=="Y": #if Yes
        filepath, datalists = file_ops.getfile("Please enter the filepath for the file to be used, including the file extension. Please include the complete path if not in this directory.")
        for datalist in datalists: #nested for loops are O^2!
            for data in datalist:  #look into reducing
                datadict[data]=[0,[],[]]#number of times chosen, items that were chosen over it,
    #items that it was chosen over
    else: #answered N (or no answer); get information through input
        data=None
        while data!="":
            data = input("Please enter one item at a time. Pressing Enter for empty input will make the previous entry the last item.\n")
            if data=="":
                break
            else:
                datadict[data]=[0,[],[]]#number of times chosen, items that were chosen over it,
    #items that it was chosen over

    if len(datadict)<=1: #if only one item in the dictionary or no items
        print(f"There was only one item: {datadict}") #show the datadict contents as result
        sys.exit("Exiting program.") #end program
    else: #make list of items to combine into pairs
        combos_list = combine.combos(list(datadict.keys())) #sends list of keys, the default returned is pairs (combinations of 2's)
        for combo in combos_list:#compare options
            #first check for items in common using dictionary info
            #to logically infer relationship
            if len(combo)==2:#to be sure each combo is only two items
                info0 = datadict[combo[0]]
                info1 = datadict[combo[1]]
                relation = comparing.infer(info0,info1)
                
                if relation == None: #ask user for input on comparison
                    chosen_option = get_one_choice(choices = combo)
                    if chosen_option==combo[0]:
                        #other_option is set to the other of the pair
                        other_option = combo[1]
                    elif chosen_option==combo[1]:
                        other_option = combo[0]
                    else:
                        sys.exit("Exiting program")

                elif relation==True:#then combo[0] should rank higher
                    chosen_option = combo[0]
                    other_option = combo[1]
                else: #relation is False, combo[1] should rank higher
                    chosen_option = combo[1]
                    other_option = combo[0]    
                #get information from datadict
                total_c,above_c,below_c = datadict[chosen_option]
                total_o,above_o,below_o = datadict[other_option]
                print(f"chosen {chosen_option}: {above_c}{below_c} \nother {other_option}: {above_o}{below_o}")
                
                #update datadict appropriately
                below_c.append(other_option) #other_option ranks below chosen_option
                datadict[chosen_option] = [increm(total_c),above_c,below_c]
                
                above_o.append(chosen_option) #chosen_option ranks above other_option
                datadict[other_option] = [total_o,above_o,below_o]
        #end combo frequency loop
        print(str(datadict)) #show message box with entire dictionary
        #write datadict keys to csv file
        file_ops.savelist(datadict.keys(),"Please provide a file name for the list of items. It will be saved with a .csv extension in data-lists.")
        
        #put keys in list in order based on totals (highest value first)
        sortedlist = sorted(datadict.items(), key = lambda keyval: keyval[1][0], reverse=True)
        file_ops.savecsv(sortedlist,"Please provide a file name for sorted dictionary entries of the comparison results. It will be saved with a .csv extension in results.")#write sortedlist to text file
       
# Main function calling
if __name__=="__main__":     
    main()