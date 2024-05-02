
# Initialize variables to store total time and count for POST and GET requests
total_post_time = 0
total_get_time = 0
post_count = 0
get_count = 0

# Open the text file
with open("a.txt", "r") as file:
    # Iterate over each line in the file
    for line in file:
        # Split the line to extract request type and time
        parts = line.split()
        if len(parts) == 6:  # Ensure it's a valid line with request information
            request_type = parts[0]
            time_taken = int(parts[4])  # Extract the time taken

            # Update total time and count based on request type
            if request_type == "POST":
                total_post_time += time_taken
                post_count += 1
            elif request_type == "GET":
                total_get_time += time_taken
                get_count += 1

# Calculate average time for POST and GET requests
avg_post_time = total_post_time / post_count if post_count > 0 else 0
avg_get_time = total_get_time / get_count if get_count > 0 else 0

# Print the results
print("Average time taken", post_count, "by POST requests:", avg_post_time, "ms" )
print("Average time taken", get_count, "by GET requests:", avg_get_time, "ms")




























# import os
# import pandas as pd
# import requests
# from datetime import datetime
# import time

# def send_post_request(device_id, timestamp, bearer_token):
#     url = f"https://api.meraki.com/api/v1/devices/{device_id}/camera/generateSnapshot"
#     headers = {"Authorization": f"Bearer {bearer_token}"}
#     payload = {
#         "timestamp": datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z',
#         "fullframe": "false"
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     if response.status_code == 200:
#         return response.json()['url']
#     else:
#         return None

# def send_get_request(url, bearer_token):
#     headers = {"Authorization": f"Bearer {bearer_token}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return True
#     else:
#         return False

# def process_excel_file(file_path, bearer_token):
#     df = pd.read_csv(file_path, header=None)
#     total_rows = len(df)
#     total_post_time = 0
#     total_get_time = 0
#     num_failures = 0

#     for index, row in df.iterrows():
#         timestamp = row[8]
#         start_time_post = time.time_ns()
#         url = send_post_request(row[0], timestamp, bearer_token)
#         end_time_post = time.time_ns()

#         if url:
#             start_time_get = time.time_ns()
#             success = send_get_request(url, bearer_token)
#             end_time_get = time.time_ns()
#             if success:
#                 total_get_time += end_time_get - start_time_get
#             else:
#                 num_failures += 1
 
#             total_post_time += end_time_post - start_time_post
#         else:
#             num_failures += 1

#     return total_rows, total_post_time, total_get_time, num_failures

# def main():
#     excel_folder = "Excel"
#     output_file = "results.xlsx"
#     bearer_token = "aa590dd9f73fc83ea5c88072aa7835e431fba4c5"

#     for file_name in os.listdir(excel_folder):
#         if file_name.endswith(".csv"):
#             file_path = os.path.join(excel_folder, file_name)
#             total_rows, post_time, get_time, failure = process_excel_file(file_path, bearer_token)
#             avg_post_time = post_time / total_rows
#             avg_get_time = get_time / total_rows

#             print(" File Name ", file_name," Total Rows ", total_rows," Average Post Time ", avg_post_time," Average Get Time ", avg_get_time," Total Failures ", failure)
#             # Write results to output excel file
#             # df = pd.DataFrame({
#             #     "File Name": [file_name],
#             #     "Total Rows": [total_rows],
#             #     "Average Post Time": [avg_post_time],
#             #     "Average Get Time": [avg_get_time],
#             #     "Total Failures": [failure]
#             # })
#             # if os.path.exists(output_file):
#             #     df.to_excel(output_file, index=False, header=False, mode='a')
#             # else:
#             #     df.to_excel(output_file, index=False)



# if __name__ == "__main__":
#     main()


















