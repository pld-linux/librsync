Summary:	Rsync libraries
Name:		librsync
Version:	0.9.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp1.sourceforge.net/rproxy/%{name}-%{version}.tar.gz
URL:		http://www.sf.net/projects/rproxy
Patch0:		%{name}-am.patch
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

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
automake -a -c

%configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}/

%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make}  DESTDIR=$RPM_BUILD_ROOT install
gzip -9nf AUTHORS COPYING NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rdiff
%{_mandir}/man1/rdiff.1.gz
%doc *.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/librsync.*
%{_mandir}/man3/librsync.3.gz
