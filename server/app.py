from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import *
from schemas import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

workouts_schema = WorkoutSchema(many=True)
exercises_schema = ExerciseSchema(many=True)
workouts_exercises_schema = WorkoutExerciseSchema(many=True)

# List all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    serialized_workouts = workouts_schema.dump(workouts)
    return jsonify(serialized_workouts), 200

# Stretch goal: include reps/sets/duration data from WorkoutExercises
# Show a single workout with its associated exercises
@app.route('/workouts/<id>', methods=['GET'])
def get_workouts_with_exercises ():
    pass


# Create a workout
@app.route('/workouts', methods=['POST'])
def create_workouts():
    pass

# Stretch goal: delete associated WorkoutExercises
# Delete a workout
@app.route('/workouts/<id>', methods=['DELETE'])
def delete_workout ():
    pass


# List all exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    serialized_exercises = exercises_schema.dump(exercises)
    return jsonify(serialized_exercises), 200

# Show an exercise and associated workouts
@app.route('/exercises/<id>', methods=['GET'])
def get_exercise_with_workout():
    pass


# Create an exercise
@app.route('/exercises', methods=['POST'])
def create_exercise():
    pass


# Stretch goal: delete associated WorkoutExercises
# Delete an exercise
@app.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise():
    pass

# Add an exercise to a workout, including reps/sets/duration
@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout():
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)