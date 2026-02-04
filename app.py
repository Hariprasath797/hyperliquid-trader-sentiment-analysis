import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# Load data
# ----------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("final_df.csv"), pd.read_csv("cluster_df.csv")

final_df, cluster_df = load_data()

# ----------------------------------
# App title
# ----------------------------------
st.title("Trader Behavior vs Market Sentiment")
st.write("Exploring how Fear and Greed impact trader performance and behavior")

# ----------------------------------
# Sidebar filters
# ----------------------------------
sentiment = st.sidebar.selectbox(
    "Select Market Sentiment",
    options=final_df['sentiment_group'].unique()
)

filtered_df = final_df[final_df['sentiment_group'] == sentiment]

# ----------------------------------
# Key Metrics
# ----------------------------------
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Average Daily PnL", round(filtered_df['daily_pnl'].mean(), 2))
col2.metric("Average Win Rate", round(filtered_df['win_rate'].mean(), 2))
col3.metric("Avg Trades / Day", round(filtered_df['num_trades'].mean(), 2))

# ----------------------------------
# PnL Distribution
# ----------------------------------
st.subheader("Daily PnL Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df['daily_pnl'], bins=50)
ax.set_xlabel("Daily PnL")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# ----------------------------------
# Trading Behavior
# ----------------------------------
st.subheader("Trading Behavior")

behavior_df = filtered_df[['num_trades', 'avg_trade_size', 'long_short_ratio']].mean()

st.bar_chart(behavior_df)

# ----------------------------------
# Trader Clusters
# ----------------------------------
st.subheader("Trader Behavioral Clusters")

cluster_summary = cluster_df.groupby('cluster').mean()
st.dataframe(cluster_summary)