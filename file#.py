import pandas as pd

# Load the CSV file into a pandas DataFrame
# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('combined_data_#.csv')

# Define the keyword you are looking for
keyword = 'meta-analysis'

# Filter rows where the title contains the keyword (case-insensitive)
matching_articles = df[df['Article Title'].str.contains(keyword, case=False, na=False)]

# Output the links of the articles that match the keyword
if not matching_articles.empty:
    print("Articles containing the keyword '{}':".format(keyword))
    for link in matching_articles['Article Link']:
        print(link)
else:
    print(f"No articles found with the keyword '{keyword}' in the title.")
