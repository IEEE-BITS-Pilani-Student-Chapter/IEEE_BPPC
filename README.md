# IEEE_BPPC
Code repository for IEEE BITS Pilani Student Chapter Website

## Installation
1. Clone or download the repository.
    ```bash
    git clone https://github.com/IEEE-BITS-Pilani-Student-Chapter/IEEE_BPPC.git
    ```
2. Create a new virtual environment for the project.
    ```bash
    python -m venv myvenv
    source myvenv/bin/activate (linux)
    myvenv\Scripts\activate.bat  (windows)
    ```
3. Install required python libraries giving in the requirements.txt file.
    ```bash
    pip install -r requirements.txt
    ```
4. Run Django migrations.
	```bash
	python manage.py makemigrations
	python manage.py migrate
	```
5. Start the application.
	```bash
	python manage.py runserver
	```
6. You are done with installation.
	Run application at `http://127.0.0.1:8000/`