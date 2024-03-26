import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage
from selenium.webdriver.common.alert import Alert


class AdminPage(BasePage):
    LOGIN_USERNAME_INPUT = (By.ID, "input-username")
    LOGIN_PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    CATALOG_MENU = (By.XPATH, "//header/div[1]/button[1]/i[1]")
    CATALOG_LINK = (
        By.XPATH, "//body/div[@id='container']/nav[@id='column-left']/ul[@id='menu']/li[@id='menu-catalog']/a[1]")
    CATEGORIES_LINK = (By.XPATH, "//a[contains(text(),'Categories')]")
    ADD_NEW_CATEGORY_BUTTON = (
        By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/a[1]/i[1]")
    CATEGORY_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    CATEGORY_META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    CATEGORY_SEO = (
        By.XPATH, "//body/div[@id='container']/div[@id='content']/div[2]/div[1]/div[2]/form[1]/ul[1]/li[3]/a[1]")
    CATEGORY_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")
    CATEGORY_SAVE_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[1]")
    PRODUCT_LINK = (By.XPATH, "//a[normalize-space()='Products']")
    ADD_NEW_PRODUCT_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/a[1]")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    PRODUCT_META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    PRODUCT_DATA = (By.XPATH, "//a[contains(text(),'Data')]")
    PRODUCT_MODEL_INPUT = (By.XPATH, "//input[@id='input-model']")
    PRODUCT_LINK_LINK = (By.XPATH, "//a[contains(text(),'Links')]")
    PRODUCT_CATEGORIES = (By.CSS_SELECTOR, "#input-category")
    PRODUCT_CATEGORIES_SELECT = (By.XPATH, "//a[contains(text(),'Devices')]")
    CATEGORY_SEO_DEVICES = (By.LINK_TEXT, "SEO")
    CATEGORY_KEYWORD_DEVICES = (By.CSS_SELECTOR, "#input-keyword-0-1")
    PRODUCT_SAVE_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[1]")
    DELETE_CHECKBOX_MOUSE = (By.XPATH, "//tbody/tr[3]/td[1]/input[1]")
    PRODUCT_NAME = (By.LINK_TEXT, "Product Name")
    DELETE_CHECKBOX_KEYBOARD = (By.XPATH, "//tbody/tr[10]/td[1]/input[1]")
    DELETE_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[3]")
    ALERT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "#alert")

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.base_url = "http://localhost/administration/"

    def login(self, username, password):
        self.go_to_site()
        self.find_element(self.LOGIN_USERNAME_INPUT).send_keys(username)
        self.find_element(self.LOGIN_PASSWORD_INPUT).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def create_category(self, category_name, category_meta_tag, category_keyword):
        self.find_element(self.CATALOG_MENU).click()
        time.sleep(0.5)
        self.find_element(self.CATALOG_LINK).click()
        time.sleep(0.5)
        self.find_element(self.CATEGORIES_LINK).click()
        time.sleep(0.5)
        self.find_element(self.ADD_NEW_CATEGORY_BUTTON).click()
        time.sleep(0.5)
        self.find_element(self.CATEGORY_NAME_INPUT).send_keys(category_name)
        time.sleep(0.5)
        self.find_element(self.CATEGORY_META_TAG_INPUT).send_keys(category_meta_tag)
        time.sleep(0.5)
        self.find_element(self.CATEGORY_SEO).click()
        time.sleep(0.5)
        self.find_element(self.CATEGORY_KEYWORD).send_keys(category_keyword)
        time.sleep(0.5)
        self.find_element(self.CATEGORY_SAVE_BUTTON).click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ALERT_SUCCESS_MESSAGE))

    def create_product(self, product_name, product_meta_tag, product_model, product_category, product_keyword):
        self.find_element(self.CATALOG_MENU).click()
        time.sleep(0.5)
        self.find_element(self.PRODUCT_LINK).click()
        time.sleep(0.5)
        self.find_element(self.ADD_NEW_PRODUCT_BUTTON).click()
        time.sleep(0.5)
        self.find_element(self.PRODUCT_NAME_INPUT).send_keys(product_name)
        time.sleep(0.5)
        self.find_element(self.PRODUCT_META_TAG_INPUT).send_keys(product_meta_tag)
        time.sleep(0.5)
        self.find_element(self.PRODUCT_DATA).click()
        time.sleep(0.5)
        self.find_element(self.PRODUCT_MODEL_INPUT).send_keys(product_model)
        time.sleep(0.5)
        self.find_element(self.PRODUCT_LINK_LINK).click()
        time.sleep(0.5)
        self.find_element(self.PRODUCT_CATEGORIES).send_keys(product_category)
        time.sleep(0.5)
        self.find_element(self.PRODUCT_CATEGORIES_SELECT).click()
        time.sleep(0.5)
        self.find_element(self.CATEGORY_SEO_DEVICES).click()
        time.sleep(0.5)
        self.find_element(self.CATEGORY_KEYWORD_DEVICES).send_keys(product_keyword)
        time.sleep(0.5)
        self.find_element(self.PRODUCT_SAVE_BUTTON).click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ALERT_SUCCESS_MESSAGE))

    def delete_product(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATALOG_MENU)).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATALOG_LINK)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_LINK)).click()
        time.sleep(1)

        # Найти элемент checkbox для удаления перед его использованием
        delete_checkbox_mouse = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DELETE_CHECKBOX_MOUSE))
        delete_checkbox_mouse.click()

        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DELETE_BUTTON)).click()
        alert1 = self.driver.switch_to.alert
        alert1.accept()

        # Обновить страницу после удаления первого продукта
        self.driver.refresh()

        # Найти элемент Product Name перед его использованием
        product_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_NAME))
        product_name.click()

        time.sleep(0.5)

        # Найти элемент checkbox для удаления перед его использованием
        delete_checkbox_keyboard = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DELETE_CHECKBOX_KEYBOARD))
        delete_checkbox_keyboard.click()

        time.sleep(0.5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                       "body:nth-child(2) div:nth-child(1) div.toast-container.position-fixed.top-0.end-0.p-3:nth-child(1) > div.alert.alert-success.alert-dismissible")))

        # Найти элемент Delete Button перед его использованием
        delete_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DELETE_BUTTON))
        delete_button.click()

        alert = self.driver.switch_to.alert
        alert.accept()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ALERT_MESSAGE))

    def go_to_admin_page(self):
        self.driver.get(self.base_url)
