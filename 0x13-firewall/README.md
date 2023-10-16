`sudo apt-get install ufw`

This command installs the UFW (Uncomplicated Firewall) package on your Linux system. UFW provides a simplified and user-friendly interface for managing firewall rules.

`sudo ufw default deny incoming -y`

This command sets the default incoming policy to "deny." It means that by default, all incoming traffic to your system is blocked. The -y flag is used to automatically confirm the change without user interaction.

`sudo ufw default allow outgoing -y`

This command sets the default outgoing policy to "allow." It means that your system is allowed to initiate outgoing connections to other hosts on the network or the internet. The -y flag again confirms this change without user interaction.

`sudo ufw allow 22/tcp`

This command allows incoming traffic on port 22 for the TCP protocol. Port 22 is commonly used for SSH (Secure Shell) connections, which is necessary for remote access to the system.

`sudo ufw allow 443/tcp`

This command allows incoming traffic on port 443 for the TCP protocol. Port 443 is commonly used for HTTPS, which is essential for secure web browsing and communication.


`sudo ufw allow 80/tcp`

This command allows incoming traffic on port 80 for the TCP protocol. Port 80 is typically used for HTTP, which is the standard protocol for unencrypted web traffic.


`sudo ufw enable`

This command activates the UFW firewall with the rules you've configured. After running this command, the firewall will be actively filtering network traffic according to the defined rules.


`sudo ufw status`

This command checks and displays the status of the UFW firewall. It will show you a list of rules that are currently in effect and indicate whether the firewall is active or not.
