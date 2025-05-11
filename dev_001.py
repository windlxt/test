import builtins
import itertools
from datetime import datetime
from tkinter import NO


@lambda _: _()
def start_time() -> str:
    """
    Returns the current date and time in ISO 8601 format.
    """

    return f"{datetime.now():%T}"


print(start_time)


# print(dir(builtins), sep="\n")
# print("==" * 20)
# print(dir(__builtins__), sep="\n")

counter = itertools.count(10, step=2)
for _ in itertools.repeat(None, 10):
    print(next(counter), end=" ")
print("\n" + "-" * 20)
