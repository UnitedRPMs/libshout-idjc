#
# spec file for package libshout-idjc
#
# Copyright (c) 2021 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

Name:               libshout-idjc
Version:            2.4.4
Release:            2%{?dist}
Summary:            Libshout modified for IDJC
Source:             https://sourceforge.net/projects/libshoutidjc.idjc.p/files/libshout-idjc-%{version}.tar.gz
URL:                http://sourceforge.net/projects/libshoutidjc.idjc.p/
Group:              System/Libraries
License:            LGPL-2.1+

BuildRequires:      libogg-devel
BuildRequires:      libvorbis-devel
BuildRequires:      speex-devel
BuildRequires:      make 
BuildRequires:      glibc-devel 
BuildRequires:      pkgconfig
BuildRequires:      autoconf 
BuildRequires:      automake 
BuildRequires:      libtool
BuildRequires:      gcc-c++

%description
This is a modified version of libshout, for IDJC.

%package devel
Summary:            Libshout modified for IDJC
Group:              Development/Libraries/C and C++
Requires:           %{name} = %{version}-%{release}

%description  devel
This is a modified version of libshout, for IDJC.

%prep
%setup -q

%build
%configure 
make

%install
make install DESTDIR=%{buildroot}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
#mv -f %{buildroot}/%{_datadir}/aclocal/shout.m4 %{buildroot}/%{_datadir}/aclocal/idjc-shout.m4

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%doc COPYING NEWS README
%{_libdir}/libshout-idjc.a
%{_libdir}/libshout-idjc.so.3
%{_libdir}/libshout-idjc.so.3.2.0
%{_libdir}/ckport/db/libshout-idjc.ckport
%{_docdir}/libshout-idjc/example.c
%{_docdir}/libshout-idjc/nonblocking.c

%files devel
%defattr(-,root,root)
%{_includedir}/shoutidjc
%{_libdir}/libshout-idjc.so
%{_libdir}/pkgconfig/shout-idjc.pc
#{_datadir}/aclocal/idjc-shout.m4


%changelog

* Mon Feb 15 2021 - David Va <davidva AT tuta DOT io> 2.4.4-2
- Updated to 2.4.4

* Tue Feb 11 2020 - David Va <davidva AT tuta DOT io> 2.4.3-2
- Rebuilt

* Thu Sep 06 2018 - David Va <davidva AT tuta DOT io> 2.4.3-1
- Updated to 2.4.3

* Mon Dec 11 2017 Francisco de la Peña <fran at fran dot cr> - 2.4.2-1
- Updated to 2.4.2

* Sun Feb 26 2017 David Vasquez <davidjeremias82 at gmail dot com> - 2.4.1-2
- Solved conflict with libshout

* Thu Jun 30 2016 David Vasquez <davidjeremias82 at gmail dot com> - 2.4.1-1
- Updated to 2.4.1

* Thu Apr 28 2016 David Vasquez <davidjeremias82 at gmail dot com> - 2.3.1-2
- Rebuilt 

* Mon Oct 27 2014 David Vasquez <davidjeremias82 at gmail dot com> - 2.3.1-1
- Initial build
