import random

states_capitals = {'Alabama': 'Montgomery',
                   'Alaska': 'Juneau',
                   'Arizona': 'Phoenix',
                   'Arkansas': 'Little Rock',
                   'California': 'Sacramento',
                   'Colorado': 'Denver',
                   'Connecticut': 'Hartford',
                   'Delaware': 'Dover',
                   'Florida': 'Tallahassee',
                   'Georgia': 'Atlanta',
                   'Hawaii': 'Honolulu',
                   'Idaho': 'Boise',
                   'Illinois': 'Springfield',
                   'Indiana': 'Indianapolis',
                   'Iowa': 'Des Moines',
                   'Kansas': 'Topeka',
                   'Kentucky': 'Frankfort',
                   'Louisiana': 'Baton Rouge',
                   'Maine': 'Augusta',
                   'Maryland': 'Annapolis',
                   'Massachusetts': 'Boston',
                   'Michigan': 'Lansing',
                   'Minnesota': 'Saint Paul',
                   'Mississippi': 'Jackson',
                   'Missouri': 'Jefferson City',
                   'Montana': 'Helena',
                   'Nebraska': 'Lincoln',
                   'Nevada': 'Carson City',
                   'New Hampshire': 'Concord',
                   'New Jersey': 'Trenton',
                   'New Mexico': 'Santa Fe',
                   'New York': 'Albany',
                   'North Carolina': 'Raleigh',
                   'North Dakota': 'Bismarck',
                   'Ohio': 'Columbus',
                   'Oklahoma': 'Oklahoma City',
                   'Oregon': 'Salem',
                   'Pennsylvania': 'Harrisburg',
                   'Rhode Island': 'Providence',
                   'South Carolina': 'Columbia',
                   'South Dakota': 'Pierre',
                   'Tennessee': 'Nashville',
                   'Texas': 'Austin',
                   'Utah': 'Salt Lake City',
                   'Vermont': 'Montpelier',
                   'Virginia': 'Richmond',
                   'Washington': 'Olympia',
                   'West Virginia': 'Charleston',
                   'Wisconsin': 'Madison',
                   'Wyoming': 'Cheyenne'}


def check_capital(state, capital):
    state = state.strip().title()
    capital = capital.strip().title()
    correct_capital = states_capitals.get(state)
    if correct_capital:
        return capital == correct_capital
    else:
        return False


def main():
    correct_answers = 0
    incorrect_answers = 0
    states = list(states_capitals.keys())
    for _ in range(5):
        state = random.choice(states)
        capital = input(f"What is the capital of {state}? ").strip()
        while capital.isdigit():
            capital = input("Invalid input. Please try again: ")
        if check_capital(state, capital):
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect.")
            incorrect_answers += 1
    print(f"You got {correct_answers} out of 5!")
    print(f"You got {incorrect_answers} wrong.")


if __name__ == '__check_capital()__':
    check_capital()
if __name__ == '__main__':
    main()
