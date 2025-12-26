from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def main():
    """Открывает сайт itcareerhub.de/ru, переходит в раздел
    'Способы оплаты' и делает скриншот этой секции."""

    # Запускаем Firefox через WebDriverManager
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    try:
        driver.maximize_window()

        # 1. Открываем сайт
        driver.get("https://itcareerhub.de/ru")
        sleep(3)  # даём странице прогрузиться

        # 2. Переходим в раздел "Способы оплаты"
        payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
        payment_link.click()
        sleep(3)

        # 3. Ищем секцию способов оплаты и делаем её скриншот
        try:
            section = driver.find_element(By.ID, "payment-methods")
            section.screenshot("payment_methods_section.png")
        except Exception:
            # fallback: скриншот всей страницы
            driver.save_screenshot("payment_methods_section.png")

        sleep(2)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
