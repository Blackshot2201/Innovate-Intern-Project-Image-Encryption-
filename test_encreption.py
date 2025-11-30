import unittest
import os
import numpy as np
from src.image_encryption import ImageEncryptor
import cv2

class TestImageEncryption(unittest.TestCase):
    def setUp(self):
        self.test_image = "data/sample_input.jpg"
        self.output_enc = "data/encrypted.bin"
        self.output_dec = "data/decrypted.jpg"
        self.key_file = "data/test.key"
        
        # Create test image if it doesn't exist
        if not os.path.exists(self.test_image):
            img = np.zeros((100, 100, 3), dtype=np.uint8)
            cv2.imwrite(self.test_image, img)

    def test_encryption_decryption(self):
        # Initialize encryptor
        encryptor = ImageEncryptor()
        
        # Encrypt the image
        encrypted = encryptor.encrypt_image(self.test_image)
        encryptor.save_encrypted(encrypted, self.output_enc)
        
        # Decrypt the image
        decrypted = encryptor.decrypt_image(encrypted)
        cv2.imwrite(self.output_dec, decrypted)
        
        # Verify files exist
        self.assertTrue(os.path.exists(self.output_enc))
        self.assertTrue(os.path.exists(self.output_dec))
        
        # Compare original and decrypted images
        original = cv2.imread(self.test_image)
        decrypted = cv2.imread(self.output_dec)
        self.assertTrue(np.array_equal(original, decrypted))
        
    def test_key_persistence(self):
        # Test with key file
        encryptor1 = ImageEncryptor()
        encryptor1.generate_key_file(self.key_file)
        
        data = encryptor1.encrypt_image(self.test_image)
        
        encryptor2 = ImageEncryptor.load_from_keyfile(self.key_file)
        decrypted = encryptor2.decrypt_image(data)
        
        original = cv2.imread(self.test_image)
        self.assertTrue(np.array_equal(original, decrypted))
        
    def tearDown(self):
        # Clean up test files
        for f in [self.output_enc, self.output_dec, self.key_file]:
            if os.path.exists(f):
                os.remove(f)

if __name__ == '__main__':
    unittest.main()
