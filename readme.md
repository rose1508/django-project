Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Ans:
By default, Django signals are executed synchronously. This means that the signal handlers run in the same thread and process as the code that sent the signal.

Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Ans:Yes, by default, Django signals run in the same thread as the code that triggers the signal.


Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Ans:By default, Django signals do not run in the same database transaction as the code that triggers them. They run in the same transaction only if the signal handler is explicitly managed using transaction.atomic.

Note: For Ques 1,2 and 3 find the code snippets signals.py and manage.py
for custom class you can find answer in rectangle.py