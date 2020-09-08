import pytest

from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, link)
    product_page.open(browser, link)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_product_name_in_success_message()
    product_page.is_basket_total_equals_product_price()

