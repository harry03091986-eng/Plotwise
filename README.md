##############################
Usage

pytest -v Delivery_Validation.py

##############################
Dependencies

External Libraries list:
pip3 install requests
pip3 install pytest
pip3 install assertpy
pip3 install pyyaml

##############################
Folder Structure:

./data --> Folder contains the "Deliveries for Planning" file

./input --> contains "input.yaml" file with "for_planning" and "planned_route_api" variables
        [planned_route_api --> Mock API Hosted on "https://my-json-server.typicode.com/harry03091986-eng/planned_route/planned_route"]
        [for_planning --> Location of the file "Deliveries for Planning"]

./lib --> Folder contains the Data Validation library

##############################

Example Output

blr-mp712:Plotwise hfernand$ pytest -v Delivery_Validation.py
======================================================================================= test session starts ========================================================================================
platform darwin -- Python 3.8.5, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /usr/local/opt/python@3.8/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/hfernand/Desktop/Plotwise
plugins: Faker-5.6.1, allure-pytest-2.8.31, asyncio-0.14.0, mock-3.5.1
collected 13 items

Delivery_Validation.py::test_planning_deliveries[482ddef5-7c9c-4253-8c7c-2a18b49ba8be] PASSED                                                                                                [  7%]
Delivery_Validation.py::test_planning_deliveries[60adbe31-d693-4dd7-8368-94545be514de] PASSED                                                                                                [ 15%]
Delivery_Validation.py::test_planning_deliveries[a69db991-0e76-4377-868a-9c428dbaf7b1] PASSED                                                                                                [ 23%]
Delivery_Validation.py::test_weight_less_than_capacity PASSED                                                                                                                                [ 30%]
Delivery_Validation.py::test_delivery_time_range[id_eta_time_range0] PASSED                                                                                                                  [ 38%]
Delivery_Validation.py::test_delivery_time_range[id_eta_time_range1] PASSED                                                                                                                  [ 46%]
Delivery_Validation.py::test_delivery_time_range[id_eta_time_range2] FAILED                                                                                                                  [ 53%]
Delivery_Validation.py::test_delivery_time_range[id_eta_time_range3] PASSED                                                                                                                  [ 61%]
Delivery_Validation.py::test_delivery_time_range[id_eta_time_range4] PASSED                                                                                                                  [ 69%]
Delivery_Validation.py::test_time_to_next_consecutive_difference[2017-11-13T07:00:00.000000Z-917-2017-11-13T08:00:17.000000Z] PASSED                                                         [ 76%]
Delivery_Validation.py::test_time_to_next_consecutive_difference[2017-11-13T08:00:17.000000Z-1971-2017-11-13T08:53:08.000000Z] PASSED                                                        [ 84%]
Delivery_Validation.py::test_time_to_next_consecutive_difference[2017-11-13T08:53:08.000000Z-0-2017-11-13T09:05:08.000000Z] PASSED                                                           [ 92%]
Delivery_Validation.py::test_time_to_next_consecutive_difference[2017-11-13T09:05:08.000000Z-3006-2017-11-13T10:30:20.000000Z] PASSED                                                        [100%]

============================================================================================= FAILURES =============================================================================================
___________________________________________________________________________ test_delivery_time_range[id_eta_time_range2] ___________________________________________________________________________

id_eta_time_range = {'60adbe31-d693-4dd7-8368-94545be514de': ['2017-11-13T08:53:08.000000Z', '2017-11-13T07:30:00.000000Z', '2017-11-13T08:30:00.000000Z']}

    @pytest.mark.parametrize("id_eta_time_range",id_eta_time_range_dict)
    def test_delivery_time_range(id_eta_time_range):
>       assert_that(data_validator.validate_eta_time_range(id_eta_time_range)).is_true()
E       AssertionError: Expected <True>, but was not.

Delivery_Validation.py:88: AssertionError
===================================================================================== short test summary info ======================================================================================
FAILED Delivery_Validation.py::test_delivery_time_range[id_eta_time_range2] - AssertionError: Expected <True>, but was not.
=================================================================================== 1 failed, 12 passed in 1.46s ===================================================================================

##############################