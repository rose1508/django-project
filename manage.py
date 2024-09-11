import myapp.signals

if __name__ == '__main__':
    print("Sending signal...")
    myapp.signals.my_signal.send(sender=None)
    print("Signal sent.")
    execute_from_command_line(sys.argv)
