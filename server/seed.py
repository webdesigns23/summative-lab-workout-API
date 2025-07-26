#!/usr/bin/env python3

from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():

	# reset data and add new example data, committing to db
	WorkoutExercise.query.delete()
	db.session.commit()

	Exercise.query.delete()
	Workout.query.delete()	
	db.session.commit()

	# Create Exercises
	bicep_curl = Exercise(name='Bicep Curl', category='Strength', equipment_needed=True)
	sprint = Exercise(name='Sprint',category='Cardio', equipment_needed=False)
	squat = Exercise(name='Squat', category='Strength', equipment_needed=False)
	jump_rope = Exercise(name='Jump Rope', category='Cardio', equipment_needed=True)
	push_up = Exercise(name='Pushup', category='Strength', equipment_needed=False)
	calf_raise = Exercise(name='Calf Raise', category='Strength', equipment_needed=False)

	db.session.add_all([bicep_curl, sprint, squat, jump_rope, push_up, calf_raise])
	db.session.commit()

	# Create Workouts
	workout1 = Workout(date=date(2025, 7, 19), duration_minutes = 20, notes="Leg day")
	workout2 = Workout(date=date(2025, 7, 24), duration_minutes = 25, notes="Interval training")
	workout3 = Workout(date=date(2025, 7, 23), duration_minutes = 30, notes="Arm day")	
	workout4 = Workout(date=date(2025, 7, 22), duration_minutes = 25, notes="Circut training")	
	workout5 = Workout(date=date(2025, 7, 21), duration_minutes = 40, notes="High Intensity Training")
	workout6 = Workout(date=date(2025, 7, 20), duration_minutes = 35, notes="Aerobic activity")
	
	db.session.add_all([workout1, workout2, workout3, workout4, workout5, workout6])
	db.session.commit()

	# Associate Workout and Exercises
	we1 = WorkoutExercise(workout_id=workout1.id, exercise_id=bicep_curl.id, reps=12, sets=3, duration_seconds= 25)
	we2 = WorkoutExercise(workout_id=workout2.id, exercise_id=sprint.id, reps=12, sets=3, duration_seconds= 30)
	we3 = WorkoutExercise(workout_id=workout3.id, exercise_id=squat.id, reps=12, sets=3, duration_seconds= 45)
	we4 = WorkoutExercise(workout_id=workout4.id, exercise_id=jump_rope.id, reps=12, sets=3, duration_seconds= 40)
	we5 = WorkoutExercise(workout_id=workout5.id, exercise_id=push_up.id, reps=12, sets=3, duration_seconds= 25)
	we6 = WorkoutExercise(workout_id=workout6.id, exercise_id=calf_raise.id, reps=12, sets=3, duration_seconds= 60)

	db.session.add_all([we1, we2, we3, we4, we5, we6])
	db.session.commit()

	print("🌱 Database seeded successfully!")