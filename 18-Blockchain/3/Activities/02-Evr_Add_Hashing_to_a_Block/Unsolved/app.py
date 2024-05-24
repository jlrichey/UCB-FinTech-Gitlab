from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import hashlib
import pandas as pd
import streamlit as st

@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.now().strftime("%H:%M:%S")
    nonce: int=0

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


# Let's create the pyChain

@dataclass
class PyChain:
    chain: List[Block]
    #add a level of difficulty into the PyChain
    difficulty: int = 4

    # Create the proof of work function

    def proof_of_work(self, block):
        calculate_hash = block.hash_block()
        num_of_zeros = "0" * self.difficulty

        # Find the hash with 4 zero at the start
        while not calculate_hash.startswith(num_of_zeros):
            block.nonce +=1
            calculate_hash = block.hash_block()
        
        return block
    
    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]


    def is_valid(self):

        block_hash = self.chain[0].hash_block()

        # For loop to find the invalid block

        for block in self.chain[1:]:

            # create a condition that compare the block_hash with the previous
            # block hash and return if it is not equal

            if block_hash != block.prev_hash:
                print("INVALID Blockchain!!!")
                return False
            
            # SEt the hash to the current block 
            block_hash = block.hash_block()

        print("VALID Blockchain")
        return True

        
############################## Streamlit Code #################

@st.cache_resource(experimental_allow_widgets=True)

def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])

pychain = setup()

st.markdown("# PyChain: A Python Blockchain Application")
st.markdown("## Store Data in the Chain")

input_data = st.text_input("Block Data")


# Add a side bar of difficulty level

difficulty = st.sidebar.slider("Block Difficult", 1, 5, 4)

pychain.difficulty = difficulty

if st.button("Add Block"):

    # Select the previous block in the chain
    prev_block = pychain.chain[-1]

    # Hash the previous block in the chain
    prev_block_hash = prev_block.hash_block()

    # Create a new block in the chain
    new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)

    # Add the new block to the chain
    pychain.add_block(new_block)

    st.write("Winning hash", new_block.hash_block())


st.markdown("## PyChain Ledger")

# Create a Pandas DataFrame to display the `PyChain` ledger
pychain_df = pd.DataFrame(pychain.chain)

# Use the Streamlit `write` function to display the `PyChain` DataFrame
st.write(pychain_df)

#### Add a button that validates the blockchain

if st.button("Validate Blockchain"):
    st.write(pychain.is_valid())


# Create a test block and view the nonce and hash of the test block

# block = Block("Test", 1)

# print(f"The original nonce of this block is: {block.nonce}")
# print(f"The original hash of this block is: {block.hash_block()}")


#Update the test block and view the nonce and hash

# block.nonce +=1
# print(f"The new nonce of this block is: {block.nonce}")
# print(f"The new hash of this block is: {block.hash_block()}")