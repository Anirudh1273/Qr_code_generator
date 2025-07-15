QR Code Generator for Resource Checklists

Objective
This is a web app that reads a CSV file and generates QR codes with the format:
resource://<Checklist>/<Location>/<Phase Number>

Each QR code:
- Encodes the correct resource format
- Displays the Name as a label below the QR image
- Can be downloaded individually (PNG) or as a compiled PDF

Tech Stack
- Backend: Python (Flask)
- Frontend: HTML + JavaScript
- Libraries: 
  - pandas – to read the CSV file  
  - qrcode – to generate QR images  
  - pillow – to draw labels  
  - reportlab – to create PDF

How to Run
1. Clone or download this project
2. Open terminal inside the project folder
3. Install dependencies:

bash
pip install flask pandas qrcode pillow reportlab
Run the app:
python app.py

Open your browser and go to:
http://127.0.0.1:5000

Input Format (CSV):
Name,Checklist,Location,Phase Number
Pump 1,Mechanical,Plant A,1
Valve 2,Electrical,Plant B,2
Pipe 3,Civil,Plant C,3

Output
PNG images in /output
PDF file containing all QR codes

Example
QR Code Text: resource://Mechanical/Plant A/1
Filename: Pump_1_Mechanical_Plant_A_1.png
