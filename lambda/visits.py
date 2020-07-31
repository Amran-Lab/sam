def get_visits(event):
    for key,value in event['Items'][0].items():
        if key == 'Visit':
            Visits = int(value)
            
    Hit = Visits + 1
    return Hit