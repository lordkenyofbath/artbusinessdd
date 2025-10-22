import streamlit as st

st.set_page_config(page_title="Art Business Valuation Model", layout="centered")

st.title("🎨 Canvas & Commerce Valuation Model")
st.markdown("Founder-grade financial snapshot for acquisition analysis")

# --- Inputs ---
st.header("🔢 Input Assumptions")
revenue = st.number_input("Annual Revenue ($)", value=1200000, step=10000)
cogs = st.number_input("Cost of Goods Sold ($)", value=480000, step=10000)
opex = st.number_input("Operating Expenses ($)", value=420000, step=10000)
asking_price = st.number_input("Asking Price ($)", value=1050000, step=10000)
growth_rate = st.slider("Expected Annual Growth Rate (%)", 0, 50, 20)
margin_compression = st.slider("Margin Compression Risk (%)", 0, 30, 0)

# --- Calculations ---
gross_profit = revenue - cogs
ebitda = gross_profit - opex
adjusted_ebitda = ebitda * (1 - margin_compression / 100)
multiple = asking_price / adjusted_ebitda if adjusted_ebitda else 0
verdict = "Justified" if multiple <= 4.5 and growth_rate >= 20 else "Inflated"

# --- Outputs ---
st.header("📊 Output Summary")
st.metric("EBITDA (Adjusted)", f"${adjusted_ebitda:,.0f}")
st.metric("Valuation Multiple", f"{multiple:.2f}x")
st.metric("Verdict", verdict)

# --- Cash Flow Forecast ---
st.header("📈 Cash Flow Forecast")
months = [3, 6, 9, 12, 15, 18]
cash_flow = [adjusted_ebitda * (m / 12) for m in months]
for m, cf in zip(months, cash_flow):
    st.write(f"Month {m}: ${cf:,.0f}")

st.caption("Model assumes linear EBITDA accrual and no major capital investments.")
