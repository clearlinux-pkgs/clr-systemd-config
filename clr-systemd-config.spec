#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-systemd-config
Version  : 179
Release  : 203
URL      : http://localhost/cgit/projects/clr-systemd-config/snapshot/clr-systemd-config-179.tar.xz
Source0  : http://localhost/cgit/projects/clr-systemd-config/snapshot/clr-systemd-config-179.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: clr-systemd-config-autostart = %{version}-%{release}
Requires: clr-systemd-config-config = %{version}-%{release}
Requires: clr-systemd-config-data = %{version}-%{release}
Requires: clr-systemd-config-license = %{version}-%{release}
Requires: clr-systemd-config-services = %{version}-%{release}
BuildRequires : /usr/bin/systemd-sysusers
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(systemd)

%description
No detailed description available

%package autostart
Summary: autostart components for the clr-systemd-config package.
Group: Default

%description autostart
autostart components for the clr-systemd-config package.


%package config
Summary: config components for the clr-systemd-config package.
Group: Default

%description config
config components for the clr-systemd-config package.


%package data
Summary: data components for the clr-systemd-config package.
Group: Data

%description data
data components for the clr-systemd-config package.


%package extras
Summary: extras components for the clr-systemd-config package.
Group: Default

%description extras
extras components for the clr-systemd-config package.


%package license
Summary: license components for the clr-systemd-config package.
Group: Default

%description license
license components for the clr-systemd-config package.


%package services
Summary: services components for the clr-systemd-config package.
Group: Systemd services

%description services
services components for the clr-systemd-config package.


%prep
%setup -q -n clr-systemd-config-179

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550861732
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1550861732
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-systemd-config
cp LICENSE %{buildroot}/usr/share/package-licenses/clr-systemd-config/LICENSE
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/modprobe.d/tpm-blacklist.conf
/usr/lib/systemd/bootchart.conf.d/clear.conf
/usr/lib/systemd/clr-image-triggers
/usr/lib/systemd/journald.conf.d/clear.conf
/usr/lib/systemd/logind.conf.d/50-lidswitch.conf
/usr/lib/systemd/network/80-dhcp.network
/usr/lib/systemd/network/80-virtual.network
/usr/lib/systemd/resolved.conf.d/80-noLLMNR.conf
/usr/lib/systemd/system-preset/80-clear.preset
/usr/lib/systemd/system.conf.d/50-nfiles.conf

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/firstboot-triggers.service

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/modules-load.d/bridge-netfilter.conf
/usr/lib/sysusers.d/clear.conf
/usr/lib/udev/rules.d/80-kvm.rules
/usr/lib/udev/rules.d/90-tpm-thinkpad.rules

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/group
/usr/share/defaults/etc/gshadow
/usr/share/defaults/etc/passwd
/usr/share/defaults/etc/shadow

%files extras
%defattr(-,root,root,-)
/usr/lib/modules-load.d/bridge-netfilter.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-systemd-config/LICENSE

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/firstboot-triggers.service
/usr/lib/systemd/system/catalog-trigger.service
/usr/lib/systemd/system/firstboot-triggers.service
/usr/lib/systemd/system/graphviz-dot-trigger.service
/usr/lib/systemd/system/hwdb-update-trigger.service
/usr/lib/systemd/system/ldconfig-trigger.service
/usr/lib/systemd/system/locale-archive-trigger.service
/usr/lib/systemd/system/mandb-trigger.service
/usr/lib/systemd/system/systemd-modules-trigger.service
/usr/lib/systemd/system/tmpfiles-trigger.service
/usr/lib/systemd/system/update-triggers.target
