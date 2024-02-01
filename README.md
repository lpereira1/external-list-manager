<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center"></h1>
</p>
<p align="center">
    <em>Whitelist Manager: Simplify Address Management Effortlessly</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/lpereira1/external-list-manager?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/lpereira1/external-list-manager?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/lpereira1/external-list-manager?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/lpereira1/external-list-manager?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=flat&logo=Gunicorn&logoColor=white" alt="Gunicorn">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running ](#-running-)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The project, named External List Manager, is a web application built using the Flask framework that enables users to manage and maintain a whitelist of IP addresses. The core functionality of the system includes creating, updating, and deleting addresses, as well as listing and exporting them. Users can register for an account, log in, and update their profile information. The application also provides password reset functionality. The project follows Flask best practices and includes various modules such as routes, forms, templates, and utilities. The codebase is designed to be deployed using Docker, with a Docker Compose file defining containers for the Flask app and NGINX as a reverse proxy. The value proposition of the External List Manager lies in its ability to simplify and streamline the management of whitelisted IP addresses, providing a secure and user-friendly platform for address maintenance.

---

##  Features

Error generating text for prompt `features`: 

---

##  Repository Structure

```sh
└── /
    ├── dev_env_file
    ├── docker-compose.yml
    ├── environment.py
    ├── requirements.txt
    ├── run.py
    └── services
        ├── application
        │   ├── Dockerfile
        │   ├── app.py
        │   ├── eal_manager
        │   │   ├── __init__.py
        │   │   ├── addresses
        │   │   │   ├── __init__.py
        │   │   │   ├── forms.py
        │   │   │   ├── routes.py
        │   │   │   └── utilities.py
        │   │   ├── addresses.db
        │   │   ├── conf
        │   │   │   └── setup.yml
        │   │   ├── config.py
        │   │   ├── errors
        │   │   │   ├── __init__.py
        │   │   │   └── handlers.py
        │   │   ├── main
        │   │   │   ├── __init__.py
        │   │   │   └── routes.py
        │   │   ├── models.py
        │   │   ├── static
        │   │   │   ├── main.css
        │   │   │   └── profile_pictures
        │   │   ├── templates
        │   │   │   ├── about.html
        │   │   │   ├── account.html
        │   │   │   ├── address.html
        │   │   │   ├── createaddress.html
        │   │   │   ├── errors
        │   │   │   ├── export_addresses.html
        │   │   │   ├── index.html
        │   │   │   ├── layout.html
        │   │   │   ├── list.txt
        │   │   │   ├── login.html
        │   │   │   ├── register.html
        │   │   │   ├── reset_password.html
        │   │   │   └── reset_request.html
        │   │   └── users
        │   │       ├── __init__.py
        │   │       ├── forms.py
        │   │       ├── routes.py
        │   │       └── utilities.py
        │   └── requirements.txt
        └── nginx
            ├── Dockerfile
            └── nginx.conf
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                |
| [dev_env_file](https://github.com/lpereira1/external-list-manager/blob/master/dev_env_file)             | This code snippet is responsible for setting up the development environment and configuring key parameters for the parent repository. It defines the Flask app, sets the environment to development, and specifies the secret key and the SQLite database URI.                                                                     |
| [requirements.txt](https://github.com/lpereira1/external-list-manager/blob/master/requirements.txt)     | The code snippet is part of the services/application module in the repository. It includes Flask app files, routes, forms, utilities, and configurations that power the main application of the system. The code ensures the functioning of the core features and logic of the application while adhering to Flask best practices. |
| [environment.py](https://github.com/lpereira1/external-list-manager/blob/master/environment.py)         | The `environment.py` file is responsible for setting up the environment variables used in the parent repository's architecture. It exports two critical values: the secret key and the URI for the SQLite database.                                                                                                                |
| [run.py](https://github.com/lpereira1/external-list-manager/blob/master/run.py)                         | This code snippet initializes and runs the application using a factory function from the eal_manager package. It allows running the app in debug mode.                                                                                                                                                                             |
| [docker-compose.yml](https://github.com/lpereira1/external-list-manager/blob/master/docker-compose.yml) | This code snippet is part of a Docker-based repository architecture. It includes a docker-compose.yml file that defines Docker containers for an application and NGINX. The application container runs a Flask app using Gunicorn, exposed on port 5000. The NGINX container acts as a reverse proxy and is exposed on port 80.    |

</details>

<details closed><summary>services.application</summary>

| File                                                                                                                     | Summary                                                                                                                                                                                                                                                     |
| ---                                                                                                                      | ---                                                                                                                                                                                                                                                         |
| [requirements.txt](https://github.com/lpereira1/external-list-manager/blob/master/services/application/requirements.txt) | The code snippet is a Flask application that provides functionality for managing addresses. It includes routes, forms, templates, and models. It requires various Flask-related dependencies.                                                               |
| [app.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/app.py)                     | This code snippet initializes and runs the application by creating an instance of the Flask app from the `eal_manager` module. The app is then run, providing the ability to debug.                                                                         |
| [Dockerfile](https://github.com/lpereira1/external-list-manager/blob/master/services/application/Dockerfile)             | The Dockerfile in the services/application directory is responsible for building a Docker image for the application. It sets the working directory, installs dependencies from the requirements.txt file, and copies the entire application into the image. |

</details>

<details closed><summary>services.application.eal_manager</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [models.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/models.py) | The `models.py` code in the `services/application/eal_manager` folder defines the database models for the application. It includes a `User` model with attributes such as `first_name`, `last_name`, `email`, and `password`, as well as a `IPAddress` model with attributes like `address`, `name`, `organization`, and `date_created`. The code also includes methods to generate and verify password reset tokens. |
| [config.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/config.py) | The code snippet in `config.py` retrieves configuration settings from `setup.yml` file and sets them as environment variables in the application. These settings include the secret key, database URI, email server details, and more.                                                                                                                                                                                |

</details>

<details closed><summary>services.application.eal_manager.main</summary>

| File                                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                           |
| [routes.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/main/routes.py) | This code is part of a Flask application within a larger repository. It contains routes for the main functionality of the application, such as rendering the start page and the about page. The code enforces the requirement of being logged in to access these routes. The start page also retrieves and displays whitelisted IP addresses from a database. |

</details>

<details closed><summary>services.application.eal_manager.addresses</summary>

| File                                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                           |
| [forms.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/addresses/forms.py)         | This code snippet is part of the eal_manager module in the parent repository. It defines a Flask form class called CreateAddress with fields for an address, description, and organization. It includes validation logic to check for duplications and validate the format of the address input.                                                                                              |
| [routes.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/addresses/routes.py)       | This code snippet is part of the addresses module in the application service of the parent repository. It contains routes for creating, updating, deleting, and listing addresses using Flask. Authentication and database operations are also implemented.                                                                                                                                   |
| [utilities.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/addresses/utilities.py) | This code snippet is located in the `addresses/utilities.py` file. Its role is to generate an export of the IP addresses stored in the application's database. It retrieves all IP addresses from the database using the `IPAddress.query.all()` method and returns the list as the result. This code is part of the `eal_manager` module within the `application` service of the repository. |

</details>

<details closed><summary>services.application.eal_manager.users</summary>

| File                                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [forms.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/users/forms.py)         | The `forms.py` file in the `services/application/eal_manager/users` directory is responsible for defining various forms used in user registration, login, updating account information, and password reset functionality. These forms are created using Flask-WTF and serve as input validation mechanisms, ensuring that the data entered by the user meets the specified requirements. The forms.py file includes four classes: `RegistrationForm`, `LoginForm`, `UpdateAccountForm`, `RequestResetForm`, and `ResetPasswordForm`. |
| [routes.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/users/routes.py)       | This code snippet contains routes for user authentication and account management in the application. It handles user registration, login, logout, account updates, and password reset functionality.                                                                                                                                                                                                                                                                                                                                 |
| [utilities.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/users/utilities.py) | This code snippet within the parent repository's architecture contains functions for saving profile pictures and sending password reset emails. It utilizes the Flask framework, PIL library for image processing, and Flask-Mail for email functionality.                                                                                                                                                                                                                                                                           |

</details>

<details closed><summary>services.application.eal_manager.conf</summary>

| File                                                                                                                        | Summary                                                                                                                                                                                                                      |
| ---                                                                                                                         | ---                                                                                                                                                                                                                          |
| [setup.yml](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/conf/setup.yml) | The code snippet in setup.yml defines the setup configuration for the application's database, default username, forms secret, mail server settings, etc., critical to the operation of the parent repository's architecture. |

</details>

<details closed><summary>services.application.eal_manager.errors</summary>

| File                                                                                                                              | Summary                                                                                                                                                                              |
| ---                                                                                                                               | ---                                                                                                                                                                                  |
| [handlers.py](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/errors/handlers.py) | This code snippet is responsible for handling errors in the application. It defines error handlers for HTTP status codes 404, 403, and 500, rendering corresponding error templates. |

</details>

<details closed><summary>services.application.eal_manager.templates</summary>

| File                                                                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [about.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/about.html)                       | This code snippet represents the about.html template page of the eal_manager application in the parent repository. It extends the layout.html template and displays the heading About Page.                                                                                                                                                                                                                             |
| [account.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/account.html)                   | This code snippet, located at `services/application/eal_manager/templates/account.html`, is a template file that renders the user account page. It displays the user's profile information, including their name, email, and profile picture. The template also provides a form for the user to update their account details, such as email, first name, last name, and profile picture.                                |
| [reset_request.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/reset_request.html)       | This code snippet is a template file for the reset_request.html page. It extends a base layout and contains a form for requesting a password reset. The form includes an email field and a submit button.                                                                                                                                                                                                               |
| [list.txt](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/list.txt)                           | The code snippet in services/application/eal_manager/templates/list.txt generates a formatted list of addresses in the parent repository's architecture. It loops through each address in the addresses variable and displays the address and corresponding name.                                                                                                                                                       |
| [address.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/address.html)                   | This code snippet is a template file called address.html within the eal_manager module in the parent repository. It defines the layout and content of a webpage displaying address details, including the address itself, creation date, and options to edit or delete the address.                                                                                                                                     |
| [register.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/register.html)                 | The code snippet is a template for the user registration page in the application. It includes form fields for email, first name, last name, password, and password confirmation, along with error handling and a submit button. The template extends a base layout and is designed to be rendered by the application.                                                                                                   |
| [createaddress.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/createaddress.html)       | This code snippet represents a template file called createaddress.html in the eal_manager module of the parent repository. It provides the HTML structure and form elements for creating a new address entry in the application.                                                                                                                                                                                        |
| [layout.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/layout.html)                     | This code snippet, located at `services/application/eal_manager/templates/layout.html`, defines the layout for the Whitelist Maintenance web application. It includes the page structure, navigation bar, and options for different actions.                                                                                                                                                                            |
| [index.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/index.html)                       | The code snippet is a Django template file (`index.html`) that renders a dynamic web page for managing whitelisted addresses. It displays a table of addresses with details such as name, IP address, organization, created by, and created on. Each address has an edit and delete button that triggers modals for confirming deletion. Pagination links are also included. The template extends a `layout.html` file. |
| [export_addresses.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/export_addresses.html) | This code snippet is part of a larger repository structure for an application called EAL Manager. It specifically handles the template for exporting addresses.                                                                                                                                                                                                                                                         |
| [login.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/login.html)                       | The code snippet is a template for the login page in the application. It extends a base layout and includes a form for users to enter their email and password to log in. It also provides the option to remember the login and a link for password reset.                                                                                                                                                              |
| [reset_password.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/reset_password.html)     | This code snippet is a template file, `reset_password.html`. It defines the HTML structure and form components for resetting a user's password in the application. The file is part of the `eal_manager` module within the parent repository's `application` service.                                                                                                                                                   |

</details>

<details closed><summary>services.application.eal_manager.templates.errors</summary>

| File                                                                                                                                  | Summary                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                                   | ---                                                                                                                                                                                                                                                                                                   |
| [403.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/errors/403.html) | This code snippet defines the contents of the 403.html error template, which is rendered when a user is denied access to a page. It extends the layout.html template and displays a message explaining the access denial.                                                                             |
| [404.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/errors/404.html) | The code snippet is a template file located at services/application/eal_manager/templates/errors/404.html in the repository. It defines the content of the 404 error page for the application, displaying a message indicating that the page was not found. This template extends a base layout file. |
| [500.html](https://github.com/lpereira1/external-list-manager/blob/master/services/application/eal_manager/templates/errors/500.html) | This code snippet represents an HTML template for displaying a server error page (500 error) in the application's error handling system. The template extends a layout file and includes a message for the user to contact the system administrator.                                                  |

</details>

<details closed><summary>services.nginx</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                        |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                            |
| [nginx.conf](https://github.com/lpereira1/external-list-manager/blob/master/services/nginx/nginx.conf) | The code snippet in the `services/nginx/nginx.conf` file is responsible for configuring the Nginx server to forward requests to the Flask application running on port 5000. It sets up an upstream server called `hello_flask` and defines rules for proxying requests and preserving headers. |
| [Dockerfile](https://github.com/lpereira1/external-list-manager/blob/master/services/nginx/Dockerfile) | The `nginx/Dockerfile` delivers the latest version of Nginx and removes the default configuration, replacing it with a custom `nginx.conf` file.                                                                                                                                               |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **HTML**: `version x.y.z`

###  Installation

1. Clone the  repository:

```sh
git clone https://github.com/lpereira1/external-list-manager/
```

2. Change to the project directory:

```sh
cd 
```

3. Install the dependencies:

```sh
> INSERT-INSTALL-COMMANDS
```

###  Running 

Use the following command to run :

```sh
> INSERT-RUN-COMMANDS
```

###  Tests

To execute tests, run:

```sh
> INSERT-TEST-COMMANDS
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/lpereira1/external-list-manager/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/lpereira1/external-list-manager/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/lpereira1/external-list-manager/issues)**: Submit bugs found or log feature requests for .

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/lpereira1/external-list-manager/
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
