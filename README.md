Personal Password Manager 
This program is a simple command-line password manager built in Python. It allows users to save, view, and generate passwords for different websites. The passwords are stored in a text file (password.txt) so they can be retrieved later.

Key Features
Load Existing Passwords: When the program starts, it reads previously saved passwords from password.txt and loads them into memory.

Save Passwords: Users can enter a website name and its password. The program stores this information both in memory and appends it to the text file.

View Passwords: Users can view saved passwords. (Currently, the code prints only the last entered site and password, which can be improved to show all saved entries.)

Generate Passwords: The program can automatically generate a random 8-character password using letters, digits, and special symbols.

Exit Option: Users can quit the program gracefully.

How It Works
The program displays a menu with four options:

Save Password

View Password

Generate Password

Exit

Based on the user’s choice, it performs the corresponding action.

Passwords are stored in a dictionary (password) and also written to a file for persistence.

Limitations / Improvements
The view password option currently only prints the last entered site and password instead of all saved ones.

Generated passwords are only 8 characters long; increasing length (e.g., 12–16) would improve security.

File handling uses append mode ("a"), which may cause duplicates. Using write mode with overwrite or structured storage (like JSON) would be cleaner.

Adding a search option (to find a password for a specific site) would make it more practical.
