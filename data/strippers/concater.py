import pandas as pd

# Read the three datasets
df1 = pd.read_csv('episode_month.csv')
df2 = pd.read_csv('episode_subject.csv')
df3 = pd.read_csv('The Joy Of Painiting - Colors Used.csv')

# Combine the datasets
combined_df = pd.concat([df2[['EPISODE']], df1, df2.drop(['EPISODE', 'TITLE'], axis=1), df3.drop(['num', 'painting_index', 'img_src', 'painting_title', 'season', 'episode', 'num_colors', 'youtube_src', 'colors', 'color_hex'], axis=1)], axis=1)

# Set 'EPISODE' as the primary key
combined_df = combined_df.set_index('EPISODE')

# Save the combined dataset to a new CSV file
combined_df.to_csv('combined_dataset.csv')