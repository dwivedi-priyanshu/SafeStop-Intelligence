import sys
import os

# This function extracts detailed error information
def error_message_detail(error, error_detail: sys):
    # exc_info() returns (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()
    
    # Extract the filename where exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message with file name, line number, and error
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


# Custom Exception class
class SensorException(Exception):
    
    # Constructor: takes error message and system error details
    def __init__(self, error_message: str, error_detail: sys):
        # Call parent Exception class constructor
        super().__init__(error_message)
        
        # Store detailed error message using helper function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    # This method is called when you print the exception
    def __str__(self):
        # Return the custom formatted error message
        return self.error_message