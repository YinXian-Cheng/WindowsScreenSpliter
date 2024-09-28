from pyvda import VirtualDesktop, get_virtual_desktops

def go_to_desktop(desktop_number: int):
    """Switch to N-th desktop. If the desktop number exceeds the number of desktops, create new desktops until the desktop number exists."""
    desktops = get_virtual_desktops()
    current_number_of_desktops = len(desktops)

    # Create new desktops if the specified desktop number exceeds the current number of desktops
    while current_number_of_desktops < desktop_number:
        VirtualDesktop.create()
        current_number_of_desktops += 1
        print(f"Created desktop {current_number_of_desktops}")

    # Switch to the target desktop
    target_desktop = VirtualDesktop(desktop_number)
    target_desktop.go()
    print("Switched to desktop", desktop_number)

def switch_desktop_view():
    """If the current desktop is desktop 1, switch to desktop 2; if the current desktop is desktop 2, switch to desktop 1."""
    current_desktop = VirtualDesktop.current().number
    print("currend desktop:", current_desktop)
    if current_desktop == 1:
        go_to_desktop(2)
        print("Switched to desktop 2")
    elif current_desktop == 2:
        go_to_desktop(1)
        print("Switched to desktop 1")
    else:
        target_desktop = VirtualDesktop(2)
        target_desktop.go()
