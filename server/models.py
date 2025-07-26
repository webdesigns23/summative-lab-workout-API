from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
	__tablename__ = 'exercises'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	category = db.Column(db.String, nullable=False)
	equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

	@validates('name')
	def validate_name(self, key, name):
		if not name:
			raise ValueError("Exercise name must be provided.")
		exercise_exists = Exercise.query.filter_by(name=name).first()
		if exercise_exists:
			raise ValueError("Exercise name must not already exist")
		return name

	# *Foreign key in WorkoutExercise
	workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete-orphan')
	# # M2M
	# workouts = db.relationship('Workout', secondary='workout_exercises', back_populates='exercises')

	def __repr__(self):
		return f'<Exercise {self.id}, {self.name}, {self.category}, {self.equipment_needed}>'

class Workout(db.Model):
	__tablename__ = 'workouts'

	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, nullable=False)
	duration_minutes = db.Column(db.Integer, nullable=False, default=0)
	notes = db.Column(db.String, nullable=False,)

	__table_args__ = (db.CheckConstraint('(duration_minutes >= 0)'),)

	@validates('date')
	def validates_date(self, key, date):
		if date > date.today():
			raise ValueError("Date cannot be before today's date.")
		return date
	
	@validates('notes')
	def validates_notes(self, key, notes):
		if len(notes) > 100:
			raise ValueError("Notes cannot exceed 100 characters.")
		return notes
	
	# *Foreign key in WorkoutExercise
	workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')
	# # M2M
	# exercises = db.relationship('Exercise', secondary='workout_exercises', back_populates='workouts')

	def __repr__(self):
		return f'<Workout {self.id}, {self.date}, {self.duration_minutes}, {self.notes}>'

class WorkoutExercise(db.Model):
	__tablename__ = 'workout_exercises'

	id = db.Column(db.Integer, primary_key=True)
	workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
	exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
	reps = db.Column(db.Integer, default=0)
	sets = db.Column(db.Integer, default=0)
	duration_seconds = db.Column(db.Integer, default=0)

	__table_args__ = (db.CheckConstraint('(reps >= 0) and (sets >= 0) and (duration_seconds >= 0)'),)

	# A Workout has many Exercises through WorkoutExercises
	workout = db.relationship('Workout', back_populates='workout_exercises')
	# A Workout has many Exercises through WorkoutExercises
	exercise = db.relationship('Exercise', back_populates='workout_exercises')

	def __repr__(self):
		return f'<WorkoutExercise {self.id}, {self.reps}, {self.sets}, {self.duration_seconds}>'
	