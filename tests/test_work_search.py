import logging
import time

import pytest
from selenium.common import NoSuchElementException


def test_work_search(browser, careers_page):
    a = 'DevOps'
    careers_page.open()
    careers_page.search.send_keys(a)
    careers_page.butt_search.click()
    time.sleep(2)

    flag = None
    for i in range(len(careers_page.result_search_name)):
        if a in careers_page.result_search_name[i]:
            flag = True
        else:
            flag = False
            break
    assert id(flag) == id(True)

    time.sleep(2)

    careers_page.search.clear()


def test_2(browser, careers_page):
    careers_page.open()
    careers_page.butt_more.click()
    assert len(careers_page.result_search_name) == 24

    try:
        elem = careers_page.butt_more
        assert False
    except NoSuchElementException:
        ...


def test_3(browser, careers_page):
    a = 'DevOps'
    careers_page.open()
    careers_page.search.send_keys(a)
    careers_page.butt_search.click()
    time.sleep(2)
    a = careers_page.butt_careers.text
    careers_page.butt_careers.click()
    time.sleep(2)
    assert a in careers_page.careers_banner.text
