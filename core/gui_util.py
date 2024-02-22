import win32gui
import win32process
import ctypes
import time

# 定义用于注入的文字
text_to_inject = "Hello, DirectX 11!"

def find_directx_window():
    """
    找到DirectX 11窗口
    """
    def enum_windows_callback(hwnd, lparam):
        class_name = win32gui.GetClassName(hwnd)
        if class_name == "WinGraphicsWindow0":  # 替换为实际的DirectX 11窗口类名
            process_id = win32process.GetWindowThreadProcessId(hwnd)[1]
            lparam.append((hwnd, process_id))

    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows[0] if windows else None

def inject_text(hwnd, text):
    """
    在窗口中注入文字
    """
    buffer_size = len(text) + 1
    # 将文字转换为字节码
    buffer = ctypes.create_unicode_buffer(buffer_size)
    ctypes.windll.user32.SetWindowTextW(hwnd, text)

def main():
    # 找到DirectX 11窗口
    directx_window_info = find_directx_window()
    if directx_window_info:
        directx_window_handle, process_id = directx_window_info
        print("Found DirectX 11 window:", directx_window_handle)
        print("Injecting text...")
        # 注入文字
        inject_text(directx_window_handle, text_to_inject)
        print("Text injected successfully!")
    else:
        print("DirectX 11 window not found.")

if __name__ == "__main__":
    main()
