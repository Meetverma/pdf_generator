from flask import Flask, request, send_file, jsonify
from xhtml2pdf import pisa
import io
import os

app = Flask(__name__)

@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    data = request.json or {}
    html = data.get("html", "<h1>No content</h1>")
    print("📥 Received HTML:", html)

    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)

    if pisa_status.err:
        print("❌ PDF generation failed")
        return jsonify({"error": "Failed to generate PDF"}), 400

    # Save debug PDF to disk (so you can verify locally)
    with open("debug_output.pdf", "wb") as f:
        f.write(pdf_buffer.getvalue())
    print("✅ PDF written to debug_output.pdf")

    # Reset buffer position before sending
    pdf_buffer.seek(0)

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="output.pdf"
    )

if __name__ == "__main__":
    # Run on port 8080
    app.run(host="0.0.0.0", port=8080)
