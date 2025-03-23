# TV Series IMDb Webscraper and Heatmaps
This project aims to create a web scraping package that can be used to scrape all episode information on a TV series from IMDb and export it into a csv for further analysis. I am using the libraries `Requests`, `bs4`, and `pandas` for this project. 

I will also further develop the code to automatically transform the data to prepare it for use in my **Heatmap** visual that I have built using `plotly.express`, explained below (code can be found in this repo).

## Webscraper
I created web scraping code

## Heatmap
I have developed two separate code templates for creating heatmap infographics.

This code will produce an infographic in the format below depending on inputs provided:

![got_hmap](https://github.com/user-attachments/assets/f400f9ec-642b-4aff-93dc-0277bd860d72)

This plots a title '{SERIES} by the numbers', calculates summary stats from the dataset and plots them as headline figures, and then plots the dataframe as a heatmap visual using a Red-Green colour scale. I have set a specific scaling for the colour scale so that the colouring will be consistent across all TV series that will be plotted through this code.

I have set this up so that there are only two constants that need changing in the code: `FILE` and `SERIES`. The file constant takes the filepath for the dataset you want to plot and the SERIES contstant takes the name of the TV series you want to plot in the infographic.

## Credits
I would like to credit Matt Barty for his video - https://www.youtube.com/watch?v=qNfxUsQ70QU which served as a guide for the development of my webscraping code.
