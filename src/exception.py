import sys
# import system

def error_message_detail(error, error_detail: sys) -> str:   
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        """
        :param error_message: error message in string format
        :param error_detail: sys module for accessing exception information
        """
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message



# import sys

# class CustomException(Exception):
#     def __init__(self, error_message, sys_info=None):
#         self.error_message = error_message
#         self.error_message_detail = self.error_message_detail(error_message, sys_info)
#         super().__init__(self.error_message)
        
#     def error_message_detail(self, error_message, sys_info):
#         try:
#             exc_type, exc_value, exc_tb = sys_info if sys_info else sys.exc_info()
#             file_name = exc_tb.tb_frame.f_code.co_filename
#             line_number = exc_tb.tb_lineno
#             error_message = f"Error occurred python script name [{file_name}] line number [{line_number}] error message [{str(error_message)}]"
#             return error_message
#         except Exception as e:
#             return f"Error in processing the exception: {str(e)}"
