Name:               libshout-idjc
Version:            2.4.2
Release:            1%{?dist}
Summary:            Libshout modified for IDJC
Source:             https://sourceforge.net/projects/libshoutidjc.idjc.p/files/libshout-idjc-%{version}.tar.gz
URL:                http://sourceforge.net/projects/libshoutidjc.idjc.p/
Group:              System/Libraries
License:            LGPL-2.1+
BuildRoot:          %{_tmppath}/build-%{name}-%{version}
BuildRequires:      libogg-devel
BuildRequires:      libvorbis-devel
BuildRequires:      speex-devel
BuildRequires:      gcc make glibc-devel pkgconfig
BuildRequires:      autoconf automake libtool

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
mv -f %{buildroot}/%{_datadir}/aclocal/shout.m4 %{buildroot}/%{_datadir}/aclocal/idjc-shout.m4

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%doc COPYING NEWS README
%{_libdir}/libshout-idjc.a
%{_libdir}/libshout-idjc.so.3
%{_libdir}/libshout-idjc.so.3.2.0
%{_libdir}/ckport/db/libshout-idjc.ckport
%{_docdir}/libshout-idjc/


%files devel
%defattr(-,root,root)
%{_includedir}/shoutidjc
%{_libdir}/libshout-idjc.so
%{_libdir}/pkgconfig/shout-idjc.pc
%{_datadir}/aclocal/idjc-shout.m4


%changelog

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
