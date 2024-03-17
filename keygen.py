import random,base64,datetime
def generate_key():
    # Generate random string of characters
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
    
    # Encode the random string in base64
    encoded_random_string = base64.b64encode(random_string.encode()).decode()
    
    # Encode the current date in base64
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    encoded_date = base64.b64encode(current_date.encode()).decode()
    
    # Concatenate the encoded random string and date with a separator
    key = f"{encoded_random_string}:{encoded_date}"
    
    return key
print("Generated key:", generate_key())