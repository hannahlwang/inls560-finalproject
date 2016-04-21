import re
import csv

# with open("ArtMFATheses.txt") as f:
#     lines = f.readlines()

# filename = input("Please enter a file name: ")

line_table=[]
file_table=[]

with open("ArtMFATheses.txt") as csvfile:
    filereader = csv.reader(csvfile, delimiter='\t')
    for row in filereader:
        rowreader = '\t'.join(row)
        file_table.append(rowreader.split("\t"))
        if re.search("^File|^Collection|^Folder|^Aggregate",rowreader):
            rowreader = rowreader.rstrip()
            line_table.append(rowreader.split("\t"))

# for row in file_table :
#     first_line = file_table[0]
#     first_line_tabbed = '\t'.join(first_line)

# print(first_line_tabbed)

# while first_line_tabbed != 'Object Type'+'\t'+'PID'+'\t'+'Title'+'\t'+'Path'+'\t'+'Label'+'\t'+'Depth'+'\t'+'Deleted'+'\t'+'Date Added'+'\t'+'Date Updated'+'\t'+'MIME Type'+'\t'+'Checksum'+'\t'+'File Size (bytes)'+'\t'+'Number of Children' :
#     print("Please enter a file name: ")
#     filename = input()
#     for row in file_table :
#         first_line = file_table[0]
#         first_line_tabbed = '\t'.join(first_line)

def makedict(datatypedict, datatype, datatypeindex) :
    datatypedict = dict()
    for row in line_table :
        datatype = row[datatypeindex]
        if datatype not in datatypedict :
            datatypedict[datatype] = 1
        else:
            datatypedict[datatype] += 1
    print(datatypedict)

makedict('object_dict', 'object', 0)
makedict('mimetype_dict', 'mimetype', 9)
makedict('deleted_dict', 'deleted_state', 6)

# print(line_table)

# object_dict = dict()

# for row in line_table :
#     object = row[0]
#     if object not in object_dict :
#         object_dict[object] = 1
#     else:
#         object_dict[object] += 1

# print(object_dict)

# deleted_dict = dict()

# for row in line_table :
#     deleted_state = row[6]
#     if deleted_state not in deleted_dict :
#         deleted_dict[deleted_state] = 1
#     else:
#         deleted_dict[deleted_state] += 1

# print(deleted_dict)

# mimetype_dict = dict()

# for row in line_table :
#     mimetype = row[9]
#     if mimetype not in mimetype_dict :
#         mimetype_dict[mimetype] = 1
#     else:
#         mimetype_dict[mimetype] += 1

# print(mimetype_dict)