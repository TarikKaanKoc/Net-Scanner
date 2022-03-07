# Net-Scanner-Tool ( English )

- Network scanning refers to the use of a computer network to gather information regarding computing systems. Network scanning is mainly used for security assessment, system maintenance, and also for performing attacks by hackers.

- With the tool we have written, we can view the ip & mac addresses in the network. In short, scanning in the network
--- 
### What is the optparse library and what does it do ? 

- optparse is a more convenient, flexible, and powerful library for parsing command-line options than the old getopt module. optparse uses a more declarative style of command-line parsing: you create an instance of OptionParser, populate it with options, and parse the command line. optparse allows users to specify options in the conventional GNU/POSIX syntax, and additionally generates usage and help messages for you. 

- Optparse module makes easy to write command-line tools. 

1. optparse make it easy to handle the command-line argument.
2. It comes default with python.
3. It allows dynamic data input to change the output

#### [*Documentation*](https://docs.python.org/3/library/optparse.html#background)

--- 
### Creating an OptionParser object √

##### `Example:`

```console

import optparse
parser = optparse.OptionParser()

```

### Defining options √

* It should be added one at a time using the add_option(). Each Option instance represents a set of synonymous command-line option string.


##### `Way to create an Option instance are:`

```console
OptionParser.add_option(option)

```
--- 

### What is the scapy library and what does it do ? 

- The Scapy module is a Python-based library used to interact with and manipulate network packets. The library is supported by both Python2 and Python3 and can be used via the command line or by importing it as a library into your Python program.

- Scapy can also be run on Windows, Mac OS, and Linux systems.

- In addition, Scapy offers two major advantages:

- While other network modules (such as Wireshark or Nmap) were built for specific purposes like packet sniffing and network scanning, Scapy’s functionalities can be used to build new, high-level functions as per the author’s requirement.
Other networking tools output filtered results by interpreting the received packets. Scapy outputs full decoded packets, leaving the interpretation up to the user.
---
  <img algin = "center" src="scapy-dec.png">

---
##### `İnstall scapy`

* To install the Scapy module in Python3, run the following command:

```console
pip3 install scapy-python3

```

* You can also download the latest developmental version from Github using:


```console
$ git clone https://github.com/secdev/scapy.git

```

#### [*Documentation*](https://scapy.readthedocs.io/en/latest/introduction.html)

---
