import csv
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Save the key to a file (you'll need this to decrypt the data later)
with open('encryption_key.key', 'wb') as key_file:
    key_file.write(key)


# Function to encrypt data
def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()


# Read the CSV file, encrypt the data, and write to a new CSV file
input_csv = 'finance_data.csv'
output_csv = 'encrypted_finance_data.csv'

with open(input_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    encrypted_data = []

    for row in reader:
        encrypted_row = [encrypt_data(item) for item in row]
        encrypted_data.append(encrypted_row)

with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(encrypted_data)

print("Data has been encrypted and saved to", output_csv)
