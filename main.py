"""This script will create and export a heatmap infographic for a given series"""

# import packages needed
import plotly.express as px
import pandas as pd

# import modules
from data_load import create_and_save_heatmap

# ------ CONSTANTS ------ #

# Update with the name of the series
SERIES = "Friends"
# Update with the filepath of the csv for the heatmap
FILE_PATH = "Data/friends.csv"
# Update with the IMDb episode web link for the webscraper
# WEB_LINK = "xxx"

print(f"Starting analysis for {SERIES} using data from {FILE_PATH}")

# Run the heatmap creator
create_and_save_heatmap(FILE_PATH, SERIES)