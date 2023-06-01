def stratification_range(period, range_time):
    for hour in range(period[0], period[1]+1):
        range_time.append(hour)
    return range_time


def study_schedule(permanence_period, target_time):
    range_time = []
    for period in permanence_period:
        if (type(period[0]) != int or
                type(period[1]) != int or
                not target_time):
            return None
        else:
            stratification_range(period, range_time)
    return range_time.count(target_time)

    # raise NotImplementedError
