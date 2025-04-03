"""This module contains functions for the creation and saving of a heatmap infographic"""

import plotly.express as px
import pandas as pd

def shape_data(file):
    """
    Reads in csv and formats data for heatmap.
    
    Parameters
    ----------

    file: The csv file to be read in

    Returns
    ---------

    Formatted dataframe
    
    """
    df = pd.read_csv(file, index_col='Episodes')  # Need to set Episodes as index for the visualisation to work
    print(f"Data loaded: {df.head(3)}")
    print("Checking for null values")
    if df.iloc[:, -1].isnull().any():
        df = df.drop(df.columns[-1], axis=1)
        print(f"NULL column dropped: \n{df.head(3)}")
    # Renaming index and columns
    df.index = [f'Ep. {str(i[8:])}' for i in df.index]  # Rename index to Ep. 1 etc.
    df.columns = [f'S{str(i[-1])}' for i in df.columns]  # Rename columns to S1 etc.
    print(f"Dataframe processed: \n{df.head(3)}")

    return df
    

def create_heatmap(df, series_name):
    """
    Create a heatmap from a defined dataframe

    Parameters
    ----------

    df: A dataframe
    series_name: A constant defined in the main script

    Returns
    ----------

    A heatmap infographic
    """

    print(f"Creating heatmap for series: {series_name}")

    max = df.max().max()
    min = df.min().min()
    avg = round(df.mean().mean(),1)

# Create the heatmap
    fig = px.imshow(df, 
                color_continuous_scale='RdYlGn',
                color_continuous_midpoint=6.5,
                text_auto='True',
                title= f'<b>{series_name} by the numbers</b><br><sup>IMDb ratings by episode',
                aspect='auto')

    fig.update_xaxes(side="top")
    fig.update_coloraxes(cmin=3, 
                        cmax=10,
    )
    # Remove the colorbar
    fig.update_layout(coloraxis_showscale=False)

    # Remove axis titles, add grids, set fontstyle
    fig.update_layout(
        xaxis_title="",
        yaxis_title="",
        plot_bgcolor='#44546A',
        paper_bgcolor='#44546A',
        yaxis = dict(
            showgrid=False,
            linecolor='lightgray',
            tickfont=dict(color='#fafafa'),
            tickmode='array',  # This ensures all ticks are displayed
            ticks='outside',  # Make sure the ticks are outside for better readability
            ticklen=8,  # Optional: controls the length of the ticks
            tickcolor='#44546A',  # Color of ticks
            tickprefix='    ',  # Add space before labels to create padding
        ),
        xaxis = dict(
            showgrid=False,
            linecolor='lightgray',
            tickfont=dict(color='#fafafa'),
            tickmode='array',  # Add ticks to provide padding
            ticks='outside', 
            ticklen=8,  # Optional: controls the length of the ticks
            tickcolor='#44546A',  # Hide ticks
        ),
    font=dict(size=20, family='Trebuchet MS'),  # General font style
        title_font=dict(
            family="Trebuchet MS",  # Font family for the title
            size=34,
            color='#fafafa'         # Font size
    ),
    title_y=0.93,
    margin=dict(t=165, b=50),
    width = 900,
    height = 600)  # change plot size

    # Add annotations
    fig.update_layout(
        annotations=[
            # Add watermark
            dict(
                text="@WillsFilms",  # Text for watermark
                x=len(df.columns) / 2.2,  # x-position (edit as necessary)
                y=len(df) / 2.2,  # y-position (edit as necessary)
                showarrow=False,
                font=dict(
                    size=50,
                    color="rgba(0, 0, 0, 0.3)"  # Black with opacity (making it semi-transparent)
                ),
                align="center",
                valign="middle",
                opacity=0.15,  # Control transparency here
            ),
            # Add source
            dict(x=0, 
                y=-0.1, 
                xref="paper",
                yref="paper",
                showarrow=False, 
                text='Source: IMDb', 
                font=dict(size=14, color='#fafafa', style='italic'),
                align='right',
                xanchor='right',
                yanchor='bottom'),
            # Add Average rating
            dict(
                text=f'Average Rating: {avg}',
                x= 0.35,
                y= 1.12,
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(size=24, color='#fafafa', style='italic'),
                align='right',
                xanchor='right',
                yanchor='bottom'),
            # Add max rating
            dict(
                text=f'Max Rating: {max}',
                x= 0.65,
                y= 1.12,
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(size=24, color='#fafafa', style='italic'),
                align='right',
                xanchor='right',
                yanchor='bottom'),
            # Add min rating
            dict(
                text=f'Min Rating: {min}',
                x= 0.95,
                y= 1.12,
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(size=24, color='#fafafa', style='italic'),
                align='right',
                xanchor='right',
                yanchor='bottom'),

        ]
            )

    return fig

def save_heatmap(fig, series_name):  
    """
    Saves heatmap to png

    Parameters
    ----------

    fig: figure returned by create_heatmap
    series_name: a string representing the name of the series
    """
    print(f"Saving heatmap for series: {series_name}")
    fig.write_image(f"{series_name}_hmap.png")

# Master function
def create_and_save_heatmap(file_path, series_name):
    """
    Creates and saves a heatmap infographic

    Parameters
    ----------

    file_path: The file path for the data to use (must be csv)
    series_name: The name of the series you are plotting
    """
    print(f"Loading data from {file_path} for series {series_name}")

    df = shape_data(file_path)
    print(f"Data shaped. Dataframe head: \n{df.head(3)}")
    
    fig = create_heatmap(df, series_name)
    print("Heatmap created successfully")
    
    save_heatmap(fig, series_name)
    print("Heatmap saved successfully")
