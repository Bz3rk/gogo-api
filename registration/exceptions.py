from rest_framework.views import exception_handler
from rest_framework.response import Response




def custom_exception_handler(exc, context):
    # Call the default exception handler first, to get the standard error response
    response = exception_handler(exc, context)

    if response is not None:
        # Customize the response here, if needed
        response.data['status_code'] = response.status_code

    return response