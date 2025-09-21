import streamlit as st
import pandas as pd

# Loan Calculator Function
def loan_schedule(principal, rate, months):
    rate = rate / 100  # convert % to decimal
    emi = principal * rate * (1 + rate)**months / ((1 + rate)**months - 1)
    
    schedule = []
    balance = principal
    
    for m in range(1, months + 1):
        interest = balance * rate
        principal_paid = emi - interest
        balance -= principal_paid
        schedule.append([m, round(emi,2), round(interest,2), round(principal_paid,2), round(balance,2)])
    
    return pd.DataFrame(schedule, columns=["Month","EMI","Interest","Principal Paid","Balance"])

# Streamlit App
st.title("📊 Loan Calculator")

# User Inputs
principal = st.number_input("Loan Amount", value=500000)
rate = st.number_input("Monthly Interest Rate (%)", value=1.0)
months = st.number_input("Loan Tenure (Months)", value=48)

if st.button("Calculate"):
    df = loan_schedule(principal, rate, months)

    st.subheader("Repayment Schedule")
    st.dataframe(df)

    st.subheader("Summary")
    st.write(f"**EMI:** {df['EMI'][0]:,.2f}")
    st.write(f"**Total Interest Paid:** {df['Interest'].sum():,.2f}")
    st.write(f"**Total Repayment:** {df['EMI'].sum():,.2f}")

    st.line_chart(df.set_index("Month")[["Interest","Principal Paid"]])
