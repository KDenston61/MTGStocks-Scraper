# Import the necessary libraries
import requests   # library for making HTTP requests
import json       # library for working with JSON data
import re         # library for working with regular expressions
from datetime import datetime   # library for working with dates and times
import csv        # library for working with CSV files
import os         # library for working with the operating system
import pandas as pd   # library for data manipulation and analysis

# Prompt the user to choose between "sealed", "sets", or "prints"
choice = input("Enter your choice (sealed/sets/prints): ")

def csv_write(card,date,file):
    """
    Write card data to a CSV file
    """
    # Check if the file exists and is empty
    prewrite = False
    try:
        if os.stat("%s.csv"%file).st_size == 0:
            prewrite=True
    except OSError:
        prewrite=True
    
    # If the file is empty or does not exist, add the headers to the CSV file
    if(prewrite):
        with open("%s.csv"%file,"a") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "date", "rarity", "avg_price", "foil", "market", "market_foil"])

    # Extract relevant data from the card dictionary
    name = card["name"]
    avg_price = card["latest_price"]["avg"]
    foil = card["latest_price"]["foil"]
    market = card["latest_price"]["market"]
    market_foil = card["latest_price"]["market_foil"]
    rarity = card["rarity"]
    row = [name, date, rarity, "$%s"%avg_price, "$%s"%foil, "$%s"%market, "$%s"%market_foil]

    # Write the row to the CSV file
    with open("%s.csv"%file,"a") as f:
        writer = csv.writer(f)
        writer.writerow(row)


# Define the API endpoint URL based on the user's choice
if choice == "sealed":
    url = "https://api.mtgstocks.com/sealed"
elif choice == "sets":
    url = "https://api.mtgstocks.com/card_sets"
elif choice == "prints":
    url = "https://api.mtgstocks.com/prints"
else:
    print("Invalid choice.")
    exit()

# Prompt the user to enter a new number
number = input("Enter a number: ")

# Add the number to the URL
url += f"/{number}"

# Define the headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Make an HTTP GET request to the endpoint with the headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:

    # Retrieve the data from the response as a JSON object
    data = response.json()

    # Create a new dictionary with only the desired key-value pairs
    if choice == "sealed":
        new_data = {
            "Name": data["name"],
            "Latest Prices": data["latestPrice"]
        }
    elif choice == "sets":
        new_data = {
            "Name": data["name"],
            #"In The Set": data["prints"]
        }
        # Iterate over each card in the "prints" section of the JSON data and write its information to a CSV file
        for card in data["prints"]:
    # Call the csv_write function to write the card's information to the CSV file
    # Also pass the date and slug information to the function
            csv_write(card, datetime.utcfromtimestamp(data["date"]/1000).strftime('%Y-%m-%d'), data["slug"])

        # Read the CSV file for the specified slug using pandas and store the data in a DataFrame object
        df = pd.read_csv(f"{data['slug']}.csv")

        # Write the DataFrame object to an Excel file with the same slug name
        writer = pd.ExcelWriter(f"{data['slug']}.xlsx")
        df.to_excel(writer, index=False)
        writer._save()

# If the user selected "prints" as the choice
    elif choice == "prints":
        # Convert the Unix timestamp for the latest price to a human-readable date and time format
        data["latest_price"]["date"] = datetime.utcfromtimestamp(data["latest_price"]["date"]/1000).strftime('%Y-%m-%d %H:%M:%S')
        # Create a new dictionary containing the name and latest price information for the card
        new_data = {
        "Name": data["name"],
        "Prices": data["latest_price"]
    }
    # Convert the new dictionary to a JSON string with an indent of 2
    json_string = json.dumps(new_data, indent=2)
    # Remove the curly braces from the string using regex
    json_string = re.sub(r"[{}]", "", json_string)
    # Print the modified JSON string to the console
    print(json_string)

# If the request was not successful, print the HTTP status code
else:
    print(f"Error: {response.status_code}")


