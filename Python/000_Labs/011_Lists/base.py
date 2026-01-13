import random
 
def random_joke(jokes):
    return random.choice(jokes)
 
joke_list = [
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
    "Why did the math book look sad? Because it had too many problems.",
    "I used to play piano by ear, but now I use my hands."
]
 
random_index = random.randint(0, len(joke_list) - 1)
print("Random joke number:", random_index)
print("Joke:", joke_list[random_index])