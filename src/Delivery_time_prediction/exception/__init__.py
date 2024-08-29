import sys


class CustomException(Exception):
    def __init__(self, error_message: Exception):
        self.error_message = self.get_detailed_error_message(error_message)

    @staticmethod
    def get_detailed_error_message(error_message: Exception) -> str:
        _, _, exce_tb = sys.exc_info()
        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_msg = f"""
        Error occurred in execution of:
        [{file_name}] at
        try block line number: [{try_block_line_number}]
        and exception block line number: [{exception_block_line_number}]
        Error Message: {error_message} 
        """

        return error_msg

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return str(CustomException.__name__)
