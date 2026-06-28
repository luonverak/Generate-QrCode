from pydantic import BaseModel, Field

class QRRequest(BaseModel):
    no:str = Field(..., description="No of qr code")
    link: str = Field(..., description="Text or URL to encode")
    qr_type: str = Field(..., description="Folder name to save QR (e.g. Facebook, Youtube)")
    fill_color: str = Field("black", description="QR code color")
    back_color: str = Field("white", description="Background color")
    box_size: int = Field(10, gt=0, le=50, description="Pixels per box")
    border: int = Field(4, gt=0, le=20, description="Border thickness")