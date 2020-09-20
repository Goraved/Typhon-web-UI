from selenium.webdriver.common.by import By


class ShopLocators:
    T_SHIRT_CATEGORY_BTN = (By.CSS_SELECTOR, 'li:nth-child(3) > a[title="T-shirts"]')
    ITEM_NAME_LBL = (By.CSS_SELECTOR, '[itemprop="name"]')
    ADD_TO_CART_BTN = (By.XPATH, '//a/span[text()="Add to cart"]')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, '[title="Proceed to checkout"]')
    SECOND_CART_STEP_BTN = (By.CSS_SELECTOR, 'p > a.button.btn.btn-default.standard-checkout.button-medium')
    TERMS_CHECKBOX = (By.XPATH, '//div[@id="uniform-cgv"]')
    PAY_WITH_BANK_BTN = (By.CSS_SELECTOR, '[title="Pay by bank wire"]')
    CONFIRM_ORDER_BTN = (By.CSS_SELECTOR, '#cart_navigation > button')
    PROFILE_BTN = (By.CSS_SELECTOR, '[title="View my customer account"]')
    ORDERS_BTN = (By.CSS_SELECTOR, '[title="Orders"]')
    ORDER_ROW = (By.CSS_SELECTOR, '#order-list > tbody > tr')
