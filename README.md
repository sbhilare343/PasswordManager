# PasswordManager
This Python code is a simple password manager application built using the Tkinter library for creating a graphical user interface (GUI). The code allows users to generate, save, and retrieve passwords for various websites along with associated email or username information. Below is a description of the key components and functionality of the code:

1. **Password Generator Function (pass_generator):**
   - This function generates a random password and displays it in the "Password" entry field.
   - It also copies the generated password to the clipboard for easy pasting.
   - The generated password consists of a combination of uppercase and lowercase letters, numbers, and special symbols.

2. **Save Password Function (save_pass):**
   - This function is called when the "Submit" button is pressed after entering website, email, and password information.
   - It first checks if all the required fields are filled and if the password is at least 6 characters long.
   - It then creates a JSON object to store the website, email, and password as key-value pairs.
   - If a JSON file named "Password.json" does not exist, it creates one. Otherwise, it updates the existing JSON file with the new data.
   - After saving the data, it clears the input fields for the next entry.

3. **Find Password Function (find_pass):**
   - This function is called when the "Search" button is pressed after entering a website name.
   - It attempts to open the "Password.json" file and load its content into a dictionary.
   - If the website name entered by the user is found in the dictionary, it displays the associated email/username and password in a message box.
   - If the website is not found or no website name is entered, it shows an appropriate message.

4. **UI Setup:**
   - The code sets up the user interface using the Tkinter library.
   - It creates a window with the title "Password Manager" and sets a minimum size.
   - A canvas is used to display an image (assuming there's a "logo.png" file in the same directory).
   - Labels, entry fields, and buttons are added to the UI for entering and displaying data.

5. **Main Application Loop:**
   - The code enters the Tkinter main loop using `window.mainloop()` to keep the GUI running and responsive.

