
![psd_logotext_cropped](https://github.com/CzynonDeTorres/FirstBite/assets/131897056/27cb3a31-7ab0-4420-a48d-12b51ff2a017)

# 🍽️ FirstBite 
Bite into your goals, one calorie at a time!

# 🏆 Description and Purpose
- This program focuses on Food Intake/diet monitoring that will help it's user to maintain one's
physically fitness and health. This will offer a variety of options to someone on a diet can intake
and help them calculate the calories. Overall, FirstBite aims to assist users in understanding their daily
calorie needs based on their specific goals, activity level, and personal information. It provides a personalize
calorie recommendation that can serve as a starting point for maintaining a healthy diet and achieving their weight-related goals.

## 💻 Setup

- Install python 3.8 or higher, newest version is recommended
- Install the third party libraries mentioned in `requirements.txt`.
- Run `main.py`.

## Additional Information 

FirstBite is a console-based calorie calculator. It assists users in determining their daily calorie requirements based on their gender, age, weight, height, and activity level.

Starting with the **start.py**, this file includes several classes such as. 

1. 👋 Welcome Screen: The program starts by displaying a welcome message and prompts the user to enter their name.

2. 📖 Goals Selection: The user is presented with three options to choose their weight goals: "Lose Weight," "Maintain Weight," or "Gain Weight." The user selects one of these goals.

3. 📑 Emphasized Options: The user is asked to select one or more options they want to emphasize. The available options include tracking macronutrients and micronutrients, modifying meals, managing stress and mental state, workout and exercise, and gaining muscle.

4. 🏃 Baseline Activity Level: The user is prompted to select their baseline activity level from a list of predefined options. Each option has an associated activity factor that is used in calculating daily calorie requirements.

5. ♀️♂️🏳️‍🌈 Gender Selection: The user selects their gender from the available options: "Cisgender Male," "Cisgender Female," or "Queer." Additional options are provided for the "Queer" selection, depending on whether the user has consumed gender-affirming medications or care.

6. 👶👱‍♂️🧓 Age Calculation: The user enters their birthdate, and the program calculates their age based on the current date.

7. 🧍🔢 Measurement Window: The user provides their height and weight information. They can choose to enter the measurements in either feet and inches or centimeters for height, and pounds or kilograms for weight. If the weight goal requires it, the user is also prompted to enter their goal weight.

8. 🍴🔢 Calorie Calculation: Using the provided information, including gender, age, weight, height, and activity level, the program calculates the user's daily calorie requirement. The calculation is based on the Harris-Benedict equation, adjusted for gender.

10. 🔢✔️ Display Daily Calorie Requirement: The program displays the calculated daily calorie requirement to the user.

as for the **fmg.py**, it includes the following functions

1. 😃😢😠 mood() function: This function prompts the user to input their current mood, such as "happy," "sad," "neutral," or "angry." It then asks the user if they would like to elaborate on their emotions. If the user chooses to provide more details, they can input their emotion notes. Otherwise, the function calls the fmg() function.

2. 🍜🍎 food_choice() function: This function presents the user with two options: "Add Meal" or "View Meals." If the user selects "Add Meal," they are prompted to select the type of meal they want to add (breakfast, lunch, dinner, snack, or indicate that they haven't eaten yet). Depending on their selection, the user is then asked to input the meal manually or scan a barcode. The program can search a database for the specified meal. If the user selects "View Meals," the program displays meals from a database.

3. 🏋️👯 exercise() function: This function displays an exercise routine obtained from a database. It then asks the user if they would like to edit their exercise routine. If the user chooses to edit, they can input the modified exercise routine. If not, the fmg() function is called.

4. 🍜😃🏋️ fmg() function: This function serves as the main menu for the program. It prompts the user to select a function: "Food," "Mood," or "Groove" (exercise). Depending on the user's selection, it calls the corresponding function (food_choice(), mood(), or exercise()). If the user enters an invalid input, the fmg() function is called again.

## 🌏✔️ Significance 

- The following are SDGs (Sustainable Development Goals) aligned with FirstBite. 

1. Good Health and Well-being (SDG 3): By promoting healthier eating habits and weight management, a calorie counter can contribute to improved health and well-being.

2. Sustainable Cities and Communities (SDG 11): Encouraging healthier food choices and sustainable eating patterns can support the development of sustainable cities and communities.

3. Responsible Consumption and Production (SDG 12): A calorie counter can raise awareness about the environmental impact of food choices and promote sustainable consumption patterns.

4. Gender Equality (SDG 5): If the program addresses specific nutritional needs or challenges faced by women, it can contribute to promoting gender equality in access to proper nutrition and health.

## 📹 Video Presentation
[youtubelink](https://youtu.be/hPH_sZuEYIc)


## 🖱️ Authors
- <a href="https://github.com/CzynonDeTorres">Czynon John P. De Torres</a>
- <a href="https://github.com/mafranzramos">Ma. Francezca L. Ramos</a>
- <a href="https://github.com/Aeruim26">Rosechel U. San Lorenzo</a>
- <a href="https://github.com/sy1ph">John Benedict A. Tolentino</a>
