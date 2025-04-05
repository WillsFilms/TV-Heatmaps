# TV Series IMDb Heatmaps
This project has created a code package that will create a heatmap infographic for a given TV series, plotting out the IMDb ratings per episode and season.

## Heatmap
The `main.py` script will create a heatmap infographic when run.

This code will produce an infographic in the format below depending on inputs provided in the `main.py` script:

![Game of Thrones_hmap](https://github.com/user-attachments/assets/a3aff4c3-0b65-498e-a0c1-62d93e608da8)

This plots a title '{SERIES} by the numbers', calculates summary stats from the dataset and plots them as headline figures, and then plots the dataframe as a heatmap visual using `lmplot` from the `plotly.express` package using a Red-Green colour scale. I have set a specific scaling for the colour scale so that the colouring will be consistent across all TV series that will be plotted through this code. Therefore, a 7.5 which is the minimum for one TV series will have the same colour as a 7.5 that is the maximum for another.

I have set the code up so that there are only two constants that need changing in the `main.py` script: `FILE` and `SERIES`. The `FILE` constant takes the filepath for the dataset you want to plot and the `SERIES` constant takes the name of the TV series you want to plot in the infographic. All processing functions take these constants and apply them to the `create_and_save_heatmap` function that is imported from the `data_load.py` module.

## Input data
The data used for input must be in a specific format for this code to work as intended. I have provided some sample datasets within the `Data` folder in this repository, as well as a structured schema for the format your data must be in:

![image](https://github.com/user-attachments/assets/72c8d7a9-68a7-4303-94a2-f44d69ab04ed)

## Future Plans
I would like to develop this infographic to include a breakdown of average ratings by season to be included alongside the heatmap in a separate column. I have developed code to produce this as a bar chart but need to test and incorporate this into the main program.
