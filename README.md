### Password Cracker

Passwords should never be stored in plain text. They should be stored as hashes, just in case the password list is discovered. However, not all hashes are created equal. 

`password_cracker.py` consists a function that takes in a SHA-1 hash of a password and returns the password if it is one of the top 10,000 passwords used. If the SHA-1 hash is NOT of a password in the database, it returns "PASSWORD NOT IN DATABASE".

The function hashes each password from `top-10000-passwords.txt` and compares it to the hash passed into the function.

The function takes an optional second argument named `use_salts`. If set to true, each salt string from the file `known-salts.txt` is appended AND prepended to each password from `top-10000-passwords.txt` before hashing and before comparing it to the hash passed into the function.

Examples:
* `b305921a3723cd5d70a375cd21a61e60aabb84ec` returns "sammy123"
* `c7ab388a5ebefbf4d550652f1eb4d833e5316e3e` returns "abacab"
* `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` returns "password"

When `use_salts` is set to `True`:
* `53d8b3dc9d39f0184144674e310185e41a87ffd5` returns "superman"
* `da5a4e8cf89539e66097acd2f8af128acae2f8ae` returns "q1w2e3r4t5"
* `ea3f62d498e3b98557f9f9cd0d905028b3b019e1` returns "bubbles1"
