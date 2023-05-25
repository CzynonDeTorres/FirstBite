from database import food, meal, user
import datetime

class Mood:
    def mood(self):
        

        def opt():
            choice = input("<yes>\n<no>\n\n")
            if choice.lower() == "yes":
                mood_notes = input("Please input your emotion notes\n\n")
            elif choice.lower() == "no":
                main()
            else:
                self.opt()

        def show(self):
            um = input("Let us know how you feel, user\n<happy>\n<sad>\n<neutral>\n<angry>\n\n")
            if um.lower() == "happy":
                user_mood = "happy"
            elif um.lower() == "sad":
                user_mood = "sad"
            elif um.lower() == "neutral":
                user_mood = "neutral"
            elif um.lower() == "angry":
                user_mood = "angry"
            else:
                self.mood()

            print("Tracking your emotions can help you understand your eating habits better.")
            print("Would you like to elaborate how you feel? (This choice is optional. All information is confidential.)")
            self.opt()



class FoodChoice:
    def __init__(self):
        self.meal_select = 0

    def view_meal(self):
        print("//// meals from database")

    def input_meal(self):
        food_check = input("Search for food in our database: ")
        food_class = food.Food()
        food_class.search_food(food_check)

        choice = input("Input your meal: ")
        food_class.set_food(choice)
        meal_obj = meal.Meal()
        user_obj = user.User()
        meal_obj.add_meal(self.meal_select, user_obj.id, choice, food_class.name, datetime.date.today())

    def add_meal(self):
        print("Please select your meal")
        self.meal_select = input("1.<Breakfast>\n2.<Lunch>\n3.<Dinner>\n4.<Snack>\n5.<I haven't eaten yet>\n\n")
        if self.meal_select == "1":
            self.input_meal()
        elif self.meal_select == "2":
            self.input_meal()
        elif self.meal_select == "3":
            self.input_meal()
        elif self.meal_select == "4":
            self.input_meal()
        elif self.meal_select == "5":
            self.food_choice()
        else:
            self.add_meal()

    def show(self):
        print("Please select a function:")
        select = input("1.<Add Meal>\n2.<View Meals>\n\n")
        if select == "1":
            self.add_meal()
        elif select == "2":
            self.view_meal()
        else:
            self.show()


class Exercise:

    def edit_routine(self):
        choice = input("<yes>\n<no>\n\n")
        if choice.lower() == "yes":
            exercise_routine = input("--edit exercise routine--\n\n")
            self.exercise()
        elif choice.lower() == "no":
            main()
        else:
            self.edit_routine()

    def show(self):
        print("")  # Exercise routine from database
        print("\nWould you like to edit your exercise routine?")
        self.edit_routine()


def main():
    food_choice = FoodChoice()
    mood_obj = Mood()
    exercise = Exercise()
    select = input("Please select a function:\n<Food>\n<Mood>\n<Groove>\n\n")
    if select.lower() == "food":
        food_choice.show()
    elif select.lower() == "mood":
        mood_obj.show()
    elif select.lower() == "groove":
        exercise.show()
    else:
        main()