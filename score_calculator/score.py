from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from sklearn.preprocessing import StandardScaler

from score_calculator.models import RecipeInput

PLATO_GRAVITY_CONSTANT = 259
PLATO_CONVERSION_THRESHOLD = 3

estimator = joblib.load('score_calculator/estimator/GBR.pkl')
scaler = joblib.load('score_calculator/estimator/scaler.pkl')

def score(recipe_input):

    converted_input = convert_from_plato_to_specific_gravity(recipe_input)
    recipe_data_frame = pd.DataFrame(converted_input.__dict__, index=[0])
    x_transform = scaler.transform(recipe_data_frame)
    return estimator.predict(x_transform)


def convert_from_plato_to_specific_gravity(recipe_input):
    if recipe_input.OG >= PLATO_CONVERSION_THRESHOLD:
        recipe_input.OG = PLATO_GRAVITY_CONSTANT / (PLATO_GRAVITY_CONSTANT - recipe_input.OG)
    if recipe_input.FG >= PLATO_CONVERSION_THRESHOLD:
        recipe_input.FG = PLATO_GRAVITY_CONSTANT / (PLATO_GRAVITY_CONSTANT - recipe_input.FG)
    if recipe_input.BoilGravity >= PLATO_CONVERSION_THRESHOLD:
        recipe_input.BoilGravity = PLATO_GRAVITY_CONSTANT / (PLATO_GRAVITY_CONSTANT - recipe_input.BoilGravity)

    return recipe_input
