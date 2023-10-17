# How to install mysql 5.7 on ubuntu
https://www.devart.com/dbforge/mysql/how-to-install-mysql-on-ubuntu/


# List Users

`SELECT user, host FROM mysql.user;`

# New user for the replica server.

-- Create the replica_user with the specified password
`CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_password';`

-- Grant the necessary privileges to replica_user for replication
`GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';`

-- Grant SELECT privileges on the mysql.user table to holberton_user
`GRANT SELECT ON mysql.user TO 'holberton_user'@'%';`

-- Flush privileges to apply the changes
`FLUSH PRIVILEGES;`

# These SQL commands do the following:

1. Create the replica_user with a specified password.
2. Grant the REPLICATION SLAVE privilege to replica_user. This privilege is necessary for replication.
3. Grant the SELECT privilege on the mysql.user table to holberton_user. This allows holberton_user to check that replica_user was created with the correct permissions.
4. Flush privileges to apply the changes.