from test_app.models import Durations


def filtered_time_query_set():
    db_set = {
        'query': lambda instance: Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query(instance),
        'hour': lambda instance: Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query_without_hour(instance),
        'day': lambda instance: Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query_without_day(instance),
        'month': lambda instance: Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query_without_month(instance),
        'year': lambda instance: Durations.filters_manager.select_related(
            'client', 'mode', 'equipment'
        ).db_query_without_year(instance),
    }
    return db_set


class CheckQuerySet:
    def __init__(self, query, key):
        self.query = query
        self.key = key

    def __result_to_output_all_data(self):
        result = ''
        for i in self.query:
            result += (
                f'Client: {i.client} '
                f'| Equipment: {i.equipment} '
                f'| Mode: {i.mode} '
                f'| Minutes: {i.minutes} '
                f'| Start: {i.start.strftime("%m/%d/%Y, %H")} '
                f'| Stop: {i.stop.strftime("%m/%d/%Y, %H")}<br> '
            )
        return result

    def __result_to_output_without_year(self):
        result = ''
        for i in self.query:
            result += (
                f'Client: {i.client} | Equipment: {i.equipment} | Mode: {i.mode} '
                f'| Minutes: {i.minutes} '
                f'| Start: No data No data No data  No data '
                f'| Stop: No data No data No data No data <br> '
            )
        return result

    def __result_to_output_without_month(self):
        result = ''
        for i in self.query:
            result += (
                f'Client: {i.client} | Equipment: {i.equipment} | Mode: {i.mode} '
                f'| Minutes: {i.minutes} '
                f'| Start: {i.start.strftime("%Y")} No data No data  No data '
                f'| Stop: {i.stop.strftime("%Y")} No data No data  No data <br> '
            )
        return result

    def __result_to_output_without_day(self):
        result = ''
        for i in self.query:
            result += (
                f'Client: {i.client} | Equipment: {i.equipment} | Mode: {i.mode} '
                f'| Minutes: {i.minutes} '
                f'| Start: {i.start.strftime("%m/%Y")} No data  No data '
                f'| Stop: {i.stop.strftime("%m/%Y")} No data  No data <br> '
            )
        return result

    def __result_to_output_without_hour(self):
        result = ''
        for i in self.query:
            result += (
                f'Client: {i.client} | Equipment: {i.equipment} | Mode: {i.mode} '
                f'| Minutes: {i.minutes} '
                f'| Start: {i.start.strftime("%m/%d/%Y")}  No data '
                f'| Stop: {i.stop.strftime("%m/%d/%Y")}  No data <br> '
            )
        return result

    def get_output(self):
        if self.key == 'query':
            return self.__result_to_output_all_data()
        elif self.key == 'hour':
            return self.__result_to_output_without_hour()
        elif self.key == 'day':
            return self.__result_to_output_without_day()
        elif self.key == 'month':
            return self.__result_to_output_without_month()
        else:
            return self.__result_to_output_without_year()
