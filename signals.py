# myapp/signals.py, Question-1:
import time
from django.dispatch import Signal

# Define a custom signal
my_signal = Signal()


# Signal handler (synchronous by default)
def my_signal_handler(sender, **kwargs):
    print("Signal received. Executing handler...")
    time.sleep(3)  # Simulate a long-running task
    print("Handler finished executing.")


# Connect the signal to the handler
my_signal.connect(my_signal_handler)

#Question-2 logic:
# myapp/signals.py
import time
from django.dispatch import Signal
import threading

# Define a custom signal
my_signal = Signal()

# Signal handler
def my_signal_handler(sender, **kwargs):
    print(f"Signal received in thread {threading.get_ident()}. Executing handler...")
    time.sleep(5)  # Simulate a long-running task
    print(f"Handler finished executing in thread {threading.get_ident()}.")

# Connect the signal
my_signal.connect(my_signal_handler)

#Question 3 logic:: 

# myapp/signals.py
from django.db import transaction
from django.dispatch import Signal

# Define a custom signal
my_signal = Signal()

# Signal handler
def my_signal_handler(sender, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal handler is in the same transaction.")
    else:
        print("Signal handler is NOT in the same transaction.")

# Connect the signal
my_signal.connect(my_signal_handler)

# myapp/views.py (or any other place where you handle a request)
from django.db import transaction
from myapp.signals import my_signal

@transaction.atomic
def my_view(request):
    print("Triggering signal...")
    my_signal.send(sender=None)
    return HttpResponse("Signal triggered.")