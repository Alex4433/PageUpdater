import os
import sys

sys.path.append("..")
sys.path.append("...")

from PageChecker.main_t import *



def test_corrent_parsions():
    ps = os.getcwd()


    mock = ["/data/1.htm", "/data/2.htm"]




    test_obj = factory_parser("pickabu", "test", "", mock=mock)
    a = test_obj.request()
    test_obj.get_posts()
    print(test_obj.data)

test_corrent_parsions()
