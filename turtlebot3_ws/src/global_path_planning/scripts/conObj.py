import time
from interface import ContractInterface
import os
from web3 import Web3, HTTPProvider
from solcx import *


class ContractObject():
	def __init__ (self, owner, _x, _y,_deadline,_price):
		self.w3 =  Web3(HTTPProvider('http://127.0.0.1:7545'))
		self.p = os.path.abspath('/home/sanjaya/Blockchain_RL/turtlebot3_ws/src/global_path_planning/contracts')
		self.con = ContractInterface(self.w3, 'crowdsourcing', self.p)
		self.con.compile_source_files()
		self.ownerAcc=self.w3.eth.accounts[3] #person who deploys(owner) #assign above -- using account number 3 for testing
		self.price=0.03 #this the contract value asign above price
		self.x=_x;
		self.y=_y;
		self.deadline=_deadline
		#owner deploys the contract
		self.contractadress=self.con.deploy_contract(self.x,self.y,self.deadline,deployment_params={'from':self.ownerAcc,'value': self.w3.toWei(self.price,'ether')}) #send the payment value while deploying
		self.con.get_instance()
		#lets check the balance
		balance=self.w3.eth.getBalance(self.contractadress)
		print("after deploying balance of the contract: ",self.w3.fromWei(balance,"ether"))	
			
	def accept(self,acceptor):
		#worker accepts the contract
		self.acceptAcc=self.w3.eth.accounts[4] #turtlebot user --put the acceptor using the account number 4 for testing
		collateral=0.02
		self.con.send('accept_contract',tx_params={'from':self.acceptAcc,'value':self.w3.toWei(collateral,'ether'), 'to':self.contractadress}) #acccepting the contract while paying the collateral
		#lets check the balance
		balance=self.w3.eth.getBalance(self.contractadress)
		print("after accepting balance of the contract: ",self.w3.fromWei(balance,"ether"))
		
	def realeaseNpay(self):
		#in the contract it is written that pay for the person who 
		self.con.send('releaseNpay',tx_params={'from':self.ownerAcc,'to':self.contractadress})
		#########-------lets check the balance of acceptor(worker) now
		balance=self.w3.eth.getBalance(self.acceptAcc)
		print("after completing balance of accept account: ",self.w3.fromWei(balance,"ether"))
		########--------lets check the balance of the contract after completing
		balance=self.w3.eth.getBalance(self.contractadress)
	
	


### need to define more methods for following functions

#######---------if cancelling the contract
#con.send('cancel_contract',tx_params={'from':acceptAcc,'to':contractadress})

########--------lets check the balance of the contract after cancelling
#balance=w3.eth.getBalance(contractadress)
#print("after cancelling balance of the contract: ",w3.fromWei(balance,"ether"))

#########-------lets check the balance of acceptor(worker) now

#balance=w3.eth.getBalance(acceptAcc)
#print("after cancelling balance of accept account: ",w3.fromWei(balance,"ether"))

#########-------After completing the contract







