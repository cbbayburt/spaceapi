# spaceapi
A convenient shortcut to call XMLRPC API via spacecmd

## Installation

### Download repositories

The `spaceapi` package is available for openSUSE 15.3, 15.4, SLES 15 SP3, SP4 and AlmaLinux 8.
```
https://download.opensuse.org/repositories/home:/cbbayburt:/Uyuni:/Utils/15.4/
https://download.opensuse.org/repositories/home:/cbbayburt:/Uyuni:/Utils/15.3/
https://download.opensuse.org/repositories/home:/cbbayburt:/Uyuni:/Utils/AlmaLinux_8/
```

### openSUSE/SLES

```bash
$ zypper addrepo https://download.opensuse.org/repositories/home:/cbbayburt:/Uyuni:/Utils/15.4/home:cbbayburt:Uyuni:Utils.repo
$ zypper install spaceapi
```

### AlmaLinux 8

```bash
$ dnf config-manager --add-repo https://download.opensuse.org/repositories/home:/cbbayburt:/Uyuni:/Utils/AlmaLinux_8/home:cbbayburt:Uyuni:Utils.repo
$ dnf install --nogpgcheck spaceapi
```
