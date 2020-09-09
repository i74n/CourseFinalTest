from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def is_product_name_in_success_message(self):
        assert self.get_element_content(*ProductPageLocators.PRODUCT_NAME) in self.get_element_content(*ProductPageLocators.SUCCESS_MESSAGE), "Incorrect element added"

    def is_basket_total_equals_product_price(self):
        assert self.get_element_content(*ProductPageLocators.PRODUCT_PRICE) == self.get_element_content(*ProductPageLocators.SUCCESS_INFO)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message not dissapeared"

