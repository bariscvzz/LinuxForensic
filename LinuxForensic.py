import paramiko

def collect_forensic_data(ip, username, password):
    ssh= paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=username, password=password)
        print("Succesfully connected to the remote host")
    except Exception as e:
        print(f"Failed to connect to the remote host due to {e}")
        return
    
    commands = [
        "cat /etc/passwd",
        "cat /etc/group",
        "cat /etc/sudoers",
        "cat /etc/hosts",
        "cat /var/log/auth.log",
        "cat /var/log/syslog",
        "lastlog",
        "cat /root/.bash_history",
        "history",
        "last -f /var/log/wtmp",
        "last -f /var/log/utmp",
        "lastcomm",
        "ps aux",
        "find / -mtime -1 -ls",
        "ip a",
        "arp -a",
        "netstat -nap"
    ]

    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()

        with open("output.txt","a") as file:
            file.write(f"{command}\n{output}\n")

    ssh.close()
    print("Forensic Data Collection is Completed")

if __name__ == "__main__":
    ip = input("Enter the Server Ip addres: ")
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")

    collect_forensic_data(ip, username, password)