from models import *
from marshmallow import Schema, fields

class ExerciseSchema(Schema):
	id = fields.Integer(dump_only=True)
	name = fields.String(required=True)
	category = fields.String(required=True)
	equipment_needed = fields.Boolean(required=True)

	workout_exercises = fields.Nested(
		lambda: WorkoutExerciseSchema, 
		many=True, 
		exclude=('workout', 'exercise'))

class WorkoutSchema(Schema):
	id = fields.Integer(dump_only=True)
	date = fields.Date(required=True)
	duration_minutes = fields.Integer(required=True)
	notes = fields.String(required=True)

	workout_exercises = fields.Nested(
		lambda: WorkoutExerciseSchema, 
		many=True, 
		exclude=('workout', 'exercise'))
	
class WorkoutExerciseSchema(Schema):
	id = fields.Integer(dump_only=True)
	reps = fields.Integer(required=False)
	sets = fields.Integer(required=False)
	duration_seconds = fields.Integer(required=False)

	workout = fields.Nested(
		lambda:WorkoutSchema, 
		many=False, 
		exclude=('workout_exercises',))
	exercise = fields.Nested(
		lambda:ExerciseSchema, 
		many=False, 
		exclude=('workout_exercises',))