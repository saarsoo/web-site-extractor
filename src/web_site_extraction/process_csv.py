from pandarallel import pandarallel
import pandas as pd

from web_site_extraction.extract_article_number import extract_article_number

pandarallel.initialize(progress_bar=True)


# Function to process a CSV file and extract article numbers
def process_csv(input_file, output_file):
    # Load the CSV file
    data = pd.read_csv(input_file, delimiter=";")

    # Extract URLs
    if "URL" not in data.columns:
        print("No 'URL' column found in the input CSV.")
        return

    urls = data["URL"]

    # Extract article numbers for each URL
    data["Artikelnummer"] = urls.parallel_apply(extract_article_number)

    # Save the updated data to a new CSV file
    data.to_csv(output_file, index=False, sep=";", quotechar='"')
    print(f"Processed data saved to {output_file}")
