Summary:	Rsync libraries
Name:		librsync
Version:	0.9.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp1.sourceforge.net/rproxy/%{name}-%{version}.tar.gz
URL:		http://www.sf.net/projects/rproxy
Patch0:		%{name}-am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
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

%package devel
Summary:	Headers and development libraries for librsync
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files. librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

This library was previously known as libhsync up to version 0.9.0.

The current version of this package does not implement the rsync
network protocol and uses a delta format slightly more efficient than
and incompatible with rsync 2.4.6.

This package contains header files necessary for developing programs
based on librsync.

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
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
automake -a -c -f
%configure \
	--enable-shared

%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/rdiff
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/rdiff.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
