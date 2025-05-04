
#!/usr/bin/env python3

# Immutable types: str, int, float, bool, bytes, tuple
# Mutable types: list, set, dic
import binascii

number: int = 10
decimal: float = 2.5
active: bool = True
names: list = ["John", "Doe"]
#name: str = 1.2
marks: tuple = (1, 24, 5)

#print(number, decimal, names)


def greet(name:str = "") -> str:
    return f"Welcome {name.title()} !"


def area_circle(radius:float) -> float:
    # pi = 3.14
    pi: float = 3.14
    return pi * (radius ** 2)

def has_passed(average: float) -> bool:
    return average >= 50

def compute_average(scores:list[int])->float:
    return sum(scores) / len(scores)

def students_performance()-> None:
    name: str = input("Enter student name: ")
    print(greet(name))

    scores: list[int] = []

    while len(scores) < 3:
        try:
            score = int(input(f"Enter the score for subject {len(scores) + 1}: "))
            scores.append(score) if (0 <= score <= 100) else print("Score must be between 0 & 100")
        except ValueError:
            print("Please enter a valid number")

    average_score:float = compute_average(scores)
    is_pass: bool = has_passed(average_score)

    print("\n ---- Report Card -----")
    print(f"Name: \t\t\t {name}")
    print(f"Scores: \t\t {scores}")
    print(f"Average: \t\t {average_score:.2f}")
    print(f"Status: \t\t {'Pass' if is_pass else 'Fail'}")

    assignments_done: int = 5
    pts: float = 2.5
    total_score: float = average_score + pts

    print(f"Bonus Pts: \t\t {pts} for {assignments_done}")
    print(f"Final Score: \t {total_score:.2f}")

if __name__ == "__main__":
    students_performance()

