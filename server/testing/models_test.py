from datetime import date
from models import *

def test_add_exercise(test_client):
    exercise = Exercise(name="Jumping Jacks", category="Cardio", equipment_needed=False)
    db.session.add(exercise)
    db.session.commit()

    assert exercise.id is not None
    assert exercise.name == "Jumping Jacks"
    assert exercise.category == "Cardio"
    assert exercise.equipment_needed == False

def test_add_workout(test_client):
    workout = Workout(date=date(2025, 7, 15), duration_minutes = 28, notes="Beach body wokout")
    db.session.add(workout)
    db.session.commit()

    assert workout.id is not None
    assert workout.date == date(2025, 7, 15)
    assert workout.duration_minutes == 28
    assert workout.notes == "Beach body wokout"
    
def test_workout_exercise_relationship(test_client):
    exercise = Exercise(name="Plank", category="Strength", equipment_needed=False)
    workout = Workout(date=date(2025, 7, 18), duration_minutes = 50, notes="Interval Training")
    db.session.add_all([exercise, workout])
    db.session.commit()
    
    test_we = WorkoutExercise(workout=workout, exercise=exercise, reps= 8, sets= 5, duration_seconds= 30)
    db.session.add(test_we)
    db.session.commit()

    assert workout.workout_exercises[0].exercise.name == "Plank"
    assert workout.workout_exercises[0].exercise.category == "Strength"
    assert workout.workout_exercises[0].exercise.equipment_needed == False
    
    assert exercise.workout_exercises[0].workout.date == date(2025, 7, 18)
    assert exercise.workout_exercises[0].workout.duration_minutes == 50
    assert exercise.workout_exercises[0].workout.notes == "Interval Training"
    
    assert test_we.workout == workout
    assert test_we.exercise == exercise
    assert test_we.reps == 8
    assert test_we.sets == 5
    assert test_we.duration_seconds == 30
