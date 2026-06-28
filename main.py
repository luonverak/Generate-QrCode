from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from dto.request.qrcode_request import QRRequest
import qrcode
import io
import os

app = FastAPI()

@app.post("/generate-qr")
def generate_qr(body: QRRequest):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=body.box_size,
        border=body.border,
    ) 
    qr.add_data(body.link)
    qr.make(fit=True)

    img = qr.make_image(fill_color=body.fill_color, back_color=body.back_color)

    # Create folder by qr_type
    folder_path = os.path.join("qr_output", body.qr_type)
    os.makedirs(folder_path, exist_ok=True)

    # ✅ Rename file by no
    file_name = f"{body.no}.png"
    file_path = os.path.join(folder_path, file_name)
    img.save(file_path)
    print(f"===== Saved to {file_path}")

    # Return as streaming response
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")