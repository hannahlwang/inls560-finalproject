import re
import csv

line_table=[]
# file_table=[]

# This is the first menu that appears, in order to determine which file will be chosen
while True:
    filechoice = input(str('-'*50 + '\n') + (
'''File Menu:
1 - ArtMFATheses.txt
2 - SILSMastersPapers.txt
3 - UNCScholPub.txt
''') + str('-'*50 + '\n') + ('Choose a file: '))
    if filechoice == '1' or filechoice == '2' or filechoice == '3' :
        break
if filechoice == '1' :
    filename = 'ArtMFATheses.txt'
elif filechoice == '2' :
    filename = 'SILSMastersPapers.txt'
elif filechoice == '3' :
    filename = 'UNCScholPub.txt'

with open(filename) as csvfile:
    filereader = csv.reader(csvfile, delimiter='\t') # Read the CSV file, using the tabs as delimiters
    for row in filereader:
        rowreader = '\t'.join(row) # Create a string that can be searched by regex
        if re.search("^File|^Collection|^Folder|^Aggregate",rowreader): # Look for lines that start with one of these object types -> rules out bad data
            rowreader = rowreader.rstrip()
            line_table.append(rowreader.split("\t")) # Make a table out of these lines

# Create a dictionary that returns all the values that correspond to each PID (a dictionary of dictionaries)
csvdict = dict()

for row in line_table :
    key = row[1]
    csvdict[key] = {
        'Object Type': row[0], 'Title': row[2], 'Path': row[3], 'Label': row[4], 'Depth': row[5], 'Deleted': row[6], 'Date Added': row[7], 
        'Date Updated': row[8], 'MIME Type': row[9], 'Checksum': row[10], 'File Size (bytes)': row[11]
        # , 'Number of Children': row[12]
        }

# This returns an alphabetized list of data associated with each PID
def csvdictviz(userchoice): 
    print('PID: ' + userchoice)
    keylst = list(csvdict[userchoice].keys())
    keylst.sort()
    for key in keylst:
        print(str(key) + ': ' + str(csvdict[userchoice][key]))

# Count all the different object types
object_type_dict = dict()
for row in line_table :
    object_type = row[0]
    if object_type not in object_type_dict :
        object_type_dict[object_type] = 1
    else:
        object_type_dict[object_type] += 1
# print(object_type_dict)

# Visualize object types with histogram
def object_type_viz() :
    print(str('-'*50))
    print('OBJECT TYPES')
    for object_type in object_type_dict:
        reduced_number = int(object_type_dict[object_type])//50 # Creates a good size for histogram (scaled down)
        print(str(object_type[:2]) + ':' + str('*'*int(reduced_number))) # Use abbreviated object titles in histogram
    print(str('-'*50))
    print('KEY:') # Key shows what the abbreviations stand for, and the actual numbers for each object type in parentheses
    for object_type in object_type_dict:
        print(str(object_type[:2]) + ' = ' + str(object_type) + ' (' + str(object_type_dict[object_type]) + ' objects)')
    
# Count all the different MIME types
mime_type_dict = dict()
for row in line_table :
    mime_type = row[9]
    if mime_type not in mime_type_dict :
        mime_type_dict[mime_type] = 1
    else:
        mime_type_dict[mime_type] += 1

# Visualize MIME types in histogram
def mime_type_viz() :
    print(str('-'*50))
    print('MIME TYPES')
    for mime_type in mime_type_dict: # Visualization
        if re.findall('[/]([a-z0-9-][a-z0-9-][a-z0-9-])',mime_type) : # If the MIME type is in the normal format, with a term following a backslash (e.g. 'text/xml')
            mime_type_abbrev = re.findall('[/]([a-z0-9-][a-z0-9-][a-z0-9-])',mime_type)
            mime_type_abbrev_str = ''.join(mime_type_abbrev)
            reduced_number = int(mime_type_dict[mime_type])//50
            print(str(mime_type_abbrev_str) + ':' + str('*'*int(reduced_number)))
        elif mime_type == '' : # If the MIME type is not specified
            mime_type_abbrev_str = 'N/A'
            reduced_number = int(mime_type_dict[mime_type])//50
            print(str(mime_type_abbrev_str) + ':' + str('*'*int(reduced_number)))
        elif mime_type == '$mimeResolver.getContentTypeFor($file.name)' : # If the MIME type is equal to this weird outlier, that doesn't have a backslash
            mime_type_abbrev_str = '$mi'
            reduced_number = int(mime_type_dict[mime_type])//50
            print(str(mime_type_abbrev_str) + ':' + str('*'*int(reduced_number)))
    print(str('-'*50))
    print('KEY:') # Key that shows what each abbreviation stands for, and the number of objects with each MIME type
    for mime_type in mime_type_dict:
        if re.findall('[/]([a-z0-9-][a-z0-9-][a-z0-9-])',mime_type) :
            mime_type_abbrev = re.findall('[/]([a-z0-9-][a-z0-9-][a-z0-9-])',mime_type)
            mime_type_abbrev_str = ''.join(mime_type_abbrev)
            print(str(mime_type_abbrev_str) + ' = ' + str(mime_type) + ' (' + str(mime_type_dict[mime_type]) + ' objects)')
        elif mime_type == '' :
            mime_type_abbrev_str = 'N/A'
            print(str(mime_type_abbrev_str) + ' = ' + str(mime_type) + ' (' + str(mime_type_dict[mime_type]) + ' objects)')
        elif mime_type == '$mimeResolver.getContentTypeFor($file.name)' :
            mime_type_abbrev_str = '$mi'
            print(str(mime_type_abbrev_str) + ' = ' + str(mime_type) + ' (' + str(mime_type_dict[mime_type]) + ' objects)')

# Make a list of all the different file sizes
file_size_lst = []
total_file_size = 0
file_size_count = 0
for row in line_table :
    file_size = row[11]
    if re.search('^[0-9]',file_size): # Only add file size to the list if it's a string of numbers
        file_size_int = int(file_size)
        file_size_lst.append(file_size_int)
        total_file_size += file_size_int
        file_size_count += 1

helptext = "This is a program that analyzes CSV exports from the Carolina Digital Repository. You must submit a tab-delimited txt file for the program to work. You can either learn about the data in the entire file, or learn about specific items by entering a PID."