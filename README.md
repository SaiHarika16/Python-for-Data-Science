# Python-for-Data-Science
3rd semester internship project

# Python for Data Science - Predicting Math Scores

This project demonstrates how Python can be used for data analysis and predictive modeling. The project uses an Excel file (`finalmarks.xlsx`) containing students' marks in various subjects. The aim is to calculate the average score of each student and predict their Mathematics score based on other subject scores using Linear Regression.

## Features

- Data Loading: Loads student data from an Excel file.
- Data Analysis: Calculates average marks for each student based on their scores in various subjects.
- Data Visualization: 
  - Displays a bar chart showing the average scores of students.
  - Displays a pie chart showing the contribution of each subject to the average score.
  - Visualizes the comparison between the original and predicted Mathematics scores.
- Predictive Modeling: Uses Linear Regression to predict the Mathematics score based on other subjects (Telugu, Hindi, English, Science, and Social).
- Model Evaluation: Evaluates the model using Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn

To install the required dependencies, run the following command:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Data

The project expects an Excel file named `finalmarks.xlsx` in the same directory. The file should contain the following columns:

- **Name**: The name of the student.
- **Telugu**: Marks in Telugu.
- **Hindi**: Marks in Hindi.
- **English**: Marks in English.
- **Mathematics**: Marks in Mathematics.
- **Science**: Marks in Science.
- **Social**: Marks in Social Science.

## How to Run

1. Clone this repository or download the project files.
2. Make sure you have the necessary dependencies installed.
3. Place the `finalmarks.xlsx` file in the project directory.
4. Run the `project.py` script:
    ```bash
    python project.py
    ```

## Results

- The script will print the original data and the data with calculated average scores.
- A bar chart will be displayed showing the average scores of students.
- A pie chart will show the contribution of each subject to the average score.
- The model will predict Mathematics scores based on other subjects, and both the original and predicted scores will be displayed.
- The script will also evaluate the model and print the Mean Absolute Error, Mean Squared Error, and Root Mean Squared Error.

### Visualization:
1. **Bar Chart**: Average Scores of Students
2. **Pie Chart**: Contribution of Each Subject to Average Score
3. **Line Graph**: Original vs Predicted Mathematics Scores

### Model Evaluation:
```
Mean Absolute Error: 0.56
Mean Squared Error: 0.58
Root Mean Squared Error: 0.76
```