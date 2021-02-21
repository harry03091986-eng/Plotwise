import json

import pytest
import requests
import yaml
from assertpy import assert_that
from requests.exceptions import HTTPError

from lib.Data_Validator import Data_Validator

# Take Input values from the 'input.yaml' file
with open('input/input.yaml') as file:
    input_vars = yaml.load(file, Loader=yaml.FullLoader)
    for_planning = input_vars['for_planning']
    planned_route_api = input_vars['planned_route_api']

# Read from the file and load the json object
with open(for_planning) as fp:
    for_planning_json = json.load(fp)

# Setup the JSON Server at https://my-json-server.typicode.com/harry03091986-eng/planned_route/planned_route
try:
    response = requests.get(planned_route_api)
    response.raise_for_status()

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6

except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6

else:
    planned_route_json = response.json()

#### Initialization of Class ####

data_validator = Data_Validator(for_planning_json, planned_route_json)

#### Initialization of Class Object####

################################################################################
#################### TEST CASES ####################
################################################################################

################################################################################
'''TestCase #1:
All deliveries from “deliveries_for_planning.json” that are in current_state
“planned” are present in “planned_route.json'''

parameters = [delivery['id'] for delivery in for_planning_json if delivery['current_state'] == "planned"]

@pytest.mark.parametrize("delivery_id",parameters)
def test_planning_deliveries(delivery_id):
    assert_that(data_validator.validate_for_planning_in_planned(delivery_id)).is_true()

################################################################################

'''TestCase #2
The sum of weights of the deliveries is less than the carrying_capacity of the
vehicle
'''
def test_weight_less_than_capacity():
    assert_that(data_validator.validate_weight_less_than_capacity()).is_true()

################################################################################

'''TestCase #3
All eta-s of deliveries in planning (estimated time of arrivals) with “type”
delivery are within the route_min_time and route_max_time'''
# all_deliveries variable can be re-used in the next test case
all_deliveries = planned_route_json['deliveries']

id_time_range_dict = [{delivery["id"]: [delivery["min_time"], delivery["max_time"]]} for delivery in all_deliveries if delivery['algorithm_fields']["type"] == "delivery"]

@pytest.mark.parametrize("id_time_range",id_time_range_dict)
def test_delivery_time_range(id_time_range):
    assert_that(data_validator.validate_delivery_time_range(id_time_range)).is_true()

################################################################################

'''TestCase #4
All eta-s of deliveries in planning are within their delivery_min_time and
delivery_max_time'''

id_eta_time_range_dict = [{delivery["id"]:[delivery["algorithm_fields"]["eta"], delivery["min_time"], delivery["max_time"]]} for delivery in all_deliveries]

@pytest.mark.parametrize("id_eta_time_range",id_eta_time_range_dict)
def test_delivery_time_range(id_eta_time_range):
    assert_that(data_validator.validate_eta_time_range(id_eta_time_range)).is_true()

################################################################################

'''TestCase #5
The travel_time_to next (in seconds) is less than or equal to the time
difference between any 2 consecutive deliveries in “planned_route.json”'''

id_eta_time_range_tuple = []

for index in range(len(all_deliveries)-1):
    id_eta_time_range_tuple.append((all_deliveries[index]["algorithm_fields"]["eta"],
                                   all_deliveries[index]["algorithm_fields"]["time_to_next"],
                                   all_deliveries[index + 1]["algorithm_fields"]["eta"]))

@pytest.mark.parametrize("current_eta, time_to_next, next_eta", id_eta_time_range_tuple)
def test_time_to_next_consecutive_difference(current_eta, time_to_next, next_eta):
    assert_that(data_validator.validate_time_to_next_consecutive_difference(current_eta, time_to_next, next_eta)).is_true()

################################################################################