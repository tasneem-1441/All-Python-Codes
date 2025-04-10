# Aim:Write a menu driven program on files to add, delete and display movie from text file
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
import os
def add_movie(filename):
    with open(filename, "a") as file:
        movie = input("Enter movie name: ")
        file.write(movie + "\n")
    print("Movie added successfully!")
def delete_movie(filename):
    movie_to_delete = input("Enter movie name to delete: ")
    if not os.path.exists(filename):
        print("File not found!")
        return
    with open(filename, "r") as file:
        movies = file.readlines()
    with open(filename, "w") as file:
        found = False
        for movie in movies:
            if movie.strip() != movie_to_delete:
                file.write(movie)
            else:
                found = True
    if found:
        print("Movie deleted successfully!")
    else:
        print("Movie not found!")
def display_movies(filename):
    if not os.path.exists(filename):
        print("File not found!")
        return
    with open(filename, "r") as file:
        movies = file.readlines()
    if movies:
        print("Movies List:")
        for movie in movies:
            print(movie.strip())
    else:
        print("No movies found!")
def menu():
    filename = "movies.txt"
    while True:
        print("\nMovie Manager")
        print("1. Add Movie")
        print("2. Delete Movie")
        print("3. Display Movies")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_movie(filename)
        elif choice == "2":
            delete_movie(filename)
        elif choice == "3":
            display_movies(filename)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")
            print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
menu()
