import turtle
# Step 2: Recursive Factorial Function
def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Step 3: Recursive Fibonacci Function
def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Step 4: Bonus - Recursive Fractal Drawing using Turtle
def draw_fractal_tree(branch_length, t):
    """Draws a recursive tree using turtle graphics."""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Step 5: User Interaction Loop
def main():
    print("🌟 Welcome to the Recursive Artistry Program! 🌟")

    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        choice = input("> ")

        if choice == "1":
            try:
                number = int(input("Enter a number to find its factorial: "))
                if number < 0:
                    print("❌ Please enter a non-negative integer.")
                else:
                    print(f"The factorial of {number} is {factorial(number)}.")
            except ValueError:
                print("❌ Invalid input. Please enter a positive integer.")

        elif choice == "2":
            try:
                position = int(input("Enter the position of the Fibonacci number: "))
                if position < 0:
                    print("❌ Please enter a non-negative integer.")
                else:
                    print(f"The {position}th Fibonacci number is {fibonacci(position)}.")
            except ValueError:
                print("❌ Invalid input. Please enter a positive integer.")

        elif choice == "3":
            print("🖼️ Drawing a fractal tree... Close the window to return to the menu.")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.left(90)
            t.speed("fastest")
            draw_fractal_tree(100, t)
            screen.exitonclick()

        elif choice == "4":
            print("👋 Goodbye! Thanks for exploring recursion!")
            break

        else:
            print("❌ Invalid option. Please choose 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()