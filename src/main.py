from window_status import is_window_running
from app_loader import open_max_app1_desktop1, open_max_app2_desktop2
from virtual_desk_manager import switch_desktop_view
from config_loader import app1_title, app2_title

def main():
    if is_window_running(app1_title, app2_title):
        switch_desktop_view()
    else:
        # 打开,移动,最大化app1到桌面1
        open_max_app1_desktop1()
        # 打开,移动,最大化app2到桌面2
        open_max_app2_desktop2()

if __name__ == "__main__":
    main()
