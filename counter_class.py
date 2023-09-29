import subprocess
from collections import Counter


def main():
    class1 = ["Alice", "Bob", "Charlie", "David",
              "Eve", "Charlie", "David", "Fred"]
    class2 = ["Fred", "Gary", "Helen", "Ivan", "Jack", "Helen", "Alice"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    c1.update(class2)
    print(c1)
    # Prints the total number of students in both classes presenting an individual count for each student
    print(sum(c1.values()))


# THIS COUNTS THE WORDS IN A TEXT FILE
# with open("texto.txt", "r") as fp:
#     def count_words(text):
#         # print(Counter(text).most_common())
#         return (Counter(text.split()))

#     words = count_words(fp.read())
# THIS READS A TEXT FILE AND PRINTS IT
fp = open('texto.txt', 'r')
for i, line in enumerate(iter(fp.readline, '')):
    subprocess.run(["say", line])
# THIS DOES IT TOO
# with open('texto.txt', 'r') as file:
#     text = file.read()
#     print(text)


text_to_read = "Hello, this is a test."

# Use the macOS built-in TTS engine (say) to read the text aloud
# subprocess.run(["say", text_to_read])
