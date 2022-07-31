def result_to_output_all_data(query):
    result = ''
    for i in query:
        result += (
            f'Client: {i.client} '
            f'| Equipment: {i.equipment} '
            f'| Mode: {i.mode} '
            f'| Minutes: {i.minutes} '
            f'| Start: {i.start.strftime("%m/%d/%Y, %H")} '
            f'| Stop: {i.stop.strftime("%m/%d/%Y, %H")}<br> '
        )
    return result


def result_to_output_without_day(query):
    result = ''
    for i in query:
        result += (
            f'Client: {i.client} | Equipment: {i.equipment} | Mode: {i.mode} '
            f'| Minutes: {i.minutes} '
            f'| Start: {i.start.strftime("%m/%Y")} No data  No data '
            f'| Stop: {i.stop.strftime("%m/%Y")} No data  No data <br> '
        )
    return result


def result_to_output_without_hour(query):
    result = ''
    for i in query:
        result += (
            f'Client: {i.client} | Equipment: {i.equipment} | Mode: {i.mode} '
            f'| Minutes: {i.minutes} '
            f'| Start: {i.start.strftime("%m/%d/%Y")}  No data '
            f'| Stop: {i.stop.strftime("%m/%d/%Y")}  No data <br> '
        )
    return result
