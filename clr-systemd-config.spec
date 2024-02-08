#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : clr-systemd-config
Version  : 207
Release  : 238
URL      : http://localhost/cgit/projects/clr-systemd-config/snapshot/clr-systemd-config-207.tar.xz
Source0  : http://localhost/cgit/projects/clr-systemd-config/snapshot/clr-systemd-config-207.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: clr-systemd-config-autostart = %{version}-%{release}
Requires: clr-systemd-config-config = %{version}-%{release}
Requires: clr-systemd-config-data = %{version}-%{release}
Requires: clr-systemd-config-libexec = %{version}-%{release}
Requires: clr-systemd-config-license = %{version}-%{release}
Requires: clr-systemd-config-services = %{version}-%{release}
Requires: clr-elf-replace
BuildRequires : /usr/bin/systemd-sysusers
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(systemd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package libexec
Summary: libexec components for the clr-systemd-config package.
Group: Default
Requires: clr-systemd-config-config = %{version}-%{release}
Requires: clr-systemd-config-license = %{version}-%{release}

%description libexec
libexec components for the clr-systemd-config package.


%package license
Summary: license components for the clr-systemd-config package.
Group: Default

%description license
license components for the clr-systemd-config package.


%package services
Summary: services components for the clr-systemd-config package.
Group: Systemd services
Requires: systemd

%description services
services components for the clr-systemd-config package.


%prep
%setup -q -n clr-systemd-config-207
cd %{_builddir}/clr-systemd-config-207

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699921732
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1699921732
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-systemd-config
cp %{_builddir}/clr-systemd-config-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/clr-systemd-config/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
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

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/firstboot-triggers.service
/usr/lib/systemd/system/timers.target.wants/networkd-fallback.timer

%files config
%defattr(-,root,root,-)
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

%files libexec
%defattr(-,root,root,-)
/usr/libexec/clr-fallback-to-systemd-networkd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-systemd-config/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/firstboot-triggers.service
%exclude /usr/lib/systemd/system/timers.target.wants/networkd-fallback.timer
/usr/lib/systemd/system/catalog-trigger.service
/usr/lib/systemd/system/clr-elf-replace-trigger.service
/usr/lib/systemd/system/firstboot-triggers.service
/usr/lib/systemd/system/graphviz-dot-trigger.service
/usr/lib/systemd/system/hwdb-update-trigger.service
/usr/lib/systemd/system/ldconfig-trigger.service
/usr/lib/systemd/system/locale-archive-trigger.service
/usr/lib/systemd/system/mandb-trigger.service
/usr/lib/systemd/system/networkd-fallback.service
/usr/lib/systemd/system/networkd-fallback.timer
/usr/lib/systemd/system/systemd-modules-trigger.service
/usr/lib/systemd/system/sysusers-trigger.service
/usr/lib/systemd/system/tmpfiles-trigger.service
/usr/lib/systemd/system/update-triggers.target
