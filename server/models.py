from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
	__tablename__ = 'exercises'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	category = db.Column(db.String)
	equipment_needed = db.Column(db.Boolean)

class Workout(db.Model):
	__tablename__ = 'workout'

	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date)
	duration_minutes = db.Column(db.Integer)
	notes = db.Column(db.Text)

class WorkoutExercises(db.Model):
	__tablename__ = 'workout-exercises'

	id = db.Column(db.Integer, primary_key=True)
	workout_id = db.Column(db.Integer)
	exercise_id = db.Column(db.Integer)
	reps = db.Column(db.Integer)
	sets = db.Column(db.Integer)
	duration_seconds = db.Column(db.Integer)
	