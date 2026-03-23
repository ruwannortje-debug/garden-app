"""
Garden Advice App.

This program gives gardening advice based on the season and plant type
entered by the user.

CHANGES MADE (Why these improvements were done):
1. Replaced hardcoded values with user input -> makes the program interactive
2. Refactored code into functions -> improves readability and modularity
3. Used dictionaries instead of multiple if statements -> makes code
   scalable and easier to maintain
4. Added plant recommendations -> improves functionality and user
   experience
5. Added detailed comments -> improves understanding and documentation
"""


# =========================
# FUNCTION: GET USER INPUT
# =========================
def get_user_input():
    """
    Ask the user for input instead of using fixed values.

    WHY:
    - Previously values were hardcoded (not flexible)
    - Now user can interact with the program
    """
    season = input(
        "Enter the season (summer/winter/spring/autumn): "
    ).strip().lower()
    plant_type = input(
        "Enter the plant type (flower/vegetable/herb): "
    ).strip().lower()
    return season, plant_type


# =========================
# FUNCTION: SEASON ADVICE
# =========================
def get_season_advice(season, season_advice_dict):
    """
    Get advice based on the season using a dictionary.

    WHY:
    - Replaces multiple if/elif statements
    - Easier to update and add more seasons later
    """
    return season_advice_dict.get(season, "No advice for this season.\n")


# =========================
# FUNCTION: PLANT ADVICE
# =========================
def get_plant_advice(plant_type, plant_advice_dict):
    """
    Get advice based on plant type using a dictionary.

    WHY:
    - More scalable than using many if statements
    - Cleaner and more readable code
    """
    return plant_advice_dict.get(
        plant_type, "No advice for this type of plant."
    )


# ==========================================
# FUNCTION: RECOMMEND PLANTS FOR THE SEASON.
# ==========================================
def get_recommended_plants(season, recommendations_dict):
    """
    Recommend plants based on the season.

    WHY:
    - Adds extra functionality to the app
    - Makes the program more useful and realistic
    """
    return recommendations_dict.get(
        season, ["No plant recommendations available."]
    )


# =========================
# FUNCTION: DISPLAY OUTPUT
# =========================
def display_advice(
    season,
    plant_type,
    season_advice_dict,
    plant_advice_dict,
    recommendations_dict
):
    """
    Combine all advice and display it to the user.

    WHY:
    - Keeps logic separate from output
    - Makes code cleaner and easier to maintain
    """
    advice = ""

    # Add season advice
    advice += get_season_advice(season, season_advice_dict)

    # Add plant advice
    advice += get_plant_advice(plant_type, plant_advice_dict)

    # Get recommendations
    recommended_plants = get_recommended_plants(season, recommendations_dict)

    # Display results
    print("\n Gardening Advice:")
    print(advice)
    print("\nRecommended plants for", season + ":")
    print(", ".join(recommended_plants))


# =========================
# MAIN PROGRAM.
# =========================
def main():
    """
    Main function that runs the program.

    WHY:
    - Keeps the program organized
    - Makes it easier to expand later
    """

    # Dictionary for season advice (replaces if statements.)
    season_advice_dict = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n",
        "spring": ("This is a great time to plant new flowers and "
                   "vegetables.\n"),
        "autumn": ("Prepare your garden for cooler weather and trim "
                   "dead leaves.\n")
    }

    # Dictionary for plant advice
    plant_advice_dict = {
        "flower": "Use fertilizer to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Make sure your herbs get enough sunlight and light watering."
    }

    # Dictionary for plant recommendations
    recommendations_dict = {
        "summer": ["Sunflowers", "Tomatoes", "Zucchini"],
        "winter": ["Kale", "Spinach", "Broccoli"],
        "spring": ["Roses", "Carrots", "Basil"],
        "autumn": ["Lettuce", "Onions", "Parsley"]
    }

    # Get user input
    season, plant_type = get_user_input()

    # Display advice
    display_advice(
        season,
        plant_type,
        season_advice_dict,
        plant_advice_dict,
        recommendations_dict
    )


# Run the program
main()
