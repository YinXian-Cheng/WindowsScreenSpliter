import ctypes
from ctypes import wintypes

# Set up Windows API functions
GetTopWindow = ctypes.windll.user32.GetTopWindow
GetNextWindow = ctypes.windll.user32.GetWindow
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
SetWindowPos = ctypes.windll.user32.SetWindowPos
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
GetWindowLong = ctypes.windll.user32.GetWindowLongW
ShowWindow = ctypes.windll.user32.ShowWindow
IsIconic = ctypes.windll.user32.IsIconic
IsZoomed = ctypes.windll.user32.IsZoomed

# Constants
GW_HWNDNEXT = 2  # Get the next window handle
GWL_STYLE = -16  # Get window style
WS_VISIBLE = 0x10000000  # Visible window style
SW_RESTORE = 9  # Restore window if minimized or maximized

# Get screen width and height
screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

# Function to check if the window is a valid top-level app window
def is_valid_app_window(hwnd):
    # Check if the window is visible and has the WS_VISIBLE style
    style = GetWindowLong(hwnd, GWL_STYLE)
    if style & WS_VISIBLE == 0:
        return False
    
    # Check if the window has a title (to filter out system windows)
    length = GetWindowTextLength(hwnd)
    if length == 0:
        return False
    
    return True

# Function to restore the window if it's minimized or maximized
def restore_window_if_needed(hwnd):
    if IsIconic(hwnd) or IsZoomed(hwnd):  # If window is minimized or maximized
        ShowWindow(hwnd, SW_RESTORE)      # Restore it to normal size

# Get the top two visible application windows
def get_top_two_windows():
    top_window = GetTopWindow(None)  # Get the topmost window handle
    if top_window is None:
        return None, None

    second_window = None

    # Iterate over all windows to find the top two app windows
    while top_window:
        if is_valid_app_window(top_window):
            if not second_window:
                second_window = GetNextWindow(top_window, GW_HWNDNEXT)  # Get second window
                while second_window and not is_valid_app_window(second_window):
                    second_window = GetNextWindow(second_window, GW_HWNDNEXT)
            break
        top_window = GetNextWindow(top_window, GW_HWNDNEXT)

    return top_window, second_window

# Resize and position windows
def split_screen_for_windows(top_window, second_window):
    if top_window:
        # Restore if the window is minimized or maximized
        restore_window_if_needed(top_window)
        # Move the topmost window to the left half
        SetWindowPos(top_window, None, 0, 0, screen_width // 2, screen_height, 0)
    if second_window:
        # Restore if the window is minimized or maximized
        restore_window_if_needed(second_window)
        # Move the second window to the right half
        SetWindowPos(second_window, None, screen_width // 2, 0, screen_width // 2, screen_height, 0)

# Get topmost and second topmost windows
top_window, second_window = get_top_two_windows()

# Split screen if both windows are found
if top_window and second_window:
    split_screen_for_windows(top_window, second_window)
else:
    print("Could not find the top or second window")
