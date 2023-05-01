from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class StockInfo(object):

    def __init__(self):
        # Create an instance of the Options class and store it as a private member variable
        self.__options = Options()
        # Add a command line argument to make the Firefox browser run in headless mode
        self.__options.add_argument('--headless')
        # Create an instance of the Firefox webdriver and store it as a private member variable
        # Also pass in the previously created Options object and set the service_log_path to os.devnull
        self.__driver = webdriver.Firefox(
            options=self.__options,
            service_log_path=os.devnull
        )

    def __ticker_is_valid(self, ticker):
        # Use the Firefox webdriver to navigate to a specific URL built with the 'ticker' parameter
        self.__driver.get(f'https://statusinvest.com.br/acoes/{ticker}')

        # Use WebDriverWait to wait up to 3 seconds for a specific element to appear
        # If the element appears, return False. Otherwise, return True
        try:
            WebDriverWait(self.__driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="main-2"]/section/div/h1/span'))
            )
            return False
        except:
            return True

    def __get_company_name(self):
        # Use WebDriverWait to wait up to 10 seconds for a specific element to appear
        # If the element appears, return its text. Otherwise, return None
        try:
            company_name = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/main/header/div[2]/div/div[1]/h1/small'))
            )
            return company_name.text
        except:
            return None

    def __scroll_until_down(self):
        # Execute JavaScript to scroll down until the end of the page
        page_len = self.__driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
            "var lenOfPage=document.body.scrollHeight;"
            "return lenOfPage;"
        )
        # Check if the whole page has been scrolled through
        match = False
        while match is False:
            last_count = page_len
            page_len = self.__driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
                "var lenOfPage=document.body.scrollHeight;"
                "return lenOfPage;"
            )
            if last_count == page_len:
                # Stop scrolling if the current page length is equal to the last page length
                match = True

    def __click_expand_buttons(self):
        # List of buttons to click in order to expand elements on the page
        buttons_to_click = ['//*[@id="main-2"]/div[8]/div/div/div[2]/div[2]/button',
                            '//*[@id="contabil-section"]/div[1]/div/div[3]/div[2]/div[1]/button',
                            '//*[@id="contabil-section"]/div[1]/div/div[2]/div[2]/div[1]/button',
                            '//*[@id="company-section"]/div[4]/div/div[2]/button']
        for button_expand in buttons_to_click:
            try:
                # Wait for the button to be visible and click it
                button = WebDriverWait(self.__driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, button_expand))
                )
                button.click()
            except:
                pass

    def __get_about_data(self):
        try:
            # Wait for the about section to be visible and retrieve the text of all <p> elements
            about = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[5]/div[4]/div/div[1]/div'))
            )
            return ' '.join([about_p.text for about_p in about.find_elements(By.XPATH, './/p')])
        except:
            return None

    def __get_table_dict(self, table_headers_xpath, table_xpath, header_len):
        try:
            data = []
            data_cleaned = []

            # Wait for table headers to be visible and extract their text
            table_headers = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, table_headers_xpath))
            )
            extracted_headers = [th_element.text for th_element in table_headers.find_elements(By.XPATH, './/th')]

            headers = ["Nome"]  # Default headers list starts with "Nome"

            # Process each extracted header text
            for head in extracted_headers:
                if head.isnumeric() and len(head) == 4:  # Check if header is a 4-digit number
                    headers.append(head)
                elif '\n' in head:  # Check if header contains a line break character
                    head_clean = head.replace('\n', ' ')  # Replace line break with space character
                    headers.append(head_clean)

            # Wait for table to be visible and extract its text
            tb = WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, table_xpath))
            )
            for tr_element in tb.find_elements(By.XPATH, './/tr'):
                data.append(tr_element.text)

            # Process each line of extracted table data
            for line in data:
                cleaned = []

                # Split line into columns and remove unwanted columns
                for column in line.split("\n"):
                    record = True

                    if column == 'format_quote':
                        record = False
                    if column == 'show_chart':
                        record = False
                    if '%' in column:
                        record = False
                    if record:
                        cleaned.append(column)

                # Process each value in the cleaned line
                for x, i in enumerate(cleaned[1:len(cleaned)]):
                    # Remove unwanted characters from value
                    cleaned[x + 1] = i.replace('M', '').replace('.', '').replace(',', '.')

                # Add cleaned line to data_cleaned list
                data_cleaned.append(cleaned)

            extracted_dict = {}

            # Create a dictionary for each line with at least header_len number of columns
            for i, res_line in enumerate([lst for lst in data_cleaned if len(lst) >= header_len]):
                if res_line == []:
                    continue

                dict_res_line = {}

                # Add each value in the line to the corresponding header key in the dictionary
                for j, valor in enumerate(res_line[1:]):
                    dict_res_line[headers[j + 1]] = valor.strip()

                # Add dictionary to extracted_dict with "Nome" value as the key
                extracted_dict[res_line[0]] = dict_res_line

            return extracted_dict
        except:
            return None

    def gather_info_by_ticker(self, ticker):
        # Initialize a dictionary to store data
        data = {'ticker': ticker,
                'error_in_selenium_driver': False,
                'ticker_is_valid': None,
                'company_name': None,
                'about': None,
                'result': None,
                'cashflow': None,
                'balancesheet': None}

        try:
            # Check if the ticker is valid
            if not self.__ticker_is_valid(ticker):
                data['ticker_is_valid'] = False
                self.__driver.quit()
                return data
            else:
                data['ticker_is_valid'] = True

            # Get the company name
            data['company_name'] = self.__get_company_name()

            # Scroll the page until the bottom
            self.__scroll_until_down()

            # Click the "expand" buttons to show more data
            self.__click_expand_buttons()

            # Get the "about" data of the company
            data['about'] = self.__get_about_data()

            # Get the financial results data
            data['result'] = self.__get_table_dict(
                table_headers_xpath='/html/body/main/div[7]/div[1]/div/div[2]/div[1]/div/table/thead/tr',
                table_xpath='/html/body/main/div[7]/div[1]/div/div[2]/div[1]/div/table/tbody',
                header_len=7
            )

            # Get the cashflow data
            data['cashflow'] = self.__get_table_dict(
                table_headers_xpath='//*[@id="contabil-section"]/div[1]/div/div[3]/div[1]/div[1]/table/thead/tr',
                table_xpath='//*[@id="contabil-section"]/div[1]/div/div[3]/div[1]/div[1]/table/tbody',
                header_len=6
            )

            # Get the balance sheet data
            data['balancesheet'] = self.__get_table_dict(
                table_headers_xpath='//*[@id="main-2"]/div[8]/div/div/div[2]/div[1]/div/table/thead/tr',
                table_xpath='//*[@id="main-2"]/div[8]/div/div/div[2]/div[1]/div/table/tbody',
                header_len=6
            )

            # Quit the selenium driver
            self.__driver.quit()

            # Return the data dictionary
            return data

        except:
            # If there is an error in the selenium driver, set the flag in the dictionary and return it
            data['error_in_selenium_driver'] = True
            return data
