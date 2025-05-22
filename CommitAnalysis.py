import re
import enum
import matplotlib.pyplot as plt
import numpy as np

#faire un enum des types de commit 

# ---------------------- Constants -------------------
COMMIT_HISTORY_DATED_FILE_PATH = "commits/CommitHistoryDated.txt"
COMMIT_HISTORY_FILE_PATH = "commits/CommitHistory.txt"
MULTIPLE_TYPE_SEPARATOR = ',' #Maybe you have a commit that you assigned to two types, some people often do, put your commit type separator here, mine is a comma
TYPE_TEXT_SEPARATOR=':' #The separator that is used in a commit to distinguish the type from the commit message


# ---------------------- Functions -------------------


def split_commit_types(multipleCommitTypes):
        commitTypeList = []
        multipleCommitTypes = multipleCommitTypes.split(MULTIPLE_TYPE_SEPARATOR)
        for oneType in multipleCommitTypes:
                oneType = oneType.strip() #if there is any whitespace around your types, this will remove it
                commitTypeList.append(oneType)
        return commitTypeList

def type_list_to_occurence_graph(commitTypeList): #returns two lists : one with each commit type, and one with their occurence, with matching positions
        typeAmount = {}
        for commitType in commitTypeList:
                if commitType=="doc": #i sometimes typed doc instead of docs so this is here to fix it
                        commitType="docs"
                if commitType in typeAmount:
                        typeAmount[commitType]+=1
                else:
                        typeAmount[commitType]=1
        return [list(typeAmount.keys()),list(typeAmount.values())]

def get_day_year_from_time(time):
        splitLine = time.split(" ")
        date = splitLine[1:3]
        year = splitLine[4]
        time = (' '.join(date)+" "+str(year)).strip()
        return time

def get_commit_type(commitMessage): #returns a list of commit types, even if there is only one, empty list if no type is found
        if TYPE_TEXT_SEPARATOR in commitMessage:
                commitType,_ = commitMessage.split(TYPE_TEXT_SEPARATOR)
                commitType = commitType.strip()
                if MULTIPLE_TYPE_SEPARATOR in commitType:
                        multipleCommitTypes = split_commit_types(commitType)
                        return multipleCommitTypes
                return [commitType]
        else : 
                return []
                

def occurence_graph():
        commitTypeList =[]
        with open(COMMIT_HISTORY_FILE_PATH) as commitFile : 
                for line in commitFile:
                        if line.__contains__(TYPE_TEXT_SEPARATOR):
                                commitIdAndType, _ = line.split(TYPE_TEXT_SEPARATOR) #get the half part of the line that has commit id and type
                                commitType = commitIdAndType.split(" ")[1] #splitting with the spaces gets you [commitid,commit type,(sometimes) blank space]
                                if(commitType.__contains__(MULTIPLE_TYPE_SEPARATOR)):
                                        commitTypeList.extend(split_commit_types(commitType))
                                        continue # instructs the program to come back at the top of the loop, otherwise the old double type would be added to the list

                                commitTypeList.append(commitType)

        commitTypes,commitOccurences = type_list_to_occurence_graph(commitTypeList)

        plt.figure(figsize=(25, 15))
        plt.bar(commitTypes,commitOccurences)
        plt.xlabel('Commit type')
        plt.ylabel('Total amount of commit')
        plt.xticks(rotation=90) 
        plt.title('Occurence of each commit type in ReOBS work') 
        plt.show()





# ---------------------- Main -----------------------
"""
using this : " git log --pretty=format:"%h%x09%an%x09%ad%x09%s" " could work
"""

commitTypeList =[]
with open(COMMIT_HISTORY_DATED_FILE_PATH) as commitFile : 
        for line in commitFile:
                line = line.split("\t") #get list like this : [commitID,AutorName,Exact date,commit message]
                line[2] = get_day_year_from_time(line[2])
                line[3] = get_commit_type(line[3].strip())
                

"""
dates = ['2024-04-01', '2024-04-02']
things = ['thing1', 'thing2']

# Example counts: rows = dates, columns = things
data = [
    [1, 2],  # April 1: thing1 = 1, thing2 = 2
    [1, 0],  # April 2: thing1 = 1, thing2 = 0
]

data = np.array(data)
bar_width = 0.35
x = np.arange(len(dates))  # [0, 1]

# Plot each group of bars
for i in range(len(things)):
    plt.bar(x + i * bar_width, data[:, i], width=bar_width, label=things[i])

# Set x-ticks in the center of grouped bars
plt.xticks(x + bar_width / 2, dates)
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Grouped Bar Chart Example')
plt.legend(title='Thing')
plt.tight_layout()
plt.show()
"""
"""
        if line.__contains__(TYPE_TEXT_SEPARATOR):
                commitIdAndType, _ = line.split(TYPE_TEXT_SEPARATOR) #get the half part of the line that has commit id and type
                commitType = commitIdAndType.split(" ")[1] #splitting with the spaces gets you [commitid,commit type,(sometimes) blank space]
                if(commitType.__contains__(MULTIPLE_TYPE_SEPARATOR)):
                        commitTypeList.extend(split_commit_types(commitType))
                        continue # instructs the program to come back at the top of the loop, otherwise the old double type would be added to the list

                commitTypeList.append(commitType)

                """
#print(commitTypeList)
