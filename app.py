import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------- SIDEBAR ----------------
st.sidebar.title("PSX Trading")
st.sidebar.caption("Decision Support")

pages = [
    "Home",
    "Dashboard",
    "Market Data",
    "Performance",
    "System Architecture",
    "About Project",
    "References",
    "Disclaimer"
]

selected = st.sidebar.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.page)
)

if selected != st.session_state.page:
    st.session_state.page = selected
    st.rerun()
# ================= HOME =================
if st.session_state.page == "Home":

    st.markdown("### Final Year Project")

    st.title("AI-Based Stock Trading Decision Support System for PSX")

    st.write(
        "An AI-based decision support system leveraging deep learning models (LSTM and DQN) "
        "to analyze historical data and assist trading decisions for Pakistan Stock Exchange securities."
    )

    # CENTER BUTTON
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Go to Dashboard", type="primary", use_container_width=True):
            st.session_state.page = "Dashboard"
            st.rerun()

    st.write("")

    # CARDS
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    c1.info("🔹 AI-Based Analysis\n\nLSTM neural networks for stock price trend prediction")
    c2.info("📈 Trading Decision Support\n\nDQN-based Buy, Sell, and Hold signal generation")
    c3.info("📊 Performance Evaluation\n\nHistorical backtesting and strategy performance analysis")
    c4.info("🛡 Risk & Sentiment Awareness\n\nFear & Greed Index and risk level indicators")

    st.warning(
        "This system is developed strictly for academic and educational purposes. "
        "It does not perform real-time trading or provide financial advice."
    )

# ================= DASHBOARD =================
elif st.session_state.page == "Dashboard":

    st.title("Trading Dashboard")
    st.caption("AI-based trading decision support using historical PSX data")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Selected Stock", "OGDC")
    col2.metric("Reference Price (Historical)", "PKR 192.50")
    col3.metric("Price Movement", "+2.35%")
    col4.metric("Trading Volume", "2.4M")

    st.caption("*Displayed values are based on historical data and for academic purposes only.")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("AI Decision\n\n### BUY")

    with c2:
        st.write("**Confidence Score**")
        st.progress(0.78)
        st.write("78%")

    with c3:
        st.warning("Risk Level\n\n### Medium")

    st.markdown("---")

    left, right = st.columns([3,1])

    with left:
        st.subheader("Price Chart - Historical vs Predicted")

        df = pd.DataFrame({
            "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
            "Actual Price": [150,152,149,160,162,158,170,175,180,178,185,190],
            "Predicted Price": [148,150,151,159,161,160,168,173,178,180,183,188]
        })

        fig = px.line(df, x="Month", y=["Actual Price","Predicted Price"])
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Fear & Greed Index")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=65,
            title={'text': "Greed"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "green"},
                'steps': [
                    {'range': [0, 30], 'color': "red"},
                    {'range': [30, 70], 'color': "orange"},
                    {'range': [70, 100], 'color': "green"}
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("AI Decision Explanation")

    st.write("**LSTM Price Prediction:** The model predicts a 3.2% price increase over the next 5 trading days based on historical price patterns and technical indicators.")

    st.write("**DQN Decision Rationale:** The reinforcement learning agent recommends a BUY action based on the predicted upward trend, current portfolio allocation, and risk-adjusted return optimization.")

    st.write("**Key Factors:** Positive momentum indicators (RSI: 58, MACD: bullish crossover), favorable market sentiment, and historical support level confirmation.")

# ================= MARKET DATA =================
elif st.session_state.page == "Market Data":

    st.title("Market Data")
    st.caption("Historical PSX stock price data used for analysis and model input")

    col1, col2 = st.columns(2)

    with col1:
        stock = st.selectbox("Select Stock", ["OGDC", "HBL"])

    with col2:
        date_range = st.selectbox("Date Range", ["Last 30 Days"])

    st.subheader(f"Historical OHLC Data – {stock}")

    df = pd.DataFrame({
        "Date": [
            "2024-01-15","2024-01-14","2024-01-13","2024-01-12",
            "2024-01-11","2024-01-10","2024-01-09","2024-01-08"
        ],
        "Open": [188.50,186.00,184.25,182.00,180.50,178.75,176.00,174.50],
        "High": [192.80,189.50,187.00,185.75,183.00,181.50,179.25,177.00],
        "Low":  [187.20,185.00,183.50,181.25,179.75,177.50,175.00,173.75],
        "Close":[191.75,188.50,186.00,184.25,182.00,180.50,178.75,176.00],
        "Volume":["2.45M","1.98M","2.12M","1.75M","2.28M","1.92M","2.05M","1.68M"]
    })

    st.dataframe(df, use_container_width=True)

    st.caption("*Displayed values are sample historical records for academic demonstration purposes.")

    st.info(
        "Data Usage: Historical market data is utilized for analysis, visualization, and as input to the prediction and decision models after preprocessing."
    )

# ================= PERFORMANCE =================
elif st.session_state.page == "Performance":

    st.title("Performance Analysis")
    st.caption("Backtesting results based on historical PSX data")

    # -------- TOP METRICS --------
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Return (Simulated)", "+12.4%")
    c2.metric("Win Rate", "61.8%")
    c3.metric("Max Drawdown", "-6.5%")
    c4.metric("Risk-Adjusted Score", "Moderate")

    st.markdown("---")

    # -------- EQUITY CURVE --------
    st.subheader("Equity Curve")

    df_equity = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
        "Equity": [100000,105000,103000,110000,115000,112000,120000,125000,130000,128000,135000,140000]
    })

    fig = px.line(df_equity, x="Month", y="Equity")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # -------- TRADE HISTORY --------
    st.subheader("Simulated Trade History")

    df_trades = pd.DataFrame({
        "Date": ["2024-01-15","2024-01-12","2024-01-10","2024-01-08","2024-01-05"],
        "Stock": ["OGDC","PPL","ENGRO","HBL","LUCK"],
        "Action": ["BUY","SELL","BUY","SELL","BUY"],
        "Reference Price": [185.50,92.75,245.00,78.50,520.25],
        "Position": ["-","-","-","-","-"],
        "Reward / Loss": ["+450","+320","+210","-180","+520"]
    })

    st.dataframe(df_trades, use_container_width=True)

    st.caption("*All results shown on this page are generated through historical backtesting and are provided solely for academic evaluation of the proposed decision support system.*")

# ================= SYSTEM =================
elif st.session_state.page == "System Architecture":

    st.title("System Architecture")
    st.caption("High-level workflow and component interaction of the proposed system")

    st.markdown("---")

    # -------- FLOW --------
    st.subheader("Overall System Flow")

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    c1.info("PSX Data\n\nHistorical stock price data (CSV)")
    c2.info("Preprocessing\n\nData cleaning and feature preparation")
    c3.info("LSTM Prediction\n\nPrice trend forecasting")
    c4.info("DQN Decision\n\nTrading decision support agent")
    c5.info("Dashboard\n\nVisualization and analysis interface")
    c6.info("User\n\nDecision interpretation and feedback")

    st.markdown("---")

    # -------- MODULES --------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("LSTM Price Prediction Module")
        st.write(
            "The Long Short-Term Memory (LSTM) model is used to capture temporal patterns "
            "in historical PSX stock price data. It learns sequential dependencies to forecast future price trends."
        )
        st.write("**Input:** Historical price sequences and derived features")
        st.write("**Output:** Predicted price movement or trend")

    with col2:
        st.subheader("DQN Decision Support Agent")
        st.write(
            "The Deep Q-Network (DQN) agent utilizes reinforcement learning to generate optimal trading decisions "
            "based on the predicted price trends and market state."
        )
        st.write("**Actions:** Buy, Sell, Hold")
        st.write("**Objective:** Maximize long-term reward while considering market risk")

    st.markdown("---")

    # -------- TECH STACK --------
    st.subheader("Technology Stack")

    t1, t2, t3, t4 = st.columns(4)

    t1.info("Deep Learning\n\nTensorFlow, Keras")
    t2.info("Data Processing\n\nPandas, NumPy")
    t3.info("Visualization\n\nMatplotlib, Plotly")
    t4.info("Web Interface\n\nStreamlit")

# ================= ABOUT =================
elif st.session_state.page == "About Project":

    st.title("About Project")
    st.caption("Research background, objectives, and academic contribution")

    st.markdown("---")

    # -------- PROBLEM STATEMENT --------
    st.subheader("Problem Statement")

    st.write(
        "Traditional stock trading largely depends on manual analysis and subjective decision-making, "
        "which is often time-consuming and influenced by emotional biases. The Pakistan Stock Exchange (PSX), "
        "as an emerging market, exhibits higher volatility and limited availability of intelligent decision "
        "support tools for individual investors, motivating the need for AI-assisted trading analysis."
    )

    st.markdown("---")

    # -------- OBJECTIVES --------
    st.subheader("Research Objectives")

    st.write("1. Develop an LSTM-based model for forecasting stock price trends using historical PSX data")
    st.write("2. Design a DQN-based trading decision support agent for Buy, Sell, and Hold recommendations")
    st.write("3. Develop an interactive web dashboard to visualize predictions, decisions, and risk indicators")
    st.write("4. Evaluate system effectiveness through historical backtesting and performance analysis")

    st.markdown("---")

    # -------- CONTRIBUTION --------
    st.subheader("Research Contribution")

    st.write("This research contributes by:")

    st.write("• Proposing an AI-based trading decision support system tailored for PSX market characteristics")
    st.write("• Integrating deep learning (LSTM) with reinforcement learning (DQN) for informed trading decisions")
    st.write("• Emphasizing explainability and risk awareness in trading signals")
    st.write("• Providing an academic prototype suitable for emerging market studies")

    st.markdown("---")

    # -------- TOOLS --------
    st.subheader("Tools & Technologies")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("Python 3.x")
        st.info("NumPy")
        st.info("Plotly")

    with c2:
        st.info("TensorFlow / Keras")
        st.info("Scikit-learn")
        st.info("Streamlit")

    with c3:
        st.info("Pandas")
        st.info("Matplotlib")
        st.info("Jupyter Notebook")
# ================= REFERENCES =================
elif st.session_state.page == "References":

    st.title("References")
    st.caption("Research papers, data sources, and related platforms")

    st.markdown("---")

    # -------- RESEARCH PAPERS --------
    st.subheader("Research Paper Citations")

    st.info("Awad, M. et al. (2023). Stock Market Prediction Using Deep Reinforcement Learning. Applied System Innovation.")
    st.info("IEEE Access (2024). A Multifaceted Approach to Stock Market Trading Using Reinforcement Learning. IEEE Access.")

    st.markdown("---")

    # -------- DATA SOURCES --------
    st.subheader("Data Sources")

    st.write("• Pakistan Stock Exchange (PSX) – Historical Stock Data")
    st.write("• PSX Data Portal (DPS) – Downloaded CSV Files")

    st.caption("*Only historical data is used for academic analysis. No real-time or paid data sources are integrated.*")

    st.markdown("---")

    # -------- PLATFORMS --------
    st.subheader("Related Trading Platforms")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("TradingView")

    with c2:
        st.info("QuantConnect")

    with c3:
        st.info("MetaTrader")

    st.caption("*These platforms are listed solely for feature comparison and are not used in the system implementation.*")
# ================= DISCLAIMER =================
elif st.session_state.page == "Disclaimer":

    st.title("Disclaimer")
    st.caption("Academic and usage-related information")

    st.markdown("---")

    # -------- EDUCATIONAL PURPOSE --------
    st.subheader("🎓 Educational & Academic Purpose")
    st.info(
        "This AI-Based Stock Trading Decision Support System is developed solely for academic and "
        "educational purposes as part of a Final Year Project. The system demonstrates the application "
        "of deep learning and reinforcement learning techniques using historical stock market data."
    )

    # -------- NOT FINANCIAL ADVICE --------
    st.subheader("⚠️ Not Financial Advice")
    st.warning(
        "The predictions, indicators, and trading signals presented by this system are provided for "
        "academic demonstration only and do not constitute financial, investment, or trading advice.\n\n"
        "• The system does not execute real trades\n"
        "• Decisions should not be based solely on system outputs\n"
        "• Financial markets involve inherent risks"
    )

    # -------- LIMITATION --------
    st.subheader("⚖️ Limitation of Scope")
    st.info(
        "This system is intended as a prototype for research and learning purposes. The results may vary "
        "depending on market conditions, data quality, and model assumptions. No guarantees regarding "
        "prediction accuracy or trading performance are claimed."
    )

    st.markdown("---")

    # -------- FOOT NOTE --------
    st.caption(
        "This disclaimer ensures clarity regarding the academic intent and responsible use of the proposed system."
    )