from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_message(self):
        assert "Your basket is empty." in self.get_element_content(*BasketPageLocators.BASKET_MESSAGE), "There are items in basket"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in basket"
