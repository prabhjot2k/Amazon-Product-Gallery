# Amazon-Products-Gallery
This application is built using Python, Django and Django REST Franework. Django REST Framework is mainly used to build Web APIs. 
This application is used to create and store database of products, just like Amazon. Just like any other backend API, it supports CRUD functions and you can utilise those to add, edit, access and even delete your products.



## Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Python 3.6+ verion
* [Django](https://www.djangoproject.com/) - Django for backend
* [Django REST Framework](https://www.django-rest-framework.org/) - Django REST Framework for REST APIs

## Steps to Run
1. Go to AmazonGallery folder.
2. Install Django:
   ```sh
   $ python -m pip install django
   ```
3. Install Django Rest Framework:
   ```sh
   $ pip install djangorestframework
   ```
4. Add `rest_framework` to your `INSTALLED_APPS` setting.
    ```sh
   INSTALLED_APPS = [
    ...
    'rest_framework',
   ]
   ```
5. Run the server with:
   ```sh
   $ python manage.py runserver
   ```
6. Checkout APIs at `127.0.0.1:8000/products/`, `127.0.0.1:8000/categories/`, `127.0.0.1:8000/sellers/` and `127.0.0.1:8000/products-filter/`
7. Add the required products using categories and sellers.
8. Perform the required CRUD operations.
9. Also, you can simplify the process of searching across multiple products by putting required filters at `127.0.0.1:8000/products-filter/`.
 
 
 
