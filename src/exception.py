import os
import pickle
import sys

class CustomException(Exception):
    def __init__(self, message, error_details: sys):
        super().__init__(message)
        self.error_details = error_details

    def __str__(self):
        return f"Error: {self.args[0]} | Details: {self.error_details}"

    @staticmethod
    def get_detailed_error_message(error_message: str, error_detail: sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        detailed_error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return detailed_error_message

    def __str__(self):
        return self.error_message