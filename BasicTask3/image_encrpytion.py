from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    original_image = Image.open(image_path)
    
    # Get image dimensions
    width, height = original_image.size
    
    # Create a new blank image of the same size
    encrypted_image = Image.new("RGB", (width, height))
    
    # Loop through each pixel and apply encryption
    for x in range(width):
        for y in range(height):
            # Get the pixel value
            pixel = original_image.getpixel((x, y))
            
            # Apply encryption algorithm
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            
            # Set the pixel value in the encrypted image
            encrypted_image.putpixel((x, y), encrypted_pixel)
    
    return encrypted_image

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    
    # Get image dimensions
    width, height = encrypted_image.size
    
    # Create a new blank image of the same size
    decrypted_image = Image.new("RGB", (width, height))
    
    # Loop through each pixel and apply decryption
    for x in range(width):
        for y in range(height):
            # Get the encrypted pixel value
            encrypted_pixel = encrypted_image.getpixel((x, y))
            
            # Apply decryption algorithm
            decrypted_pixel = tuple((p - key) % 256 for p in encrypted_pixel)
            
            # Set the pixel value in the decrypted image
            decrypted_image.putpixel((x, y), decrypted_pixel)
    
    return decrypted_image

# Example usage:
image_path = "bee.jpeg"
key = 123456

# Encrypt the image
encrypted_image = encrypt_image(image_path, key)
encrypted_image.save("encrypted_image.png")

# Decrypt the encrypted image
decrypted_image = decrypt_image("encrypted_image.png", key)
decrypted_image.save("decrypted_image.png")
