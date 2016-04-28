Name:               libshout-idjc
Version:            2.3.1
Release:            1%{?dist}
Summary:            Libshout modified for IDJC
Source:             http://prdownloads.sourceforge.net/project/idjc/libshout-idjc/libshout-idjc-%{version}.tar.gz
URL:                http://sourceforge.net/projects/idjc/
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
make LDFLAGS+=-lspeex

%install
make install DESTDIR=%{buildroot}


%files 
%defattr(-,root,root)
%doc COPYING NEWS README
%{_libdir}/libshout-idjc.a
%{_libdir}/libshout-idjc.la
%{_libdir}/libshout-idjc.so.3
%{_libdir}/libshout-idjc.so.3.2.0

%files devel
%defattr(-,root,root)
%{_includedir}/shoutidjc
%{_libdir}/libshout-idjc.so
%{_libdir}/pkgconfig/shout-idjc.pc

%changelog
* Mon Oct 27 2014 David Vasquez <davidjeremias82 at gmail dot com> - 2.3.1-1
- Initial build
