import pandas as pd
import mysql.connector
from collections import defaultdict

# Read the combined dataset
combined_df = pd.read_csv('data/combined_dataset.csv')

# Data cleaning and validation
combined_df = combined_df.dropna(subset=['EPISODE'])  # Remove rows with missing episode IDs
combined_df['EPISODE'] = combined_df['EPISODE'].astype(str)  # Ensure episode IDs are strings

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="adelknode",
    password="MU8myHoHo",
    database="joy_of_coding"
)

# Create a cursor object
cursor = mydb.cursor()

# Drop existing tables (if they exist)
cursor.execute("DROP TABLE IF EXISTS Episodes")
cursor.execute("DROP TABLE IF EXISTS Subjects")
cursor.execute("DROP TABLE IF EXISTS Colors")

# Create the Episodes table
cursor.execute("""
CREATE TABLE Episodes (
    EPISODE VARCHAR(10) PRIMARY KEY,
    Title VARCHAR(100),
    Month VARCHAR(20)
)
""")

# Create the Subjects table
cursor.execute("""
CREATE TABLE Subjects (
    EPISODE VARCHAR(10),
    Subject VARCHAR(50),
    PRIMARY KEY (EPISODE, Subject),
    FOREIGN KEY (EPISODE) REFERENCES Episodes(EPISODE)
)
""")

# Create the Colors table
cursor.execute("""
CREATE TABLE Colors (
    EPISODE VARCHAR(10),
    Color VARCHAR(50),
    PRIMARY KEY (EPISODE, Color),
    FOREIGN KEY (EPISODE) REFERENCES Episodes(EPISODE)
)
""")

# Create a defaultdict to store unique colors and subjects
unique_colors = defaultdict(lambda: len(unique_colors))
unique_subjects = defaultdict(lambda: len(unique_subjects))

# Insert data into Episodes table
for _, row in combined_df.iterrows():
    episode = row['EPISODE']
    title = row['Title'].strip() if pd.notnull(row['Title']) else ''  # Strip leading/trailing whitespaces
    month = row['Month'].strip() if pd.notnull(row['Month']) else ''  # Strip leading/trailing whitespaces

    sql = "INSERT INTO Episodes (EPISODE, Title, Month) VALUES (%s, %s, %s)"
    cursor.execute(sql, (episode, title, month))

# Insert data into Subjects table
for _, row in combined_df.iterrows():
    episode = row['EPISODE']
    subjects = [unique_subjects[s.strip()] for s in (
        "APPLE_FRAME,AURORA_BOREALIS,BARN,BEACH,BOAT,BRIDGE,BUILDING,BUSHES,CABIN,CACTUS,"
        "CIRCLE_FRAME,CIRRUS,CLIFF,CLOUDS,CONIFER,CUMULUS,DECIDUOUS,DIANE_ANDRE,DOCK,"
        "DOUBLE_OVAL_FRAME,FARM,FENCE,FIRE,FLORIDA_FRAME,FLOWERS,FOG,FRAMED,GRASS,GUEST,"
        "HALF_CIRCLE_FRAME,HALF_OVAL_FRAME,HILLS,LAKE,LAKES,LIGHTHOUSE,MILL,MOON,MOUNTAIN,"
        "MOUNTAINS,NIGHT,OCEAN,OVAL_FRAME,PALM_TREES,PATH,PERSON,PORTRAIT,RECTANGLE_3D_FRAME,"
        "RECTANGULAR_FRAME,RIVER,ROCKS,SEASHELL_FRAME,SNOW,SNOWY_MOUNTAIN,SPLIT_FRAME,"
        "STEVE_ROSS,STRUCTURE,SUN,TOMB_FRAME,TREE,TREES,TRIPLE_FRAME,WATERFALL,WAVES,"
        "WINDMILL,WINDOW_FRAME,WINTER,WOOD_FRAME"
    ).split(',') if s.strip()]

    for subject in subjects:
        sql = "INSERT INTO Subjects (EPISODE, Subject) VALUES (%s, %s)"
        cursor.execute(sql, (episode, subject))

# Insert data into Colors table
for _, row in combined_df.iterrows():
    episode = row['EPISODE']
    colors = [unique_colors[c.strip()] for c in (
        "Black_Gesso,Bright_Red,Burnt_Umber,Cadmium_Yellow,Dark_Sienna,Indian_Red,Indian_Yellow,"
        "Liquid_Black,Liquid_Clear,Midnight_Black,Phthalo_Blue,Phthalo_Green,Prussian_Blue,"
        "Sap_Green,Titanium_White,Van_Dyke_Brown,Yellow_Ochre,Alizarin_Crimson"
        ).split(',') if c.strip()]

    for color in colors:
        sql = "INSERT INTO Colors (EPISODE, Color) VALUES (%s, %s)"
        cursor.execute(sql, (episode, color))

# Commit changes and close the connection
mydb.commit()
cursor.close()
mydb.close()
