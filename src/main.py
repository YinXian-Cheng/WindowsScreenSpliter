import subprocess
import time
from pyvda import get_apps_by_z_order, VirtualDesktop, get_virtual_desktops
import pygetwindow as gw
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 获取APP1和APP2的配置信息
app1_title = config['APP1']['title']
app1_path = config['APP1']['path']
app2_title = config['APP2']['title']
app2_path = config['APP2']['path']

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
    """Wait for the process to start running by checking window titles."""
    while not gw.getWindowsWithTitle(process_title):
        time.sleep(0.3)

def switch_between_desktops():
    """If the current desktop is desktop 1, switch to desktop 2; if the current desktop is desktop 2, switch to desktop 1."""
    current_desktop = VirtualDesktop.current().number
    if current_desktop == 1:
        target_desktop = VirtualDesktop(2)
        target_desktop.go()
        print("Switched to desktop 2")
    elif current_desktop == 2:
        target_desktop = VirtualDesktop(1)
        target_desktop.go()
        print("Switched to desktop 1")
    else:
        print(f"Current desktop is {current_desktop}, which is not 1 or 2")

def open_and_maximize_app1():
    """打开Steam并最大化到桌面1"""
    # 切换到桌面1
    desktop1 = VirtualDesktop(1)
    desktop1.go()
    print("Switched to desktop 1")

    # 启动Steam
    subprocess.Popen(app1_path)
    wait_for_process(app1_title)  # 等待Steam启动

    # 获取Steam窗口
    windows = gw.getWindowsWithTitle(app1_title)
    if windows:
        window = windows[0]
        window.maximize()  # 最大化窗口
    else:
        print("无法找到Steam的窗口")

def open_and_move_app2_to_desktop2():
    """打开WeChat并将其移动到桌面2并最大化"""
    # 检查桌面2是否存在
    desktops = get_virtual_desktops()
    if len(desktops) < 2:
        print("Desktop 2 does not exist. Creating desktop 2.")
        VirtualDesktop.create()

    # 启动WeChat
    subprocess.Popen(app2_path)
    wait_for_process(app2_title)  # 等待WeChat启动

    # 获取WeChat窗口
    windows = gw.getWindowsWithTitle(app2_title)
    if windows:
        window = windows[0]
        print(f"Current window is {window.title}")

        # 目标桌面为桌面2
        target_desktop = VirtualDesktop(2)

        # 将窗口移动到桌面2
        app_list = get_apps_by_z_order()
        if app_list:
            current_window = app_list[0]  # 假设WeChat是最新打开的窗口
            current_window.move(target_desktop)
            print(f"Moved window {current_window.hwnd} to desktop {target_desktop.number}")

            # 切换到桌面2
            target_desktop.go()
            print("Switched to desktop number 2")

            # 再次获取WeChat窗口并最大化
            windows = gw.getWindowsWithTitle(app2_title)
            app2_window = None

            # Iterate through the windows to find the correct WeChat window
            for win in windows:
                if app2_title.lower() in win.title.lower():
                    app2_window = win
                    break

            if app2_window:
                app2_window.maximize()
                print(f"App2 maximized on desktop {target_desktop.number}")
            else:
                print("无法找到app2的窗口")
        else:
            print("No windows found to move.")
    else:
        print("无法找到app2的窗口")

def main():
    if is_window_running(app1_title, app2_title):
        switch_between_desktops()
    else:
        # 打开并最大化Steam
        open_and_maximize_app1()
        # 打开并移动WeChat到桌面2
        open_and_move_app2_to_desktop2()

if __name__ == "__main__":
    main()