import pandas as pd
from IPython.display import display


card_df = pd.read_csv("C:/Users/TheEp/OneDrive/Desktop/Python/Tarot Project/tarotcarddesc.csv")
card_df = card_df.set_index("cardCode")
read_type_list = ["LOVE", "CAREER", "FINANCE", "SPIRITUALITY", "HEALTH", "FAMILY", "FRIENDSHIP", "OTHER"]
subject_list = ["ME", "PARTNER", "FAMILY MEMBER", "FRIEND", "COLLEAGUE", "OTHER"]
i = 0 # iterator used as counter in loop

reading_schema = [
    'Card',
    'Position',
    'Position_Desc',
    'Suit',
    'Element',
    'Arcana Type',
    'Time',
    'Read_ID'
]


def user_input():

    reading_data_df = pd.DataFrame([], columns=reading_schema) #ties reading_data_df to established schema above
    start_time = str(pd.Timestamp.now())[:16] #captures singular time for each run of user_input()
    user_name = input('What is your name? ').upper() #prompts user for name; used to create Read_ID column
    read_id = user_name + "_" + start_time #appends user_name and start_time with underscore to make split easier for later analysis

    print(read_type_list)
    while True:
        read_type = input(
            "What is the subject of your reading? (Love, Career, etc.) "
            ).strip().upper() #prompts user for reading type

        if read_type in read_type_list:
            break
        
        print(read_type_list)
        print("Not a Valid Selection; please select from the list above.")

    while True:
        subject_question = input(
            "Is the reading about a specific subject? (Y/N?) "
            ).strip().lower() #prompts user for subject question

        if subject_question not in ["y", "n"]:
            print("Not a Valid Selection; please select Y or N.")
            continue

        if subject_question == "y":

            while True:
                print(subject_list)
                subject = input(
                    "Who is the reading about? (Select from the list above) "
                    ).strip().upper() #prompts user for subject

                if subject in subject_list:
                    break
                    
                print("Not a Valid Selection; please select from the list above.")

            break

        else:
            subject = "GENERAL"
            break
    
    while True:
        card_code = input('Enter card code: (enter "q" to quit) ') #prompts user for card code; allows user to exit loop with "q"

        if card_code.lower() == 'q':
            break
        
        if card_code not in card_df.index:
            print("Not a Valid Selection")
            continue

        selected_card = card_df.loc[card_code] #connects user input to cardCode index
    
        position = input("Enter the card position (up or rx): ").lower()

        if position.lower() == "up":
            position_desc = selected_card["upScript"]
   
        elif position.lower() == "rx":
             position_desc = selected_card["rxScript"]
        else:
            print("Not a valid selection")
            continue
    
    while True:
        bottom_card = card_code
        bottom_card_question = input("Do you want to record the bottom? (Y/N?): ").lower()
        
        if bottom_card_question not in ["y", "n"]:
            print("Not a Valid Selection; please select Y or N: ")
            continue

        if bottom_card_question == "y":

            while True:
                bottom_card = input(
                    "Enter the code for the card at the bottom of the deck?: "
                    ).strip()

                if bottom_card in card_df.index:
                    break

                print("Not a valid selection.")

            break

        else: bottom_card = "None"

        card = selected_card["cardName"]
        suit = selected_card["suit"]
        elements = selected_card["elements"]
        arcana_type = selected_card["arcanaType"]
        bottom_card = selected_card["cardName"]
        time = str(pd.Timestamp.now())[:16]

        temp_df = pd.DataFrame({
            "Read_Type": [read_type],
            "Subject": [subject],
            "Card": [card],
            "Position": [position],
            "Position_Desc": [position_desc],
            "Suit": [suit],
            "Element": [elements],
            "Arcana Type": [arcana_type],
            "Bottom Card": 
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
    "C:/Users/TheEp/OneDrive/Desktop/Python/Tarot Project/cardData.csv"
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