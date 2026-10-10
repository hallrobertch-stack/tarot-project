import pandas as pd
import datetime as dt
import re
from IPython.display import display

#Initializes dataframe schema
reading_data_schema = [
    "Card",
    "Position",
    "Time"
]
# Initializing the dataframe with the schema
reading_data_df = pd.DataFrame([] , columns = reading_data_schema)

#Prompts initial user input
print("Enter the codes and positions for the drawn cards. Type 'quit' to quit.")

#User input
while True:
    #Card information
    card_code = input("Enter card code: ")
    if card_code.lower() == 'quit':
        break

    position = input("Enter card position: ")
    # get the timestamp after user input
    ts = pd.Timestamp.now()
    # converting to a string to make splitting easier
    ts = str(ts)
    # Regex pattern: 4 digits, a dash, 2 digits, a dash, 2 digits, a colon, 2 digits
    # Then stop once reaching the end of the specified data/numbers
    # Next time, try using the python "split()" function to split up a given String
    time = re.sub(r"(^\d{4}-\d{2}-\d{2} \d{2}:\d{2}).*", r"\1", ts)
    
    # the below dataframe is being re-created after each pass through the loop
    # the Schema must be the same as the "reading_data_df" to ensure the data lines up
    # reference: 
    # reading_data_schema = [
    #     "Card",
    #     "Position",
    #     "Time"
    # ]
    temp_df = pd.DataFrame({'Card': [card_code], 'Position': [position],"Time": [time]})
    display(temp_df) # printing out each loop

    reading_data_df = pd.concat([reading_data_df, temp_df])

display(reading_data_df)

reading_data_df.to_csv()
#prints reading_data and time_string
print("Collected Data:")

# Pulling in the last run
recentRun_df = pd.read_csv("C:/Users/TheEp/OneDrive/Desktop/Python/Tarot Project/recentRun.csv")
# Put the last run result into the previous run dataframe to combine all data
master_df = pd.concat([reading_data_df, recentRun_df])

########################################################################################################################
# The below section shows how to more dynamically read in files in a way
# that you ca re-use the path.

# #baseFilePath path to general project folder
# baseFilePath = f"\Users\TheEp\OneDrive\Desktop\Python\Tarot Project"
# #fileName - specific name without extension
# fileName = "tarotcarddesc"
# #fullPath - stitches filetype to fileName
# # use the "f" operator to stitch together variables and plain text
# fullPath = f"{baseFilePath}\{fileName}.csv"


exportFullPath = r"C:/Users/TheEp/OneDrive/Desktop/Python/Tarot Project/recentRun.csv"
master_df.to_csv(exportFullPath, sep=',',index=None)
