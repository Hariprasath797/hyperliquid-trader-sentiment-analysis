# Hyperliquid Trader Behavior vs Market Sentiment

## Overview
This project analyzes how market sentiment, measured using the Fear & Greed Index,
influences trader behavior and performance on the Hyperliquid platform. The goal
is to identify behavioral patterns and derive actionable insights that can inform
smarter, sentiment-aware trading strategies.

---

## Objective
- Understand how trader performance (PnL, win rate, downside risk) varies across
  Fear and Greed market regimes
- Examine how traders adjust behavior such as trade frequency, position size, and
  directional bias in response to sentiment
- Translate analytical findings into practical trading rules and risk-management
  strategies

---

## Datasets
- **Fear & Greed Index**  
  Daily Bitcoin market sentiment classified into Fear, Neutral, and Greed regimes

- **Hyperliquid Historical Trader Data**  
  Trade-level execution data including timestamps, trade size, direction, and
  realized PnL

> **Note:** Raw datasets are excluded from the repository due to file size limits
and can be provided separately upon request.

---

## Methodology
1. Performed an initial data audit to assess data quality and completeness
2. Converted timestamps and aligned sentiment and trading data at a daily
   granularity (date + account)
3. Engineered trader-level daily metrics:
   - Daily PnL
   - Win rate
   - Average trade size
   - Number of trades per day
   - Long/short ratio
4. Compared trader performance and behavior across Fear and Greed regimes
5. Segmented traders based on activity level and consistency
6. Derived actionable strategy recommendations grounded in empirical findings

---

## Key Insights
- Trader profitability declines during Fear regimes, accompanied by a higher
  proportion of losing days
- Greed regimes are characterized by increased trade frequency and larger position
  sizes, indicating risk-on behavior
- Consistent traders exhibit greater resilience to sentiment shifts compared to
  high-frequency or inconsistent traders

---

## Actionable Strategies
- **Risk Reduction During Fear Regimes**  
  Limit trade frequency and position sizes during Fear periods, particularly for
  frequent and inconsistent traders, to reduce drawdowns

- **Selective Aggression During Greed Regimes**  
  Allow increased activity and risk exposure during Greed periods only for traders
  with demonstrated consistency and strong historical win rates

---

## Bonus Analysis
- **Predictive Modeling**  
  Built a lightweight logistic regression model to predict next-day trader
  profitability using market sentiment and recent trading behavior

- **Trader Clustering**  
  Clustered traders into behavioral archetypes based on activity, risk-taking, and
  performance characteristics

- **Interactive Dashboard**  
  Implemented a Streamlit dashboard to explore trader performance, behavior metrics,
  and sentiment regimes interactively

---

## Outputs

The `outputs/` directory contains key charts and tables generated from the
analysis and Streamlit dashboard, including PnL distributions across sentiment
regimes and trader behavioral cluster summaries.

---

## How to Run
1. Open the main notebook:
   hyperliquid_trader_behavior_analysis.ipynb
2. Run all cells from top to bottom
3. Ensure the following files are present in the project directory:
   hyperliquid_trader_behavior_analysis.ipynb,
   app.py,
   final_df.csv,
   cluster_df.csv
4. Open a terminal / PowerShell in the project folder.
   Run the Streamlit app:
   streamlit run app.py
   
---

## Project Structure

├── hyperliquid_trader_behavior_analysis.ipynb
├── app.py
├── README.md
├── writeup.md
└── outputs/
    ├── final_df.csv
    └── cluster_df.csv
