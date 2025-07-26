from models import *
from marshmallow import Schema, fields, validate, ValidationError
import datetime

class ExerciseSchema(Schema):
	id = fields.Integer(dump_only=True)
	name = fields.String(required=True)
	category = fields.String(required=True)
	equipment_needed = fields.Boolean(required=True)

	workout_exercises = fields.Nested(
		lambda: WorkoutExerciseSchema, 
		many=True, 
		exclude=('workout', 'exercise'))
	
	@validates('name')
	def validate_name(self, key, name):
		if not name:
			raise ValueError("Exercise name must be provided.")
		exercise_exists = Exercise.query.filter_by(name=name).first()
		if exercise_exists:
			raise ValueError("Exercise name must not already exist")
		return name

class WorkoutSchema(Schema):
	id = fields.Integer(dump_only=True)
	date = fields.Date(required=True)
	duration_minutes = fields.Integer(required=True, validate=validate.Range(min=1))
	notes = fields.String(required=True)

	workout_exercises = fields.Nested(
		lambda: WorkoutExerciseSchema, 
		many=True, 
		exclude=('workout', 'exercise'))
	
	@validates('date')
	def validate_date(self, key, date):
		try:
			datetime.strptime(date, '%Y-%m-%d')
		except ValueError:
			raise ValidationError("Date format must be YYYY-MM-DD.")
		return date

	@validates('notes')
	def validates_notes(self,key, note):
		if len(note) >= 50:
			raise ValueError("Notes cannot be longer than 50 characters.")
		return note
	
class WorkoutExerciseSchema(Schema):
	id = fields.Integer(dump_only=True)
	reps = fields.Integer(required=False, validate=validate.Range(min=1))
	sets = fields.Integer(required=False, validate=validate.Range(min=1))
	duration_seconds = fields.Integer(required=False, validate=validate.Range(min=1))

	workout = fields.Nested(
		lambda:WorkoutSchema, 
		many=False, 
		exclude=('workout_exercises',))
	exercise = fields.Nested(
		lambda:ExerciseSchema, 
		many=False, 
		exclude=('workout_exercises',))