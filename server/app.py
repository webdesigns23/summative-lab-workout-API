from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import *
from schemas import *
from marshmallow import ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

workout_schema = WorkoutSchema()
exercise_schema = ExerciseSchema()

workouts_schema = WorkoutSchema(many=True)
exercises_schema = ExerciseSchema(many=True)
workouts_exercises_schema = WorkoutExerciseSchema(many=True)

# Workout endpoints
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    serialized_workouts = workouts_schema.dump(workouts)
    return jsonify(serialized_workouts), 200

@app.route('/workouts/<id>', methods=['GET'])
def get_workouts_with_exercises (id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({'error':"Workout not found."}), 404
    serialized_workout = workout_schema.dump(workout)
    return jsonify(serialized_workout), 200

@app.route('/workouts', methods=['POST'])
def create_workouts():
    try:
        workout_data = workout_schema.load(request.json)
        new_workout = Workout(**workout_data)
        db.session.add(new_workout)
        db.session.commit()
        serialized_workout = workout_schema.dump(new_workout)
        return jsonify(serialized_workout), 201
    except ValidationError as error:
        return jsonify(error.messages), 404

@app.route('/workouts/<id>', methods=['DELETE'])
def delete_workout (id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({"error": "Workout not found."}),404
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message":"Successfully deleted"}), 204

# Exercise endpoints

@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    serialized_exercises = exercises_schema.dump(exercises)
    return jsonify(serialized_exercises), 200

@app.route('/exercises/<id>', methods=['GET'])
def get_exercise_with_workout(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({'error':"Exercise not found."}), 404
    serialized_exercise = exercise_schema.dump(exercise)
    return jsonify(serialized_exercise), 200

@app.route('/exercises', methods=['POST'])
def create_exercise():
    try:
        exercise_data = exercise_schema.load(request.json)
        new_exercise = Exercise(**exercise_data)
        db.session.add(new_exercise)
        db.session.commit()
        serialized_exercise = exercise_schema.dump(new_exercise)
        return jsonify(serialized_exercise), 201
    except ValidationError as error:
        return jsonify(error.messages), 404

@app.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({"error": "Exercise not found."}),404
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({"message":"Successfully deleted"}), 204

# Add an exercise to a workout, including reps/sets/duration
@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout():
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)