import pytest
from data.testdata import (
    ProductData,
    SortMenu,
    SideMenu,
    ContainerHeader,
    AccountData,
)


def test_id_001_products_title_displayed(product_page):
    expected_title_name = ContainerHeader.names[0]
    
    assert product_page.catalog_displayed() is True, "[F] product page undisplayed"
    assert product_page.get_title_name() == expected_title_name, \
        "[F] product page title name is wrong"

def test_id_002_products_list_displayed(product_page):
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

def test_id_003_click_product_move_to_detail(product_page, detail_page):
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

def test_id_004_click_review_star(product_page):

    for product in ProductData.products_data:
        for i in range(1, 6):
            card = product_page.find_product_card(product["name"])

            product_page.click_review_star(card, i)

            assert product_page.check_modal_button() is True, \
                "[F] Review message box undisplayed"

            product_page.click_close_modal()

def test_id_005_check_sort_menu(product_page):
    product_page.click_sort_button()

    for sort_name in SortMenu.button_names:
        assert product_page.check_sort_menu(sort_name) is True, \
            f"[F] {sort_name} Sort menu box undisplayed"

def test_id_005_click_name_ascending(product_page):
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

def test_id_006_click_name_descending(product_page):
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

def test_id_007_click_price_ascending(product_page):
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

def test_id_008_click_price_descending(product_page):
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

def test_id_009_click_side_menu(product_page):
    product_page.open_side_menu()

    for button_names in SideMenu.button_names:
        assert product_page.check_side_menu(button_names) is True, \
        f"{button_names} Side menu undisplayed"

def test_id_010_click_catalog_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    catalog_button = SideMenu.button_data["Catalog"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(catalog_button)

    actual_title_name = app_page.get_title_name()

    assert product_page.catalog_displayed() is True, \
        "[F] product page undisplayed"

    assert expected_title_name[0] == actual_title_name, \
        "[F] product page title is wrong"


def test_id_011_click_webview_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    webview_button = SideMenu.button_data["Webview"]["locator_name"]
    product_page.open_side_menu()
    product_page.click_menu(webview_button)

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[1] == actual_title_name, \
        "[F] Webview page undisplayed"


def test_id_012_click_qr_scan_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    qr_scan_button = SideMenu.button_data["QR Scan"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(qr_scan_button)

    if app_page.permission_message_is_displayed() is True:
        app_page.click_only_this_time()

    if app_page.google_message_is_displayed() is True:
        app_page.click_agree_button()

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[2] == actual_title_name, \
        "[F] QR Scan page undisplayed"


def test_id_013_click_geo_location_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    Geo_location_button = SideMenu.button_data["Geo Location"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(Geo_location_button)

    if app_page.permission_message_is_displayed() is True:
        app_page.click_only_this_time()

    if app_page.google_message_is_displayed() is True:
        app_page.click_agree_button()

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[3] == actual_title_name, \
        "[F] Geo Location page undisplayed"


def test_id_014_click_drawing_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    drawing_button = SideMenu.button_data["Drawing"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(drawing_button)

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[4] == actual_title_name, \
        "[F] Drawing page undisplayed"


def test_id_015_click_about_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    about_button = SideMenu.button_data["About"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(about_button)

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[5] == actual_title_name, \
        "[F] About page undisplayed"


def test_id_016_click_reset_button(
    product_page,
    app_page,
    detail_page
):
    product = ProductData.products_data[0]
    name = product["name"]
    catalog_button = SideMenu.button_data["Catalog"]["locator_name"]
    reset_button = SideMenu.button_data["Reset"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(catalog_button)

    card = product_page.find_product_card(name)
    product_page.click_product(card)

    detail_page.click_add_cart()
    detail_page.go_back()

    product_page.open_side_menu()
    product_page.click_menu(reset_button)

    app_page.alert_message_is_displayed()
    app_page.click_agree_button()

    app_page.alert_message_is_displayed()
    app_page.click_agree_button()

    app_page.go_back()

    product_page.find_cart_badge()
    cart_badge_count = product_page.check_cart_count()

    assert cart_badge_count is False, \
        "[F] Failed Reset App State"


def test_id_017_click_finger_print_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    finger_print_button = SideMenu.button_data["Finger Print"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(finger_print_button)

    if app_page.alert_message_is_displayed() is True:
        app_page.click_agree_button()

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[6] == actual_title_name, \
        "[F] Finger Print page undisplayed"


def test_id_018_click_login_button(product_page, login_page):
    expected_title_name = ContainerHeader.names
    login_button = SideMenu.button_data["Login"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(login_button)

    actual_title_name = login_page.get_title_name()

    assert expected_title_name[7] == actual_title_name, \
        "[F] login page undisplayed"


def test_id_019_click_logout_button(
    product_page,
    app_page,
    login_page
):
    expected_title_name = ContainerHeader.names
    login_button = SideMenu.button_data["Login"]["locator_name"]
    logout_button = SideMenu.button_data["Logout"]["locator_name"]

    username = AccountData.vaild_user["username"]
    password = AccountData.vaild_user["password"]

    product_page.open_side_menu()
    product_page.click_menu(login_button)

    login_page.login(username, password)

    product_page.open_side_menu()
    product_page.click_menu(logout_button)

    if app_page.alert_message_is_displayed():
        app_page.click_agree_button()

    if app_page.alert_message_is_displayed():
        app_page.click_agree_button()

    actual_title_name = login_page.get_title_name()

    assert expected_title_name[7] == actual_title_name, \
        "[F] Failed LogOut"


def test_id_020_click_api_calls_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    api_calls_button = SideMenu.button_data["API Calls"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(api_calls_button)

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[8] == actual_title_name, \
        "[F] API calls page undisplayed"


def test_id_021_click_bot_video_button(product_page, app_page):
    expected_title_name = ContainerHeader.names
    bot_video_button = SideMenu.button_data["Bot Video"]["locator_name"]

    product_page.open_side_menu()
    product_page.click_menu(bot_video_button)

    actual_title_name = app_page.get_title_name()

    assert expected_title_name[9] == actual_title_name, \
        "[F] Bot video page undisplayed"
