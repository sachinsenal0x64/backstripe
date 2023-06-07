
# # # Decrypt Keys

import base64


# Get the checkout link from the user
checkoutlink = input("\nEnter the checkout link: ")

# Decode the value after the '#' character
plain_ck = checkoutlink.split("#")[0].replace("https://checkout.stripe.com/c/pay/", "")

obfuscated_pk = checkoutlink.split("#")[1]

# Decrypted ck value
ck = f"{plain_ck}"

# Obfuscated PK value
obfuscated_pk = f"{obfuscated_pk}"
obfuscated_pk = obfuscated_pk.replace("%2F", "/")

# Add padding characters to the end of the obfuscated_pk value
while len(obfuscated_pk) % 4 != 0:
    obfuscated_pk += "="

# Decode the obfuscated_pk value from base64
decoded_pk = base64.b64decode(obfuscated_pk.encode("utf-8"))

print("Decoded PK value:", decoded_pk)

dry = ""

for c in decoded_pk:
    dry += chr(5 ^ c)

print("Decrypted ck value:", ck)

print("Decrypted PK value:", dry)






# Encrypt Keys

import base64
import json


# decrypt_pk 

start = "fidkdWxOYHwnPyd1blppbHNgWkBLPTNJV1ZSc39paVYxakBhPF99REI0ajU1bXF9RGhvYmQnKSdjd2poVmB3c2B3Jz9xd3BgKSdpZHxqcHFRfHVgJz8ndmxrYmlgWmxxYGgnKSdga2RnaWBVaWRmYG1qaWFgd3YnP3F3cGB4JSUl"

encods = base64.b64decode(start.encode('utf-8'))

print(encods)


pit =  ""


while len(pit) % 4 != 0:
    pit += "="


for p in encods:
    n = chr( 5 ^ p)
    pit += n
    
    
print(pit)



# encrypt_pk 


encrypt_pk = ""

# pit = json.dumps(pit)

for i in pit:   
    i = chr( 5 ^ ord(i))
    encrypt_pk += i
    

endecodee = base64.b64encode(encrypt_pk.encode('utf-8'))

checkout_link = f"https://checkout.stripe.com/c/pay/#{endecodee}"


print(checkout_link)




# encode checkout details


import json
import base64
import requests as r


cs = input("Enter the checkout session: ")

pk = input("Enter the pk: ")

dic_load = {"apiKey":f"{pk}","fromServer":True,"layoutType":"single_item","enablePlaceholders":True}


url = f"https://api.stripe.com/v1/payment_pages/{cs}/init"

header = {
    
    "authority": "api.stripe.com",
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type":"application/x-www-form-urlencoded",
    "origin":"https://checkout.stripe.com",
    "referer":"https://checkout.stripe.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
    
    
    
}

data = (f"key={pk}&eid=NA&browser_locale=en-US&redirect_type=stripe_js")


res = r.post(url=url,headers=header,data=data)

print(res.text)

# data = json.dumps(dic_load)


obs = "="

for c in data:
    obs += chr(ord(c) ^ 5 )
    
    
obs = obs.replace('%','').replace('x','x%%%')

unicode_escape_obs = obs.encode("utf-8")

unicode_escape_obs = base64.b64encode(unicode_escape_obs)

print(unicode_escape_obs)    











