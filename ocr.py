import easyocr
from rapidocr import RapidOCR


"""A separate class for Ocr"""
class Ocr:

    """Constructor function for applying ocr strategy"""

    def __init__(self, file_path, ocr_strategy = None, backup_strategy = None):
        
        """take price and discount strategy"""

        self.file_path = file_path
        self.ocr_strategy = ocr_strategy
        self.backup_strategy = backup_strategy
        

    def run(self):
        """function to run the strategy"""
        try:
            print("hello")
            self.ocr_strategy(self.file_path)
        except:
            self.backup_strategy(self.file_path)
            print("error")


"""function dedicated for easy ocr"""
def easy_ocr(file_path):
    print("Using Easy OCR Strategy")
    reader = easyocr.Reader(['en'])
    result = reader.readtext(file_path, detail=0)
    print("OCR Result: ", result)
    return result

def rapid_ocr(file_path):
    engine = RapidOCR()

    result = engine(file_path)
    print(result)
    result.vis("vis_result.jpg")


    
def backup_strategy(file_path):
    print("Using Backup OCR Strategy")
    return ["Backup OCR Result"]
    

"""main function"""
if __name__ == "__main__":
    
    """Use easyocr"""
    print(Ocr(file_path='./random-invoice.png', ocr_strategy = rapid_ocr, backup_strategy = easy_ocr).run())
