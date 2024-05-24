import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Connect to web3

w3=Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Get the helper functions from the contract and connect to the smart contract ABI.json

@st.cache_resource()

def load_contract():

    # load the contract using ABI.json file
    with open(Path('./ArtToken/artwork_abi.json')) as contract_json:
        artwork_abi = json.load(contract_json)

    # Read the address of the contract
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Assign the contract_address to the ABI.json contract 

    smart_contract = w3.eth.contract(
        address = contract_address, 
        abi = artwork_abi
    )

    return smart_contract


# Let's call the function so it works

load_smart_contract = load_contract()


### Streamlit front-end

st.title("Register new ArtWork")

user_accounts = w3.eth.accounts
address = st.selectbox("Select Artwork Owner", options=user_accounts)
artwork_uri = st.text_input("Enter the URI of the Artwork")

if st.button("Click to Register Artwork"):
    transaction_hash = load_smart_contract.functions.registerArtwork(address, artwork_uri).transact({'from':address, 'gas':1000000})
    receipt = w3.eth.waitForTransactionReceipt(transaction_hash)
    st.write("Transaction receipt mined: ")
    st.write(dict(receipt))


