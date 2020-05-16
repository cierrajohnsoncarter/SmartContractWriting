# Import the dependencies
from web3 import Web3
import json

# Set up web3 connection with ganache
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Get the 1st account from ganache and make it the default account in order to sign the transaction
web3.eth.defaultAccount = web3.eth.accounts[0]

# Get the address of the contract
address = web3.toChecksumAddress('0x1306f7f374dae71da1d66be6a4f7457cf5065d57')

# Get the abi
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

# Instantiate the contract
contract = web3.eth.contract(address=address, abi=abi)

# Read the greeting
print(contract.functions.greet().call())

# Update the contract greeting
tx_hash = contract.functions.setGreeting(
    'Hello, this is a new greeting').transact()

print(tx_hash)

# Don't display anything until a reciept of the transaction is generated
web3.eth.waitForTransactionReceipt(tx_hash)

# Display the new greeting
print('Updated greeting: {}'.format(contract.functions.greet().call()))
