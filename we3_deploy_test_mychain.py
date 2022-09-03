from web3 import Web3
import json,os,time,sys
from ethereum import utils
import os,requests

generate_n = 10

'''
target = input('Input Target Phrase\n>')

priv = utils.sha3(os.urandom(4096))
addr = utils.checksum_encode(utils.privtoaddr(priv))

while not addr.lower().startswith('0x{}'.format(target)):
    priv = utils.sha3(os.urandom(4096))
    addr = utils.checksum_encode(utils.privtoaddr(priv))

print('Address: {}\nPrivate Key: {}'.format(addr, priv.hex()))
time.sleep(10000000)
'''
def register(bbb,filename):
    log = open('./'+filename,'w+')
    log.write('%s'%bbb)
    log.close()


json_list = []

w3 = Web3(Web3.HTTPProvider('http://45.32.28.98:8544'))
print(w3.isConnected())
print(w3.eth.blockNumber)

for i in range(generate_n):
	json_list_sub = {}
	priv = utils.sha3(os.urandom(4096)).hex()
	addr = utils.checksum_encode(utils.privtoaddr(priv))
	json_list_sub['priv'] = priv
	json_list_sub['addr'] = addr
	data = json.dumps({'receiverAddress':str(addr)})
	print(data)
	res = requests.post(url='https://stage2-faucet.zksync.dev/ask_money',data=data,headers={'Content-Type':'application/json'})
	print(res.text)
	time.sleep(5)
	continue








	account = w3.toChecksumAddress("0x797aBA77b9cc6d31fa65D13bedF33C10c8e45d32")
	key = ""

	amount = 5000.5
	my_balance = float(w3.eth.getBalance(account))/10**18
	if my_balance - amount>0 and amount-int(amount)>0.1128:
	    nonce = w3.eth.getTransactionCount(account,"pending")
	    transaction = {
	            'chainId': 19921128,
	            'to': w3.toChecksumAddress(addr),
	            'value': w3.toWei(str(amount), 'ether'),
	            'gas': 30000,
	            'gasPrice': w3.toWei(str(2), 'gwei'),
	            'nonce': nonce,
	        }
	    signed = w3.eth.account.sign_transaction(transaction, key)
	    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
	    print(w3.toHex(tx_hash)) 
	    while True:
	        time.sleep(1)
	        try:
	            receipt = w3.eth.getTransactionReceipt(tx_hash)
	            print(receipt)
	        except:
	            print('wait...')
	            continue
	        break
	time.sleep(10)


	account = w3.toChecksumAddress(addr)
	private_key = priv

	#print(w3.eth.getBalance(account))


	#deploy code
	nonce = w3.eth.getTransactionCount(account)
	transaction = {
			'from':account,
			'chainId': 19921128,
		    'gas': 1000000,
		    'gasPrice': w3.toWei(str(2), 'gwei'),
		    'nonce': nonce,
		}

	print(transaction)

	data_json = json.load(open('./assets/Mydatabase.json'))
	abi = data_json["abi"]
	bytecode = data_json["bytecode"]

	Faucet = w3.eth.contract(abi=abi,bytecode=bytecode)
	print(Faucet)
	contract_data = Faucet.constructor().buildTransaction(transaction)
	print(contract_data)
	signed_tx = w3.eth.account.signTransaction(contract_data, private_key)
	print(signed_tx)
	tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
	print(tx_hash)
	#time.sleep(10)
	while True:
		try:
			receipt = w3.eth.getTransactionReceipt(tx_hash)
			print(receipt['contractAddress'])
			json_list_sub['contractAddress'] = receipt['contractAddress']
			break
		except:
			#print("Unexpected error:", sys.exc_info()[0])
			time.sleep(1)
	print(json_list_sub)
	json_list.append(json_list_sub)

print(json_list)

for i in json_list:
	print("'"+i['contractAddress']+"',...")

register(json.dumps(json_list),'priv_address1.txt')


'''
faucet = w3.eth.contract(address=w3.toChecksumAddress('0x89C33cE410fF76fE21c8A336a7D45833DBAf91e5'),abi=abi)
print(faucet.functions.greet().call())
'''


'''

func = greeter.functions.setGreeting('nuanbaobao520')
nonce = w3.eth.getTransactionCount(account)
params = {
    'gas': 300000,
    'gasPrice': w3.toWei(str(10), 'gwei'),
    'nonce': nonce,
}
tx = func.buildTransaction(params)
signed_tx = w3.eth.account.signTransaction(tx, private_key)
print(signed_tx)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
'''








#transfer code

'''
w3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.matic.network:443'))
print(w3.isConnected())
print(w3.eth.blockNumber)

account = w3.toChecksumAddress("0xa30042A5C0d2D7908Ba628d636B8dfa86fB77896")
key = ""

print(w3.eth.getBalance(account))

estimate_gas

nonce = w3.eth.getTransactionCount(account)
transaction = {
		'chainId': 137,
	    'to': w3.toChecksumAddress('0xaf1538424f432e086ce50eca04767231462027e4'),
	    'value': w3.toWei(str(0.001), 'ether'),
	    'gas': 30000,
	    'gasPrice': w3.toWei(str(3), 'gwei'),
	    'nonce': nonce,
	}

print(transaction)
#tx = w3.buildTransaction(transaction)
signed = w3.eth.account.sign_transaction(transaction, key)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
print(w3.toHex(tx_hash))
'''