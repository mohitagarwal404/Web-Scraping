# Web Scraping Tool

Welcome to the Web Scraping Data Extraction project! 
This Python script leverages the `requests`, `BeautifulSoup`, and `json` libraries to scrape and extract data from a website. 
The script focuses on gathering information related to any category in a specific location and category.

## Usage

1. **Install Dependencies:**
   - Make sure you have Python installed on your system.
   - Install the required libraries using the following command:
     ```bash
     pip install requests beautifulsoup4 pandas
     ```

2. **Configure Script:**
   - Replace `'Your url'` with the actual base URL of the website you are scraping.
   - Modify the `cat_list` variable to include the categories you are interested in.

3. **Run the Script:**
   - Execute the script using the following command:
     ```bash
     python script.py
     ```
   - The script will start extracting data from the specified website.

## Script Overview

### 1. Initialization

The script begins by importing necessary libraries (`requests`, `time`, `BeautifulSoup`, `json`, `re`, and `pandas`).

### 2. Configuration

- `urlsArr`: List to store profile URLs.
- `page_no`: Variable to track the current page number.
- `page_end`: Variable to store the total number of pages for a category.
- `location`: Variable indicating the target location.
- `cat_list`: List of categories to scrape.

## Note

- The script is tailored to the structure of the target website. Ensure that the HTML structure remains consistent for accurate data extraction.
- Adjustments to the script may be necessary based on changes in the website's structure.

