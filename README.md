# spaceapi
A convenient shortcut to call XMLRPC API via spacecmd

[![build result](https://build.opensuse.org/projects/home:cbbayburt:Uyuni:Utils/packages/spaceapi/badge.svg?type=default)](https://build.opensuse.org/package/show/home:cbbayburt:Uyuni:Utils/spaceapi)

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
