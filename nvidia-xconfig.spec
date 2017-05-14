Name:           nvidia-xconfig
Version:        381.22
Release:        1%{?dist}
Summary:        NVIDIA xorg.conf configurator

License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
Source0:        http://download.nvidia.com/XFree86/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  m4
Requires:       nvidia-driver-cfg%{?_isa}


%description
NVIDIA's tool for manipulating X server configuration files.


%prep
%setup -q


%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} NV_VERBOSE=1 STRIP_CMD="/bin/true"


%install
rm -rf %{buildroot}
%make_install INSTALL="install -p" PREFIX=%{_prefix}
mv %{buildroot}%{_bindir} %{buildroot}%{_sbindir}


%files
%doc COPYING
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Sun May 14 2017 Jajauma's Packages <jajauma@yandex.ru> - 381.22-1
- Update to latest upstream release
- Fix broken FTP D/L link

* Sun Nov 27 2016 Jajauma's Packages <jajauma@yandex.ru> - 375.20-1
- Update to latest upstream version

* Thu Oct 20 2016 Jajauma's Packages <jajauma@yandex.ru> - 367.57-1
- Update to latest upstream release

* Sun Oct 09 2016 Jajauma's Packages <jajauma@yandex.ru> - 367.44-1
- Public release
