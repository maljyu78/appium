import pytest
from pages.product import ProductPage
from pages.app import AppPage
from pages.login import LoginPage
from pages.product_detail import ProductDetailPage
from data.testdata import (
    ProductData,
    SortMenu,
    SideMenu,
    ContainerHeader,
    AccountData,
)


def test_id_001_products_title_displayed(driver):
    product_page = ProductPage(driver)
    expected_title_name = ContainerHeader.names[0]
    
    assert product_page.catalog_displayed() is True, "[F] product page undisplayed"
    assert product_page.get_title_name() == expected_title_name, \
        "[F] product page title name is wrong"

def test_id_002_products_list_displayed(driver):
    product_page = ProductPage(driver)

    for product in ProductData.products_data:
        name = product["name"]
        price = product["price"]

        card = product_page.find_product_card(product["name"])
        actual_products = product_page.get_product_info(card)
        actual_name = actual_products["name"]
        actual_price = actual_products["price"]
        
        is_matched = (
            actual_name == name
            and price in actual_price
        )
        assert is_matched, (
            f"[F] Product information is incorrect: "
            f"{name}"
        )

def test_id_003_click_product_move_to_detail(driver):
    product_page = ProductPage(driver)
    detail_page = ProductDetailPage(driver)

    for product in ProductData.products_data:
        name = product["name"]
        price = product["price"]
        card = product_page.find_product_card(name)

        product_page.click_product(card)

        actual_product = detail_page.get_detail_info()
        actual_name = actual_product["name"]
        actual_price = actual_product["price"]

        assert actual_name == name, (
            f"[F] Product name incorrect: "
            f"Expected={name}, "
            f"Actual={actual_name}"
        )

        assert price in actual_price, (
            f"[F] Product price incorrect: "
            f"Expected={price}, "
            f"Actual={actual_price}"
        )

        detail_page.go_back()

def test_id_004_click_review_star(driver):
    product_page = ProductPage(driver)

    for product in ProductData.products_data:
        for i in range(1, 6):
            card = product_page.find_product_card(product["name"])

            product_page.click_review_star(card, i)

            assert product_page.check_modal_button() is True, \
                "[F] Review message box undisplayed"

            product_page.click_close_modal()

def test_id_005_check_sort_menu(driver):
    product_page = ProductPage(driver)

    product_page.click_sort_button()

    for sort_name in SortMenu.button_names:
        assert product_page.check_sort_menu(sort_name) is True, \
            f"[F] {sort_name} Sort menu box undisplayed"

def test_id_005_click_name_ascending(driver):
    product_page = ProductPage(driver)

    expected = sorted(
        [product["name"] for product in ProductData.products_data],
        key= str.lower
    )
    name_asc = SortMenu.button_names[0]

    product_page.click_sort_button()
    actual_products = product_page.click_sort_menu_buttons(name_asc)

    actual_names = [
        product["name"]
        for product in actual_products
    ]
    assert expected == actual_names, (
        f"[F] Failed name ascending\n"
        f"Expected={expected}\n"
        f"Actual={actual_names}"
    )

def test_id_006_click_name_descending(driver):
    product_page = ProductPage(driver)

    expected = sorted(
        [product["name"] for product in ProductData.products_data],
        key= str.lower,
        reverse=True
    )
    name_desc = SortMenu.button_names[1]

    product_page.click_sort_button()
    actual_products = product_page.click_sort_menu_buttons(name_desc)

    actual_names = [
        product["name"]
        for product in actual_products
    ]
    assert expected == actual_names, (
        f"[F] Failed name descending\n"
        f"Expected={expected}\n"
        f"Actual={actual_names}"
    )

def test_id_007_click_price_ascending(driver):
    product_page = ProductPage(driver)

    expected = [
        product["name"]
        for product in sorted(
            ProductData.products_data,
            key=lambda item: float(
                item["price"].replace(",", "")
            )
        )
    ]
    price_asc = SortMenu.button_names[2]

    product_page.click_sort_button()
    actual_products = product_page.click_sort_menu_buttons(price_asc)

    actual_names = [
        product["name"]
        for product in actual_products
    ]
    assert expected == actual_names, (
        f"[F] Failed price ascending\n"
        f"Expected={expected}\n"
        f"Actual={actual_names}"
    )

def test_id_008_click_price_descending(driver):
    product_page = ProductPage(driver)

    expected = [
            product["name"]
            for product in sorted(
                ProductData.products_data,
                key=lambda item: float(
                    item["price"].replace(",", "")
                ),reverse=True
            )
        ]
    price_desc = SortMenu.button_names[3]

    product_page.click_sort_button()
    actual_products = product_page.click_sort_menu_buttons(price_desc)

    actual_names = [
        product["name"]
        for product in actual_products
    ]
    assert expected == actual_names, (
        f"[F] Failed price descending\n"
        f"Expected={expected}\n"
        f"Actual={actual_names}"
    )

def test_id_009_click_side_menu(driver):
    product_page = ProductPage(driver)

    product_page.open_side_menu()

    for button_names in SideMenu.button_names:
        assert product_page.check_side_menu(button_names) is True, \
        f"{button_names} Side menu undisplayed"

def test_id_010_click_side_menu_buttons(driver):
    product_page = ProductPage(driver)
    app_page = AppPage(driver)
    login_page = LoginPage(driver)
    detail_page = ProductDetailPage(driver)
    expected_title_name = ContainerHeader.names

    for button in SideMenu.button_names:
        if button["name"] == "Reset":
            product = ProductData.products_data[0]
            name = product["name"]

            menu_catalog_button = next(
                item for item in SideMenu.button_names
                if item["name"] == "Catalog"
            )
            print(f"{menu_catalog_button["name"]}")
            product_page.open_side_menu()
            product_page.click_menu(menu_catalog_button["locator_name"])

            card = product_page.find_product_card(name)
            product_page.click_product(card)

            detail_page.click_add_cart()
            detail_page.go_back()

            product_page.open_side_menu()
            product_page.click_menu(button["locator_name"])
        
        elif button["name"] == "Logout":
            username = AccountData.vaild_user["username"]
            password = AccountData.vaild_user["password"]

            menu_login_button = next(
                item for item in SideMenu.button_names
                if item["name"] == "Login"
            )
            product_page.open_side_menu()
            product_page.click_menu(menu_login_button["locator_name"])
            
            login_page.login(username, password)
            
            product_page.open_side_menu()
            product_page.click_menu(button["locator_name"])

        else:
            product_page.open_side_menu()
            product_page.click_menu(button["locator_name"])

        match button["name"]:
            case "Catalog":
                actual_title_name = app_page.get_title_name()

                assert product_page.catalog_displayed() is True, \
                "[F] product page undisplayed"
                assert expected_title_name[0] == actual_title_name, \
                "[F] product page title is wrong"
            
            case "Webview":
                actual_title_name = app_page.get_title_name()

                assert expected_title_name[1] == actual_title_name, \
                "[F] Webview page undisplayed"

            case "QR Scan":
                if app_page.permission_message_is_displayed() is True:
                    app_page.click_only_this_time()

                if app_page.google_message_is_displayed() is True:
                    app_page.click_agree_button()

                actual_title_name = app_page.get_title_name()

                assert expected_title_name[2] == actual_title_name, \
                "[F] QR Scan page undisplayed"
            
            case "Geo Location":
                if app_page.permission_message_is_displayed() is True:
                    app_page.click_only_this_time()

                if app_page.google_message_is_displayed() is True:
                    app_page.click_agree_button()

                actual_title_name = app_page.get_title_name()

                assert expected_title_name[3] == actual_title_name, \
                "[F] Geo Location page undisplayed"
            
            case "Drawing":
                actual_title_name = app_page.get_title_name()
                
                assert expected_title_name[4] == actual_title_name, \
                "[F] Drawing page undisplayed"
            
            case "About":
                actual_title_name = app_page.get_title_name()

                assert expected_title_name[5] == actual_title_name, \
                "[F] About page undisplayed"
            
            case "Reset":
                app_page.alert_message_is_displayed()
                app_page.click_agree_button()

                app_page.alert_message_is_displayed()
                app_page.click_agree_button()
                app_page.go_back()

                cart_badge_count = product_page.check_cart_count()

                assert cart_badge_count is False, \
                "[F] Failed Reset App State"
            
            case "Finger Print":
                if app_page.alert_message_is_displayed() is True:
                    app_page.click_agree_button()

                actual_title_name = app_page.get_title_name()

                assert expected_title_name[6] == actual_title_name, \
                "[F] Finger Print page undisplayed"
            
            case "Login":
                actual_title_name = login_page.get_title_name()
                assert expected_title_name[7] == actual_title_name, \
                "[F] Finger Print page undisplayed"
            
            case "Logout":
                if app_page.alert_message_is_displayed():
                    app_page.click_agree_button()

                if app_page.alert_message_is_displayed():
                    app_page.click_agree_button()

                actual_title_name = login_page.get_title_name()

                assert expected_title_name[7] == actual_title_name, \
                "[F] Failed LogOut"
            
            case "Api Calls":
                actual_title_name = app_page.get_title_name()

                assert expected_title_name[8] == actual_title_name, \
                "[F] Finger Print page undisplayed"
            
            case "Bot Video":
                actual_title_name = app_page.get_title_name()

                assert expected_title_name[9] == actual_title_name, \
                "[F] Finger Print page undisplayed"

            case _:
                raise ValueError(f"Button click failed: {button["name"]}")