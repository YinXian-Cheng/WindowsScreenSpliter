import time
import pygetwindow as gw
import sys

def is_window_running(app1_title, app2_title):
    """Check if windows with app1_title and app2_title exist."""
    app1_running = False
    app2_running = False

    # Check for windows with app1_title
    windows = gw.getWindowsWithTitle(app1_title)
    if windows:
        app1_running = True

    # Check for windows with app2_title
    windows = gw.getWindowsWithTitle(app2_title)
    if windows:
        app2_running = True

    return app1_running and app2_running

def wait_for_process(process_title):
    """Wait for the process to start running by checking window titles(Should be within 30 seconds)."""
    i = 0
    while not gw.getWindowsWithTitle(process_title):
        time.sleep(0.2)
        i += 1
        if i >= 150:  # 150 * 0.2 seconds = 30 seconds
            print("No response in 30 seconds")
            sys.exit(1)

            