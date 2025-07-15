from flask import Flask, request, send_file, jsonify, render_template
import pandas as pd
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
from reportlab.pdfgen import canvas


app = Flask(__name__)
UPLOAD_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    df = pd.read_csv(file)

    pdf_path = os.path.join(UPLOAD_FOLDER, "all_qr_codes.pdf")
    c = canvas.Canvas(pdf_path)

    for index, row in df.iterrows():
        name = str(row['Name']).strip().replace(" ", "_")
        checklist = str(row['Checklist']).strip().replace(" ", "_")
        location = str(row['Location']).strip().replace(" ", "_")
        phase = str(row['Phase Number']).strip()

        qr_data = f"resource://{checklist}/{location}/{phase}"
        filename = f"{name}_{checklist}_{location}_{phase}.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        # For Generating a QR code
        qr = qrcode.make(qr_data)
        qr = qr.resize((300, 300))

        # To Add a name label
        img = Image.new("RGB", (300, 340), "white")
        img.paste(qr, (0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((10, 310), row['Name'], fill="black")

        img.save(filepath)

        # For Adding to PDF
        c.drawImage(filepath, 100, 550 - (index % 3) * 220, width=200, height=200)
        if index % 3 == 2:
            c.showPage()

    # Finish and save as a PDF
    c.save()
    return jsonify({"message": "QR codes generated!", "folder": UPLOAD_FOLDER})

# To donwload the PDF
@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    return send_file(os.path.join(UPLOAD_FOLDER, "all_qr_codes.pdf"))

if __name__ == '__main__':
    app.run(debug=True)
