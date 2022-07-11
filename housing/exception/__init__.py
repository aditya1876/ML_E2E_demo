import os
import sys

#creating a custom exception class
class HousingException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):
        """
        This method creates an object of Exception class and stores in error_message and details about the error are stored in error_details
        """

        super().__init__(error_message) #passing the error to the parent class=Exception Class
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message, error_detail=error_detail)


    #below method is to display the error message in a formatted way that i want. Return type will be str
    #the method is static because we want to be able to call the method without creating an object of the class. we can directly pass the arguments and call the method.
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error_message:Exception object
        error_detial: object of sys module
        """    
        _,_,exec_tb = error_detail.exc_info() #Returns information about the most recent exception caught by except clause in the current or older stack frame

        exception_block_line_number= exec_tb.tb_frame.f_lineno
        try_block_line_number= exec_tb.tb_lineno
        file_name= exec_tb.tb_frame.f_code.co_filename        

        error_message=f"""
        Error occured in script:
        [{file_name}] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}]
        error message: [{error_message}]
        """
        
        return error_message
    
    def __str__(self):
        return self.error_message

    def __repr__(self)->str:
        return HousingException.__name__.str() 

    """
    Explaination of __str__ and __repr__ functions above:

    IN JUPYTER NOTEBOOK, exectute the following code

    class Demo():
        def __str__(self):
            return "In str fn"
        
        def __repr__(self):
            return "In repr function"

    d=Demo()

    #EXECUTE IN A CELL 
    d
    #output - In repr function

    #EXECUTE IN A CELL
    print(d)
    #output - In str fn
    """
