import requests
from django.http import JsonResponse
from .models import *

def fetch_book_details(request,title):
    print("title",title)
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    data = response.json()

    if data['num_found'] > 0:
        book_data = data['docs'][0]  # Assuming the first result is the correct one
        book_details = {
            'title': book_data.get('title'),
            'author': ', '.join(book_data.get('author_name', [])),
            'published_date': book_data.get('first_publish_year'),
            'page_count': book_data.get('number_of_pages_median', 0),
            'isbn': book_data.get('isbn')[0] if 'isbn' in book_data else None
        }
        return JsonResponse(book_details)
    return None



