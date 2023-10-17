# Bash script to configure and run Nginx as Nginx

#!/usr/bin/env bash:
This line is called a shebang and tells the system to execute the script using the Bash shell.

`pkill apache2`

This line kills (terminates) any running Apache web server processes (apache2). It ensures that Apache is stopped before attempting to start Nginx. However, it's important to note that forcefully killing processes like this can be disruptive and might not be the best approach, especially in a production environment.

`chown nginx:nginx /etc/nginx/nginx.conf`

This line changes the ownership of the Nginx configuration file (/etc/nginx/nginx.conf) to the nginx user and group. This is done to ensure that the Nginx process, which will run as the nginx user, can read and modify its configuration.

`chmod 777 /etc/nginx/nginx.conf`

This line changes the permissions of the Nginx configuration file to allow read, write, and execute permissions for everyone. Setting the file permissions to 777 is generally not recommended from a security perspective because it allows full access to the file by anyone. It's better to use more restrictive permissions, depending on your needs and security considerations.

`sed -i 's/80/8080/g' /etc/nginx/sites-available/default`

This line uses the sed command to perform a search and replace operation on the Nginx configuration file located at /etc/nginx/sites-available/default. It looks for instances of "80" (presumably, the default HTTP port) and replaces them with "8080". This changes the default port Nginx listens on from 80 to 8080.

`sudo -u nginx service nginx start`

This line starts the Nginx service (nginx) as the nginx user. The sudo -u nginx part is used to run the service command as the nginx user. It starts the Nginx service with the new configuration.
