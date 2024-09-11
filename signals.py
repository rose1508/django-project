# myapp/signals.py
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
