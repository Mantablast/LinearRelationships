import csv
import os
fileList = "listOfFiles.csv"          # Go get the list of files plz
delCount = 0                          # Counter for files deleted
with open(fileList, 'r') as csvfile:  # Read the csv
    reader = csv.reader(csvfile)
    for row in reader:                # Loop time. Go through and check if the path exists in the folder
        path = "/Users/aimeejesso/PycharmProjects/LinearRelationships/DIR1/" + row[0]
        if os.path.exists(path):      # If it does, trash it
            os.remove(path)
            delCount = delCount + 1
        else:
            print("The file does not exist. Next file.")
print("All done!  " + str(delCount) + " files were removed from your data set")  # Tally deleted files after



