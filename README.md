# YouTube Comments Sentiment Analysis

## Overview
This project analyzes YouTube comments using Python and Natural Language Processing (NLP) to identify positive, negative, and neutral sentiments.

## Dataset
- File: `UScomments.csv`
- Data: YouTube comments

## Technologies Used
- Python
- Pandas
- NumPy
- TextBlob
- Matplotlib
- WordCloud
- Emoji

## Workflow
1. Data Loading
2. Data Checking and Cleaning
3. Exploratory Data Analysis (EDA)
4. Sentiment Analysis using TextBlob
5. Sentiment Classification
6. Positive, Negative, and Neutral Word Clouds
7. Emoji Extraction and Frequency Analysis
8. Data Visualization

## Sentiment Classification
- Polarity greater than `0.3`: Positive
- Polarity less than `-0.3`: Negative
- Polarity between `-0.3` and `0.3`, including both boundaries: Neutral

## Visualizations
- Sentiment distribution chart
- Positive Word Cloud
- Negative Word Cloud
- Neutral Word Cloud
- Top 10 most-used emojis chart

## How to Run
1. Install the required Python libraries.
2. Place the dataset in the notebook's working directory.
3. Open the notebook in Jupyter Notebook.
4. Run the cells in order.

## Author
Nija Lathiya
