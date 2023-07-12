This is an example of a constraints solving problem from codewars.com. I don't think I can link to the specific challenge.

The code includes:

* test.py the tests, from codewars
* main.py my solution
* constraints.py which is a constraint solving mini-framework from the book Classic Computer Science Problems in Python, some free content from Manning 

https://freecontent.manning.com/constraint-satisfaction-problems-in-python/
https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter3/csp.py

Run test.py to run the tests. constraints.py uses generic types, so requires Python 3.7+. The solution uses the walrus operator and so requires Python 3.8+.

The 'top-level' function is find_out_mr_wrong which is at the bottom of main.py.

The explanation of the framework and the example they give are very good. It uses a backtracking recursive search to find a solution. It keeps trying solutions and applying the constraints, backtracking as soon as the constraints fail and recursively continuing from the last known good partial solution.


The definition of the challenge (which includes an ambiguity) is below. The input is a series of statements about positions in a queue from which you are to deduce the order of the queue. Except at least one person is always lying. Find the liar (or return None if there are multiple).

# Task

Mr.Right always tell the truth, Mr.Wrong always tell the lies.

Some people are queuing to buy movie tickets, and one of them is Mr.Wrong. Please judge who is Mr.Wrong according to their conversation.

## Input 

A string array: conversation

They always talking about I'm in ... position., The man behind me is ... ., The man in front of me is ... ., There are/is ... people in front of me., There are/is ... people behind me..

Please note that everyone has at least one sentence and only one people is Mr.Wrong ;-)

## Output 

A string: The name of Mr.Wrong. If can not judge, return null (when several valid solutions are possible).

Examples:

    conversation=[
    "John:I'm in 1st position.",
    "Peter:I'm in 2nd position.",
    "Tom:I'm in 1st position.",
    "Peter:The man behind me is Tom."
    ]
    findOutMrWrong(conversation) should return "Tom"

    conversation=[
    "John:I'm in 1st position.",
    "Peter:I'm in 2nd position.",
    "Tom:I'm in 1st position.",
    "Peter:The man in front of me is Tom."
    ]
    findOutMrWrong(conversation) should return "John"

    conversation=[
    "John:I'm in 1st position.",
    "Peter:There is 1 people in front of me.",
    "Tom:There are 2 people behind me.",
    "Peter:The man behind me is Tom."
    ]
    findOutMrWrong(conversation) should return "Tom"

    const conversation=[
    "John:The man behind me is Peter.",
    "Peter:There is 1 people in front of me.",
    "Tom:There are 2 people behind me.",
    "Peter:The man behind me is Tom."
    ]
    findOutMrWrong(conversation) should return null

Two solutions are possible in the last example: 1) Peter is Mr.Wrong and the order is Tom, John, Peter; 2) Tom is Mr.Wrong and the order is John, Peter, Tom. In this case, the result is null.

