This is a Selenium-based end-to-end test automation framework built using Python and Pytest, designed to test the complete user journey on the Rahul Shetty Academy Practice Website.
The project follows the Page Object Model (POM) to separate test logic from UI interactions, ensuring scalability and maintainability. It covers everything from login functionality to product selection, checkout, delivery location selection, and verification of the success message.

This framework includes:
Dynamic locators using Selenium WebDriver
Parametrized test data for login inputs
Centralized setup using conftest.py and BaseClass
Logging mechanism that stores logs with timestamps in a dedicated logs/ folder
HTML test reports using pytest-html plugin
Clear and assertive validation at each step of the user flow

