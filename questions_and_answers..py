
def quest_ask(question, answer):
    error = ""
    global score
    try:
        response = (input(question))
        if response == answer:
            print("Correct")
            score += 1
            return response
        else:
            print("Incorrect")
    except ValueError:
        print(error)




# Main routine


q1 = quest_ask("What does NBA stand for?", "national basketball association".lower().strip())
q2 = quest_ask("How many teams are there in the NBA?", "30".lower().strip())
q3 = quest_ask("How tall is an official nba rim", "10 Foot".lower().strip())
q4 = quest_ask("What Player has scored the most points in a single game?", "Wilt Chamberlain".lower().strip())
q5 = quest_ask("Who is the shortest player in NBA history", "Muggsy Bogues".lower().strip())
q6 = quest_ask("Who is the tallest player in NBA history", "Yao Ming".lower().strip())

print(score)
print("Well done! Your total score was {} out of 6".format(score))
