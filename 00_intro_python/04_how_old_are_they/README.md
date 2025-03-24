# Age Riddle Solver

## Problem Statement

Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

- Anton is 21 years old.
- Beth is 6 years older than Anton.
- Chen is 20 years older than Beth.
- Drew is as old as Chen's age plus Anton's age.
- Ethan is the same age as Chen.

Your code should store each person's age in a variable and print their names and ages at the end.  
The autograder is sensitive to capitalization and punctuation, so be careful!

## Solution 

```python
def main():
    print("")

    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew : int = chen + anton
    ethan = chen

    # print out all of the ages
     
    print(f"Anton age is {anton}.")
    print(f"Beth age is {beth}.")
    print(f"chen age is {chen}.")
    print(f"Drew age is {drew}.")
    print(f"Ethan age is {ethan}.")

if __name__ == '__main__':
    main()



