# STRIPE-REVERSE-CHECKOUT-SESSION

🔓 You have the ability to decrypt the checkout URLs and restore them to their original form. (ENCRYPT + DECRYPT) and Stripe Checkout Session to grab Payment information (Decrypted and kind of reverse engineered version)


## 🧾 The NutShell

Stripe Checkout Session: They use the [XOR](https://en.wikipedia.org/wiki/XOR_cipher) algorithm to obfuscate the client-side key (PK_KEY) in the Checkout URL. They also encode it, and if you want to automate something Via just using a URL, you can't directly do that. I know this automatically decrypts in the browser, and you can also just grab it via Selenium or any other automation library, but it's very slow. So that's why I spent my time trying to find out this, so I just tried to brute force the correct digit (0 to 1000) because you want to find the key; otherwise, you can't do anything about that. We want to use the [BITWISE operator](https://en.wikipedia.org/wiki/XOR_cipher), so my code was very simple, and I found the correct digit, which was number 5. Hak, yeah, it was a very easy key. You just want to have some understanding about this, and everything is crackable!.

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
