import hashlib

def read_dictionary(file_path):
    """Reads a dictionary file and returns a list of words."""
    with open(file_path, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words]

def hash_password(password, algorithm='sha256'):
    """Hashes the given password using the specified algorithm (MD5 or SHA-256)."""
    if algorithm.lower() == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm.lower() == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing algorithm. Choose either 'md5' or 'sha256'.")

def dictionary_attack(hash_to_crack, dictionary, algorithm='sha256'):
    """Performs a dictionary attack on a given hash using the specified algorithm."""
    for word in dictionary:
        hashed_word = hash_password(word, algorithm)
        if hashed_word == hash_to_crack:
            return word
    return None

if __name__ == "__main__":
    dictionary_file = "dictionary.txt"  # Path to your dictionary file
    hash_to_crack = input("Enter the hash to crack: ").strip()
    algorithm = input("Enter the hashing algorithm (MD5 or SHA-256): ").strip().lower()

    dictionary = read_dictionary(dictionary_file)
    cracked_password = dictionary_attack(hash_to_crack, dictionary, algorithm)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found in the dictionary.")
