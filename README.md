# StudyChallenger

![banner](https://cdn.discordapp.com/attachments/951765233091870740/1199685914797035570/image.png?ex=65c37193&is=65b0fc93&hm=faf6792e4b1c50eea61eede5227f074cb0466a0e1f66e75a6f5dcee5f6aa9c07&)

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (version 3.6 or higher)
- pip (Python package installer)

## Installation

1. Clone the project repository:

    ```bash
    git clone https://github.com/LopesLs/StudyChallenger.git
    ```

2. Navigate to the project directory:

    ```bash
    cd StudyChallenger
    ```

3. Create a virtual environment:
    - On Windows:

        ```bash
        python -m venv .venv
        ```

    - On Linux:

        ```bash
        python3 -m venv .venv
        ```

4. Activate the virtual environment:

    - On macOS and Linux:

      ```bash
      source .venv/bin/activate
      ```

    - On Windows:

      ```bash
      .\.venv\Scripts\activate
      ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Set up the database:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser (admin) account:

    ```bash
    python manage.py createsuperuser
    ```

## Running the Project

To run the Django project, execute the following command:

```bash
python3 manage.py runserver
```

And you have the website active in `localhost:8000` for test and use it.

Fell free to colaborate in this project!!!
