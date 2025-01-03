# Team 7 Exam Score Checker

# Input exam scores for each team member
naruto_score = int(input("Enter Naruto's exam score: "))
sasuke_score = int(input("Enter Sasuke's exam score: "))
sakura_score = int(input("Enter Sakura's exam score: "))

# Function to determine performance and teacher's comment
def evaluate_score(name, score):
    if score > 90:
        print(f"{name}'s score: {score} - Excellent! Kakashi says, 'You've surpassed expectations!'")
    elif 70 <= score <= 90:
        print(f"{name}'s score: {score} - Good! Iruka says, 'You're improving steadily!'")
    else:
        print(f"{name}'s score: {score} - Needs Improvement! Kakashi says, 'Focus on training harder!'")

# Evaluate scores for each team member
evaluate_score("Naruto", naruto_score)
evaluate_score("Sasuke", sasuke_score)
evaluate_score("Sakura", sakura_score)

