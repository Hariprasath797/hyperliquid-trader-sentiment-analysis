# Hyperliquid Trader Behavior vs Market Sentiment

## Objective
Analyze how market sentiment (Fear/Greed) relates to trader behavior and
performance on Hyperliquid, and derive actionable trading insights.

---

## Datasets
- **Fear & Greed Index**: Daily Bitcoin market sentiment (Fear / Greed)
- **Hyperliquid Historical Trader Data**: Trade-level execution and PnL data

---

## Methodology
1. Loaded and audited both datasets
2. Converted timestamps and aligned data at daily level (date + account)
3. Engineered trader-level daily metrics:
   - Daily PnL
   - Win rate
   - Average trade size
   - Trade frequency
   - Long/short ratio
4. Compared trader performance and behavior across Fear vs Greed regimes
5. Segmented traders based on behavior and consistency
6. Derived actionable strategy recommendations

---

## Key Insights
- Trader performance deteriorates during Fear regimes, with lower PnL and
  higher frequency of losing days
- Trade frequency and position sizes increase during Greed regimes
- Consistent traders are more resilient to sentiment shifts than
  high-frequency or inconsistent traders

---

## Actionable Strategies
- Reduce risk exposure during Fear regimes, especially for frequent and
  inconsistent traders
- Allow selective risk-taking during Greed regimes only for consistent traders

---

## Bonus Work
- Built a simple predictive model to estimate next-day trader profitability
  using sentiment and behavior features
- Clustered traders into behavioral archetypes
- Implemented a lightweight Streamlit dashboard to explore results interactively

---

## How to Run
1. Open the notebook:
   `hyperliquid_trader_behavior_analysis.ipynb`
2. Run all cells top to bottom
3. (Optional) Run Streamlit dashboard:
   ```bash
   streamlit run app.py
