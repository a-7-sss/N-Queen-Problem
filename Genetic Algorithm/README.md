# N-Queens Problem Using Genetic Algorithm

This is a small project where I try to solve the N-Queens problem using a Genetic Algorithm.  
The N-Queens problem means we need to put N queens on a chess board (N x N) so the queens do not attack each other.

This method (Genetic Algorithm) is not the best or fastest, but it is simple and it can get a good solution most of the time.

---

## What is the N-Queens Problem?

The idea is to place N queens on the board.  
A queen can attack another queen if they are in:

- the same row  
- the same diagonal  
(the column is always different in my representation)

So the goal is to make a board with **0 attacks**.

---

## Why I Used Genetic Algorithm?

I used GA because:

- it is easy to implement  
- it can find a solution without checking all possibilities  
- it works okay for medium size N  
- I already studied the idea so I wanted to try it  

---

## How I Represent the Board

I use a list of numbers.  
The index of the list = column  
The value = row

Example for N = 8:

```
[2, 4, 1, 7, 5, 0, 6, 3]
```

This means queen in column 0 is in row 2, column 1 in row 4, and so on.

---

## Fitness Function

The fitness is the number of attacks between queens.  
If two queens attack each other, the fitness becomes worse.  
A perfect solution has **fitness = 0**.

---

## Selection

I use something simple:  
I take 3 random solutions and choose the one with the best fitness.

---

## Crossover

I take part from parent 1 and part from parent 2.

---

## Mutation

I change one random place in the list.

---

## Code Example

The code is below in the project file.  
It's simple Python code and not very advanced.

---

## Example Output

```
Solution: [4, 6, 1, 5, 2, 0, 3, 7]
```

This is one solution for N = 8.

---

## Advantages

- Easy to write  
- Works for many N values  
- Does not need strong math  

---

## Disadvantages

- It is random, so the result may change  
- Not the best performance  
- Sometimes it takes time to find a good solution  

---

## Conclusion

Genetic Algorithm is not perfect, but it can solve the N-Queens problem in a simple way.  
This project helped me understand how GA works with a real example.
