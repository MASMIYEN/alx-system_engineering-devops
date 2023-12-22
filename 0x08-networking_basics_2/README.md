
<img src="https://aceworldpub.com.ng/wp-content/uploads/2022/03/unnamed.png" width="200" height="100"> <img src="https://www.svgrepo.com/show/22246/internet.svg" width="200" height="90"> 




# 0x08. Networking basics #1

DevOps Network SysAdmin

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/285/s7kpNYq.png)

## Resources

**Read or watch**:

-   [What is localhost](https://intranet.alxswe.com/rltoken/Odcc_tyAQlcANCCrtmxo6A "What is localhost")
-   [What is 0.0.0.0](https://intranet.alxswe.com/rltoken/fUb9IpnxrNaddMljzwbhJQ "What is 0.0.0.0")
-   [What is the hosts file](https://intranet.alxswe.com/rltoken/4_MBpFTulKliFM69jCPzOQ "What is the hosts file")
-   [Netcat examples](https://intranet.alxswe.com/rltoken/OR0lOEwAw9I1Rj4aGp1Ljg "Netcat examples")

**man or help**:

-   `ifconfig`
-   `telnet`
-   `nc`
-   `cut`


## Learning Objectives
### General

-   What is localhost/127.0.0.1
-   What is 0.0.0.0
-   What is  `/etc/hosts`

#### Question #0

What is  `localhost`?

-   A hostname that means  _this IP_
    
-   A hostname that means  _this computer_ ✔
    
-   An IP attached to a computer
    

#### Question #1

What is  `0.0.0.0`?

-   All IPv4 addresses on the local machine ✔
    
-   All the IPs
    
-   It means null in networking

## Tasks

| Task | File |
| ---- | ---- |
| 0. Change your home IP | [0-change_your_home_IP](./0-change_your_home_IP) |
| 1. Show attached IPs | [1-show_attached_IPs](./1-show_attached_IPs) |
| 2. Port listening on localhost | [100-port_listening_on_localhost](./100-port_listening_on_localhost) |

### 0. Change your home IP

mandatory

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

-   `localhost`  resolves to  `127.0.0.2`
-   `facebook.com`  resolves to  `8.8.8.8`.
-   The checker is running on Docker, so make sure to read  [this](https://intranet.alxswe.com/rltoken/XSXhQPoDu3QecXs3j9XgPQ "this")

Example:

```
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ sudo ./0-change_your_home_IP
sylvain@ubuntu$
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms

```

In this example we can see that:

-   before running the script,  `localhost`  resolves to  `127.0.0.1`  and  `facebook.com`  resolves to  `157.240.11.35`
-   after running the script,  `localhost`  resolves to  `127.0.0.2`  and  `facebook.com`  resolves to  `8.8.8.8`

If you’re running this script on a machine that you’ll continue to use, be sure to revert  `localhost`  to  `127.0.0.1`. Otherwise, a lot of things will stop working!

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x08-networking_basics_2`
-   File:  `0-change_your_home_IP`


### 1. Show attached IPs

mandatory

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

Example:

```
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$

```

Obviously, the IPs displayed may be different depending on which machine you are running the script on.

Note that we can see our  `localhost`  IP :)

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x08-networking_basics_2`
-   File:  `1-show_attached_IPs`


### 2. Port listening on localhost

#advanced

Write a Bash script that listens on port  `98`  on  `localhost`.

**Terminal 0**

Starting my script.

```
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost

```

**Terminal 1**

Connecting to  `localhost`  on port  `98`  using  `telnet`  and typing some text.

```
sylvain@ubuntu$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test

```

**Terminal 0**

Receiving the text on the other side.

```
sylvain@ubuntu$ sudo ./100-port_listening_on_localhost
Hello world
test

```

For the sake of the exercise, this connection is made entirely within  `localhost`. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!

**Repo:**

-   GitHub repository:  `alx-system_engineering-devops`
-   Directory:  `0x08-networking_basics_2`
-   File:  `100-port_listening_on_localhost`