def main():
    total_tickets = 0
    movie_list = []

    while True:
        movie_name = input("Enter movie name (if done, type 'done'): ")

        if movie_name.lower() == 'done':
            break

        movie_list.append(movie_name)

        try:
            tickets = int(input("How many tickets would you like for {}? ".format(movie_name)))
            total_tickets += tickets
        except ValueError:
            print("Please enter a correct number")

        print("Your total number of tickets is: ", total_tickets)

    print("\nList of movies entered:")
    for movie in movie_list:
        print(movie)


if __name__ == "__main__":
    main()
