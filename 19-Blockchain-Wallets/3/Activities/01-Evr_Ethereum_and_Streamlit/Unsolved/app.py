# Streamlit Application

# Imports
import streamlit as st
from ethereum import generate_account, get_balance, send_transaction
from web3 import Web3

################################################################################
# Connect Ganache
w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
# Import the functions from ethereum.py
account = generate_account(w3)
################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Automating Ethereum with Streamlit!")
st.text("\n")
st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
st.write(account.address)

################################################################################
st.text("\n")
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Account Balance:")

ether_balance = get_balance(w3,account.address)
st.write(ether_balance)

####################################### Bring Send Transaction to the front user ##########
st.text("\n")
st.text("\n")
st.text("\n")
st.markdown("## Ethereum Transaction:")

### Create the input cell for receiver and amount
receiver = st.text_input("Input the receiver address")
amount = st.number_input("Input the amount of ether")

#### Create the button

if st.button("Send Transaction"):

    trasaction_hash = send_transaction(w3, account, receiver, amount)

    ## Display the hash
    st.text("\n")
    st.text("\n")
    st.markdown('## Ethereum Trasaction Hash: ')

    st.write(trasaction_hash)