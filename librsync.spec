Summary:	Rsync libraries
Summary(pl):	Biblioteki rsync
Name:		librsync
Version:	0.9.5.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp1.sourceforge.net/rproxy/%{name}-%{version}.tar.gz
# Source0-md5:	d65dcd7dce50ba71364a1c0b15ce21bd
URL:		http://www.sf.net/projects/rproxy/
Patch0:		%{name}-am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

%description -l pl
librsync jest implementacj± algorytmu rsync, pozwalaj±cego na zdalne
porównywanie plików binarnych. librsync liczy ró¿nice sum kontrolnych
plików, wiêc nie wymaga obecno¶ci obu plików do sprawdzenia ró¿nic.

Ta biblioteka by³a wcze¶niej znana jako libhsync, do wersji 0.9.0
w³±cznie.

Ta wersja nie ma implementacji sieciowego protoko³u rsync i u¿ywa
formatu delt nieco wydajniejszego i niekompatybilnego z rsyncem w
wersji 2.4.6.

%package devel
Summary:	Headers for librsync
Summary(pl):	Pliki nag³ówkowe librsync
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains header files necessary for developing programs
based on librsync.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do budowania programów
u¿ywajacych librsync.

%package static
Summary:	Static librsync library
Summary(pl):	Statyczna biblioteka librsync
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static librsync library.

%description static -l pl
Statyczna biblioteka librsync.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared

%{__make} CFLAGS="%{rpmcflags}"

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
