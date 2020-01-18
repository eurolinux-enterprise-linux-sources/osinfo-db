# -*- rpm-spec -*-

%define PatchedSource ../%{name}-%{version}-patched.tar.xz

Summary: osinfo database files
Name: osinfo-db
Version: 20181214
Release: 1%{?dist}
License: LGPLv2+
Source0: https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
Source1: /https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz.asc
URL: http://libosinfo.org/
BuildRequires: intltool
BuildRequires: osinfo-db-tools
BuildArch: noarch
Requires: hwdata

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%prep
%setup -q

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
* Thu Dec 14 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181214-1
- Resolves: rhbz#1652088 - Rebase to the latest upstream release

* Thu Dec 06 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181203-1
- Resolves: rhbz#1652088 - Rebase to the latest upstream release

* Mon Jun 11 2018 Felipe Borges <feborges@redhat.com> - 20180531-1
- Rebase to 20180531
- Add RHEL 7.6
- Resolves: rhbz#1559001, rhbz#1576376

* Fri Feb 02 2018 Felipe Borges <feborges@redhat.com> - 20170813-6
- Both files inserted in the previous release were not processed.

* Fri Feb 02 2018 Felipe Borges <feborges@redhat.com> - 20170813-5
- Add OpenSUSE Leap 42.3 data
- Add Windows Server 2016 data
- Resolves: rhbz#1496711, rhbz#1474751

* Mon Jan 08 2018 Felipe Borges <feborges@redhat.com> - 20170813-4
- Add Fedora 27

* Wed Dec 06 2017 Felipe Borges <feborges@redhat.com> - 20170813-3
- Fix data of RHEL 7.5
- Resolves: rhbz#1511756

* Thu Oct 26 2017 Felipe Borges <feborges@redhat.com> - 20170813-2
- Add RHEL 7.5 data
- Resolves: #rhbz#1504600

* Mon Oct 16 2017 Felipe Borges <feborges@redhat.com> - 20170813-1
 - Update source URL to Pagure
 - Drop the rhel-7.4 data patch
 - Update to new release
 - Resolves: rhbz#1479731

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
