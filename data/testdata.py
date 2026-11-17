class AccountData:
    vaild_user = {
        "username": "bob@example.com",
        "password": "10203040"
    }

    wrong_id = {
        "username": "bpb@example.com",
        "password": "10203040"
    }

    wrong_pw = {
            "username": "bob@example.com",
            "password": "10203050"
        }

    locked_user = {
        "username": "alice@example.com",
        "password": "10203040"
    }

class ProductData:
    products_data = [
        {"id": "backpack", "name": "Sauce Labs Backpack", "price": "29.99"},
        {"id": "bike_light", "name": "Sauce Labs Bike Light", "price": "9.99"},
        {"id": "bolt_tshirt", "name": "Sauce Labs Bolt T-Shirt", "price": "15.99"},
        {"id": "fleece_jacket", "name": "Sauce Labs Fleece Jacket", "price": "49.99"},
        {"id": "onesie", "name": "Sauce Labs Onesie", "price": "7.99"},
        {"id": "red_tshirt", "name": "Test.allTheThings() T-Shirt", "price": "15.99"}
    ]

class SortMenu:
    button_names = [
        "name_asc",
        "name_desc",
        "price_asc",
        "price_desc"
    ]

class SideMenu:
    button_names = [
        {"name": "Catalog", "locator_name": "menu_catalog"},
        {"name": "Webview", "locator_name": "menu_webview"},
        {"name": "QR Scan", "locator_name": "menu_qr_scan"},
        {"name": "Geo Location", "locator_name": "menu_geo_location"},
        {"name": "Drawing", "locator_name": "menu_drawing"},
        {"name": "About", "locator_name": "menu_about"},
        {"name": "Reset", "locator_name": "menu_reset_app_state"},
        {"name": "Finger Print", "locator_name": "menu_finger_print"},
        {"name": "Login", "locator_name": "menu_login"},
        {"name": "Logout", "locator_name": "menu_logout"},
        {"name": "Api Calls", "locator_name": "menu_api_calls"},
        {"name": "Bot Video", "locator_name": "menu_sauce_bot_video"},
    ]

class ContainerHeader:
    names = [
        "Products",
        "Webview",
        "QR Code Scanner",
        "Geo Location",
        "Drawing",
        "About",
        "FingerPrint",
        "Login",
        "API calls",
        "SauceBot - The Beginning",
    ]