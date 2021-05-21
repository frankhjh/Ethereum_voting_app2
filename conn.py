from web3 import Web3
import json
w3=Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
try:
    if w3.isConnected():
        print('connected!')
except:
    print('non connected!')
with open('abi2.json','r') as f:
    abi=json.load(f)
sorting_contract=w3.eth.contract(address='0xB1cE91D39Bb3DC71B2D70b72Ba65Ccf1cF9b8FC3', #remember to replace it with your own deployment result
                              abi=abi)

if __name__=='__main__':
    leader_addrs=[sorting_contract.functions.leader_address(i).call() for i in range(3)]
    for addr in leader_addrs:
        print(sorting_contract.functions.Leaders(addr).call())

