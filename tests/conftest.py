import pytest
import subprocess
import time
import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pathlib import Path

class OStype:
    ANDROID = "android"
    IOS = "ios"

def detect_current_platform():
    max_retries = 3
    retry_delay = 3

    for attempt in range(1, max_retries + 1):
        print(f"\n[INFO] Scanning active device ({attempt}/{max_retries})")

        try:
            result = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                check=True,
            )

            print("[DEBUG] adb devices output:")
            print(result.stdout)

            devices = []

            for line in result.stdout.splitlines():
                parts = line.split()

                # 예: emulator-5554    device
                if len(parts) == 2 and parts[1] == "device":
                    devices.append(parts[0])

            if devices:
                print(f"[NOTI] Android Device detected: {devices}")
                return OStype.ANDROID

        except FileNotFoundError as error:
            print("[ERROR] adb executable was not found in Python PATH.")
            print(f"[ERROR] {error}")

        except subprocess.CalledProcessError as error:
            print("[ERROR] adb command execution failed.")
            print(error.stderr)

        if attempt < max_retries:
            print(f"[INFO] Device not found. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

    raise RuntimeError(
        "No active Android device detected. "
        "Check adb connection and Python execution environment."
    )

@pytest.fixture(scope="session")
def appium_server():
    service = AppiumService()

    service.start(args= ['--address', '127.0.0.1', '--port', '4723', '--relaxed-security'])
    print("[noti] complete appium server started")

    yield service

    service.stop()
    print("[noti] complete appium server killed")

@pytest.fixture(scope="function")
def driver(appium_server):
    target_platform = detect_current_platform()
    project_root = Path(__file__).resolve().parent.parent

    if target_platform == OStype.ANDROID:
        apk_path = project_root / "apps" / "Android-MyDemoAppRN.1.3.0.build-244.apk"
        if not apk_path.exists():
            raise FileNotFoundError(
                f"APK file was not found : {apk_path}."
                )
        print(f"[INFO] APK path : {apk_path}")

        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.device_name = 'emulator-5554'
        options.app = str(apk_path)

    elif target_platform == OStype.IOS:
        ios_path = project_root / "apps" / "iOS-Simulator-MyRNDemoApp.1.3.0-162.zip"
        if not ios_path.exists():
            raise FileNotFoundError(
                f"iOS app not found at {ios_path}. Please check the path."
            )
        print(f"[INFO] iOS app path : {ios_path}")

        options = XCUITestOptions()
        options.platform_name = 'iOS'
        options.automation_name = 'XCUITest'
        options.device_name = 'iPhone 14'
        options.app = str(ios_path)

    else:
        raise ValueError(f"incorrect type: {target_platform}")

    driver = webdriver.Remote('http://localhost:4723', options=options)

    driver.platform = target_platform

    try:
        dont_show_btn = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))
        )
        dont_show_btn.click()
        time.sleep(1)

    except Exception:
        pass

    finally:
        driver.implicitly_wait(0)

    yield driver

    driver.quit()