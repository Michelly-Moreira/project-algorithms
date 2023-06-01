def stratification_range(period, range_time):
    for hour in range(period[0], period[1]+1):
        range_time.append(hour)
    return range_time


def study_schedule(permanence_period, target_time):
    range_time = []
    for period in permanence_period:
        # print(isinstance(period[0] , int))
        # print(isinstance(period[1] , int))
        # print(not(target_time))
        if (type(period[0]) != int or type(period[1]) != int or not(target_time)):
            return None
        else: stratification_range(period, range_time)
    return range_time.count(target_time)
    # raise NotImplementedError

# permanence_period = [(2,2), (1,2), (2,3), (1,5), (4,5)]
# target_time = []
# print(study_schedule(permanence_period, target_time))