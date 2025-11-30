import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from PIL import Image
import io

class ImageEncryptor:
    def __init__(self, key=None):
        """
        Initialize the encryptor with an optional key.
        If no key is provided, a random one will be generated.
        """
        self.key = key if key else get_random_bytes(32)  # AES-256
        self.block_size = AES.block_size

    def encrypt_image(self, image_path):
        """
        Encrypts an image file and returns the encrypted data
        """
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read image file")
            
        # Convert image to byte array
        _, img_encoded = cv2.imencode('.jpg', img)
        image_bytes = img_encoded.tobytes()
        
        # Create cipher object
        cipher = AES.new(self.key, AES.MODE_CBC)
        
        # Encrypt the image data
        ct_bytes = cipher.encrypt(pad(image_bytes, self.block_size))
        
        # Return IV + ciphertext
        return cipher.iv + ct_bytes

    def decrypt_image(self, encrypted_data):
        """
        Decrypts encrypted image data and returns a PIL Image object
        """
        # Extract IV and ciphertext
        iv = encrypted_data[:self.block_size]
        ct = encrypted_data[self.block_size:]
        
        # Create cipher object
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        # Decrypt the data
        pt = unpad(cipher.decrypt(ct), self.block_size)
        
        # Convert back to image
        img = cv2.imdecode(np.frombuffer(pt, dtype=np.uint8), cv2.IMREAD_COLOR)
        return img

    def save_encrypted(self, encrypted_data, output_path):
        """Save encrypted data to file"""
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)

    def load_encrypted(self, encrypted_path):
        """Load encrypted data from file"""
        with open(encrypted_path, 'rb') as f:
            return f.read()

    def encrypt_to_file(self, image_path, output_path):
        """Encrypt image and save directly to file"""
        encrypted = self.encrypt_image(image_path)
        self.save_encrypted(encrypted, output_path)
        
    def decrypt_to_file(self, encrypted_path, output_path):
        """Decrypt image and save to file"""
        encrypted = self.load_encrypted(encrypted_path)
        img = self.decrypt_image(encrypted)
        cv2.imwrite(output_path, img)
        
    def generate_key_file(self, key_path):
        """Save the encryption key to a file"""
        with open(key_path, 'wb') as f:
            f.write(self.key)
            
    @classmethod
    def load_from_keyfile(cls, key_path):
        """Create an instance using a saved key file"""
        with open(key_path, 'rb') as f:
            key = f.read()
        return cls(key)
