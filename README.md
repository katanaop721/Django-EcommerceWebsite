<p align="center">
  <p align="center">
    <a href="https://justdjango.com/?utm_source=github&utm_medium=logo" target="_blank">
      <img src="https://assets.justdjango.com/static/branding/logo.svg" alt="JustDjango" height="72">
    </a>
  </p>
  <p align="center">
      Django Ecommerce Website
  </p>
</p>

<h2>PROJECT SUMMARY</h2>
"Store Illuminate is a state-of-the-art ecommerce platform designed to provide a seamless and enjoyable shopping experience for customers. Built using the powerful web framework Django and utilizing PostgreSQL for data storage, Store Illuminate is a robust and scalable solution for online shopping. User authentication is made secure through the use of JSON Web Tokens (JWT), ensuring that sensitive customer information is protected at all times.

One of the key features of Store Illuminate is its custom-built, RESTful API. This API allows for easy integration with third-party services such as shipping providers, payment gateways, and more, making the checkout process quick and efficient. The platform's 'Features' field showcases the full range of functionalities available to customers, including a powerful search engine, real-time order tracking, and multiple payment options.

Store Illuminate is also designed with security in mind. Customer data is securely stored using PostgreSQL, and the platform employs industry-standard security measures such as encryption and regular backups to protect against data loss. With its user-friendly interface and powerful underlying technology, Store Illuminate is the ideal ecommerce solution for businesses of all sizes. Whether you're looking to sell products online for the first time, or you're looking for a better platform for your existing ecommerce operation, Store Illuminate has everything you need to succeed."

<h2>"Getting Started with Store Illuminate:</h2>

1. Clone the repository to your local machine using git clone.<br>
2. Open the cloned repository in your preferred IDE.<br>
3. Create a virtual environment for the project and activate it.
4. Install the required dependencies listed in the requirements.txt file using pip install -r requirements.txt.<br>
5. Set up a local PostgreSQL database for the project.<br>
6. Create a .env file in the project root directory and add the following environment variables:<br>
7. DEBUG: Set this to True for development, False for production.<br>
8. SECRET_KEY: A secret key used by Django for various purposes.<br>
9. DB_NAME: The name of the PostgreSQL database.<br>
10. DB_USER: The database user.<br>
11. DB_PASSWORD: The database user's password.<br>
12. DB_HOST: The database host (e.g. localhost).<br>
13. DB_PORT: The database port (e.g. 5432).<br>
14. Run python manage.py migrate to apply the database migrations.<br>
15. Run python manage.py runserver to start the development server.<br>
16. Open your web browser and navigate to http://localhost:8000/ to access the Store Illuminate platform."<br>


<h2>NOTE</h2>
I have removed the merchant key and id for security issue.
Please Add your Merchant ID and Key in views.py file. So that the Paytm payment method works.


