from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
	__tablename__ = 'exercises'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	category = db.Column(db.String)
	equipment_needed = db.Column(db.Boolean, default=False)

	# *Foreign key in WorkoutExercise
	workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete-orphan')
	# M2M
	workouts = db.relationship('Workout', secondary='workout_exercises', back_populates='exercises')

	def __repr__(self):
		return f'<Exercise {self.id}, {self.name}, {self.category}, {self.equipment_needed}>'

class Workout(db.Model):
	__tablename__ = 'workouts'

	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date)
	duration_minutes = db.Column(db.Integer)
	notes = db.Column(db.Text)
	
	# *Foreign key in WorkoutExercise
	workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')
	# M2M
	exercises = db.relationship('Exercise', secondary='workout_exercises', back_populates='workouts')

	def __repr__(self):
		return f'<Workout {self.id}, {self.date}, {self.duration_minutes}, {self.notes}>'

class WorkoutExercise(db.Model):
	__tablename__ = 'workout_exercises'

	id = db.Column(db.Integer, primary_key=True)
	workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
	exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
	reps = db.Column(db.Integer)
	sets = db.Column(db.Integer)
	duration_seconds = db.Column(db.Integer)

	# A Workout has many Exercises through WorkoutExercises
	workout = db.relationship('Workout', back_populates='workout_exercises')
	# A Workout has many Exercises through WorkoutExercises
	exercise = db.relationship('Exercise', back_populates='workout_exercises')

	def __repr__(self):
		return f'<WorkoutExercise {self.id}, {self.reps}, {self.sets}, {self.duration_seconds}>'
	