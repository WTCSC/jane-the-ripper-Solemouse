import hashlib
#Checks if the word list file exists
def main():
    print("---Welcome to a Hash Cracker---")
    while True:
        word_list = input("\nWhat is your word list file?")
        try:
            with open(word_list, 'r') as test_file:
                break
        except FileNotFoundError:
            print("Invalid File")
#Checks if the hash list file exists
    while True:
        hash_list = input("What is your hash list file?")
        try:
            with open(hash_list, 'r') as test_file:
                break
        except FileNotFoundError:
            print("Invalid File")
# Password Cracker
def password_cracker(hash_list, name_list):
    hashes = []
    done_hashes = ""
    with open(hash_list, "r") as f:
        for line in f 

            
   
    
        

        

    
