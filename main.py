import ctypes
from ctypes import wintypes

# Set up Windows API functions
GetTopWindow = ctypes.windll.user32.GetTopWindow
GetNextWindow = ctypes.windll.user32.GetWindow
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
SetWindowPos = ctypes.windll.user32.SetWindowPos

# Constants
GW_HWNDNEXT = 2  # Get the next window handle

# Get screen width and height
screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

# Get the top two visible windows
def get_top_two_windows():
    top_window = GetTopWindow(None)  # Get the topmost window handle
    if top_window is None or not IsWindowVisible(top_window):
        return None, None

    second_window = GetNextWindow(top_window, GW_HWNDNEXT)  # Get second window handle
    while second_window and not IsWindowVisible(second_window):  # Find the next visible window
        second_window = GetNextWindow(second_window, GW_HWNDNEXT)
    
    return top_window, second_window

# Resize and position windows
def split_screen_for_windows(top_window, second_window):
    if top_window:
        # Move the topmost window to the left half
        SetWindowPos(top_window, None, 0, 0, screen_width // 2, screen_height, 0)
    if second_window:
        # Move the second window to the right half
        SetWindowPos(second_window, None, screen_width // 2, 0, screen_width // 2, screen_height, 0)

# Get topmost and second topmost windows
top_window, second_window = get_top_two_windows()

# Split screen if both windows are found
if top_window and second_window:
    split_screen_for_windows(top_window, second_window)
else:
    print("Could not find the top or second window")
