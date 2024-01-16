# Python Async comprehension

~[](https://miro.medium.com/v2/resize:fit:720/format:webp/1*QIH11ANjUwb7Gye_aktWOQ.png)

An asynchronous comprehension allows a list, set, or dict to be created using the “async for” expression with an asynchronous iterable. We propose to allow using async for inside list, set and dict comprehensions. This will create and schedule coroutines or tasks as needed and yield their results into a list.

Python has extensive support for synchronous comprehensions, allowing to produce lists, dicts, and sets with a simple and concise syntax. We propose implementing similar syntactic constructions for the asynchronous code.

To illustrate the readability improvement, consider the following example:

```python
result = []
async for i in aiter():
    if i % 2:
        result.append(i)
```

With the proposed asynchronous comprehensions syntax, the above code becomes as short as:

```python
result = [i async for i in aiter() if i % 2]
```

The PEP also makes it possible to use the await expressions in all kinds of comprehensions:

```python
result = [await fun() for fun in funcs]
```

## Resources
- [PEP 530 Async comprehensions](https://peps.python.org/pep-0530/)

- [a brief overview](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)

- [using "async for"](https://superfastpython.com/asyncio-async-for/)

- [async comprehensions in python](https://superfastpython.com/asynchronous-comprehensions/#:~:text=An%20asynchronous%20comprehension%20allows%20a,list%2C%20set%20and%20dict%20comprehensions.&text=This%20will%20create%20and%20schedule,their%20results%20into%20a%20list.)

- [asyncio.gather() method](https://superfastpython.com/asyncio-gather)

## Learning Objectives

- How to write an `asynchronous generator`
- How to use `async comprehensions`
- How to `type-annotate generators`
