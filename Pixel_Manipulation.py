from PIL import Image

def swap_pixels(image):
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (g, b, r)

    return image

def encrypt_image(image_path):
    image = Image.open(image_path)
    encrypted_image = swap_pixels(image)
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(image_path):
    image = Image.open(image_path)
    decrypted_image = swap_pixels(image)
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully.")

def main():
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ")
        if choice.lower() == 'q':
            break
        if choice.lower() not in ['e', 'd']:
            print("Invalid choice. Please try again.")
            continue

        image_path = input("Enter the image file path: ")

        if choice.lower() == 'e':
            encrypt_image(image_path)
        else:
            decrypt_image(image_path)

if __name__ == "__main__":
    main()
