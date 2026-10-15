# users = [
#     ["ovoxo", "rahasia", "admin"],
#     ["milo", "itu", "user"],
# ]

# # --- 1. SISTEM LOGIN DINAMIS ---
# current_user = None
# current_role = None

# while True:
#     print("=== LOGIN ===")
#     username = input("Enter username: ")
#     if username: # Memastikan input tidak kosong
#         password = input("Enter password: ")

#         # Mengecek ke seluruh daftar user
#         login_success = False
#         for user_data in users:
#             if username == user_data[0] and password == user_data[1]:
#                 current_user = user_data[0]
#                 current_role = user_data[2]
#                 login_success = True
#                 break
        
#         if login_success:
#             print(f"\nWelcome {current_role} {current_user}!")
#             break
#         else:
#             print("Invalid username or password! Try again?\n")


# --- 2. DATA UTAMA ---
list_films = [
    ["Whiplash", "2014", "Damien Chazelle", "107 minutes", "4.4"],
    ["Inception", "2010", "Christopher Nolan", "148 minutes", "4.2"],
    ["The dark knight", "2008", "Christopher Nolan", "152 minutes", "4.5"],
    ["Interstellar", "2014", "Christopher Nolan", "169 minutes", "4.5"],
    ["Taxi driver", "1976", "Martin Scorsese", "114 minutes", "4.1"],
    ["The godfather", "1972", "Francis Ford Coppola", "175 minutes", "4.5"],
]

index = input("masukan index: ")
data = int(index)-1
print(list_films[data][0])
print(f"release: {list_films[data][1]}")
print(f"directed by: {list_films[data][2]}")
print(f"duration: {list_films[data][3]}")
print(f"ratings: {list_films[data][4]}")
# cancel = ['b', 'B']
# watchlist_user = []

# # --- 3. MENU UTAMA ---
# while True:
#     print("\n=== MAIN MENU ===")
#     print("[1] list films")
#     print("[2] watchlist")
    
#     # Cek apakah role user adalah admin
#     is_admin = (current_role == "admin")
#     if is_admin:
#         print("[3] add films")
#         print("[4] edit data films")
        
#     print("[0] exit")

#     choices = input("Choose between the options: ")

#     # --- OPSI 1: DAFTAR FILM & DETAIL ---
#     if choices == "1":
#         print("\n--- DAFTAR FILM ---")
#         for i, film in enumerate(list_films):
#             # i + 1 agar tampilan dimulai dari angka 1
#             print(f"{i + 1}. {film[0]}") 
            
#         input_index = input("\nChoose film number to see more detail ('b' to cancel): ")
        
#         if input_index in cancel:
#             continue
            
#         # Menggunakan isdigit() agar program tidak error/crash jika diisi huruf
#         if input_index.isdigit():
#             # Kurangi 1 karena indeks list dimulai dari 0, tapi input user dari 1
#             index = int(input_index) - 1 
            
#             # Cek apakah angka yang dimasukkan valid (tidak kurang dari 0 atau kelebihan)
#             if 0 <= index < len(list_films):
#                 film = list_films[index]
#                 print(f"\n--- {film[0]} ---")
#                 print(f"Release    : {film[1]}")
#                 print(f"Directed by: {film[2]}")
#                 print(f"Duration   : {film[3]}")
#                 print(f"Ratings    : {film[4]}")
#             else:
#                 print("\nNumber not found. Please select a valid film number.")
#         else:
#             print("\nInvalid input. Please enter a number.")

#     # --- OPSI 2: WATCHLIST ---
#     elif choices == "2":
#         print("\n--- YOUR WATCHLIST ---")
#         if len(watchlist_user) == 0:
#             print("Your watchlist is empty!")
#         else:
#             for i, film in enumerate(watchlist_user):
#                 print(f"[{i+1}] {film}")
        
#         # Opsi pembatalan ('b') sekarang bisa berfungsi
#         input_index = input("\nAdd film number here (press 'b' to cancel): ")
        
#         if input_index in cancel:
#             continue
        
#         if input_index.isdigit():
#             index = int(input_index) - 1
            
#             if 0 <= index < len(list_films):
#                 judul_film = list_films[index][0]
                
#                 if judul_film not in watchlist_user:
#                     watchlist_user.append(judul_film) 
#                     print(f"\n'{judul_film}' successfully added to your watchlist!")
#                 else:
#                     print(f"\n'{judul_film}' is already in your watchlist!")
#             else:
#                 print("\nInvalid input or movie is not available.")
#         else:
#             print("\nInvalid input. Please enter a valid number.")

#     # --- OPSI 3 & 4: ADMIN ONLY ---
#     elif choices == "3" and is_admin:
#         print("\n[Menu Add Films - Segera Datang]")
        
#     elif choices == "4" and is_admin:
#         print("\n[Menu Edit Data Films - Segera Datang]")

#     # --- OPSI 0: EXIT ---
#     elif choices == "0":
#         print("Thank you! Exiting program...")
#         break # Menghentikan perulangan 'while True' menu utama

#     # --- JIKA INPUT SALAH ---
#     else:
#         print("\nInvalid choice. Please select a valid option from the menu.")