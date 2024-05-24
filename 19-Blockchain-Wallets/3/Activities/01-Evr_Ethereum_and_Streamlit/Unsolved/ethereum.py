# Ethereum Account Functions

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3
#############################################
#Connect to Ganache
w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
################################################################################

# Create a function called `generate_account` that automates the Ethereum
# account creation process
# Access the mnemonic phrase from the `.env` file
# Create Wallet object instance
# Derive Ethereum private key
# Convert private key into an Ethereum account
# Return the account from the function


def generate_account(w3):
    # Call os.getenv("MNEMONIC") and save it's value as a variable named mnemonic
    mnemonic = os.getenv("MNEMONIC")

    # Instantiate a new instance of Wallet and pass it the mnemonic variable
    wallet = Wallet(mnemonic)


    # Calling the derive_account method on your wallet instance
    # Pass the string eth to the method
    private, public = wallet.derive_account("eth")


    # Construct the Ethereum account by calling Account.privateKeyToAccount
    # Pass it your private key variable
    account = Account.privateKeyToAccount(private)

    # Print the account's 
    return account

#### Create a function that allow me to get the balance of the address from Ganache


def get_balance(w3, address):

    # Get balance function from web3
    wei_balance = w3.eth.get_balance(address)

    ether = w3.fromWei(wei_balance, 'ether')

    return ether



######## SEnd a transaction ########

def send_transaction(w3, account, receiver, ether):
    ## set up the gas strategy

    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)


    #Convert the amount of ether that I will send to wei

    wei_value = w3.toWei(ether, "ether")

    #Calculate the gas estimate price

    gas_estimate = w3.eth.estimateGas({
    'to': receiver, 
    'from': account.address, 
    'value': wei_value
    })

    # Set up my transaction 
    # Send the transaction to the blockchain
    transaction_execution_setup = {
    'to': receiver, 
    'from': account.address, 
    'gas': gas_estimate, 
    'gasPrice': 670519845,
    "nonce": w3.eth.getTransactionCount(account.address)
    }

    # Sign/validate the transaction

    signed_transaction = account.signTransaction(transaction_execution_setup)

    send_the_transaction = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    return send_the_transaction

