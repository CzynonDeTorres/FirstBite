import os
import datetime

# Clear Console 
# Clearing the console

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Calorie Calculator
# Calculates the Daily Calorie Intake Target of the user

class CalorieCalculator:
    def __init__(self, gender, age, weight, height, activity_factor):
        self.gender = gender
        self.age = age
        self.weight_in_kg = weight
        self.height_in_cm = height
        self.activity_factor = activity_factor
        self.cal_msg = ''

    def calculate_daily_calories(self):
        if self.gender == "Male":
            bmr = 66 + (6.23 * float(self.weight_in_kg)) + (12.7 * float(self.height_in_cm)) - (6.8 * float(self.age))
        else:
            bmr = 655 + (4.35 * float(self.weight_in_kg)) + (4.7 * float(self.height_in_cm)) - (4.7 * float(self.age))

        daily_calories = round(bmr * self.activity_factor)
        return daily_calories
    
    def show(self):
        daily_calories = self.calculate_daily_calories()
        self.cal_msg = "Your daily calorie requirement is {}." .format(daily_calories)
        print(self.cal_msg)

# Goals Window
# Asking the user for their weight goals

class GoalsWindow:
    def __init__(self):
        self.title = "Goals Selection"
        self.goal_options = {
            "1": "Lose Weight",
            "2": "Maintain Weight",
            "3": "Gain Weight"
        }
        self.selected_goal = ""
        self.change_goal = False  # Flag to indicate if goal needs to be changed

    def show(self):
        clear_console()
        while True:
            print(self.title)
            print("Let's start with your goals. Select one:")
            self.display_options()
            choice = input("Enter the number corresponding to your goal: ") 
            self.selected_goal = self.process_choice(choice)

            if self.change_goal:
                self.change_goal = False
                continue  # Return to the start of the loop to select a new goal

            break  # Exit the loop and proceed to the next window

    def display_options(self):
        for key, value in self.goal_options.items():
            print(f"{key}. {value}")

    def process_choice(self, choice):
        if choice in self.goal_options.keys():
            return self.goal_options[choice]
        else:
            print("Invalid choice. Please try again.")
            return self.process_choice(input("Enter the number corresponding to your goal: "))

    def get_goal_weight_required(self):
        return self.selected_goal in ["Lose Weight", "Gain Weight"]
    
    def get_selected_goal(self):
        return self.selected_goal
    
# Emphasize Options Window 
# User prompting selected features

class EmphasizedOptionsWindow:
    def __init__(self):
        self.options = {
            "1": "Track My Micronutrients & Macronutrients",
            "2": "Modify My Meals",
            "3": "Manage Stress & Mental State",
            "4": "Workout & Exercise",
            "5": "Gain Muscle"
        }
        self.title = "Emphasized Options"
        self.emphasized_options = ""
        self.selected_options = []

    def show(self):
        clear_console()
        print(self.title)
        print("What do you want to emphasize? Select one or more options:")
        for key, value in self.options.items():
            print(f"{key}. {value}")
        print("Enter the corresponding numbers separated by commas (e.g., 1, 3, 5): ")
        choices = input()
        self.emphasized_options = self.process_choices(choices)

    def process_choices(self, choices):
        for choice in choices.strip(", "):
            if choice in self.options.keys():
                self.selected_options.append(self.options[f'{choice}'])
        return self.selected_options
    
    def get_selected_options(self):
        options = self.selected_options
        output = ""
        for selected in options:
            output += f'{selected}, '
        output = output[:-2]
        return output

# Measurement Window
# To prompt the height and weight of the

class MeasurementWindow:
    def __init__(self, goals_window):
        self.title = "Measurement Window"
        self.height = 0
        self.weight = 0
        self.height_in_cm = 0
        self.weight_in_kg = 0
        self.goal_weight = 0
        self.age = AgeCalculationWindow().show()

    def get_measurement(self, measurement_type):
        options = {
            "height": {
                "1": "Feet & Inches",
                "2": "Centimeters"
            },
            "weight": {
                "1": "Pounds",
                "2": "Kilograms"
            },
            "goal weight": {
                "1": "Pounds",
                "2": "Kilograms"
            }
        }
        clear_console()
        print(f"What is your {measurement_type}?")
        option = input(f"Enter 1 for {options[measurement_type]['1']}, or 2 for {options[measurement_type]['2']}: ")

        if option == "1" and measurement_type == "height":
            feet = input("Enter the feet part of your height: ")
            inches = input("Enter the inches part of your height: ")
            self.height_in_cm = self.convert_feet_inches_to_cm(feet, inches)
        elif option == "2" and measurement_type == "height":
            cm = float(input("Enter your height in centimeters: "))
            self.height_in_cm = float(cm)
        elif option == "1" and measurement_type == "weight":
            pounds = float(input("Enter your weight in pounds: "))
            self.weight_in_kg = self.convert_pounds_to_kg(pounds)
        elif option == "2" and measurement_type == "weight":
            kg = float(input("Enter your weight in kilograms: "))
            self.weight_in_kg = float(kg)
        elif option == "1" and measurement_type == "goal weight":
            pounds = float(input("Enter your goal weight in pounds: "))
            self.goal_weight = self.convert_pounds_to_kg(pounds)
        elif option == "2" and measurement_type == "goal weight":
            kg = float(input("Enter your goal weight in kilograms: "))
            self.goal_weight = float(kg)
        else:
            print("Invalid option. Please try again.")
            self.get_measurement(measurement_type)

    def get_goal_weight(self, selected_goal):
        if self.get_goal_weight_required(selected_goal):
            print("Please enter your goal weight.")
            self.get_measurement("goal weight")
        else:
            return None

    def get_goal_weight_required(self, selected_goal):
        if "Maintain" not in selected_goal:
            return True

    def convert_feet_inches_to_cm(self, feet, inches):
        feet = float(feet)
        inches = float(inches)
        # Conversion logic from feet & inches to centimeters
        height_in_cm = (feet * 30.48) + (inches * 2.54)
        return float(height_in_cm)

    def convert_pounds_to_kg(self, pounds):
        # Conversion logic from pounds to kilograms
        weight_in_kg = float(pounds) * 0.45359237
        return float(weight_in_kg)

    def show(self):
        clear_console()
        print(self.title)
        goals_window = GoalsWindow()  # Create instance of GoalsWindow
        self.height = self.get_measurement("height")
        self.weight = self.get_measurement("weight")
        self.goal_weight = self.get_goal_weight(goals_window.selected_goal)

# Age Calculation Window 

class AgeCalculationWindow:
    def __init__(self):
        self.title = "Age Calculation"
        self.age = 0

    def show(self):
        clear_console()
        print(self.title)
        self.calculate_age()

    def calculate_age(self):
        birthdate = self.get_valid_birthdate()
        today = datetime.date.today()
        self.age = float(today.year - birthdate.year - (today < datetime.date(today.year, birthdate.month, birthdate.day)))

    def get_valid_birthdate(self):
        while True:
            try:
                return datetime.datetime.strptime(input("Enter your birthdate (YYYY-MM-DD): "), "%Y-%m-%d").date()
            except ValueError:
                print("Invalid birthdate format. Please try again.")

# Gender Selection Window

class GenderSelectionWindow:
    def __init__(self):
        self.title = "Gender Selection"
        self.gender_options = {
            "1": "Cisgender Male",
            "2": "Cisgender Female",
            "3": "Queer"
        }
        self.selected_gender = None

    def show(self):
        clear_console()
        print(self.title)
        self.display_options()
        choice = self.get_valid_choice()
        self.selected_gender = self.process_choice(choice)

        if self.selected_gender == "Queer":
            self.show_queer_options()
        elif self.selected_gender in ["Cisgender Male", "Cisgender Female"]:
            return  # Proceed to the next window
        else:
            print("Invalid choice. Please try again.")
            self.show()

    def display_options(self):
        for key, value in self.gender_options.items():
            print(f"{key}. {value}")

    def get_valid_choice(self):
        while True:
            choice = input("Enter the number corresponding to your gender: ")
            if choice in self.gender_options:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def process_choice(self, choice):
        return self.gender_options[choice]

    def show_queer_options(self):
        meds_choice = input("Have you consumed any gender-affirming medications or care in general? (Y/N): ")
        meds_choice = meds_choice.upper()

        if meds_choice == "Y":
            print("Consult with a healthcare provider about what is the best choice for your needs.")
            gender_choices = {"1": "Masc", "2": "Fem"}
        elif meds_choice == "N":
            gender_choices = self.gender_options.copy()
            del gender_choices["3"]  # Remove "Queer" option
        else:
            print("Invalid choice. Please try again.")
            self.show_queer_options()

        self.show_gender_options(gender_choices)

    def show_gender_options(self, choices):
        print("Select your sex assigned at birth.")
        for key, value in choices.items():
            print(f"{key}. {value}")

        self.selected_gender = choices[input("Enter the number corresponding to your choice: ")]

# Activity Level Window
# Determining the user's activeness level

class ActivityLevelWindow:
    activity_levels = [
        {"name": "Not Very Active", "factor": 1.2},
        {"name": "Lightly Active", "factor": 1.375},
        {"name": "Active", "factor": 1.55},
        {"name": "Very Active", "factor": 1.725}
    ]

    def __init__(self):
        self.title = "Baseline Activity Level"
        self.activity_level = None

    def show(self):
        clear_console()
        print(self.title)
        self.display_options()
        choice = input("Enter the number corresponding to your activity level: ")
        self.activity_level = self.process_choice(choice)

    def display_options(self):
        for index, activity in enumerate(self.activity_levels, start=1):
            print(f"{index}. {activity['name']}")

    def process_choice(self, choice):
        try:
            choice_index = int(choice) - 1
            return self.activity_levels[choice_index]["factor"]
        except (ValueError, IndexError):
            return "Invalid choice. Please try again."

# Finalize Goal Window
# User needs to finalize their goal and choices to proceed

class FinalizeGoalWindow:
    def __init__(self, selected_goal, selected_options):
        self.title = "Finalizing Your Choices"
        self.selected_goal = selected_goal
        self.selected_options = selected_options

    def show(self):
        clear_console()
        self.goal_message = "Selected Goal: {}".format(self.selected_goal)
        self.option_message = "Selected Emphasized Options: {}".format(self.selected_options)
        print(self.title)
        print(self.goal_message)
        print(self.option_message)
        return self.confirm_changes()

    def confirm_changes(self):
        while True:
            confirm = input("Do you want to change your selected goal and emphasized options? (Y/N): ")
            if confirm.upper() == "Y":
                return True
            elif confirm.upper() == "N":
                return False

# Press Key Prompt
# To be able to proceed to the next window

class PressKeyPrompt:
    def __init__(self, message):
        self.message = message

    def show(self):
        print(self.message)
        input()

# Welcome Screen
# Greeting the user and prompting name

class WelcomeScreen:
    def __init__ (self):
        self.title = "Welcome to First Bite!"
        self.name = None
        self.message = None

    def show(self):
        clear_console()
        print(self.title)
        self.name = input("What would you like to be called? ")
        self.message = ("Hi {}! Thank you for letting us in your journey! ".format(self.name))
        print(self.message)


def main():

    # Displaying the Welcome Screen

    welcome = WelcomeScreen()
    welcome.show()

    # Displaying the Press Key Prompt (to proceed to the next portion)

    press_key_prompt = PressKeyPrompt("Press any key to continue...")
    press_key_prompt.show()

    # Displaying the Goals Window and select goal

    goals_window = GoalsWindow()
    goals_window.show()

    # Displaying the Emphasized Goals Window

    emphasized_options_window = EmphasizedOptionsWindow()
    emphasized_options_window.show()

    # Displaying the Finalized

    finalize_window = FinalizeGoalWindow(
        selected_goal = goals_window.get_selected_goal(),
        selected_options= emphasized_options_window.get_selected_options())
    finalize_window.show()

    # Displaying the Activity Level Window

    activity_level_window = ActivityLevelWindow()
    activity_level_window.show()

    # Displaying the Gender Selection Window

    gender_window = GenderSelectionWindow()
    gender_window.show()

    # Displaying the Measurement Window

    age_calculation_window = AgeCalculationWindow()
    goals_window = GoalsWindow()    
    measurement_window = MeasurementWindow(goals_window.selected_goal)
    measurement_window.show()

    # Displaying the Calorie Calculator

    calorie_counter = CalorieCalculator(
        gender=gender_window.selected_gender,
        age=age_calculation_window.age,
        weight=measurement_window.weight_in_kg,
        height=measurement_window.height_in_cm,
        activity_factor=activity_level_window.activity_level
    )
    calorie_counter.show()

if __name__ == "__main__":
    main()