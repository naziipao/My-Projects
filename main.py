import streamlit as st
import requests

st.title("Chapter five")
st.header("Live currency converter")


# initial_currency = st.selectbox("Initial currency: " , ["BDT" , "EUR", "USD"])
# given_amount = st.number_input("Enter the amount: " , min_value=0)
# target_currency = st.selectbox("In which currency you want to convert: " , ["BDT" ,"EUR" , "USD"])
url = "https://v6.exchangerate-api.com/v6/b6f39e38b0a5cc52bb82eaa7/codes"
response_test = requests.get(url)
data_test = response_test.json()
currency_list = data_test["supported_codes"]
initial_currency_list = st.selectbox("Select initial currency:", options=currency_list, format_func=lambda x: f"{x[0]} - {x[1]}")
initial_currency = initial_currency_list[0]
given_amount = st.number_input("Enter the amount: " , min_value=0)
target_currency_list = st.selectbox("Select target currency:", options=currency_list, format_func=lambda x: f"{x[0]} - {x[1]}")
target_currency = target_currency_list[0]

if st.button("Convert"):
    url_initial = f"https://v6.exchangerate-api.com/v6/b6f39e38b0a5cc52bb82eaa7/latest/{initial_currency}"
    response = requests.get(url_initial)

    if response.status_code == 200:
        url_target = f"https://v6.exchangerate-api.com/v6/b6f39e38b0a5cc52bb82eaa7/latest/{target_currency}"
        data = response.json()
        rate_initial = data["conversion_rates"][initial_currency]
        rate_target = data["conversion_rates"][target_currency]
        converted_toUSD = rate_initial * given_amount
        converted_toTarget = converted_toUSD * rate_target
        st.success(f"{given_amount} {initial_currency} = {converted_toTarget} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")