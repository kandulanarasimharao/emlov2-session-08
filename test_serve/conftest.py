import pytest

my_params = {
    "ServerPublicAddress": "PublicIP",
    "ModelName": "Model",
}


def pytest_addoption(parser):
    for my_param_name, my_param_default in my_params.items():
        parser.addoption(f"--{my_param_name}", action="store", default=my_param_default)

@pytest.fixture()
def pass_parameters(request):
    for my_param in my_params:
        setattr(request.cls, my_param, request.config.getoption(f"--{my_param}"))