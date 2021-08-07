#!/usr/bin/env python3
import pandas as pd

#Declare all data from functions beforehand
raw_list = []
symbol_list = '[]()<>'
https_https = ['http', 'https']
url_check = ':'
url_list = []
with_port_list = []

#Just some extra code to help make the output pretier with lines of dots between 
#outputs
def break_fullstops(lines_of_dots):
    n = 1
    while n <= lines_of_dots:
        print('.................................................................')
        n = n + 1

#Converts the file into a more usable format, in this case a pandas dataframe
#This also corrects the data to ensure its more usable continuing down in the
#Script
def file_filter(text_file):
    with open(text_file) as gobuster_input:
        read_gobuster_lines = gobuster_input.readlines()
        for line in read_gobuster_lines:
            raw_list.append(line.split())
        raw_dataframe = pd.DataFrame(raw_list)
        column_count = '6'
        for index_number in column_count:
            for row_data in raw_dataframe[int(index_number)]:
                for symbol in symbol_list:
                    if symbol in row_data:
                        line_by_line = row_data.replace(symbol, '')
                        for url_start in https_https:
                            if url_start in line_by_line:
                                url_list.append(line_by_line)
        url_dataframe = pd.DataFrame(url_list)
        url_dataframe_no_dups = url_dataframe.drop_duplicates(subset=None, keep='first', inplace=False)
        actions_to_take(url_dataframe_no_dups[0])


#Take actions using the data inputed, such as filtering it into priority based order,
#URLs that contained port numbers will be higher importance
def actions_to_take(input_url_dataframe):
    print('What would you like to see?')
    break_fullstops(1)
    print("1) URL's with ports")
    break_fullstops(1)
    action_input = input()
    if action_input == "1":
        print('You have selected to view websites with ports')
        for url in input_url_dataframe:
            if url.count(url_check) > 1:
                with_port_list.append(url)
        print(with_port_list)
        break_fullstops(2)
    else:
        print('Wrong input selected')

#User input processing
print('Please input the path to the output text file from GoBuster.')
break_fullstops(2)
text_file_input = input()
if text_file_input != '':
    break_fullstops(2)
    print('Started Succesfully')
    break_fullstops(2)
    file_filter(text_file_input)


