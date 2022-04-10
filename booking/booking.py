import os
import time
from selenium import webdriver
from selenium.webdriver.common import keys
import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\Selenium Drivers", tearDown = False):
        self.driver_path = driver_path
        self.tearDown = tearDown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tearDown:
            self.quit() 

    def land_first_page(self):
        self.get(const.BASE_URL)

    #(10/04/2022)Comment change currency as currently in testing phase
    """
    def change_currency(self, currency = None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        select_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        select_currency_element.click()
    """

    def enter_destination(self, destination = None):
        search_bar = self.find_element_by_id('ss')
        search_bar.clear()
        search_bar.send_keys(destination)
        destination_element = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        destination_element.click()

    def dates_of_trip(self, check_in, check_out):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]'
        )
        check_out_element.click()

    def number_of_adults(self, count):
        list_element = self.find_element_by_id("xp__guests__toggle")
        list_element.click()
        if(count == 1):
            decrease_count_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_count_element.click()
        else:
            increase_count_element = self.find_element_by_css_selector(
                'button[aria-label="Increase number of Adults"]'
            )
            for i in range(count - 2):
                increase_count_element.click()

    
    def number_of_children(self, count):
        list_element = self.find_element_by_id("xp__guests__toggle")
        list_element.click()
        increase_count_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Children"]'
        )
        for i in range(count):
            increase_count_element.click()
            print(f'{i+1}')
            select_age_element = self.find_element_by_css_selector(
                f'select[aria-label="Child {i+1} age"]'
            )
            select_age_element.click()
            time.sleep(3)
            age_element = self.find_element_by_css_selector(
                'option[value="6"]'
            )
            age_element.click()
        

    
    def number_of_rooms(self, count):
        list_element = self.find_element_by_id("xp__guests__toggle")
        list_element.click()
        increase_count_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Rooms"]'
        )
        for i in range(count - 1):
            increase_count_element.click()
            
         






