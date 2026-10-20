import os

users = {
    "ovoxo" : ["rahasia", "admin"],
    "milo" : ["itu", "user"],
}
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("[1] Login")
    print("[2] Register")
    choice = input("Choose option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")


        if username in users and password == users[username][0]:
            print(f"\nwelcome {username}!\n")
            current_user = username
        else:
            print("invalid username or password! Try again?\n")
            continue

    elif choice == "2":
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")

        registered_usernames = list(users.keys())
        if new_username in registered_usernames:
            print("Username already exists! Try again.\n")
        else:
            users[new_username] = [new_password, "user"]
            print("Registration successful! Please login.\n")
        continue
    else:
        print("invalid input.")
        continue


    list_films = [
        {"title": "Whiplash", "release": "2014", "director": "Damien Chazelle", "duration": "107 minutes", "rating": "4.4"},
        {"title": "Interstellar", "release": "2014", "director": "Christopher Nolan", "duration": "169 minutes", "rating": "4.5"},
        {"title": "Taxi driver", "release": "1976", "director": "Martin Scorsese", "duration": "114 minutes", "rating": "4.1"},
        {"title": "The godfather", "release": "1972", "director": "Francis Ford Coppola", "duration": "175 minutes", "rating": "4.5"},
    ]

    cancel = ['b', 'B']
    watchlist_user = []
    added_films = []
    deleted_film = []

    user_role = users[current_user][1]

    while True:
        print("[1]list films\n"
              "[2]watchlist")
        if user_role == "admin":
            print("[3]add films\n"
                  "[4]edit data films\n"
                  "[5]delete film")
        print("[0]exit")
        choices = input("choose between the option: ")
    
        if choices == "1":
            while True:
                for i, film in enumerate(list_films):
                    print(f"{i + 1}. {film['title']}")

                input_index = input("choose to see more detail(b to cancel): ")
                
                valid_index = [str(i+1) for i in range(len(list_films))]

                if input_index in cancel:
                    break
                elif input_index in valid_index:
                    data = int(input_index)-1
                    print(f"\n--- {list_films[data]['title']} ---")
                    print(f"release: {list_films[data]['release']}")
                    print(f"directed by: {list_films[data]['director']}")
                    print(f"duration: {list_films[data]['duration']}")
                    print(f"ratings: {list_films[data]['rating']}\n")
                else:
                    print("invalid input.")
                
        elif choices == "2":
            if len(watchlist_user) == 0:
                print("your watchlist is empty!")
            else:
                print("--- Your Watchlist ---")
                for i, film in enumerate(watchlist_user):
                    print(f"{i+1}. {film}")
            
            input_index = input("add film index here(b to cancel): ")

            valid_index = [str(i+1) for i in range(len(list_films))]

            if input_index.lower() == 'b':
                continue

            elif input_index in valid_index:
                index = int(input_index) - 1
                title_film = list_films[index]['title']

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
            
            if input_film in cancel or input_film.lower() in [c.lower() for c in cancel]:
                continue
            else:
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

            for i, film in enumerate(list_films):
                print(f"{i + 1}. {film['title']}")

            input_index = input("pick an index films to change the data(b to back): ")

            if input_index in cancel or input_index.lower() in [c.lower() for c in cancel]:
                continue
            elif input_index.isdigit() and 1 <= int(input_index) <= len(list_films):
                data = int(input_index) - 1

                print(f"--- {list_films[data]['title']} ---")
                print(f"release: {list_films[data]['release']}")
                print(f"directed by: {list_films[data]['director']}")
                print(f"duration: {list_films[data]['duration']}")
                print(f"ratings: {list_films[data]['rating']}")
                print("--------------------")

                print("Insert the new data (or just press enter to keep the old data):")
                title = input(f"title [{list_films[data]['title']}]: ") or list_films[data]['title']
                release = input(f"release [{list_films[data]['release']}]: ") or list_films[data]['release']
                directed = input(f"directed by [{list_films[data]['director']}]: ") or list_films[data]['director']
                duration = input(f"duration [{list_films[data]['duration']}]: ") or list_films[data]['duration']
                ratings = input(f"ratings [{list_films[data]['rating']}]: ") or list_films[data]['rating']

                list_films[data] = {
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

            for i, film in enumerate(list_films):
                print(f"{i + 1}. {film['title']}")

            valid_index = [str(i + 1) for i in range(len(list_films))]

            input_index = input("pick an index films to delete(b to back): ")
            if input_index in cancel or input_index.lower() in [c.lower() for c in cancel]:
                continue
                
            if input_index in valid_index:
                deleted_film = list_films.pop(int(input_index) - 1)
                print(f"Film {deleted_film['title']} successfully deleted.")
            else:
                print("Pilihan tidak valid!")

        elif choices == "0":
            break

        else:
            print("invalid input.")
    break