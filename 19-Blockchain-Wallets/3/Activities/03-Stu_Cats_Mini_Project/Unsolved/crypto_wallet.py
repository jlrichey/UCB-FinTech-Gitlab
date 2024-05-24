# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account, Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


# Wallet functionality

#@TODO create a function called generate account do not forget to add each of the following steps

def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    
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
    
#@TODO create a function called generate account do not forget to add each of the following steps
def get_balance(address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance function from web3
    wei_balance = w3.eth.get_balance(address)

    ether = w3.fromWei(wei_balance, 'ether')

    return ether

