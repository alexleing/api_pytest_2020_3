import pytest
import requests
from k7.common_functions import login_fuc,update_info,get_info
import os
'''
:arg scope: the scope for which this fixture is shared, one of
                ``"function"`` (default), ``"class"``, ``"module"``,
                ``"package"`` or ``"session"``.
'''
# @pytest.fixture(scope="session")
# def host():
#     h =  "http://49.235.92.12:6009"
#     return h


def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",action="store",default="http://49.235.92.12:6009",help="whatever"
    )


@pytest.fixture(scope="session", autouse=True)
def host(request):
    # print("获取到命令行参数：{}".format(request.config.option["--cmdhost"]))
    os.environ["host"] = request.config.getoption("--cmdhost")


