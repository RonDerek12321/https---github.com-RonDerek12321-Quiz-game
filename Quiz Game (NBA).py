#Introduction

print("Welcome to the NBA quiz!")

# Begin with questions

questions = ("Which NBA player has the most total points in NBA history?: ",
             "Which of these coaches have played in the NBA?: ",
             "Who is this season's MVP?: ",
             "Who is the tallest player in NBA history?: ",
             "Which of these coaches haven't been fired this season?: ",
             "Which player didn't become an all-star this season?: ",
             "What team had the best record this season?: ",
             "What is Giannis Antetokounmpo's nickname?: ",
             "Which player had the most points in a game: ",
             "Which of these players don't have a signature shoe?: ",
             "How many rings does Stephen Curry have?: ",
             "How many MVPs did Kobe Bryant get in his career?: ",
             "Which team did Michael Jordan retire with?: ",
             "Which team has the number 1 pick for this year's draft?: ",
             "Who is the youngest MVP in NBA history?: ")

# 2D Tuple of options - 4 for every question as each inner Tuple will have four elements

options = ("A. Kareem Abdul-Jabbar, B. Michael Jordan, C. LeBron James, D. Dillon Brooks",
           "A. Quin Snyder, B. Steve Kerr, C. Nick Nurse, D. Gregg Popovich",
           "A. Nikola Jokic, B. Giannis Antetokounmpo, C. Jayson Tatum, D. Joel Embiid",
           "A. Gheorghe Muresan, B. Yao Ming, C. Tacko Fall, D. Chris Paul",
           "A. Mike Budenholzer, B. Doc Rivers, C. Monty Williams, D. Mike Brown",
           "A. Tyrese Haliburton, B. Jrue Holiday, C. James Harden, D. Jaylen Brown",
           "A. Boston Celtics, B. Milwaukee Bucks, C. Golden State Warriors, D. Denver Nuggets",
           "A. The King, B. The Greek Freek, C. The Beard, D. The Greek Freak",
           "A. Wilt Chamberlain, B. Ben Simmons, C. Michael Jordan, D. Kobe Bryant",
           "A. Zion WIlliamson, B. Kyrie Irving, C. Nikola Jokic, D. Spencer Dinwiddie",
           "A. 4, B. 3, C. 2, D. 5",
           "A. 3, B. 2, C. 5, D. 1",
           "A. Washington Wizards, B. Cleveland Cavaliers, C. Chicago Bulls, D. New York Knicks",
           "A. Portland Trailblazers, B. San Antonio Spurs, C. Charlotte Hornets, D. Orlando Magic",
           "A. Michael Jordan, B. Derrick Rose, C. Kevin Durant, D. Magic Johnson")

# These are the answers for each question

answers = ("C", "B", "D", "A", "D", "C", "B", "D", "A", "C", "A", "D", "A", "B", "B")

# Initialize variables
score = 0
total_questions = len(questions)

# Iterate through each question
for i in range(total_questions):
    # Print the question and options
    print(f"\nQuestion {i + 1}: {questions[i]}")
    print(options[i])

    # Get user's answer and convert it to uppercase
    user_answer = input("Your answer (A, B, C, or D): ").upper()

    # Check if the user's answer is valid
    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid option. Skipping to the next question.")
        continue

    # Get the correct answer
    correct_answer = answers[i]

    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

# Calculate the percentage score
percentage = (score / total_questions) * 100

# Print the final score
print("\nYour Score:", score, "out of", total_questions)
print("Percentage Score:", percentage, "%")
