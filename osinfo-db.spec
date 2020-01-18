# -*- rpm-spec -*-

%define PatchedSource ../%{name}-%{version}-patched.tar.xz

Summary: osinfo database files
Name: osinfo-db
Version: 20170423
Release: 2%{?dist}
License: LGPLv2+
Source0: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz
Source1: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz.asc
URL: http://libosinfo.org/
BuildRequires: intltool
BuildRequires: osinfo-db-tools
BuildArch: noarch
Requires: hwdata

Patch0: add-rhel7.4-data.patch

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%prep
%setup -q
%patch0 -p1 -b .add-rhel7.4-data

# For us to be able to apply patches on top of a rebase,
# we:
# 1. unpack the sources
# 2. patch the sources
# 3. pack the sources in a tarball
# 4. feed the patched tarball to osinfo-db-import
%build
tar -cvJf %{PatchedSource} ../%{name}-%{version}/

%install
osinfo-db-import  --root %{buildroot} --dir %{_datadir}/osinfo %{PatchedSource}

%files
%dir %{_datadir}/osinfo/
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema

%changelog
* Tue Jun 27 2017 Felipe Borges <feborges@redhat.com> - 20170423-2
- Make this spec file patchable
- Add RHEL 7.4 data
- Resolves: rhbz#1462641

* Tue Jun  6 2017 Fabiano Fidêncio <fidencio@redhat.com> - 20170423-1
- Update osinfo-db to a new release
- Resolves: rhbz#1456950, rhbz#1456947

* Wed May 31 2017 Felipe Borges <feborges@redhat.com> - 20170225-3
- Fedora/RHEL passwords must be wrapped by a single quote
- Resolves: rhbz#1456950

* Wed May 31 2017 Felipe Borges <feborges@redhat.com> - 20170225-2
- Add RHEL-6.9 and RHEL-7.3 info
- Resolves: rhbz#1456947

* Sat Feb 25 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170225-1
- Update to new release

* Sat Feb 11 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170211-1
- Update to new release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170121-2
- 20170121-1 used an incorrect tarball

* Sat Jan 21 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170121-1
- Update to new release

* Sat Jan 14 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170114-1
- Update to new release

* Sat Jan 07 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170107-1
- Update to new release

* Wed Oct 26 2016 Daniel P. Berrange <berrange@redhat.com> - 20161026-1
- Update to new release

* Fri Jul 29 2016 Daniel P. Berrange <berrange@redhat.com> - 20160728-1
- Initial package after split from libosinfo (rhbz #1361596)
