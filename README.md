# web-scraping
# Project Name: Pakistani Wheat Prices Scraper

### 1. Project Overview
* **Target Website:** https://kissanstore.pk/wheat-price-in-pakistan/
* **Data Fields Extracted:** Location, Retail Price (PKR), Wholesale Price (PKR)
* **Tools Used:** Python, BeautifulSoup, Requests, Pandas
* **Purpose:** Scrape and analyze wheat price data across different regions in Pakistan to provide market insights

### 2. Setup Instructions

1. Clone this repo:
   git clone [https://github.com/salihaafarooq/web-scraping]
  

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Run the scraper:**
   python scraper.py
  

### 3. Challenges & Solutions

**Challenge:** Finding the correct HTML element structure
- **Solution:** Used BeautifulSoup's `find_all()` method with both 'td' and 'th' selectors to handle different table cell types. Some locations use header cells instead of data cells.


