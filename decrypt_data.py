import csv
from cryptography.fernet import Fernet

# Load the key for decryption
with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)


# Function to decrypt data
def decrypt_data(data):
    return cipher.decrypt(data.encode()).decode()


# Read the encrypted CSV file, decrypt the data, and write to a new CSV file
encrypted_csv = 'encrypted_finance_data.csv'
decrypted_csv = 'decrypted_finance_data.csv'

with open(encrypted_csv, newline='') as csvfile:
    reader = csv.reader(csvfile)
    decrypted_data = []

    for row in reader:
        decrypted_row = [decrypt_data(item) for item in row]
        decrypted_data.append(decrypted_row)

with open(decrypted_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(decrypted_data)

print("Data has been decrypted and saved to", decrypted_csv)
