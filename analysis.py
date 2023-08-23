import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import streamlit as st


# Load your DataFrame (replace this with your actual data)
df = pd.read_csv('./ViratKohli.76centuries.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df['Strike Rate'] = df['Strike Rate'].fillna(
    df.groupby('Format')['Strike Rate'].transform('mean'))
df['Year'] = pd.to_datetime(df['Date'])
df['Year'] = df['Year'].dt.year


# Create a layout with two columns
col1, col2 = st.columns(2)

# Widgets in the first column
with col1:
    st.image('./Virat_Kohli.png', width=200,  use_column_width=200)
    st.text("Virat Kohli")
    st.text('Born:5 November 1988 (age 34)')

# Widgets in the second column
with col2:
    st.write("Virat Kohli is an Indian international cricketer and the former captain of the Indian national cricket team. Widely regarded as one of the greatest batsmen in the history of the sport. Kohli holds numerous records in his career which includes scoring most runs in T20 internationals and IPL, fastest to reach 10,000 ODI runs. In 2020, the International Cricket Council named him the male cricketer of the decade. Kohli has also contributed to India's successes, including winning the 2011 World Cup and the 2013 Champions trophy. He is among the only four Indian cricketers who has played 500 matches for India")


# App title and picture
st.title("Virat Kohli Centuries Analysis")
st.sidebar.image('Bro_code logo.png', width=150)


# Slicer for choosing the Format
selected_format = st.sidebar.selectbox(
    "Choose Format", ["All format", "ODI", "Test", "T20I"])

# Filter the DataFrame based on the selected Format
if selected_format == "All format":
    filtered_df = df
else:
    filtered_df = df[df['Format'] == selected_format]
st.write('`Choose the format from sidebar for analysis according to each format`')
# # Show the filtered DataFrame with infinite scroll
st.dataframe(filtered_df, height=300, hide_index=True)

# Graph 3
st.subheader("Number of hundred in every format")
fig3 = px.bar(filtered_df.groupby('Format', as_index=False)['Score'].count().sort_values(by='Score', ascending=False), x='Format',
              y='Score', text='Score', color='Format', labels={'Score': 'count'},  title='<b>Hundreds over the formats</b>')
st.plotly_chart(fig3)

# Graph 1
st.subheader("Number of Hundreds Against each  Team  ")

fig1 = px.bar(filtered_df.groupby(['Against'], as_index=False)['Score'].count().sort_values(by='Score', ascending=False),
              x='Against', y='Score', color='Against', text="Score",
              labels={'Score': 'Count'}, template='ggplot2', title=f'<b>Number of Hundreds Against each Team in {selected_format} </b>')
st.plotly_chart(fig1)


# Graph 2
st.subheader("Number of hundreds over year in every Format")
fig2 = px.bar(filtered_df.groupby(['Format', 'Year'], as_index=False)['Score'].count(), x='Year', y='Score', text='Score', labels={
              'Score'}, color='Format', template='seaborn', title=f'<b>Hundreds over the years in {selected_format}</b>')
# Add annotation for the pandemic year (2020)
fig2.add_annotation(
    x=2020,
    text="Pandemic Year",
    showarrow=True,
    arrowhead=5,
    arrowcolor="red",
    ax=0, ay=-50  # Adjust the arrow position and direction
)

st.plotly_chart(fig2)

# Graph 4
st.subheader("Strike Rate over every Format")
fig4 = px.bar(filtered_df.groupby('Format', as_index=False)['Strike Rate'].mean(
), x='Format', y='Strike Rate', color='Format', title=f'<b>Strike Rate When Kohli Hits a Ton across {selected_format}</b>', width=500)
# fig4.update_layout(title_x=0.5, margin=dict(l=10, r=10, t=40, b=20))
st.plotly_chart(fig4)

# Graph5
st.subheader("Virat as Captain")
fig5 = px.bar(filtered_df.groupby(['Captain', 'Result'], as_index=False)['Score'].count(), x='Captain', y='Score', color='Result', text='Score', labels={
              'Out/Not Out': 'result', 'Score': 'Century'}, template='ggplot2', title='<b>Match Result Based on Virat\'s Hundred when he was Captain</b>', height=700)
st.plotly_chart(fig5)
# Graph6
st.subheader("Centuries in each countries")
fig6 = px.choropleth(filtered_df.groupby('Against', as_index=False)['Score'].count(), locations='Against', locationmode='country names', color='Score', labels={
                     'Score': 'Count'}, hover_data=['Score'], template='plotly', title=f'<b>Map View of Kohli\'s Centuries against opponents in{selected_format}')

st.plotly_chart(fig6)


# Graph 7
st.subheader("Virat Kohli's Score at each venues against every team")
fig7 = px.treemap(filtered_df, path=[px.Constant('Virat Kohli\'s centuries'), 'Against', 'Venue', 'Score'], hover_name='Against', hover_data=[
                  'Year'], template='plotly_dark', title=f'<b>TreeMap of Kohli\'s centuries in different stadiums in {selected_format}')
fig7.update_layout(margin=dict(l=20, r=20, t=60, b=20))
fig7.update_traces(root_color='Skyblue')
st.plotly_chart(fig7)

# Graph 8
st.subheader("Impact of his century on match result over every format")
fig8 = px.sunburst(df.groupby(['Format', 'Against', 'Result'], as_index=False)['Score'].count(), path=[
                   'Format', 'Result', 'Against'], values='Score', color='Result', title='<b>Match results over the formats when Kohli scored a Hundred</b>')
fig8.update_layout(margin=dict(l=20, r=20, t=30, b=20))

st.plotly_chart(fig8)
st.sidebar.markdown(
    """
    <div style = "position: absolute; display:flex; top:250px;">
    <a   href  = "shivjha1226@gmail.com" target                                      = "_blank">
    <img src   = "https://portfolio-shivi.netlify.app/assets/man-3224c7f9.png" width = 60 />
    </a>
    <p style = "font-size: 15px; color: Green;">Bro_CODE <br  style="margin-top:0;"/>Shivnandan Jha</p>   </div>
    <div style = "position: absolute; display:flex; gap:20px; top:300px;  margin-left:21px;">
    <a   href  = "https://www.linkedin.com/in/shiv-nandan-jha-4179a4251" target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               = "_blank">
    <img src   = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAABcCAMAAADUMSJqAAAAYFBMVEUAd7f///8AcbQAdbYAa7KXu9nP4O3M3OsAc7Xl7/YAbrOQttdzpc5MjcH0+fuuyOBnnMkog73s9Pm0zeN9rNK80+aIsdQAaLFYlcbc5vGfv9s/icDF2uode7kof7sAYq7hDdldAAACZklEQVRoge2a27KjIBBF5RKDreL9njj//5djkokjIIZTaR5OlbsqDwFdhW2zG0ICskhmeREgqsgz+eAGy6cKQDBMOBMQVC94yzHBb/H2Aa+8sBd6RQLpB/2QDDLwxYYsyIUvuMiDAjVPtmKo6e0gARyAUx8PJLo+G6JoGKcOHQ99RP4pLCgum1/IRjlqloLCXuiIYxc90XTHg9NIhzdovsNynU3IjJUyUJnwGivqnRGVpY5gJUwnTfjtd8AHE47m9pCZ8ATrhYrUhOPNIjDiglgDxaSxJaarQ63CU9T6Csl23BOyodPiusb7jr4uYHyOmzCsauFnPUOBc/BSoL2KbfShlT0fcZHjczKY0lUFsDfFbF3Ic5uFUSllOTSX1IF/Vyz99kpFNit2GT42CpTFqvuX4/whA3TrSp7JCI3aWlPGk9L0oQscDp5ftcufQ+eh2hrTvYK4aDicGY7wP7dd9hIbdjB2N3i74/vvsR9s3Nzg2ldFmX2h4wY/VG8NOwI8tCYkApxMtqhjwK2VEQMuO49wa1x+AC8v/TT1444LtJbi6A6PORWMCdqNRldjCbozvF7nCr/ofYNlHrnCt/Ow03ttBuMK3zqIsZGS81cjV1KZGTspS7o4wtW79VpC0m/gpeqrtNXgFu9yg1/VXBOJ2k0sv+C4wTX3MN5o8g08Vqcg0/cMJ/yEn/ATfsJP+Ak/4S+4tjVGhesrs9fCjI57rf/hQoPb9i0wRhu9f2uFatva6jsHkQ57d+3Qga7i61WbRgrmveJDvyd5PfjzemTp9bDV3zExk34PuP0ezRNSMX9/KvD3d4i/QB8pnxFRoRMAAAAASUVORK5CYII=" alt = "LinkedIn", width = 30/>
    </a>
     <a   href = "https://github.com/ShivNandanJha" target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               = "_blank">
<img src="data:image/png;base64,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", width=30/>
    </a>
    </div>
   
    """,
    unsafe_allow_html=True,
)
hide_streamlit_style = """
            <style>
             footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.write("Made with `♥`  by `Bro_CODE` Shivnandan Jha")