import json
import pyodbc
import re
from datetime import datetime, timezone


def parse_messages(file_path):
    messages = []
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(r'\[INF\] Received message from topic /merakimv/.*/custom_analytics', line):
                json_str_match = re.search(r'\{.*\}', line)  # Using regex to extract JSON string
                if json_str_match:
                    json_str = json_str_match.group(0)
                    data= json.loads(json_str)

                    parts = line.split()
                    unixepoch = data.get('timestamp')
                    dt_object = datetime.fromtimestamp(unixepoch / 1000.0, tz=timezone.utc)
                    timestamp = dt_object.strftime("%Y-%m-%d %H:%M:%S.%f") + "Z"
                    topic_parts = parts[8].split('/')
                    camera_serial = topic_parts[-2] if len(topic_parts) >= 3 else "Unknown"

                    outputs = data.get('outputs', [])
                    messages.append({"UnixEpoch": unixepoch, "Timestamp": timestamp ,"CameraSerial": camera_serial, "Outputs": outputs})
    return messages


def insert_messages(messages, connection_string):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    for message in messages:
        for output in message['Outputs']:
            cursor.execute("INSERT INTO Detection (UnixEpoch, Timestamp, CameraSerial, Class, BoundingBoxLeft, BoundingBoxTop, BoundingBoxRight, BoundingBoxBottom, Score, InferenceId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",message['UnixEpoch'], message['Timestamp'],message['CameraSerial'], int(output['class']), output['location'][0], output['location'][1], output['location'][2], output['location'][3], float(output['score']), int(output['id']))

    conn.commit()
    conn.close()

def main():
    connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\\local2;DATABASE=Nexturn_CE;Trusted_Connection=yes;'
    messages = parse_messages('logs/log-20240421.txt')

    insert_messages(messages, connection_string)

if __name__ == "__main__":
    main()
