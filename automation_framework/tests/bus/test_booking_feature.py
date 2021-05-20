import pytest
from automation_framework.modules.bus.bus_booking_page import BusBooking
from time import sleep
import logging

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("RedBusSetup")
class TestBusBooking:
    log.info("___________TestBusBooking_________")
    def test_book_bus_and_verify(self):
        log.info("test case : test_book_bus_and_verify : start")
        bus_page = BusBooking(self.driver)
        bus_page.select_source()
        sleep(5)
        log.info("test case : test_book_bus_and_verify : finish")