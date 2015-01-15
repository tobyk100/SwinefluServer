logfile = 'capture.log'

def parselogs():
    with open(logfile, 'r+') as f:
        contents = f.read()
    return contents
    # Do things with contents