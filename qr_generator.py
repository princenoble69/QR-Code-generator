import qrcode

def generate_atu_qr_code(filename="atu_website_qr.png"):
    """
    Generates a QR code image linked directly to the ATU application website 
    and saves it as a PNG file.
    """
    # The data to be encoded is the website URL
    data = "https://application.atu.edu.gh/"
    
    try:
        # Create a QRCode object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher correction for better readability
            box_size=10,
            border=4,
        )
        
        # Add the data
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create and save the image
        img = qr.make_image(fill_color="darkblue", back_color="white") # Changed colors for visual appeal
        img.save(filename)
        
        print(f"Successfully generated QR Code for: {data}")
        print(f"Saved to file: {filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Run the Function ---
generate_atu_qr_code()