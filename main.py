import rsa
from BlockChain import BlockChain
from Transaction import Transaction
from User import User


block_chain = BlockChain()

(publicKeyForUser1, privateKeyForUser1) = rsa.newkeys(1024)
(publicKeyForUser2, privateKeyForUser2) = rsa.newkeys(1024)
(publicKeyForUser3, privateKeyForUser3) = rsa.newkeys(1024)
(publicKeyForUser4, privateKeyForUser4) = rsa.newkeys(1024)
(publicKeyForUser5, privateKeyForUser5) = rsa.newkeys(1024)
(publicKeyForUser6, privateKeyForUser6) = rsa.newkeys(1024)
(publicKeyForUser7, privateKeyForUser7) = rsa.newkeys(1024)
(publicKeyForUser8, privateKeyForUser8) = rsa.newkeys(1024)
(publicKeyForUser9, privateKeyForUser9) = rsa.newkeys(1024)
(publicKeyForUser10, privateKeyForUser10) = rsa.newkeys(1024)

user1 = User("Liam", publicKeyForUser1, privateKeyForUser1)
user2 = User("Noah", publicKeyForUser2, privateKeyForUser2)
user3 = User("Oliver", publicKeyForUser3, privateKeyForUser3)
user4 = User("Elijah", publicKeyForUser4, privateKeyForUser4)
user5 = User("James", publicKeyForUser5, privateKeyForUser5)
user6 = User("William", publicKeyForUser6, privateKeyForUser6)
user7 = User("Benjamin", publicKeyForUser7, privateKeyForUser7)
user8 = User("Lucas", publicKeyForUser8, privateKeyForUser8)
user9 = User("Henry", publicKeyForUser9, privateKeyForUser9)
user10 = User("Theodore", publicKeyForUser10, privateKeyForUser10)


transaction_data1 = {
    "from": user1.name,
    "to": user2.name,
    "amount": 100
}

transaction_data2 = {
    "from": user2.name,
    "to": user1.name,
    "amount": 50
}
transaction_data3 = {
    "from": user3.name,
    "to": user4.name,
    "amount": 80
}
transaction_data4 = {
    "from": user7.name,
    "to": user6.name,
    "amount": 70
}
transaction_data5 = {
    "from": user5.name,
    "to": user10.name,
    "amount": 100
}

transaction1 = Transaction(transaction_data1)
transaction1.seller_signature = user1.signature(transaction1)
transaction1.buyer_signature = user2.signature(transaction1)

transaction2 = Transaction(transaction_data2)
transaction2.seller_signature = user1.signature(transaction2)
transaction2.buyer_signature = user2.signature(transaction2)

transaction3 = Transaction(transaction_data3)
transaction3.seller_signature = user3.signature(transaction2)
transaction3.buyer_signature = user4.signature(transaction2)

transaction4 = Transaction(transaction_data4)
transaction4.seller_signature = user7.signature(transaction2)
transaction4.buyer_signature = user6.signature(transaction2)

transaction5 = Transaction(transaction_data5)
transaction5.seller_signature = user5.signature(transaction2)
transaction5.buyer_signature = user10.signature(transaction2)

block_chain.new_transaction(transaction1)
block_chain.new_transaction(transaction2)
block_chain.new_transaction(transaction3)
block_chain.new_transaction(transaction4)
block_chain.new_transaction(transaction5)

block_chain.new_block()

for block in block_chain.block_chain:
    print(block.convertstring())


'''
SANTHA MATE IMRE
HORA37
DEIK-PTI-MSC
2022-AUTUMN
'''

