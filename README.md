
## Getting Started

### Prerequisites
- Python 3.x
- Other dependencies listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/NurulloMahmud/fundraiser.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fundraiser
   ```
3. Create and activate virtual environment:
   ```bash
   python3 -m venv env
   ```
   ```bash
   source env/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Make migrations to create the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
3. Open a web browser and navigate to `http://localhost:8000/` to view the application.
