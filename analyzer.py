from collections import defaultdict

log_file = "sample_log.txt"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "failed" in line:
            ip = line.split()[0]
            failed_attempts[ip] += 1

print("IP suspeitos:")

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"{ip} -> {count} tentativas de login falhadas")
