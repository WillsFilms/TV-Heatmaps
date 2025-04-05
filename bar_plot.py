import pandas as pd
import plotly.express as px

def prep_season_stats(df):

    results = {}

    for column_name, column_data in df.items():
        max_value = round(column_data.max(),1)
        min_value = round(column_data.min(),1)
        avg_value = round(column_data.mean(),1)
        
        results[column_name] = {'Max': max_value, 'Min': min_value, 'Average': avg_value}

    # Convert the dictionary into a DataFrame to display the results
    stats_df = pd.DataFrame(results)

    stats_df_bar = stats_df.transpose().reset_index()

    return stats_df_bar


def create_bar(stats_df_bar, series):

    bar = px.bar(stats_df_bar,
                x='index',
                y='Average',
                title= f'<b>{series} seasons by average IMDb rating<b>',
                labels={'Average': 'Average'},
                template='simple_white')

    bar.update_layout(
        xaxis_title="",
        yaxis_title="",
        plot_bgcolor='#44546A',
        paper_bgcolor='#44546A',
        yaxis = dict(
            showgrid=True,
            gridcolor='lightgray',
            linecolor='lightgray',
            tickcolor='lightgray',
            tickfont=dict(color='#fafafa'),
            range=[0,10.1]
        ),
        xaxis = dict(
            showgrid=False,
            linecolor='lightgray',
            tickcolor='lightgray',
            tickfont=dict(color='#fafafa'),
        ),
    font=dict(size=20, family='Trebuchet MS'),  # General font style
        title_font=dict(
            family="Trebuchet MS",  # Font family for the title
            size=30,
            color='#fafafa'         # Font size
    ),
    title_y=0.94,
    margin=dict(t=120),
    width = 800,
    height = 600)  # change plot size

    # Update the bar trace to add data labels (values) to the bars
    bar.update_traces(
        text=stats_df_bar['Average'],  # Add IMDb Score as text labels on bars
        textposition='inside',  # Position the text inside the bars
        texttemplate='%{text}',  # Format the text to show the values
        insidetextanchor='end',  # Align text at the start of the bars (can use start, middle or end)
        textfont = dict(
            size=14,
            weight='bold'
        )
    )
    # Update bar colour
    bar.update_traces(
        marker=dict(color='#cfd0b5'
    ))

    # Add watermark
    bar.update_layout(
        annotations=[
            # Watermark
            dict(
                text="@WillsFilms",  # Text for watermark
                x=5,  
                y=len(stats_df_bar)/2,  
                showarrow=False,
                font=dict(
                    size=50,
                    color="rgba(0, 0, 0, 0.3)"  
                ),
                align="center",
                valign="middle",
                opacity=0.15,  
            ),
            dict(x=-0.2, 
                y=-0.15, 
                xref="paper",
                yref="paper",
                showarrow=False, 
                text='Source: IMDb', 
                font=dict(size=14, color='lightgray', style='italic'),
                align='right',
                xanchor='right',
                yanchor='bottom')
        ]
            )

    return bar

# Master function

def prep_and_create_bar(df, series):

    prep_season_stats(df)

    create_bar