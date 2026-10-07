import streamlit as st
import requests

# Page settings
st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱"
)

st.title("💱 Jyothirmai Currency Converter")
st.write("Convert money from one currency to another.")

# Currency list
currencies = {
    "USD": "US Dollar",
    "INR": "Indian Rupee",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "SGD": "Singapore Dollar"
}

# User inputs
amount = st.number_input(
    "Enter amount",
    min_value=0.01,
    value=1.0
)

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "From",
        list(currencies.keys())
    )

with col2:
    to_currency = st.selectbox(
        "To",
        list(currencies.keys()),
        index=1
    )

# Convert button
if st.button("Convert 💱"):

    if from_currency == to_currency:
        result = amount

        st.success(
            f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
        )

    else:
        url = (
            f"https://api.frankfurter.app/latest"
            f"?amount={amount}"
            f"&from={from_currency}"
            f"&to={to_currency}"
        )

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            result = data["rates"][to_currency]

            st.success(
                f"{amount:.2f} {from_currency} = "
                f"{result:.2f} {to_currency}"
            )

        else:
            st.error("Unable to get exchange rate.")