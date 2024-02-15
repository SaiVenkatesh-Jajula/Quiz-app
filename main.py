"""
command line interface program!...
Program is used for conduct quiz !...
"""
import json

with open("quiz.json", 'r') as file:
    content = file.read()
quiz = json.loads(content)

#Storing user inputs for each question
for item in quiz:
    print(f"Q.{item['Question']}")
    options = item['Options']
    for i in options:
        print(f"{options.index(i) + 1}-{i}")
    answer = int(input("Enter your option:"))
    item['user_chosen'] = answer

totalscore = 0
print("\nEvaluation:")
#Calculation and showing final result
for index, item in enumerate(quiz):
    if item['user_chosen'] == item['Answer']:
        totalscore += 1
        print(f"{index+1}Q : User Chosen : {item['user_chosen']} and Answer is {item['Answer']}")
    else:
        print(f"{index+1}Q : User Chosen : {item['user_chosen']} but Answer is {item['Answer']}")

print(f"Total Score: {totalscore}/{len(quiz)}")
