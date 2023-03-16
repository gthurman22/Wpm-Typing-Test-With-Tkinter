#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
import random
import time

# define a list of sentences for the user to type
sentences = [
    'The quick brown fox jumps over the lazy dog.',
    'The pen is mightier than the sword, if you are John Wick.',
    'No pain, no gain, or just use Rogaine.',
    'A glass of orange juice will not keep the heartburn away.',
    'A boiled egg in the morning is really hard to beat.',
    'Ask not what your country can do for you, ask what you can do for your country.'
]

#define global variables
sentence = ''
sentence_index = 0
words_typed = 0
time_left = 60
timer_label = None

#define a function to start the game
def generate_sentence():
    global sentence, sentence_index
    sentence_index = random.randint(0, len(sentences)-1)
    sentence = sentences[sentence_index]

#define a function to check if the user input matches the sentence
def check_sentence(event):
    global words_typed, sentence_index
    if entry.get() == sentence:
        words_typed += len(sentence.split())
        entry.delete(0, 'end')
        generate_sentence()
        sentence_label.config(text=sentence)
    else:
        entry.delete(0, 'end')

# Define a function to update the time left
def update_time():
    global time_left, timer_label, words_typed, score_label
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time left: {time_left}")
        timer_label.after(1000, update_time)
    else:
        if entry.get() == "":
            timer_label.config(text="Time's up!")
        wpm = words_typed / 60
        if wpm >= 50:
            score_label.config(text=f"Words typed: {words_typed} WPM: {wpm:.2f} Amazing job!")
        else:
            score_label.config(text=f"Words typed: {words_typed} WPM: {wpm:.2f}")

#define a function to start the game
def game():
    global words_typed, time_left, sentence_label, entry, score_label, timer_label
    words_typed = 0
    time_left = 60
    generate_sentence()

    sentence_label = tk.Label(window, text=sentence, font=('Arial', 20))
    sentence_label.pack(pady=10)

    entry = tk.Entry(window, font=('Arial', 20))
    entry.pack(pady=10)
    entry.bind('<Return>', check_sentence)
    entry.focus()

    score_label = tk.Label(window, text="Words typed: 0 WPM: 0.00", font=('Arial', 16))
    score_label.pack(pady=10)

    timer_label = tk.Label(window, text=f"Time left: {time_left}", font=('Arial', 16))
    timer_label.pack(pady=10)
    update_time()

if __name__ == "__main__":
    # creating GUI window
    window = tk.Tk()
    window.title("Typing Speed Test")
    window.geometry("500x400")

    start_button = tk.Button(window, text="Start", font=('Arial', 20), command=game)
    start_button.pack(pady=10)

    window.mainloop()


# In[ ]:




