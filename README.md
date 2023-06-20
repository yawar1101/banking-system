# Banking System Project

This is a Django-based project for a banking system that allows users to transfer money between multiple customers. The project does not require a login page or user creation. It focuses solely on the transfer of money between customers.

## Database

The project utilizes a database to store customer information and record transfers. You can choose from various database options such as MySQL, MongoDB, Postgres, etc. Ensure that you have the necessary database server installed and running.

## Installation

1. Clone the repository:

    `https://github.com/yawar1101/banking-system.git`

2. Change to the project directory:

    `cd banking_system`
  
3. Create a virtual environment:

    `python3 -m venv myenv`
  
4. Activate the virtual environment:

    * For Linux/Mac:
   
        `source myenv/bin/activate`
      
    * For Windows:
  
        `myenv\Scripts\activate`
      
5. Install the project dependencies:

    `pip install -r requirements.txt`
    
6. Apply database migrations:

   `python manage.py migrate`
   
7. Start the development server:

   `python manage.py runserver`
    
8. Open a web browser and visit `http://localhost:8000` to access the application.

## Usage
  1. Home Page
     * The home page displays a list of all customers.
  2. View All Customers
     * Click on a customer's name to view their details.
  3. Select and View One Customer
     * On the customer's details page, click on the "Transfer Money" button to initiate a transfer.
  4. Transfer Money
     * Select the customer to transfer money to from the list of all customers.
     * After the transfer, you will be redirected to the customer's details page.
     * Repeat the process to transfer money between multiple customers.

## Contributing

Contributions to the banking system project are welcome. If you find any issues or have suggestions for improvements, please open a new issue or submit a pull request on the project's repository.
