from bs4 import BeautifulSoup
from phe import paillier
import requests
import json


N = 2048 # Paillier N
url = "http://0.0.0.0:8080/prediction"

public_key, private_key = paillier.generate_paillier_keypair(n_length=N)

secret_number_list = [0,0,0,0,0,0,0,0,0,0] # for w0 (bias), which is equal: 0.0545806884765625
secret_number_list = [1,0,0,0,0,0,0,0,0,0] # for w1, w0 + w1 = 0.189849853515625; w1 = 0.189849853515625 - 0.0545806884765625 = 0.13526916503
secret_number_list = [0,1,0,0,0,0,0,0,0,0] # for w2, w0 + w2 = 0.0817108154296875; w2 = 0.0817108154296875 - 0.0545806884765625 = TODO
secret_number_list = [0,0,1,0,0,0,0,0,0,0] # for w3, w0 + w3 = 0.2404632568359375; w3 = 0.2404632568359375 - 0.0545806884765625 = TODO
secret_number_list = [0,0,0,1,0,0,0,0,0,0] # for w4, w0 + w4 = 0.069122314453125; w4 = 0.069122314453125 - 0.0545806884765625 = TODO
secret_number_list = [0,0,0,0,1,0,0,0,0,0] # for w5, w0 + w5 = 0.1114959716796875; w5 = 0.1114959716796875 - 0.0545806884765625 = TODO
secret_number_list = [0,0,0,0,0,1,0,0,0,0] # for w6, w0 + w6 = 0.1644744873046875; w6 = 0.1644744873046875 - 0.0545806884765625 = TODO
secret_number_list = [0,0,0,0,0,0,1,0,0,0] # for w7, w0 + w7 = 0.220703125; w7 = 0.220703125 - 0.0545806884765625 = TODO
secret_number_list = [0,0,0,0,0,0,0,1,0,0] # for w8, w0 + w8 = 0.0946807861328125; w8 = 0.0946807861328125 - 0.0545806884765625 = TODO
secret_number_list = [0,0,0,0,0,0,0,0,1,0] # for w9, w0 + w9 = 0.108489990234375; w9 = 0.108489990234375 - 0.0545806884765625 = TODO
secret_number_list = [0,0,0,0,0,0,0,0,0,1] # for w10, w0 + w10 = 0.210235595703125; w10 = 0.210235595703125 - 0.0545806884765625 = 0.15565490722

# We have to send D+1 queries to get all the parameters of the model

encrypted_number_list = [public_key.encrypt(x, precision=2**(-16)).ciphertext() for x in secret_number_list]  # check this

response = requests.post(url, json={"pub_key_n": public_key.n, "enc_feature_vector": encrypted_number_list})
json_data = response.json()
ciphertext = json_data["enc_prediction"]
predNumberEncrypted = paillier.EncryptedNumber(public_key, ciphertext, exponent=-8) # check this

print("predNumber=", private_key.decrypt(predNumberEncrypted))
