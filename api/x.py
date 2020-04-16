from sources.src.execution_tools.driver_pool import DriverPool

driver = DriverPool().create_driver()
driver.get('https://google.com')
