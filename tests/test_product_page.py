import pytest
from pages.product import ProductPage
from pages.base import BasePage
from data.testdata import ProductData, SortMenu
from pages.product_detail import ProductDetailPage

def test_id_001_products_title_displayed(driver):
    product_page = ProductPage(driver)

    assert product_page.catalog_displayed() is True, "[F] product page undisplayed"

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

        product_page.click_all_product(card)

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


