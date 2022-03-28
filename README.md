# MakeMyDegree

MakeMyDegree is an open-source, intuitive user interface web app for course planning and administration targeted towards college students and administrators.

# Getting Started

1: Clone the repository or download our latest release at https://github.com/jadham2/MakeMyDegree/releases.

2: Create a `.env/` file in the `/backend/` file containing the following fields:
```py
DJANGO_SECRET_KEY='your-Django-secret-here' # Your Django server secret key here.
DB_NAME='database' # The name of your PostgreSQL database. Some good candidates are "makemydegree' or 'makemydegreedb'
DB_USER='admin' # The name of the admin user of the PostgreSQL database. This user will have all permissions on the DB.
DB_PASS='useful-password-here' # The password to the PostgreSQL database.
```
3: Download Docker at https://docs.docker.com/get-docker/.

4: Once your Docker has been installed and configured, navigate to where you installed this project, and run `docker-compose up -d`. You will now be able to interface with your server using tools such as DBeaver or pgAdmin.

5: Navigate to the `/frontend/` folder and run `npm start`.

6: Open the website at `http://localhost:3000/` and start your course planning!
