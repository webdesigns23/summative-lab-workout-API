# Backend Workout API

## Project Description
The API will be responsible for tracking workouts and their associated exercises. Each workout can include multiple exercises, with sets, reps, or duration attached to each. Exercises need to be reusable so a trainer can add the same exercise to various workouts.


## Tools and Resources Featured in this Project:
- Python 3.8.13+
- Text Editor or IDE (e.g., VS Code)
- Git + GitHub
- Virtualenv
- Python Packages listed in requirements.txt

## SET UP:
- Fork and clone the summative-lab-workout-API repository.

- Run the following commands:
	1. set up a virtual environment with pipenv, virtualenv, or uv
	2. use requirments.txt to install necessary pip dependencies 
		$ pip install -r requirements.txt

	3. Navigate into the server/ directory and set environment variables:
		$ cd server
		$ export FLASK_APP=app.py
		$ export FLASK_RUN_PORT=5555

## Entitites:
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

## Endpoints and Functionality
1. GET /workouts
- List all workouts

2. GET /workouts/<id>
- Stretch goal: include reps/sets/duration data from WorkoutExercises
- Show a single workout with its associated exercises

3. POST /workouts
- Create a workout

4. DELETE /workouts/<id>
- Stretch goal: delete associated WorkoutExercises
- Delete a workout

5. GET /exercises
- List all exercises

6. GET /exercises/<id>
- Show an exercise and associated workouts

7. POST /exercises
- Create an exercise

8. DELETE /exercises/<id>
- Stretch goal: delete associated WorkoutExercises

9. Delete an exercise
- Delete an exercise

10. POST workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
- Add an exercise to a workout, including reps/sets/duration

## Tests:
- Pytests to check models
- run using $ python -m pytest -v
