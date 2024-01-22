from datetime import datetime, timedelta
from collections import Counter

# Read the Given "TestLog.txt" file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()             # Parse using readlines() Function



# collecting all Error messages
def error_messages(log_lines):                 
    all_error = []
    for line in log_lines:
        if "ERROR" in line:
            all_error.append(line.strip())
    return all_error



# Unique Error message with occurences
def unique_error(log_lines):
    unique_errors = {}
    for line in log_lines:
        if "ERROR" in line :
            # the content after the third colon is the Error message
            value = line.split(":")[3].strip()
            if value in unique_errors:
                unique_errors[value] += 1
            else:
                unique_errors[value] = 1
                
    for value, count in unique_errors.items():
        print(f"{value} : {count} Occurrences")



# analyze timestamps
def analyze_timestamps(log_lines):
    timestamps = []
    for line in log_lines:
        if "INFO" in line or "ERROR" in line or "WARN" in line:
            # the first two elements after splitting are the date and time
            timestamp_str = ' '.join(line.split(' ')[0:2])
            timestamps.append(datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S'))

    # To find the seconds between two patterns 
    time_diffs = []
    for i in range(1, len(timestamps)):
        time_diffs.append(timestamps[i] - timestamps[i-1])

    # Analyze time differences for patterns or anomalies
    average_time_diff = sum(time_diffs, timedelta()) / len(time_diffs)
    max_time_diff = max(time_diffs)
    min_time_diff = min(time_diffs)

    print("Average Time Difference Between Consecutive Events:", average_time_diff)
    print("Maximum Time Difference Between Consecutive Events:", max_time_diff)
    print("Minimum Time Difference Between Consecutive Events:", min_time_diff)


#summary of user activities, including the most and least active users.
def summarize_user_activities(log_lines):
    users = [] 
    for line in log_lines:
        if "User" in line:
            users.append(line.split("'")[1])

    user_count = {}
    for user in set(users):  # Using set to get unique users
        user_count[user] = users.count(user)

    sorted_users = sorted(user_count.items(), key=lambda x: x[1])
    min_count = sorted_users[0][1]
    max_count = sorted_users[-1][1]

    # Collecting how many peoples are more active and how many peoples are less active
    least_active_users = []
    most_active_users = [] 
    for user, count in sorted_users:
        if count == min_count:
            least_active_users.append((user,count))
        if count == max_count:
            most_active_users.append((user,count))

    return most_active_users, least_active_users


#Display the results and organized manner
def display_results(log_lines, error_messages, most_active_user, least_active_user):
    print("======== Parse the file and extract information ==========")
    for i in log_lines:
        print(i.strip())

    print("\n======== error messages in the file ==========")
    for i in error_messages:
        print(i.strip())

    print("\n======= Log Analysis Results =========")
    print(f"Total Errors: {len(error_messages)}")
    print("Unique Error Messages:")
    unique_error(log_lines)
    
    
    print("\n========== Timestamp Analysis: =========")
    analyze_timestamps(log_lines)
    
    print("\n========== User Activity Summary: =============")
    print(f"Most Active User: {most_active_user}")
    print(f"Least Active User: {least_active_user} ")


file_path = input("Enter the path where the file is present: ")
try:
    log_lines = read_file(file_path)
    error_messages = error_messages(log_lines)
    most_active_user, least_active_user = summarize_user_activities(log_lines)
    display_results(log_lines, error_messages, most_active_user, least_active_user)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
