#
# spec file for package spaceapi
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           spaceapi
Version:        0.2.0
Release:        2
Summary:        A convenient shortcut to call XMLRPC API via spacecmd
License:        GPL-3.0-or-later
URL:            https://github.com/cbbayburt/spaceapi
Source0:        %{name}-%{version}.tar.gz
Requires:       spacecmd
BuildArch:      noarch

%description
A convenient shortcut to call XMLRPC API via spacecmd.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 src/spaceapi.sh %{buildroot}%{_bindir}/%{name}
install -D -m 0644 src/spaceapi-bash-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%files
%license LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%config %{_sysconfdir}/bash_completion.d/%{name}

%changelog

