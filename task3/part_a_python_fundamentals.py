"""
Task 03 - Part A: Python Fundamentals (30 Marks)
1. Data types and their uses
2. User-defined functions with parameters and return values
3. List and dictionary comprehensions
4. OOP: classes, objects, constructors, inheritance
"""


# ---------------------------------------------------------------------------
# 1. Python data types and their uses
# ---------------------------------------------------------------------------
def demonstrate_data_types():
    print("=" * 60)
    print("1. Python Data Types")
    print("=" * 60)

    examples = {
        "int": (42, "Whole numbers - counting, indexing, IDs"),
        "float": (3.14159, "Decimal numbers - measurements, averages, prices"),
        "str": ("PKCERT Internship", "Text - names, messages, file paths"),
        "bool": (True, "True/False - flags, conditions"),
        "list": ([1, 2, 3, "mixed", 4.5], "Ordered, mutable collection"),
        "tuple": ((10, 20), "Ordered, immutable collection - fixed records"),
        "dict": ({"name": "Ali", "age": 22}, "Key-value mapping - structured data"),
        "set": ({1, 2, 2, 3}, "Unordered, unique items - de-duplication"),
        "NoneType": (None, "Represents 'no value' - default/placeholder"),
    }

    for type_name, (value, use_case) in examples.items():
        print(f"{type_name:10s} -> {value!r:30s} | Use: {use_case}")
    print()


# ---------------------------------------------------------------------------
# 2. User-defined functions with parameters and return values
# ---------------------------------------------------------------------------
def add(a, b):
    """Simple positional-parameter function that returns a value."""
    return a + b


def describe_student(name, age=18, *subjects, **extra_info):
    """Demonstrates default args, *args and **kwargs."""
    info = f"{name} (age {age}) is studying: {', '.join(subjects) if subjects else 'N/A'}"
    if extra_info:
        info += " | Extra: " + ", ".join(f"{k}={v}" for k, v in extra_info.items())
    return info


def demonstrate_functions():
    print("=" * 60)
    print("2. User-Defined Functions")
    print("=" * 60)
    print("add(5, 7) ->", add(5, 7))
    print(describe_student("Ahmad", 21, "Python", "AI", city="Karachi"))
    print()


# ---------------------------------------------------------------------------
# 3. List and dictionary comprehensions
# ---------------------------------------------------------------------------
def demonstrate_comprehensions():
    print("=" * 60)
    print("3. List & Dictionary Comprehensions")
    print("=" * 60)

    numbers = range(1, 11)

    # List comprehension: squares of even numbers
    even_squares = [n ** 2 for n in numbers if n % 2 == 0]
    print("Even squares (list comprehension):", even_squares)

    # Dict comprehension: number -> square mapping
    square_map = {n: n ** 2 for n in range(1, 6)}
    print("Number -> square (dict comprehension):", square_map)

    # Nested list comprehension: flatten a matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [value for row in matrix for value in row]
    print("Flattened matrix:", flattened)

    print(
        "\nBenefits: comprehensions are more concise and often faster than an "
        "equivalent for-loop with .append()/[]=, since the looping happens in "
        "optimized C code under the hood, and the intent (build a new "
        "list/dict from an iterable) is clearer at a glance."
    )
    print()


# ---------------------------------------------------------------------------
# 4. OOP: classes, objects, constructors, inheritance
# ---------------------------------------------------------------------------
class Person:
    """Base class demonstrating a constructor and instance methods."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


class Student(Person):
    """Derived class demonstrating inheritance and method overriding."""

    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)  # reuse parent constructor
        self.student_id = student_id
        self.major = major

    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I study {self.major} (ID: {self.student_id})."


def demonstrate_oop():
    print("=" * 60)
    print("4. OOP - Classes, Objects, Constructors, Inheritance")
    print("=" * 60)

    person = Person("Sara", 30)
    student = Student("Bilal", 20, "PK-2026-101", "Artificial Intelligence")

    print(person.introduce())
    print(student.introduce())
    print("Is student a Person?", isinstance(student, Person))
    print()


if __name__ == "__main__":
    demonstrate_data_types()
    demonstrate_functions()
    demonstrate_comprehensions()
    demonstrate_oop()
