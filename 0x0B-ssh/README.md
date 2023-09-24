

#  What is a server?
A server is a computer or software system that provides services, resources, or data to other computers or clients on a network. Servers are designed to be always available and highly reliable, serving requests from multiple clients simultaneously. They can be used for various purposes, such as hosting websites, managing databases, providing email services, and more.

# SSH (Secure Shell)
SSH, which stands for Secure Shell, is a cryptographic network protocol used to securely connect to and manage remote servers over a potentially unsecured network. It provides a secure channel for authentication and data transfer, ensuring confidentiality and integrity of the communication. SSH is commonly used for remote administration, file transfers, and tunneling network connections.

# How to create an SSH RSA key pair?

`ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`

This command generates a 4096-bit RSA key pair and associates it with your email address.

# How to connect to a remote host using an SSH RSA key pair
1. Ensure that you have the public key (id_rsa.pub) in your ~/.ssh directory.
2. Use the ssh command to connect to the remote host. Replace `username` with your remote username and `hostname` with the remote server's address
`ssh username@hostname` If your private key is stored in the default location (~/.ssh/id_rsa), SSH will automatically use it for authentication.

* using #!/usr/bin/env bash is a more flexible and portable way to specify the interpreter for your Bash scripts, ensuring they work reliably across various environments.

