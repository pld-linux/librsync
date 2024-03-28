#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Rsync library
Summary(pl.UTF-8):	Biblioteka rsync
Name:		librsync
Version:	2.3.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/librsync/librsync/releases
# TODO use:
#Source0:	https://github.com/librsync/librsync/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/librsync/librsync/archive/v%{version}.tar.gz
# Source0-md5:	71d227be94f6fbfc7b6d0fce3ce81861
URL:		https://librsync.sourceforge.net/
BuildRequires:	cmake >= 3.6
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files. librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

This library was previously known as libhsync up to version 0.9.0.

The current version of this package does not implement the rsync
network protocol and uses a delta format slightly more efficient than
and incompatible with rsync 2.4.6.

%description -l pl.UTF-8
librsync jest implementacją algorytmu rsync, pozwalającego na zdalne
porównywanie plików binarnych. librsync liczy różnice sum kontrolnych
plików, więc nie wymaga obecności obu plików do sprawdzenia różnic.

Ta biblioteka była wcześniej znana jako libhsync, do wersji 0.9.0
włącznie.

Ta wersja nie ma implementacji sieciowego protokołu rsync i używa
formatu delt nieco wydajniejszego i niekompatybilnego z rsyncem w
wersji 2.4.6.

%package devel
Summary:	Headers for librsync
Summary(pl.UTF-8):	Pliki nagłówkowe librsync
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files necessary for developing programs
based on librsync.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do budowania programów
używających librsync.

%package static
Summary:	Static librsync library
Summary(pl.UTF-8):	Statyczna biblioteka librsync
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librsync library.

%description static -l pl.UTF-8
Statyczna biblioteka librsync.

%prep
%setup -q

%build
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_RDIFF=OFF \
	-DBUILD_SHARED_LIBS=OFF

%{__make}
cd ..
%endif

install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	 DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.md NEWS.md README.md THANKS TODO.md
%attr(755,root,root) %{_bindir}/rdiff
%attr(755,root,root) %{_libdir}/librsync.so.*.*
%attr(755,root,root) %ghost %{_libdir}/librsync.so.2
%{_mandir}/man1/rdiff.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librsync.so
%{_includedir}/librsync.h
%{_includedir}/librsync_export.h
%{_mandir}/man3/librsync.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/librsync.a
%endif
