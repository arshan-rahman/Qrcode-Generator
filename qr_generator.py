import qrcode

url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\arsha\\Documents\\qrcode\\qrcode.png"

img = qrcode.make(url)
img.save(file_path)

print("Your QR code has been successfully saved to your device!")