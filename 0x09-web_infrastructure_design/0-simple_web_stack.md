# Description
This is a simple web infrastructure that hosts a website that is reachable via www.foobar.com
the website is hosted on a single server that contains the database and application server

# Specifics About This Infrastructure
* What is a server: A server is a computer or software system that provides services or resources to other computers, known as clients, over a network. Servers handle requests and deliver data or perform specific tasks, such as hosting websites or storing files.
* What is the role of the domain name: The role of a domain name is to provide a human-readable and memorable address for resources on the internet, like websites or email servers.
* What type of DNS record www is in www.foobar.com: The "www" in "www.foobar.com" is typically a CNAME (Canonical Name) DNS record that points to the actual hostname or domain where the website content is hosted.
* What is the role of the web server: A web server is responsible for delivering web content (e.g., HTML pages, images, files) to users' web browsers in response to HTTP requests. It processes these requests and sends back the appropriate web pages.
* What is the role of the application server: An application server is responsible for running software applications and handling application-specific tasks. It often processes business logic, communicates with databases, and generates dynamic content for web applications.
* What is the role of the database: A database stores and manages structured data. In web applications, it's used to store, retrieve, and manage data such as user information, product details, or content. Application servers interact with databases to read and update data dynamically.
* What is the server using to communicate with the computer of the user requesting the website: The server typically uses the HTTP (Hypertext Transfer Protocol) to communicate with the user's computer when the user requests a website. HTTP is the foundation of data communication on the World Wide Web, allowing the transfer of web pages and other resources between the server and the user's web browser.

# Issues With This Infrastructure
* There are multiple SPOF (Single Point Of Failure) in this infrastructure.
For example, if the MySQL database server is down, the entire site would be down.
* Downtime and Failures: Hardware failures, software crashes, or misconfigurations can lead to downtime. Implementing effective backup and disaster recovery strategies is crucial.
* Scalability Challenges: LAMP stacks can face difficulties when scaling horizontally (adding more servers) due to limitations in database replication, load balancing, and session management.
* 

