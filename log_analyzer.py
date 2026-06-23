error_count = 0
warning_count = 0
failed_login_count = 0

with open("sample_log.txt", "r") as file:
    logs = file.readlines()

for log in logs:

    if "ERROR" in log:
        error_count += 1

    if "WARNING" in log:
        warning_count += 1

    if "Failed login" in log:
        failed_login_count += 1

print("\nSecurity Log Analysis Report")
print("-" * 35)

print(f"Total Errors: {error_count}")
print(f"Total Warnings: {warning_count}")
print(f"Failed Login Attempts: {failed_login_count}")

print("\nRisk Assessment")

if failed_login_count >= 3:
    print("⚠️ Multiple failed login attempts detected")

if error_count >= 2:
    print("⚠️ Critical system errors detected")

print("\nAnalysis Completed")
