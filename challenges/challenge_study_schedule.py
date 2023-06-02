def study_schedule(permanence_period, target_time):
    numbers_students = 0
    # print('target time =', target_time)
    for entry, exit in permanence_period:
        # print(entry, ' ', target_time >= entry )
        # print(exit, ' ', target_time <= exit)
        if (type(entry) != int or
                type(exit) != int or
                not target_time):
            return None
        #elif target_time >= entry and target_time <= exit:
        elif entry <= target_time <= exit:
            numbers_students += 1
    return numbers_students

    # raise NotImplementedError
# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5))
