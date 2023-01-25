from rest_framework.pagination import PageNumberPagination

class DynamicPagination(PageNumberPagination):
    # custom pagination and the parameters can be override according to user request  
    page_size = 6
    page_size_query_param = 'page' 
    max_page_size = 5
    page_query_param = 'p'