import re
import pandas as pd

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    # df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    # df['user'] = users
    # df['message'] = messages
    # df.drop(columns=['user_message'], inplace=True)
    
    # df['only_date'] = df['message'].dt.date
    # df['year'] = df['message'].dt.year
    # df['month_num'] = df['message_date'].dt.month
    # df['month'] = df['message_date'].dt.month_name()
    # df['day'] = df['message_date'].dt.day
    # df['day_name'] = df['message_date'].dt.day_name()
    # df['hour'] = df['message_date'].dt.hour
    # df['minute'] = df['message_date'].dt.minute

    return df