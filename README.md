# real-state-data-scrapper-zillow
This repository is created for the assessment test of SlashByte Studio

## Overview
This Python script allows users to scrape real estate data from Zillow for a specified location. It retrieves property details such as price, address, and URL and saves the data in a JSON format.

## Dependencies
- Python 3.x
- `requests` library
- `BeautifulSoup` from `bs4`
- `json`
- `os`

## Setup
1. **Install Dependencies:**
```
pip install requests beautifulsoup4
```

2. **Execution:**
- Update the `location` variable in the main section (`__main__`) of the script to your desired city (default: 'austin').
- Run the script in a Python environment.

## Code Structure
- **`RealEstateScraper` Class:**
- Initializes with a default location (Delaware) or the specified location.
- `get_real_estate_data()`: Scrapes real estate data from Zillow based on the provided location.

- **`DataProcessor` Class:**
- `save_to_json(data, filepath)`: Saves the scraped real estate data into a JSON file at the specified filepath.

- **Main Execution:**
  - Initializes the `RealEstateScraper` with the specified location.
  - Retrieves real estate data using the scraper.
  - Saves the obtained data into a JSON file (`real_estate_data.json`) at the current working directory.

## Usage
- Update the `location` variable in the script's main section to target a specific city or area for real estate data retrieval.
- Run the script to execute the data scraping process.
- The JSON file (`real_estate_data.json`) will be generated in the current working directory containing the scraped real estate information.

