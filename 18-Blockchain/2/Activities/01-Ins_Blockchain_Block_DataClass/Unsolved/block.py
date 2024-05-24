# Creating a Blockchain Block with a DataClass

#Import libraries

from dataclasses import dataclass
from datetime import datetime
from typing import Any
import streamlit as st
import hashlib
from typing import List
import pandas as pd

# Create the block as data class

@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.now().strftime("%H:%M:%S")

    def hash_block(self):
        sha =hashlib.sha256()

        # Encode my block
        data = str(self.data).encode()

        # Update my hash or hash it
        sha.update(data)

        # Encode the creator ID
        creator_id = str(self.creator_id).encode()

        sha.update(creator_id)

        # Timestamp inot a encoded string
        timestamp = str(self.timestamp).encode()

        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()

        sha.update(prev_hash)

        return sha.hexdigest()

############# Create the Chain ################

@dataclass
class Pychain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]
    
@st.cache_resource(experimental_allow_widgets=True)
# @st.cache(allow_output_mutation=True)

def setup():
    print("Initializing the Chain")
    first_block = Pychain([Block(data="Genesis", creator_id=0)])
    return first_block


pychain = setup()

st.markdown("# Python Block")
st.markdown("## Store data in each block")
st.sidebar.markdown("### New Block Hash")


# Create the user input 

input_data = st.text_input("Block Data")


#Create a button to add the data

if st.button("Add Block"):

    ## Select the previous block 
    prev_block = pychain.chain[-1]

    # Hash the previous block 
    prev_block_hash = prev_block.hash_block()

    new_block = Block(data=input_data, creator_id=1001, prev_hash=prev_block_hash)

    # Add to the block 
    pychain.add_block(new_block)
    # st.write(new_block)

    # # Let's write the hash
    # block_hash = new_block.hash_block()

    # st.write(f"The block hash is: {block_hash}")
# Print my output
# print(new_block)
st.markdown("## Pychain ledger")

pychain_df = pd.DataFrame(pychain.chain)

st.write(pychain_df)
# STart a new chain
# pychain = Pychain([Block(data="Genesis", creator_id=0)])

# print(pychain)

# Access the previous block

# prev_block = pychain.chain[-1]

# prev_block_hash = prev_block.hash_block()

# Calculate the hash for the block 

# block_hash = new_block.hash_block()

# print(prev_block_hash)

### Create a new block @@@@

# new_block = Block(data="This is my second block ever", creator_id=100, prev_hash=prev_block_hash)


#### add the the new block to the chain 

# pychain.add_block(new_block)

# print(pychain)



#################### Create a data class counter which will keep track hash count #################

# @dataclass
# class Counter:
#     count: int = 2

#     def update_count(self):
#         self.count = self.count + 1


# new_counter = Counter()

# #update teh counter 
# new_counter.update_count()
# new_counter.update_count()

# print("The current count is : ", new_counter.count)

##################################### This is Streamlit Code ###########################
##Create the header

