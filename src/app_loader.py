import subprocess
import pygetwindow as gw
from pyvda import VirtualDesktop, get_virtual_desktops, get_apps_by_z_order, AppView
from config_loader import app1_title, app1_path, app2_title, app2_path
from window_status import wait_for_process
from virtual_desk_manager import go_to_desktop

def open_max_app1_desktop1():
    """Open App1, move it to Desktop1, and maximize it."""
    # Switch to Desktop 1
    go_to_desktop(1)

    # Get App1 window and move it to Desktop 1
    windows = gw.getWindowsWithTitle(app1_title)
    if windows:
        current_desktop = VirtualDesktop.current()
        print(f"Current desktop is number {current_desktop}")

        # Use the first window that matches
        current_window = windows[0]
        target_desktop = VirtualDesktop(1)

        # Get the AppView object for the window to move it
        current_window_appview = AppView(current_window._hWnd)
        current_window_appview.move(target_desktop)
        print(f"Moved window {current_window._hWnd} to {target_desktop.number}")

        # Maximize the window using pygetwindow's method
        current_window.maximize()
        print(f"Maximized window {current_window._hWnd}")

        VirtualDesktop(1).go()
        print("Went to desktop number 1")

    else:
        # Start App1
        subprocess.Popen(app1_path)
        wait_for_process(app1_title)  # Wait for App1 to start
        open_max_app1_desktop1()  # Retry after starting the app

def open_max_app2_desktop2():
    """Open App2, move it to Desktop2, and maximize it."""
    # Switch to Desktop 2
    go_to_desktop(2)

    # Get App2 window
    windows = gw.getWindowsWithTitle(app2_title)
    if windows:
        current_desktop = VirtualDesktop.current()
        print(f"Current desktop is number {current_desktop}")

        current_window = windows[0]
        target_desktop = VirtualDesktop(2)

        current_window_appview = AppView(current_window._hWnd)
        current_window_appview.move(target_desktop)
        print(f"Moved window {current_window._hWnd} to {target_desktop.number}")

        current_window.maximize()
        print(f"Maximized window {current_window._hWnd}")

        VirtualDesktop(2).go()
        print("Moved to desktop number 2")

    else:
        # Start App2
        subprocess.Popen(app2_path)
        wait_for_process(app2_title)  # Wait for App2 to start
        open_max_app2_desktop2()  # Retry after starting the app

'''
def open_max_app2_desktop2():
    """Open App2, move it to Desktop 2, and maximize it."""
    # Check if Desktop 2 exists
    desktops = get_virtual_desktops()
    if len(desktops) < 2:
        print("Desktop 2 does not exist. Creating desktop 2.")
        VirtualDesktop.create()

    # Get App2 window and move it to Desktop 2
    windows = gw.getWindowsWithTitle(app2_title)
    if windows:
        # Move window to Desktop 2
        for window in windows:
            if app2_title.lower() in window.title.lower():
                app2_window = window
                target_desktop_index = 1  # Desktop 2 index
                pyvda.MoveWindowToDesktopNumber(app2_window._hWnd, target_desktop_index)
                VirtualDesktop(2).go()  # Switch to Desktop 2
                app2_window.maximize()
                break
    else:
        # Start App2
        subprocess.Popen(app2_path)
        wait_for_process(app2_title)  # Wait for App2 to start
        # Get App2 window and move it to Desktop 2
        windows = gw.getWindowsWithTitle(app2_title)
        # Target Desktop 2
        target_desktop = VirtualDesktop(2)

        # Move window to Desktop 2
        app_list = get_apps_by_z_order()
        if app_list:
            current_window = app_list[0]  # Assume App2 is the most recent window
            current_window.move(target_desktop)
            print(f"Moved window {current_window.hwnd} to desktop {target_desktop.number}")

            # Switch to Desktop 2
            target_desktop.go()
            print("Switched to desktop number 2")

            # Maximize App2 window
            windows = gw.getWindowsWithTitle(app2_title)
            app2_window = None

            # Iterate through the windows to find the correct App2 window
            for win in windows:
                if app2_title.lower() in win.title.lower():
                    app2_window = win
                    break

            if app2_window:
                app2_window.maximize()
            else:
                print("No app2 window found")
        else:
            print("No app2 window found")
'''
            