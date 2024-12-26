def greet():
    print("Hello")
    print("Welcome to Chapter Four")

# Simulate starting a new chapter in an online course
def start_new_chapter(chapter_number):
    print(f"Starting Chapter {chapter_number}...")
    if chapter_number == 4:
        greet()
    else:
        print(f"Welcome to Chapter {chapter_number}")

# Example usage
start_new_chapter(4)