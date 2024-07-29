# AltNews.in Web Scraping Project
This repository contains a Python-based web scraping project focused on extracting fact-checking data from [AltNews.in](https://www.altnews.in/). The project utilizes a combination of Python, Scrapy, and Selenium to navigate through the dynamic content of AltNews.in and collect valuable information for analysis and verification.

## Motivation
In an era where information is abundant, distinguishing between truth and misinformation is crucial. AltNews.in, a platform dedicated to fact-checking and debunking fake news, serves as a valuable source for combating misinformation. This web scraping project aims to empower users by providing a tool to analyze and verify news, contributing to a more informed society.

## Key Features

1. **Dynamic Content Handling**: Utilizes Scrapy and Selenium to navigate AltNews.in's dynamic content, ensuring comprehensive extraction of fact-checking data.

2. **Efficient File Management**: Dynamically creates directories for organized storage of scraped data, enhancing efficiency and providing a structured approach to data handling.

3. **Fact-Checking Data Extraction**: Meticulously collects details such as author names, saying dates, headlines, rulings, publishers, and article URLs for in-depth fact-checking analysis.

4. **CSV Repository**: Writes data to a CSV file, serving as a comprehensive repository for easy access and analysis of fact-checking information.

5. **Individual Text Files for Articles**: Optimizes organization by writing each fact-checking article to a text file, providing detailed information for in-depth analysis and reference.



## Requirements
- **Python 3.x**
- **Scrapy**
- **Pandas**
- **Fiddler**

## Getting Started
1. **Clone the Repository:**
    ```
    git clone https://github.com/Muneeb1030/WebScrapper_AltNews.git
    ```

2. **Install Dependencies:**
    ```
    pip install scrapy selenium pandas
    ```


3. **Run the Scraper:**
    ```
    scrapy crawl altnews
    ```

## Additional Information
- **Customization:**
    - Tailor the scraper to your needs by modifying the Scrapy spiders.
- **GitHub Repository:**
    - Explore, contribute, and stay updated on the [GitHub repository](https://github.com/Muneeb1030/WebScrapper_AltNews.git).
  
## Disclaimer
This project is intended for educational purposes and strictly adheres to Altnew's terms of service. Users are advised to deploy the scraper responsibly and in compliance with platform policies.

## Contributors
- M Muneeb ur Rehman

Feel free to fork, contribute, and enhance the capabilities of this AltNews scraper. Happy scraping! 🌐💻


