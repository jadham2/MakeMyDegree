# MakeMyDegree

MakeMyDegree is an open-source, intuitive user interface web app for course planning and administration targeted towards college students and administrators.

## Project goal (i.e., what are we set off to solve)
With more and more complex degree requirements in colleges nowadays, students are struggling to find an efficient and straightforward tool that helps them lay out their course plans every semester. Oftentimes it requires quite a few advising appointments and hours digging around school websites to have a concrete schedule planned out. Our project aims to an an interactive student course planner, with which a student can flexibly plan their degree by semesters and get immediate feedback on if they plan meets all the graduation requirements. 

## Approach (i.e., what makes this project unique?)
Unlike existing solutions that are either very unintuitive to use or locked behind a paywall, our solution is easy to use and completely free. Our solution is also open-source for any other developers that want to deploy/improve upon our work. Our solution offers straightforward UI for semester planning - a single drag-and-drop action is needed to place a course in your plan, instead of multiple tedious clicks and typing. Once the user saves their plane, it will automatically be audited by our backend by checking if all the degree requirements are met.

## Competing projects (i.e., are there any similar projects?)
Many universities offer degree planning tools, such as myPurduePlan from Purdue University or Plan Ahead by University of Illinois. However, students often find these tools confusing and difficult to use. The format in which the semester plan feedbacks are given is also unintuitive, often requiring explanations from academic advisors.

There are also paid solutions that help students plan each semester and track availability of their desired courses, such as Coursicle. These tools are very helpful for students when registering for popular courses, however, they do not offer the auditing feature that helps users validate their course plan meets the degree requirements.

## Project status and Roadmap
### Criteria our project aims to achieve: 
* **University agnostic**: 
  * Users from various universities can utilize our solution.
* **Schedule validation**: 
  * Users can get reliable feedback on if their plan meets graduation requirements. 
* **Intuitive UI**: 
  * The frontend should be self-explanatory and easy to use.
* **Curriculum plan easily updatable**: 
  * University administrators/advisors should be able to easily make updates to the degree plans when applicable.
* **Easy to deploy**: 
  * Developers should build/deploy our tool with ease.

### Roadmap and current status:
* **University agnostic**: 
  * Currently scrapped only the Purdue ECE degree plan
  * By April 1, scrape all degree plans from Purdue
  * By April 10, scrape degree plans from vaious universities
* **Schedule validation**: 
  * Currently, preliminary DB, API in shape
  * By April 10, complete DB, API (including validation logic) 
* **Intuitive UI**: 
  * Currently, preliminary frontend very intuitive and easy to use
  * By April 15, Connect frontend with backend
  * By April 20, beautify and polish final UI.
* **Curriculum plan easily updatable**: 
  * Currently achieved, DB admin roles can invoke updates to curriculum requirements table
* **Easy to deploy**: 
  * Currently achieved, developers can easily download our newest release and either use `docker compose` to build from our source code, or directly use our docker images to start a container.

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
