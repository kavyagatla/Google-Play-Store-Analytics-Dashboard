import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pytz

# --- GLOBAL SETTINGS ---
st.set_page_config(page_title="Gatla Kavya - Internship Dashboard", layout="wide")
ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist)
current_hour = current_time.hour

st.title("📊 Google Play Store Analytics Dashboard")
st.info(f"🕒 Current IST Time: {current_time.strftime('%H:%M:%S')}")


# --- DATA LOADING & CLEANING ---
@st.cache_data
def load_and_clean_data():
    try:
        df = pd.read_csv("Play Store Data.csv")
    except FileNotFoundError:
        st.error("Error: 'Play Store Data.csv' not found!")
        return pd.DataFrame()

    def clean_size(size):
        if isinstance(size, str):
            if 'M' in size: return float(size.replace('M', ''))
            if 'k' in size: return float(size.replace('k', '')) / 1024
            if size == 'Varies with device': return 0.0
        try: return float(size)
        except: return 0.0

    def clean_installs(inst):
        if isinstance(inst, str):
            clean_val = inst.replace(',', '').replace('+', '')
            try: return float(clean_val)
            except: return 0.0
        return 0.0

    df['Size_MB'] = df['Size'].apply(clean_size)
    df['Installs_Numeric'] = df['Installs'].apply(clean_installs)
    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce').fillna(0)

    # Android Version Clean
    df['Android_Ver_Clean'] = df['Android Ver'].str.extract(r'(\d+\.?\d*)')[0].astype(float)

    if 'sentiment_subjectivity' not in df.columns:
        df['sentiment_subjectivity'] = 0.6

    return df

df = load_and_clean_data()

# --- SIDEBAR ---
selection = st.sidebar.radio("Navigation", [
    "Home",
    "Task 1",
    "Task 2",
    "Task 3",
    "Task 4",
    "Task 5",
    "Task 6"
])

# --- HOME ---
if selection == "Home":
    st.success("Select a task from sidebar")

# --- TASK 1 ---
elif selection == "Task 1":
    if 17 <= current_hour < 19:
        categories = ['GAME','BEAUTY','BUSINESS','COMICS','COMMUNICATION','DATING','ENTERTAINMENT','SOCIAL','EVENTS']

        df1 = df[
            (df['Rating'] > 3.5) &
            (df['Category'].str.upper().isin(categories)) &
            (df['Reviews'] > 500) &
            (~df['App'].str.contains('S', case=False)) &
            (df['sentiment_subjectivity'] > 0.5) &
            (df['Installs_Numeric'] > 50000)
        ].copy()

        trans = {'BEAUTY': 'सौंदर्य', 'BUSINESS': 'வணிகம்', 'DATING': 'Dating-Service'}
        df1['Category_Display'] = df1['Category'].str.upper().replace(trans)

        color_map = {}
        for cat in df1['Category_Display'].unique():
            color_map[cat] = 'pink' if cat.upper() == 'GAME' else 'blue'

        fig = px.scatter(df1, x="Size_MB", y="Rating",
                         size="Installs_Numeric",
                         color="Category_Display",
                         color_discrete_map=color_map,
                         hover_name="App")

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Visible only 5PM–7PM")

# --- TASK 2 ---
elif selection == "Task 2":
    if 18 <= current_hour < 20:
        df2 = df[~df['Category'].str.upper().str.startswith(('A','C','G','S'))]

        top5 = df2.groupby('Category')['Installs_Numeric'].sum().nlargest(5).reset_index()

        top5['Highlight'] = top5['Installs_Numeric'] > 1_000_000
        top5['Country_Code'] = 'IND'

        fig = px.choropleth(top5,
                            locations="Country_Code",
                            color="Installs_Numeric",
                            hover_name="Category")

        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(top5)
    else:
        st.error("Visible only 6PM–8PM")

# --- TASK 3 ---
elif selection == "Task 3":
    if 18 <= current_hour < 21:
        df3 = df[
            (~df['App'].str.lower().str.startswith(('x','y','z'))) &
            (df['Category'].str.upper().str.startswith(('E','C','B'))) &
            (df['Reviews'] > 500) &
            (~df['App'].str.contains('S', case=False))
        ].copy()

        df3['Last Updated'] = pd.to_datetime(df3['Last Updated'], errors='coerce')
        df3 = df3.dropna()

        df3_group = df3.groupby([df3['Last Updated'].dt.to_period('M'),'Category'])['Installs_Numeric'].sum().reset_index()
        df3_group['Last Updated'] = df3_group['Last Updated'].dt.to_timestamp()

        df3_group['Growth'] = df3_group.groupby('Category')['Installs_Numeric'].pct_change()

        fig = px.line(df3_group, x="Last Updated", y="Installs_Numeric", color="Category")

        for _, r in df3_group[df3_group['Growth'] > 0.20].iterrows():
            fig.add_vrect(x0=r['Last Updated']-pd.DateOffset(days=15),
                          x1=r['Last Updated']+pd.DateOffset(days=15),
                          fillcolor="green", opacity=0.2)

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Visible only 6PM–9PM")

# --- TASK 4 ---
elif selection == "Task 4":
    if 16 <= current_hour < 18:
        df4 = df[
            (df['Rating'] >= 4.2) &
            (~df['App'].str.contains(r'\d')) &
            (df['Category'].str.upper().str.startswith(('T','P'))) &
            (df['Reviews'] > 1000) &
            (df['Size_MB'].between(20,80))
        ].copy()

        df4['Last Updated'] = pd.to_datetime(df4['Last Updated'], errors='coerce')
        df4 = df4.dropna()

        area = df4.groupby([df4['Last Updated'].dt.to_period('M'),'Category'])['Installs_Numeric'].sum().reset_index()
        area['Last Updated'] = area['Last Updated'].dt.to_timestamp()

        area['Growth'] = area.groupby('Category')['Installs_Numeric'].pct_change()

        fig = px.area(area, x="Last Updated", y="Installs_Numeric", color="Category")

        for _, r in area[area['Growth'] > 0.25].iterrows():
            fig.add_vrect(x0=r['Last Updated']-pd.DateOffset(days=15),
                          x1=r['Last Updated']+pd.DateOffset(days=15),
                          fillcolor="red", opacity=0.2)

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Visible only 4PM–6PM")

# --- TASK 5 ---
elif selection == "Task 5":
    if 15 <= current_hour < 17:
        df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

        df5 = df[
            (df['Rating'] >= 4.0) &
            (df['Size_MB'] > 10) &   # FIXED
            (df['Last Updated'].dt.month == 1)
        ]

        top10 = df5.groupby('Category').agg({
            'Rating':'mean','Reviews':'sum','Installs_Numeric':'sum'
        }).nlargest(10,'Installs_Numeric').reset_index()

        fig = px.bar(top10, x="Category", y=["Rating","Reviews"], barmode="group")

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Visible only 3PM–5PM")

# --- TASK 6 ---
elif selection == "Task 6":
    if 13 <= current_hour < 14:

        df['Price_Clean'] = (
            df['Price']
            .astype(str)
            .str.replace('$', '', regex=False)
        )

        df['Price_Clean'] = pd.to_numeric(df['Price_Clean'], errors='coerce').fillna(0)

        df['Revenue'] = df['Installs_Numeric'] * df['Price_Clean']

        df6 = df[
            (df['Installs_Numeric'] >= 10000) &
            (df['Revenue'] >= 10000) &
            (df['Size_MB'] > 15) &
            (df['Content Rating'] == 'Everyone') &
            (df['App'].str.len() <= 30) &
            (df['Android_Ver_Clean'] > 4.0)
        ]

        top3 = df6.groupby('Category')['Installs_Numeric'].sum().nlargest(3).index
        df6 = df6[df6['Category'].isin(top3)]

        chart = df6.groupby(['Category','Type']).agg({
            'Installs_Numeric': 'mean',
            'Revenue': 'mean'
        }).reset_index()

        fig = px.bar(chart, x="Category", y=["Installs_Numeric", "Revenue"], color="Type")

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.error("Visible only 1PM–2PM")