from noninput_task import NonInputExecution
from input_task import InputExecution
from api_task import ApiExecution
from stock_task import StockExecution

try:
    InputExecution(reply,sentence)
    try:
        NonInputExecution(reply)
    except:
        print("")
    try:
        ApiExecution(reply,sentence)
    except:
        print("")
    try:
        StockExecution(reply,sentence)
    except:
        print("")
except:
    print("")

