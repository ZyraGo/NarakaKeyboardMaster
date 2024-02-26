import win32gui

def enum_window_classes(hwnd, classes):
    class_name = win32gui.GetClassName(hwnd)
    if class_name not in classes:
        classes.append(class_name)

def print_window_classes():
    classes = []
    win32gui.EnumWindows(enum_window_classes, classes)
    print("当前所有窗体类:")
    for class_name in classes:
        print(class_name)

print_window_classes()

# {11AD28A8-838B-4781-BCA9-4CE43C38818F}
# ForegroundStaging
# tooltips_class32
# Shell_TrayWnd
# TopLevelWindowForOverflowXamlIsland
# popupshadow
# TrayNotifyWnd
# PerryShadowWnd
# CMainDialog
# NotifyIconOverflowWindow
# SystemTray_Main
# ATL:00007FF8B8690550
# ATL:00007FF8AD59D230
# PNIHiddenWnd
# #32770
# SunAwtFrame
# Chrome_WidgetWin_1
# GDI+ Hook Window Class
# SunAwtToolkit
# EmotionTipWnd
# CWebviewControlHostWnd
# ChatContactMenu
# HttpImgHoverWnd
# WeChatMainWndForPC
# SessionDragWnd
# FLUTTER_RUNNER_WIN32_WINDOW
# Chrome_WidgetWin_0
# Chrome_StatusTrayWindow
# Chrome_SystemMessageWindow
# Base_PowerMessageWindow
# crashpad_SessionEndWatcher
# ApplicationManager_DesktopShellWindow
# OleDdeWndClass
# OfficePowerManagerWindow
# ServiceWorkerGlobalScopeHost Window Class
# WorkerW
# Windows.UI.Core.CoreWindow
# DuiTimerManagerWnd
# QEventDispatcherWin32_Internal_Widget2077653808
# ConsoleWindowClass
# TimerDispatchWnd
# EventDispatchWnd
# ATL:00007FF89A4FC000
# .class.1
# COMTASKSWINDOWCLASS
# OperationStatusWindow
# .class.3
# SystemSettingsHandlerWorkerWindowSta-00007FF8BE4C0000
# ApplicationFrameWindow
# PersonalizationThemeChangeListener
# KWpsPushBubble
# __#_ACCOUNTSDK WINIPC CHANNEL NAME_#__
# KAccountWnd_Kso_classname_qingSdk
# RealtekAudioBackgroundProcessClass
# .class.2
# PDADevMonitorClass
# ImeGuard
# YunBrowserDetectServiceWnd
# SecHealth Window Class
# .NET-BroadcastEventWindow.b7ab7b.0
# HelperWndClass
# BluetoothNotificationAreaIconWindowClass
# MS_WebcheckMonitor
# TSVNCacheWindow
# RealtekAudioAdminBackgroundProcessClass
# PwrMgrBkGndWindow
# Postures Broadcast Listener Class
# EdgeUiInputTopWndClass
# TabletModeCoverWindow
# DummyDWMListenerWindow
# PushNotificationsPowerManagement
# DDEMLEvent
# DDEMLMom
# {EE79C473-8AFB-40a5-9E35-0F66CF6B4A8E}
# Dwm
# CicLoaderWndClass
# WinGraphicsWindow0
# Progman
# IME
# SoPY_Status
# SoPY_Comp
# SoPY_Hint
# SoPY_UI
# Sogou_TSF_UI
# MSCTFIME UI
