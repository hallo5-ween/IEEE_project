import pandas as pd

# Load the CSV file
file_path = "combined_data_#.csv"  
df = pd.read_csv(file_path)

# Ensure columns exist
if 'Article Title' in df.columns and 'Article Link' in df.columns:
    # Filter rows where the title contains "meta-analysis" (case-insensitive)
    filtered = df[df['Article Title'].str.contains("meta-analysis", case=False, na=False)]
    
    # Output results
    for _, row in filtered.iterrows():
        print(f"{row['Article Title']}: {row['Article Link']}")
else:
    print("Error: The CSV file must contain 'title' and 'link' columns.")
