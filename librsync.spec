Summary:	Rsync libraries
Summary(pl.UTF-8):   Biblioteki rsync
Name:		librsync
Version:	0.9.7
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/librsync/%{name}-%{version}.tar.gz
# Source0-md5:	24cdb6b78f45e0e83766903fd4f6bc84
Patch0:		%{name}-link.patch
URL:		http://librsync.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt-devel
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
Summary(pl.UTF-8):   Pliki nagłówkowe librsync
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
Summary(pl.UTF-8):   Statyczna biblioteka librsync
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librsync library.

%description static -l pl.UTF-8
Statyczna biblioteka librsync.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/rdiff
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/rdiff.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
