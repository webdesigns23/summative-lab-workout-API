Backend Workout API
=======

# Project Description:
The API will be responsible for tracking workouts and their associated exercises. Each workout can include multiple exercises, with sets, reps, or duration attached to each. Exercises need to be reusable so a trainer can add the same exercise to various workouts.


# Tools and Resources Featured in this Project:
- [GitHub Repo](https://github.com/webdesigns23/summative-lab-workout-API.git)
- Python 3.8.13+
- Text Editor or IDE (e.g., VS Code)
- Git + GitHub
- Virtualenv
- Python Packages listed in requirements.txt

# Set Up and Installation:
1. Fork and clone the GitHub Repo
```bash
git clone <repo_url>

```
2. Set up your virtual environment of choice (virtualenv prefered)
```bash
virtualenv backendapi
source backendapi/bin/activate
```
3. Install PyPi dependencies using requiements.txt
```bash
pip install -r requirements.txt
```
4. Navigate into the server/ directory and set environment variables:
```bash
cd server
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
```
5. Create a migrations folder, run initial migration and update
```bash
cd server
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```
6. Populate database with initial data
```bash
python seed.py
```
# Running Application:
You can run the Flask server with:
```bash
python app.py
```

# Entitites:
1. Exercise
- id (integer, primary key)
- name (string)
- category (string)
- equipment_needed (boolean)

2. Workout
- id (integer, primary key)
- date (date)
- duration_minutes (integer)
- notes (text)

3. WorkoutExercises (Join Table)
- id (primary key)
- workout_id (foreign key to Workout)
- exercise_id (foreign key to Exercise)
- reps (integer)
- sets (integer)
- duration_seconds (integer)

# API Endpoints and Functionality:

## Workouts
`GET /workouts`
* List all workouts
 
`GET /workouts/<id>`
* Stretch goal: include reps/sets/duration data from WorkoutExercises and shows a single workout with its associated exercises

`POST /workouts`
* Create a workout

`DELETE /workouts/<id>`
* Stretch goal: delete associated WorkoutExercises and Delete a workout

## Exercises
`GET /exercises`
* List all exercises

`GET /exercises/<id>`
* Show an exercise and associated workouts

`POST /exercises`
*Create an exercise

`DELETE /exercises/<id>`
* Stretch goal: delete associated WorkoutExercises and Delete an exercise

## Workout Exercises Relationship
`POST workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`
* Add an exercise to a workout, including reps/sets/duration

# Testing:
Use Pytests to run test to check models
```bash
python -m pytest -v
```
# Commit and Push Git History
1. Add your changes to the staging area by executing
2. Create a commit by executing 
3. Push your commits to GitHub by executing 
4. If you created a separate feature branch, remember to open a PR on main and merge.
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

