# Python Countdown Timer

A simple command-line countdown timer built using Python's `time` module. This project is a great beginner exercise to understand while loops, basic user input, and time manipulation in Python.

## Overview

This countdown timer:
- Accepts the duration (in seconds) as user input.
- Counts down in real time, displaying minutes and seconds in `MM:SS` format.
- Handles invalid input to prevent errors.
- Notifies the user with a completion message when the timer reaches zero.

## Features

- **User-Friendly:** Simply input the number of seconds to start the countdown.
- **Real-Time Countdown:** Uses a while loop with `time.sleep(1)` to update the timer every second.
- **Formatted Display:** Converts seconds into a neat `MM:SS` display using Python’s `divmod()` function.
- **Error Handling:** Catches invalid (non-numeric) inputs and prompts the user to try again.

## How It Works

1. **Input:** The program prompts the user to enter a time value in seconds.
2. **Looping:** The script runs a loop that:
   - Converts the remaining seconds into minutes and seconds.
   - Prints the formatted time.
   - Pauses for one second before decrementing the timer.
3. **Completion:** Once the time runs out, the program displays `00:00` and prints "Timer Completed!".