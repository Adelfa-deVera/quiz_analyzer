quiz = []

for i in range(1,6):
    quizzes = int(input(f"Enter quiz {i} score: "))
    quiz.append(quizzes)

sum = sum(quiz)
average = sum/len(quiz)
highest = max(quiz)
lowest = min(quiz)
ascending = sorted(quiz)
descending = sorted(quiz, reverse=True)

print("===== QUIZ SCORE REPORT =====")
print(f"Quiz Scores: {quiz}")
print("Number of quizzes: 5")
print(f"Total Score: {sum}")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Ascending: {ascending}")
print(f"Descending: {descending}")
print(f"Original Scores: {quiz}")