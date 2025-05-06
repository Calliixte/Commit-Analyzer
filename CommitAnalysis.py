import enum
import matplotlib.pyplot as plt

#faire un enum des types de commit 

# ---------------------- Constants -------------------

COMMIT_HISTORY_FILE_PATH = "CommitHistoryAlice.txt"
MULTIPLE_TYPE_SEPARATOR = ',' #Maybe you have a commit that you assigned to two types, some people often do, put your commit type separator here, mine is a comma
TYPE_TEXT_SEPARATOR=':' #The separator that is used in a commit to distinguish the type from the commit message


# ---------------------- Functions -------------------


def split_commit_types(multipleCommitTypes):
        commitTypeList = []
        multipleCommitTypes = commitType.split(MULTIPLE_TYPE_SEPARATOR)
        for oneType in multipleCommitTypes:
                oneType = oneType.strip() #if there is any whitespace around your types, this will remove it
                commitTypeList.append(oneType)
        return commitTypeList

def list_to_graph(commitTypeList): #returns two lists : one with each commit type, and one with their occurence, with matching positions
        typeAmount = {}
        for commitType in commitTypeList:
                if commitType=="doc": #i sometimes typed doc instead of docs so this is here to fix it
                        commitType="docs"
                if commitType in typeAmount:
                        typeAmount[commitType]+=1
                else:
                        typeAmount[commitType]=1
        return [list(typeAmount.keys()),list(typeAmount.values())]


# ---------------------- Main -----------------------


"""
TODO : Move this to a function and have different ways of fetching commits, for example having one that allows fetching time
using this : "git log --pretty=format:"%h%x09%an%x09%ad%x09%s" could work
"""

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

commitTypes,commitOccurences = list_to_graph(commitTypeList)

plt.figure(figsize=(25, 15))
plt.bar(commitTypes,commitOccurences)
plt.xlabel('Commit type')
plt.ylabel('Total amount of commit')
plt.xticks(rotation=90) 
plt.title('Occurence of each commit type in ReOBS work') 
plt.show()



