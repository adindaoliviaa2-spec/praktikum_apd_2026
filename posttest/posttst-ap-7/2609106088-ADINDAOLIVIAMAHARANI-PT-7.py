import os
users = {
    "ovoxo": ["rahasia", "admin"],
    "milo": ["itu", "user"],
}
list_films = [
    {"title": "Whiplash", "release": "2014", "director": "Damien Chazelle", "duration": "107 minutes", "rating": "4.4"},
    {"title": "Interstellar", "release": "2014", "director": "Christopher Nolan", "duration": "169 minutes", "rating": "4.5"},
    {"title": "Taxi driver", "release": "1976", "director": "Martin Scorsese", "duration": "114 minutes", "rating": "4.1"},
    {"title": "The godfather", "release": "1972", "director": "Francis Ford Coppola", "duration": "175 minutes", "rating": "4.5"},
]
watchlist_user = []
current_user = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def detail_films(index):
    try:
        film = list_films[index]
        print(f"\n--- {film['title']} ---")
        print(f"release: {film['release']}")
        print(f"directed by: {film['director']}")
        print(f"duration: {film['duration']}")
        print(f"ratings: {film['rating']}\n")
    except IndexError:
        print("invalid input.")


def updated_films(films, index=0):
    if index >= len(films):
        return
    print(f"{index + 1}. {films[index]['title']}")
    updated_films(films, index + 1)


def validation_index(input_str, max_len):
    try:
        val = int(input_str)
        if 1 <= val <= max_len:
            return val - 1
        return None
    except ValueError:
        return None


def get_user_role():
    global current_user, users
    if current_user in users:
        return users[current_user][1]
    return "user"


def is_watchlist_empty():
    global watchlist_user
    return len(watchlist_user) == 0


def main():
    global current_user, watchlist_user, list_films
    clear()

    while True:
        try:
            print("[1] Login")
            print("[2] Register")
            choice = input("Choose option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")

                if username in users and password == users[username][0]:
                    print(f"\nwelcome {username}!\n")
                    current_user = username
                    break
                else:
                    print("invalid username or password! Try again?\n")
                    continue

            elif choice == "2":
                new_username = input("Enter new username: ")
                new_password = input("Enter new password: ")

                if new_username in users:
                    print("Username already exists! Try again.\n")
                else:
                    users[new_username] = [new_password, "user"]
                    print("Registration successful! Please login.\n")
                continue
            else:
                print("invalid input.")
                continue
        except Exception as x:
            print(f"something went wrong: {x}")

    added_films = []

    while True:
        try:
            user_role = get_user_role()
            print("[1]list films\n[2]watchlist")
            if user_role == "admin":
                print("[3]add films\n[4]edit data films\n[5]delete film")
            print("[0]exit")

            choices = input("choose between the option: ")

            if choices == "1":
                while True:
                    if not list_films:
                        print("list films is empty.")
                        break
                    print("\n--- Film List ---")
                    updated_films(list_films)

                    input_index = input("choose to see more detail(b to cancel): ")
                    if input_index.lower() == 'b':
                        break

                    idx = validation_index(input_index, len(list_films))
                    if idx is not None:
                        detail_films(idx)
                    else:
                        print("invalid input.")

            elif choices == "2":
                if is_watchlist_empty():
                    print("your watchlist is empty!")
                else:
                    print("--- Your Watchlist ---")
                    for i, film in enumerate(watchlist_user):
                        print(f"{i+1}. {film}")

                input_index = input("add film index here(b to cancel): ")
                if input_index.lower() == 'b':
                    continue

                idx = validation_index(input_index, len(list_films))
                if idx is not None:
                    title_film = list_films[idx]['title']
                    if title_film not in watchlist_user:
                        watchlist_user.append(title_film)
                        print(f"{title_film} successfully added to your watchlist!")
                    else:
                        print(f"{title_film} is already in your watchlist!")
                else:
                    print("invalid input.")

            elif choices == "3":
                if user_role != "admin":
                    print("invalid input.")
                    continue

                if not added_films:
                    print("you haven't added film yet")
                else:
                    print("--- Added Films ---")
                    for title in added_films:
                        print(f"{title}")

                input_film = input("add your films include the data here\n"
                                   "for example: (title film), (years release), (director), (film duration), (rating)\n"
                                   "(b to cancel):")

                if input_film.lower() == 'b':
                    continue

                film_data = [item.strip() for item in input_film.split(",")]
                if len(film_data) == 5:
                    added_films.append(film_data[0])
                    list_films.append({
                        "title": film_data[0],
                        "release": film_data[1],
                        "director": film_data[2],
                        "duration": film_data[3],
                        "rating": film_data[4]
                    })
                    print("successfully added!")
                else:
                    print("invalid input!")

            elif choices == "4":
                if user_role != "admin":
                    print("invalid input.")
                    continue

                updated_films(list_films)
                input_index = input("pick an index films to change the data(b to back): ")
                if input_index.lower() == 'b':
                    continue

                idx = validation_index(input_index, len(list_films))
                if idx is not None:
                    detail_films(idx)
                    print("Insert the new data (or just press enter to keep the old data):")
                    title = input(f"title [{list_films[idx]['title']}]: ") or list_films[idx]['title']
                    release = input(f"release [{list_films[idx]['release']}]: ") or list_films[idx]['release']
                    directed = input(f"directed by [{list_films[idx]['director']}]: ") or list_films[idx]['director']
                    duration = input(f"duration [{list_films[idx]['duration']}]: ") or list_films[idx]['duration']
                    ratings = input(f"ratings [{list_films[idx]['rating']}]: ") or list_films[idx]['rating']

                    list_films[idx] = {
                        "title": title,
                        "release": release,
                        "director": directed,
                        "duration": duration,
                        "rating": ratings
                    }
                    print("Data successfully updated!")
                else:
                    print("invalid input.")

            elif choices == "5":
                if user_role != "admin":
                    print("invalid input.")
                    continue

                updated_films(list_films)
                input_index = input("pick an index films to delete(b to back): ")
                if input_index.lower() == 'b':
                    continue

                idx = validation_index(input_index, len(list_films))
                if idx is not None:
                    deleted_film = list_films.pop(idx)
                    print(f"Film {deleted_film['title']} successfully deleted.")
                else:
                    print("invalid input.")

            elif choices == "0":
                break
            else:
                print("invalid input.")

        except Exception as x:
            print(f"something went wrong: {x}")


if __name__ == "__main__":
    main()