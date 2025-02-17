import sys

## Error message function 
## gives the error message, the scipt name and line of error
def error_message_detail(error,error_detail:sys):
    # extract the error details from sys 
    # ignores the first two elements of the sys list
    # names traceback object as exc_tb
    _,_,exc_tb=error_detail.exc_info()

    # get the file name from the traceback object
    # get the line number from the traceback object
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno

    # format error message including file name, line number and error message
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,line_number,str(error))

    return error_message

# create a CustomException class that inherits from the Exception class
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message