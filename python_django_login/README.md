The User Management System is a web application developed using Django, a powerful Python-based web framework. This system allows users to register, log in, and manage their profiles securely. It's designed to cater to two primary user roles: patients and doctors. Key Features:

User Registration and Authentication:

Users can sign up by providing essential details like username, email, first name, last name, address, city, state, and pin code. Robust user authentication ensures secure login using registered credentials. User Groups and Permissions:

Implemented different user groups using Django's Group model to categorize users as patients or doctors. Assigned distinct permissions to each group for managing access control to specific features or functionalities. User-Specific Views and Functionality:

Utilized Django's views to handle user-specific functionalities, including registration, login, and profile management. Rendered personalized content on the home page based on the logged-in user's role and information. User Profile Management:

Users can manage their profiles, view their details, update personal information, and upload profile pictures. Implemented form validation to ensure data integrity and user input security. Security Measures:

Employed Django's built-in security features to handle password hashing, protecting user credentials from security breaches. Implemented password validation rules to ensure strong and secure passwords. Technologies Used:

Django Framework: Leveraged Django's powerful features for rapid development, including its ORM, authentication system, and template engine. HTML/CSS/Bootstrap: Designed user-friendly and responsive front-end interfaces using HTML, CSS, and Bootstrap for enhanced user experience.
