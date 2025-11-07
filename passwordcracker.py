import hashlib

def main():
    print("---Hash Cracker---")
    while True:
        word_list = input("\nWhat is your word list file named?")
        try:
            with open(word_list, 'r'):
                break
        except FileNotFoundError:
            print("Invalid File")
    while True:
        hash_list = input("What is your hash list file named?")
        try:
            with open(hash_list, 'r'):
                break
        except FileNotFoundError:
            print("Invalid File")
    done_hashes, hashes = password_cracker(hash_list, word_list)
    if done_hashes:
        print(done_hashes, end="")
    else:
        print("No matches found.")

def password_cracker(hash_list, name_list):
    hashes = []
    done_hashes = ""
    with open(hash_list, "r") as f:
        for line in f:
            value = line.strip()
            if value:
                hashes.append(value.lower())
    with open(name_list, "r") as f:
        for line in f:
            word = line.strip()
            if not word:
                continue
            word_hash = hashlib.md5(word.encode()).hexdigest()
            if word_hash in hashes:
                hashdex = hashes.index(word_hash)
                done_hashes += f"[+] {hashes[hashdex]} matched to {word}\n"
    return done_hashes, hashes

if __name__ == "__main__":
    main()
