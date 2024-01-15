# Aynchronous Programming in Python

![](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/Understanding-Asynchronous-Programming-in-Python_Watermarked.4b590c7c03ea.jpg)

Async programming allows you to write concurrent code that runs in a single thread. The first advantage compared to multiple threads is that you decide where the scheduler will switch from one task to another, which means that sharing data between tasks it's safer and easier.

## Concurrency vs Parallelism

Concurrency and parallelism can sound really similar but in programming there is an important difference. Immagine you are writing a book while cooking, even if it seems like you are doing both tasks at the same time, what you are doing is switching between the two tasks, while you wait for the water to boil you are writing your book, but while you are chopping some vegetables you pause your writing. This is called concurrency. The only way to do these two tasks in parallel is having two people, one writing and one cooking, which is what multicore CPU do.
### Concurrency

![](https://res.cloudinary.com/practicaldev/image/fetch/s--d28fU0gK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/eduzmp4zt3898xz5dfia.jpeg)

### Parellelism

![](https://res.cloudinary.com/practicaldev/image/fetch/s--d28fU0gK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/eduzmp4zt3898xz5dfia.jpeg)

## Resources

- [Async with python](https://dev.to/welldone2094/async-programming-in-python-with-asyncio-12dl)

- [Getting started with async](https://realpython.com/python-async-features/)

- [AsyncIO in python](https://realpython.com/async-io-python/)

- [Aysnc python doc](https://docs.python.org/3/library/asyncio.html)

## Learning Objectives

- `async` and `await` syntax
- How to execute an `async program with asyncio`
- How to run `concurrent coroutines`
- How to create `asyncio tasks`
- How to use the `random module`

## Coroutines

A coroutine is the result of an asynchronous function which can be declared using the keyword async before def

```python
async def my_func(args):
    return args**2

routines = my_func(args)
```
When we declare a function using the async keyword the function is not run, instead, a coroutine object is returned.
