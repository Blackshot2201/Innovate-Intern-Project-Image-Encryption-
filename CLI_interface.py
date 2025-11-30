import argparse
from image_encryption import ImageEncryptor
import os

def main():
    parser = argparse.ArgumentParser(description="Image Encryption Tool")
    
    # Operation selection
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", action="store_true", help="Encrypt an image")
    group.add_argument("-d", "--decrypt", action="store_true", help="Decrypt an image")
    
    # File arguments
    parser.add_argument("-i", "--input", required=True, help="Input file path")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    parser.add_argument("-k", "--keyfile", help="Key file path (default: generate new key)")
    
    args = parser.parse_args()
    
    # Process the operation
    if args.encrypt:
        if args.keyfile:
            encryptor = ImageEncryptor.load_from_keyfile(args.keyfile)
        else:
            encryptor = ImageEncryptor()
            # Save the generated key
            keyfile = os.path.splitext(args.output)[0] + ".key"
            encryptor.generate_key_file(keyfile)
            print(f"Generated new key file: {keyfile}")
        
        encryptor.encrypt_to_file(args.input, args.output)
        print(f"Image encrypted and saved to: {args.output}")
        
    elif args.decrypt:
        if not args.keyfile:
            parser.error("Key file required for decryption (-k/--keyfile)")
            
        encryptor = ImageEncryptor.load_from_keyfile(args.keyfile)
        encryptor.decrypt_to_file(args.input, args.output)
        print(f"Image decrypted and saved to: {args.output}")

if __name__ == "__main__":
    main()
