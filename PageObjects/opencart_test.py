import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import allure
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from MainPage import MainPage
from ProductPage import ProductPage
from CartPage import CartPage
from RegisterPage import RegisterPage
from AdminPage import AdminPage




@allure.feature("First test")
@allure.title("screenshot view")
def test_screenshot(driver,logger):
    main_page = MainPage(driver,logger)
    main_page.go_to_site()
    time.sleep(1)
    product_page = ProductPage(driver,logger)
    time.sleep(1)
    product_page.open_product()
    time.sleep(1)
    product_page.open_thumbnail()
    time.sleep(1)
    product_page.next_lightbox()
    time.sleep(1)
    product_page.next_lightbox()
    time.sleep(1)
    product_page.next_lightbox()
    time.sleep(1)


@allure.feature("Second test")
@allure.title("Cart")
def test_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    cart_page = CartPage(driver, logger)
    time.sleep(1)
    cart_page.add_to_cart()
    time.sleep(1)
    cart_page.open_cart()
    time.sleep(1)
    cart_items = cart_page.get_cart_items()
    time.sleep(1)
    if cart_items:
        print("Корзина не пуста")
    else:
        print("Корзина пуста")
    time.sleep(1)


@allure.feature("Third test")
@allure.title("PC")
def test_pc_category(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(1)
    main_page.open_pc_category()
    time.sleep(2)
    product_items = main_page.get_pc_items()
    time.sleep(1)
    if product_items:
        print("Страница категории PC пуста.")
    else:
        print("Страница категории PC не пуста.")


@allure.feature("Fourth test")
@allure.title("Register")
def test_register(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(2)
    register_page = RegisterPage(driver, logger)
    time.sleep(1)
    register_page.open_register_page()
    time.sleep(1)
    register_page.register_user("Да", "Га", "gaga@gmail.com", "12345")
    time.sleep(1)


@allure.feature("Fifth test")
@allure.title("Search")
def test_search(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(2)
    main_page.search("камеры")
    time.sleep(1)


@allure.feature("Sixth test")
@allure.title("wishlist")
def test_add_to_wishlist(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(1)
    product_page = ProductPage(driver, logger)
    time.sleep(1)
    product_page.add_to_wishlist(1)
    time.sleep(1)


@allure.feature("Seventh test")
@allure.title("Camera")
def test_add_camera_to_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    product_page = ProductPage(driver, logger)
    time.sleep(1)
    product_page.camera()
    time.sleep(1)
    product_page.add_to_cart_camera()
    time.sleep(1)


@allure.feature("eight test")
@allure.title("Tablet")
def test_add_tablet_to_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    product_page = ProductPage(driver, logger)
    time.sleep(1)
    product_page.tablet()
    time.sleep(1)
    product_page.add_to_cart_tablet()
    time.sleep(1)


@allure.feature("Ninth test")
@allure.title("Htc")
def test_add_htc_to_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(1)
    product_page = ProductPage(driver, logger)
    product_page.htc()
    time.sleep(1)
    product_page.add_to_cart_htc()
    time.sleep(2)


@allure.feature("Tenth test")
@allure.title("Submit")
def test_submit_review(driver, logger):
    main_page = MainPage(driver, logger)
    time.sleep(2)
    main_page.go_to_site()
    time.sleep(2)
    product_page = ProductPage(driver, logger)
    time.sleep(1.5)
    product_page.open_review_form()
    time.sleep(1.5)
    product_page.submit_review("Blinchik", "очень хороший товар, мне он прям зашёл")
    time.sleep(1.5)

@allure.feature("Eleventh test")
@allure.title("Login")
def test_login_admin(driver, logger):
    admin_page = AdminPage(driver, logger)
    admin_page.login("user", "bitnami")


@allure.feature("Twelfth test")
@allure.title("Category")
def test_create_category(driver, logger):
    admin_page = AdminPage(driver, logger)
    admin_page.create_category("Devices", "Devices", "Devices")


@allure.feature("Thirteenth test")
@allure.title("Product")
def test_create_product(driver, logger):
    admin_page = AdminPage(driver, logger)
    admin_page.create_product("Computer mouse 1", "Computer mouse 1", "Computer mouse 1", "Devices", "Computer_mouse_1")
    admin_page.create_product("Computer mouse 2", "Computer mouse 2", "Computer mouse 2", "Devices", "Computer_mouse_2")
    admin_page.create_product("Keyboard 1", "Keyboard 1", "Keyboard 1", "Devices", "Keyboard_1")
    admin_page.create_product("Keyboard 2", "Keyboard 2", "Keyboard 2", "Devices", "Keyboard_2")
#
#
@allure.feature("Fourteenth test")
@allure.title("Check")
def test_check_created_products(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    main_page.search("Mouse")
    product_items = main_page.get_product_items()
    assert len(product_items) == 2, f"Ожидалось 2 мышки товара, но найдено {len(product_items)}"
    main_page.search("Keyboard")
    product_items = main_page.get_product_items()
    assert len(product_items) == 2, f"Ожидалось 2 клавиатуры, но найдено {len(product_items)}"


@allure.feature("Fifteenth test")
@allure.title("Delete")
def test_delete_created_products(driver, logger):
    admin_page = AdminPage(driver, logger)
    admin_page.go_to_admin_page()
    admin_page.login("user", "bitnami")
    admin_page.delete_product()


@allure.feature("Sixteenth test")
@allure.title("Check deleted")
def test_check_deleted_products(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    main_page.search("Mouse")
    product_items = main_page.get_product_items()
    assert len(product_items) == 1, f"Ожидался 1 мышиный товар, но найдено {len(product_items)}"

    main_page.search("Keyboard")
    product_items = main_page.get_product_items()
    assert len(product_items) == 1, f"Ожидался 1 клавиатурный товар, но найдено {len(product_items)}"
