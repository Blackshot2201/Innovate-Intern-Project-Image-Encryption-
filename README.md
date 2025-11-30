🔐 Image Encryption & Decryption Tool
Innovate Intern – Final Project Submission

This project is a secure Image Encryption & Decryption System built using AES-256 encryption, developed as part of the Innovate Intern Program.
It allows users to encrypt images into unreadable ciphertext and decrypt them back using a unique key file — ensuring maximum data protection.

🚀 Features

🔒 AES-256 Encryption (Industry-Standard Security)

🧩 CBC Mode with Automatic IV Generation

🗂️ Key Generation & Key File Saving System

🖼️ Supports JPG, PNG, and other common image formats

💻 Simple Command-Line Interface (CLI)

⚡ High performance using OpenCV & PyCryptodome

🔑 Decryption requires the same key file (high security)

📌 Project Structure
📂 Project Root
├── CLI_interface.py        # Command-line interface for encrypt/decrypt
├── Image_encreption.py     # AES-256 encryption/decryption core logic
├── test                # test sets are that doing a test
└── README.md               # Documentation

🛠️ Installation
1️⃣ Install Dependencies

Use the following command to install required libraries:

pip install opencv-python Pillow pycryptodome numpy

2️⃣ Clone the Repository
git clone https://github.com/Blackshot2201/Innovate-Intern-Project-Image-Encryption
cd ONGC-Project-

🧪 Usage (CLI Commands)

The CLI tool is powered by CLI_interface.py and supports both encryption and decryption operations.

🔐 Encrypt an Image
python CLI_interface.py -e -i input.jpg -o encrypted.bin


✔ Automatically creates a .key file
✔ Saves encrypted bytes in .bin format

🔓 Decrypt an Image
python CLI_interface.py -d -i encrypted.bin -o output.jpg -k encrypted.key


✔ Requires the original key file
✔ Successfully restores the original image

🔧 How It Works (Technical Summary)
AES-256 Encryption – Secure & Reliable

This project uses AES-256 (Advanced Encryption Standard) in CBC mode, ensuring strong protection.

Process overview:

A 32-byte random key is generated (if no key is provided)

The image is read and converted to bytes

Data is padded and encrypted

A random IV (Initialization Vector) is added

Output file = IV + encrypted ciphertext

📸 Example Workflow
1️⃣ Input Image

photo.jpg

2️⃣ Encryption Output

photo_encrypted.bin

photo_encrypted.key

3️⃣ Decryption Output

photo_decrypted.jpg (restored image)

📚 Learning Outcome

During this project, the following concepts were explored and implemented:

🔐 Cryptography & AES-256

🧠 Image processing using OpenCV

🗂️ Secure key management

🧩 CLI-based Python utilities

📁 Binary file handling

🛡 Data confidentiality & protection

🏆 Credits

Developed by: Your Name
Program: Innovate Intern – ONGC Project

If you found this useful, don’t forget to ⭐ star the repository!
