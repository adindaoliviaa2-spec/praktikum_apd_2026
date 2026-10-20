import os
users = [
    ["ovoxo", "rahasia", "admin"],
    ["milo", "itu", "user"],
]
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("[1] Login")
    print("[2] Register")
    choice = input("Choose option: ")

    if choice == "1":
        if username := input("Enter username: "):
            password = input("Enter password: ")

            login_success = False
            for user in users:
             if username == user[0] and password == user[1]:
                print(f"\nwelcome {user[2]} {user[0]}!\n")
                login_success = True
                break
            
            if login_success:
                break
            else:
                print("invalid username or password! Try again?\n")

    elif choice == "2":
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")

        registered_usernames = [u[0] for u in users]
        if new_username in registered_usernames:
            print("Username already exists! Try again.\n")
        else:
            users.append([new_username, new_password, "user"])
            print("Registration successful! Please login.\n")
    else:
        print ("invalid input.")
  
list_films = [["Whiplash", "2014", "Damien Chazelle", "107 minutes", "4.4"],
              ["Interstellar", "2014", "Christopher Nolan", "169 minutes", "4.5"],
              ["Taxi driver", "1976", "Martin Scorsese", "114 minutes", "4.1"],
              ["The godfather", "1972", "Francis Ford Coppola", "175 minutes", "4.5"],
              ]

cancel = ['b', 'B']
watchlist_user = []
added_films = []
deleted_film = []
while True:
      print("[1]list films\n"
            "[2]watchlist")
      if valid_admin := (username == users[0][0]):
            print("[3]add films\n"
            "[4]edit data films\n"
            "[5]delete film")
      print ("[0]exit")
      choices = input ("choose between the option: ")
    
      if choices == "1":
            while True:
                for i, film in enumerate(list_films):
                    print(f"{i + 1}. {film[0]}")

                input_index = input("choose to see more detail(b to cancel): ")
                
                valid_index = [str(i+1) for i in range(len(list_films))]

                if input_index in cancel:
                    break
                elif input_index in valid_index:
                    data = int(input_index)-1
                    print(f"\n--- {list_films[data][0]} ---")
                    print(f"release: {list_films[data][1]}")
                    print(f"directed by: {list_films[data][2]}")
                    print(f"duration: {list_films[data][3]}")
                    print(f"ratings: {list_films[data][4]}\n")
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
            title_film = list_films[index][0]

            if title_film not in watchlist_user:
                watchlist_user.append(title_film)
                print(f"{title_film} successfully added to your watchlist!")
            else:
                print(f"{title_film} is already in your watchlist!")
        else:
            print("invalid input.")

      elif choices == "3":
            if not added_films:
                print("you haven't added film yet")
            else:
                print("--- Added Films ---")
                for title in added_films:
                    print(f"{title}")

            input_film = input("add your films include the data here\n"
                "for example: (title film), (years release), (director), (film duration), (rating)\n"
                    "(b to cancel):")
            
            if input_film.lower() in cancel:
                continue
            else:
                film_data = [item.strip() for item in input_film.split(",")]
                if len(film_data) == 5:
                    added_films.append(film_data[0])  
                    list_films.append(film_data)      
                    print("successfully added!")
                else:
                    print("invalid input!")

      elif choices == "4":
            for i, film in enumerate(list_films):
                print(f"{i + 1}. {film[0]}")

            input_index = input("pick an index films to change the data(b to back): ")

            if input_index.lower() in cancel:
                continue
            elif input_index.isdigit() and 1 <= int(input_index) <= len(list_films):
                data = int(input_index) - 1

                print(f"--- {list_films[data][0]} ---")
                print(f"release: {list_films[data][1]}")
                print(f"directed by: {list_films[data][2]}")
                print(f"duration: {list_films[data][3]}")
                print(f"ratings: {list_films[data][4]}")
                print("--------------------")

                print("Masukkan data baru (tekan Enter untuk menyimpan nilai lama):")
                title = input(f"title [{list_films[data][0]}]: ") or list_films[data][0]
                release = input(f"release [{list_films[data][1]}]: ") or list_films[data][1]
                directed = input(f"directed by [{list_films[data][2]}]: ") or list_films[data][2]
                duration = input(f"duration [{list_films[data][3]}]: ") or list_films[data][3]
                ratings = input(f"ratings [{list_films[data][4]}]: ") or list_films[data][4]

                list_films[data] = [title, release, directed, duration, ratings]
                print("Data successfully updated!")
            else:
                print("invalid input.")

      elif choices == "5":
            for i, film in enumerate(list_films):
                print(f"{i + 1}. {film[0]}")

            valid_index = [str(i + 1) for i in range(len(list_films))]

            input_index = input("pick an index films to delete(b to back): ")
            if input_index.lower() in cancel:
                continue
                
            if input_index in valid_index:
                deleted_film = list_films.pop(int(input_index) - 1)
                print(f"Film {deleted_film[0]} berhasil dihapus!")
            else:
                print("Pilihan tidak valid!")

      elif choices == "0":
        break