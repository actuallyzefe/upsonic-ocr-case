from fastapi import FastAPI
from pydantic import BaseModel
from ocr import Ocr, easy_ocr, rapid_ocr
import uvicorn

app = FastAPI()


class OcrRequest(BaseModel):
    ocr_strategy: str
    backup_strategy: str 

@app.post("/ocr")
async def process_ocr(request: OcrRequest):
    strategy_map = {
        "easy_ocr": easy_ocr,
        "rapid_ocr": rapid_ocr
    }
    
    if request.ocr_strategy not in strategy_map:
        return {"error": f"Invalid ocr_strategy. Choose from: {list(strategy_map.keys())}"}
    
    if request.backup_strategy not in strategy_map:
        return {"error": f"Invalid backup_strategy. Choose from: {list(strategy_map.keys())}"}
    

    ocr_strategy_func = strategy_map[request.ocr_strategy]
    backup_strategy_func = strategy_map[request.backup_strategy]
    

    ocr = Ocr(
        file_path="./random-invoice.png",
        ocr_strategy=ocr_strategy_func,
        backup_strategy=backup_strategy_func
    )
    
    ocr.run()
    
    return {
        "message": "OCR processing completed",
        "file_path": "./random-invoice.png",
        "ocr_strategy": request.ocr_strategy,
        "backup_strategy": request.backup_strategy,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)