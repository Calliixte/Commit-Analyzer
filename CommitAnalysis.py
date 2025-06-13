import re
import enum
from collections import defaultdict
from datetime import datetime
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
                oneType = oneType.lower().strip() #normalize output
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

def commits_over_time_graph():
        """
        get the corresponding file with : git log --pretty=format:"%h%x09%an%x09%ad%x09%s"
        """
        commit_counts = defaultdict(lambda: defaultdict(int))

        with open(COMMIT_HISTORY_DATED_FILE_PATH) as commitFile:
                for line in commitFile:
                        parts = line.strip().split("\t")
                        if len(parts) < 4:
                                continue  # skip malformed lines
                        commit_id, author, date_str, message = parts
                        date_str = get_day_year_from_time(date_str)
                        commit_types = get_commit_type(message.strip())

                        for ctype in commit_types:
                                ctype = ctype.lower().strip()
                                if ctype.startswith("merge"):  # exclude branch merges
                                        continue
                                if ctype == "doc":
                                        ctype = "docs"
                                commit_counts[date_str][ctype] += 1

        sorted_dates = sorted(commit_counts.keys(), key=lambda d: datetime.strptime(d, "%b %d %Y"))

        # Gather all commit types
        all_commit_types = set()
        for counts in commit_counts.values():
                all_commit_types.update(counts.keys())

        # Build data for plotting
        plot_data = {ctype: [] for ctype in all_commit_types}
        for date in sorted_dates:
                counts = commit_counts[date]
                for ctype in all_commit_types:
                        plot_data[ctype].append(counts.get(ctype, 0))

        # Plot
        plt.figure(figsize=(12, 6))
        for ctype, y_values in plot_data.items():
                plt.plot(sorted_dates, y_values, marker='o', label=ctype)

        plt.xlabel("Date")
        plt.ylabel("Number of commits")
        plt.title("Commit types over time")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

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

                                commitTypeList.append(commitType.lower().strip())

        commitTypes,commitOccurences = type_list_to_occurence_graph(commitTypeList)

        plt.figure(figsize=(25, 15))
        plt.bar(commitTypes,commitOccurences)
        plt.xlabel('Commit type')
        plt.ylabel('Total amount of commit')
        plt.xticks(rotation=90) 
        plt.title('Occurence of each commit type in ReOBS work') 
        plt.show()





# ---------------------- Main -----------------------
occurence_graph()
