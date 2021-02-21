import datetime

class Data_Validator:

    def __init__(self, for_planning_json, planned_route_json):
        self.for_planning_json = for_planning_json
        self.planned_route_json = planned_route_json

    def validate_for_planning_in_planned(self, id_for_planning):
        #id_for_planning == Planning delivery ID
        all_deliveries = self.planned_route_json['deliveries']
        # All Planned Deliveries
        all_planned_delivery_ids = [planned_delivery['id'] for planned_delivery in all_deliveries if planned_delivery['current_state'] == "planned"]

        if id_for_planning in all_planned_delivery_ids:
            return True
        else:
            return False

    def validate_weight_less_than_capacity(self):
        # List of All Deliveries
        all_deliveries = self.planned_route_json['deliveries']
        # Deliveries with Weight
        weight_array = [delivery['algorithm_fields']['weight'] for delivery in all_deliveries if 'weight' in delivery['algorithm_fields'].keys()]

        if sum(weight_array) <= self.planned_route_json['resource']['carrying_capacity']:
            return True
        else:
            return False

    def validate_delivery_time_range(self, id_time_range_dict):
        # Route Min and Max times
        route_min_time = self.planned_route_json["route_min_time"]
        route_max_time = self.planned_route_json["route_max_time"]
        # Delivery Id: [Min_time, Max_time]
        for values in id_time_range_dict.values():
            min_delivery_time, max_delivery_time = values

        if str(min_delivery_time) >= str(route_min_time) and str(max_delivery_time) <= str(route_max_time):
            return True
        else:
            return False

    def validate_eta_time_range(self, id_eta_time_range_dict):
        ## Delivery Id: [Eta, Min_time, Max_time]
        for values in id_eta_time_range_dict.values():
            eta_time, min_delivery_time, max_delivery_time = values

        if str(eta_time) >= str(min_delivery_time) and str(eta_time) <= str(max_delivery_time):
            return True
        else:
            return False


    def validate_time_to_next_consecutive_difference(self, current_eta, time_to_next, next_eta):

        str_current_eta = str(current_eta)
        str_next_eta = str(next_eta)

        current_date_obj = datetime.datetime.strptime(str_current_eta, '%Y-%m-%dT%H:%M:%S.%fZ')
        next_date_obj = datetime.datetime.strptime(str_next_eta, '%Y-%m-%dT%H:%M:%S.%fZ')

        diff_in_seconds_date_object = next_date_obj - current_date_obj

        diff_in_seconds = diff_in_seconds_date_object.seconds

        if time_to_next <= diff_in_seconds:
            return True
        else:
            return False