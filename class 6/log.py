import logging

# Налаштування логування
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Створення повідомлень різних рівнів
logging.debug("Це повідомлення DEBUG")
logging.info("Це повідомлення INFO")
logging.warning("Це повідомлення WARNING")
logging.error("Це повідомлення ERROR")
logging.critical("Це повідомлення CRITICAL")