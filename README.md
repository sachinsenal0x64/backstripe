<div align="center">
   <a href="https://stripe.com">
  <img src="/assets/stripe.svg" width="250" height="125" alt="stripe">
</a>


# STRIPE-REVERSE-CHECKOUT-SESSION


> Made for purely educational purposes.

🔓 You have ability to decrypt the checkout URLs and restore them to their original form. (ENCRYPT + DECRYPT) and Stripe Checkout Session to grab Payment information (Reverse Engineered Version)
</div>

<br>


## 🧾 Use Cases

- 🦾 Automation
- 🤖 Flexible

<br>

## 🧾 The NutShell

On May 5, 2023, Stripe.com added security measures by using an XOR algorithm to encrypt the client-side key (pk-key) and base64 for the checkout URL. This encryption makes automating tasks with the checkout URL challenging. While automation libraries like Selenium can extract the pk-key, it's slow and not how stripe.com handles the backend. To overcome this, I spent time reverse engineering Stripe API & finding the correct decryption key, using a simple brute force method testing numbers 0 to 1000. The correct key turned out to be 5, allowing for a straightforward Python code to decrypt and build a checkout session in a reverse way.

<br>

## 🔑 GAME CHANGER 

ACTUAL SIMPLE DECRYPTING PART (AFTER THE DECODE)

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
