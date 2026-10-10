import pandas as pd
from IPython.display import display


card_df = pd.read_csv("C:/Users/TheEp/OneDrive/Desktop/Python/Tarot Project/tarotcarddesc.csv")
card_df = card_df.set_index("cardCode")

reading_schema = [
    'Card',
    'Position',
    'Position_Desc',
    'Time',
    'Read_ID'
]


def user_input():

    reading_data_df = pd.DataFrame([], columns=reading_schema)

    start_time = str(pd.Timestamp.now())[:16]

    user_name = input('What is your name? ').upper()

    read_id = user_name + "_" + start_time

    while True:
        card_code = input('Enter card code: ')

        if card_code.lower() == 'q':
            break

        
        if card_code not in card_df.index:
            print("Not a Valid Selection")
            continue

        selected_card = card_df.loc[card_code]
    
        position = input("Enter the card position (up or rx): ").lower()

        if position.lower() == "up":
            position_desc = selected_card["upScript"]
   
        elif position.lower() == "rx":
             position_desc = selected_card["rxScript"]
        else:
            print("Not a valid selection")
            continue

        card = selected_card["cardName"]
        time = str(pd.Timestamp.now())[:16]

        temp_df = pd.DataFrame({
            "Card": [card],
            "Position": [position],
            "Position_Desc": [position_desc],
            "Time": [time],
            "Read_ID": [read_id]
        })

        reading_data_df = pd.concat(
            [reading_data_df, temp_df],
            ignore_index=True
        )

        display(reading_data_df)

    return reading_data_df

import os 

reading_data_df = user_input()

exportFullPath = (
    "C:/Users/TheEp/OneDrive/Desktop/Python/Tarot Project/tarotData.csv"
    )

if os.path.exists(exportFullPath):
    recentRun_df = pd.read_csv(exportFullPath)
    master_df = pd.concat(
        [recentRun_df, reading_data_df],
        ignore_index=True
        )

else: 
    master_df = reading_data_df

master_df.to_csv(
    exportFullPath,
    index=False
    )

# Use the split function to isolate the Users Name from the Read_Id