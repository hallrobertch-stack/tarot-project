import pandas as pd
from pathlib import Path
from  IPython.display import display
from collections import Counter as ct

#turns cardData.csv to DataFrame
analysis_df = pd.read_csv(rf"C:\Users\TheEp\OneDrive\Desktop\Python\Tarot Project\cardData.csv")

#creates separate columns to isolate User_ID from DateTime info in "Read_ID" column
analysis_df[["User_ID", "Reading_Time"]] = (
    analysis_df["Read_ID"].str.split("_", n=1, expand=True) #n=1 stops split after first underscore
)

user_id = analysis_df["User_ID"] #creates variable using just User_ID column created by above split function
reading_time = analysis_df["Reading_Time"] #creates variable using just Reading_Time column created by above split function
position_desc = (
    analysis_df["Position_Desc"] #isolates the "Position_Desc" column from analysis_df DataFrame
    .str.split(",", expand=False) #splits each descriptor in the "Position_Desc" column
    .explode() #turns split descriptors into its own row so Counter can count individual descriptors
    .str.strip() #strips any lingering spaces
    .str.lower() #normalizes info in "Position_Desc" column to allow for easier searching/counts
)

descriptor_terms = ct(position_desc) #uses Counter class to create a tally of each descriptor in position_desc

def total_descriptor_counter(): #counts how many times a word shows up in full analysis_df DataFrame based on user input
    count_desc = input(
        "Which descriptor are you wanting to count? "
        ).strip().lower() #allows user to input possible descriptors to determine count

    #aggregates total number of times the input is in position_desc variable (AKA "Position_Desc" column in dataframe)
    total = sum (
        count
        for descriptor, count in descriptor_terms.items() #items() counts each descriptor using info in exploded rows
        if count_desc in descriptor
    )

    #outputs number of times a given descriptor is listed in the "Position_Desc" column of cardData.csv
    print(f"{count_desc}: {total}")

def reading_data_by_user_id(): #displays readings for specific user and outputs to a separate csv file
    input_user_id = input(
        "Which user ID are you wanting to isolate? "
        ).strip().upper()

    user_readings = analysis_df.loc[analysis_df["User_ID"] == input_user_id] #locates input_user_id in "User_ID" column

    if user_readings.empty:
        print(f"No readings found for {input_user_id}.") #shows error message and re-prompts user for valid user ID
        return

    display(user_readings)

    export_user_id = input(
        "Would you like to export this information into a separate .csv file (Y/N)? "
        ).strip().upper()

    if export_user_id == "Y":

        export_user_path = Path(
            rf"C:\Users\TheEp\OneDrive\Desktop\Python\Tarot Project\Reads by User\{input_user_id}_readings.csv"
        )

        user_readings.to_csv(export_user_path, index=False)
        print(f"Exported to {export_user_path}")

def reading_data_by_id():
    display_read_id = analysis_df["Read_ID"].unique()
    display(display_read_id)
    input_reading_id = input(
        "Input the Read_ID from the above list to see the attached data: "
                             ).upper()
    
    read_id_reading = analysis_df.loc[analysis_df["Read_ID"] == input_reading_id] #locates Read_ID in original csv
    input_reading_id = input_reading_id.replace(":", '_')
    if read_id_reading.empty:
        print(f"{input_reading_id} is not a valid read ID.")
        return

    display(read_id_reading)


    export_read_id = input(
        "Would you like to export this information into a separate .csv file (Y/N)? "
        ).strip().upper()

    if export_read_id.upper() == "Y":

        export_read_path = Path(
                rf"C:\Users\TheEp\OneDrive\Desktop\Python\Tarot Project\Reads by Read ID\{input_reading_id}_.csv"
            )

        # export_read_path.parent.mkdir(parents=True, exist_ok=True)
        read_id_reading.to_csv(
            export_read_path, index=False
            )
        print(f"Exported to {export_read_path}")
    
choice = input("Count descriptors for entire dataset (1), isolate a user's readings (2), or display a specific reading (3)? ")

if choice == "1":
    total_descriptor_counter()
elif choice =="2":
    reading_data_by_user_id()
elif choice == "3":
    reading_data_by_id()