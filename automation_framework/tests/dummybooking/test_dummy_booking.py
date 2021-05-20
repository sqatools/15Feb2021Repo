import pytest
from automation_framework.modules.dummy_ticket.dummy_ticket_page import DummyTicket
from automation_framework.data.dummy_ticket_page_data import *
from time import sleep
import logging

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("dummy_setup")
class TestDummyBooking:
    log.info("___________TestDummyBooking________")

    def test_provide_passenger_entry(self):
        log.info("test cases : test_provide_passenger_entry : start")
        global dm
        dm = DummyTicket(self.driver)
        dm.enter_first_name(user_name)
        dm.enter_lastname(last_name)
        log.info("test cases : test_provide_passenger_entry : finish")

    def test_select_date_of_birth_and_other_info(self):
        log.info("test cases : test_select_date_of_birth_and_other_info : start")
        dm.select_dob(dob_month, dob_year)
        dm.select_male_gender()
        sleep(2)
        log.info("test cases : test_select_date_of_birth_and_other_info : finish")

    def test_select_more_passenger(self):
        log.info("test cases : test_select_more_passenger : start")
        dm.select_more_passenger(extra_passenger)
        sleep(5)
        log.info("test cases : test_select_more_passenger : finish")


