# STRIPE-REVERSE-CHECKOUT-SESSION

Stripe Checkout Session to grab Payment information (Decrypted + Kinda Reverse Engineered Version )

🔓 You have the ability to decrypt the checkout URLs and restore them to their original form.

## 🧾 The NutShell

Stripe Checkout Session they use [XOR](https://en.wikipedia.org/wiki/XOR_cipher) algorithm to obfuscate PK KEY (CLIENT SIDE KEY) in (CHECKOUT URL) also they encode it and if you want to automate something via just using url you cant directly do that i know this automatic decrypt in browser you can just grab via using selenium or any other automation library but its slow :/  so thats why i spend my time to find out this so i just try to brute force the correct digit (0 to 1000) bcs you want to find key else you cant do anything for that we want to use [BITWISE OPERATOR ](https://en.wikipedia.org/wiki/XOR_cipher) so my code was very simple and i found the correct digit its was number 5 hak yeah its was very easy key you just want to have some understand and everything Crackable btw i use python to do this.

## 🔑 GAME CHANGER 

ACTUAL DECRYPTING PART

```

print("Decoded PK value:", decoded_pk)

dry = ""

for c in decoded_pk:
    dry += chr(5 ^ c)

print("Decoded ck value:", ck)

print("Decrypted PK value:", dry)

```
