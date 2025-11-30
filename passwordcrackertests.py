import unittest
import hashlib
from passwordcracker import password_cracker

class TestPasswordCracker(unittest.TestCase):
    def test_single_match(self):
        with open("words.txt","w") as w: w.write("password\n")
        with open("hashes.txt","w") as h: h.write(hashlib.md5(b"password").hexdigest()+"\n")
        done_hashes, hashes = password_cracker("hashes.txt","words.txt")
        self.assertEqual(hashes, [hashlib.md5(b"password").hexdigest()])
        self.assertIn(f"[+] {hashlib.md5(b'password').hexdigest()} matched to password", done_hashes)

    def test_no_match(self):
        with open("words.txt","w") as w: w.write("not_in_list\n")
        with open("hashes.txt","w") as h: h.write(hashlib.md5(b"something_else").hexdigest()+"\n")
        done_hashes, hashes = password_cracker("hashes.txt","words.txt")
        self.assertEqual(hashes, [hashlib.md5(b"something_else").hexdigest()])
        self.assertEqual(done_hashes, "")

    def test_multiple_matches(self):
        with open("words.txt","w") as w: w.write("alpha\nbeta\n")
        with open("hashes.txt","w") as h: 
            h.write(hashlib.md5(b"alpha").hexdigest()+"\n")
            h.write(hashlib.md5(b"beta").hexdigest()+"\n")
        done_hashes, hashes = password_cracker("hashes.txt","words.txt")
        self.assertIn(f"[+] {hashlib.md5(b'alpha').hexdigest()} matched to alpha", done_hashes)
        self.assertIn(f"[+] {hashlib.md5(b'beta').hexdigest()} matched to beta", done_hashes)

    def test_empty_files(self):
        with open("words.txt","w") as w: w.write("")
        with open("hashes.txt","w") as h: h.write("")
        done_hashes, hashes = password_cracker("hashes.txt","words.txt")
        self.assertEqual(hashes, [])
        self.assertEqual(done_hashes, "")

if __name__ == "__main__":
    unittest.main()
