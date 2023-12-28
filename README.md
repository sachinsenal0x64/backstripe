<div align="center">
   <a href="https://stripe.com">
  <img src="/assets/stripe.svg" width="250" height="125" alt="stripe">
</a>


<img src="https://cdn.jsdelivr.net/gh/sachinsenal0x64/PICX-IMAGE-HOSTING@master/ledstrip.3024rqxzahq0.gif"
width="1800"  height="3">


# STRIPE-REVERSE-CHECKOUT-SESSION


> Made for purely educational purposes.

🔓 You have ability to decrypt the checkout URLs and restore them to their original form. (ENCRYPT + DECRYPT) and Stripe Checkout Session to grab Payment information (Decrypted and kind of reverse engineered version)
</div>

<br>

## 🧾 The NutShell

Stripe.com (May 5, 2023): XOR algorithm to obfuscate the client-side key (pk-key) and base64 to encode checkout url.so if you want to automate something by just using checkout url, you can't directly do that the reason is its encrypted so you have to decrypt. I know this automatically decrypts in the browser, and you can also just grab pk_key  via using selenium or any other automation library, but it's very slow and it's not how stripe backend works. So that's why I spent my time trying to find out the correct key to decrypt this session url using xor algorithm. I just tried to brute force the correct digit using the range of numbers (0 to 1000); otherwise, you can't do anything. In python we have to use  a bitwise operator to proceed xor, and my code was very simple. It has a full reverse headless way to build a checkout session. Also I found the correct digit, it was number 5 this is the keypoint.

<br>

## 🔑 GAME CHANGER 

ACTUAL DECRYPTING PART (AFTER THE DECODE)

```Python
# DECODE

print("Decoded PK value:", decoded_pk)

# ASSIGN

dry = ""

# DECRYPT WITH VALUE 5

for c in decoded_pk:
    dry += chr(5 ^ c)

print("Decoded ck value:", ck)

print("Decrypted PK value:", dry)

```
