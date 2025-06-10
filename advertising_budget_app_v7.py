
import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Retailer Advertising Budget Calculator", layout="centered")

# -- Branding Header --
st.markdown(
    "<h2 style='text-align: center;'>Retailer Advertising Budget Calculator</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div style='text-align: center;'>Powered by <strong>Tempur</strong>, <strong>Sealy</strong>, and <strong>Stearns & Foster</strong></div><br>",
    unsafe_allow_html=True,
)

# -- Inputs --
retailer_name = st.text_input("Enter Retailer Name", value="Example Retailer")
sales_goal = st.number_input("Enter Sales Goal ($)", min_value=0, step=1000)
av_percent = st.selectbox(
    "Select Ad Spend Strategy",
    options=[
        ("8%", "Fixed Growth"),
        ("10%", "Growth"),
        ("12%", "Growth in Competitive Market"),
    ],
    format_func=lambda x: f"{x[1]} ({x[0]})"
)

brand_mix = {}
st.markdown("### Brand Mix (Must Total 100%)")
col1, col2 = st.columns(2)
with col1:
    brand_mix["Tempur-Pedic"] = st.slider("Tempur-Pedic", 0, 100, 25)
    brand_mix["Stearns & Foster"] = st.slider("Stearns & Foster", 0, 100, 25)
with col2:
    brand_mix["Sealy"] = st.slider("Sealy", 0, 100, 25)
    brand_mix["Sherwood"] = st.slider("Sherwood", 0, 100, 25)

total_mix = sum(brand_mix.values())
mix_color = "green" if total_mix == 100 else "red"
st.markdown(f"<span style='color:{mix_color}; font-weight:bold;'>Total Mix: {total_mix}%</span>", unsafe_allow_html=True)

# -- Calculate Budget --
if sales_goal > 0 and total_mix == 100:
    percent_value = int(av_percent[0].replace("%", "")) / 100
    total_budget = sales_goal * percent_value
    brand_budgets = {brand: total_budget * pct / 100 for brand, pct in brand_mix.items()}

    st.markdown("## 📊 Budget Summary")
    st.markdown(f"**Retailer:** {retailer_name}")
    st.markdown(f"**Sales Goal:** ${sales_goal:,.2f}")
    st.markdown(f"**Ad Strategy:** {av_percent[1]}")
    st.markdown(f"**Total Ad Budget:** ${total_budget:,.2f}")

    for brand, amount in brand_budgets.items():
        st.markdown(f"- **{brand}:** ${amount:,.2f}")

    # -- Pie Chart --
    fig, ax = plt.subplots()
    ax.pie(brand_budgets.values(), labels=brand_budgets.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    # -- Motivational Quotes --
    quotes = [
        "Let's turn those dreams into data-driven decisions!",
        "More eyeballs, more foot traffic, more success.",
        "A solid plan today means more Tempur wins tomorrow.",
        "Sleep isn’t the only thing we improve – so is strategy.",
        "You're not just spending – you're investing in results!"
    ]
    st.markdown(f"💬 *{random.choice(quotes)}*")

    st.markdown(f"<div style='text-align:center; margin-top:2em;'>Powered by Tempur Sealy for <strong>{retailer_name}</strong></div>", unsafe_allow_html=True)
else:
    st.warning("Please ensure the brand mix totals 100% and that you've entered a sales goal.")
