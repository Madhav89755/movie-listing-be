import sys

def unknown_exception_logger(e:Exception)->str:
    """
    This function logs the important details regarding the exception 
    that is passed on to this function like:
    - Exception Details
    - Exception Type
    - Exception occurred in file name
    - Exception occurred on line 
    """
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    print("======================================================")
    print(f"Exception is: {e}")
    print(f"Exception type: {str(exception_type)}")
    print(f"File name: {str(filename)}")
    print(f"Line number: {str(line_number)}")
    print("======================================================")
    return str(e)

