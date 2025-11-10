from fastapi import FastAPI, UploadFile, File, Form
from ocr import Ocr, easy_ocr, rapid_ocr
import uvicorn

app = FastAPI()


@app.post("/ocr")
async def process_ocr(file: UploadFile = File(...), ocr_strategy: str = Form(...), backup_strategy: str = Form(...)):
    strategy_map = {
        "easy_ocr": easy_ocr,
        "rapid_ocr": rapid_ocr
    }
    
    if ocr_strategy not in strategy_map:
        return {"error": f"Invalid ocr_strategy. Choose from: {list(strategy_map.keys())}"}
    
    if backup_strategy not in strategy_map:
        return {"error": f"Invalid backup_strategy. Choose from: {list(strategy_map.keys())}"}
    

    file_path = f"./{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    
    ocr = Ocr(
        file_path=file_path,
        ocr_strategy=strategy_map[ocr_strategy],
        backup_strategy=strategy_map[backup_strategy]
    )
    
    ocr.run()
    
    return {
        "message": "OCR processing completed",
        "file_path": file_path,
        "ocr_strategy": ocr_strategy,
        "backup_strategy": backup_strategy,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)