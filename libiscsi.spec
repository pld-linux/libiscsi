Summary:	Clientside library to implement the iSCSI protocol
Summary(pl.UTF-8):	Biblioteka kliencka implementująca protokół iSCSI
Name:		libiscsi
Version:	1.20.2
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
#Source0Download: https://github.com/sahlberg/libiscsi/tags
Source0:	https://github.com/sahlberg/libiscsi/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a046ba4e327591f5d0f4853f7f761efc
URL:		https://github.com/sahlberg/libiscsi
BuildRequires:	CUnit
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	libgcrypt-devel
BuildRequires:	libibverbs-devel
BuildRequires:	librdmacm-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libiscsi is a clientside library to implement the iSCSI protocol that
can be used to access resource of an iSCSI Target.

The library is fully async with regards to iSCSC commands and SCSI
tasks, but a sync layer is also provided for ease of use for simpler
applications.

%description -l pl.UTF-8
Libiscsi to biblioteka kliencka implementująca protokół iSCSI. Można
jej używać do dostępu do zasobów na celu iSCSI (iSCSI Target).

Biblioteka jest w pełni asynchroniczna względem poleceń iSCSI i zadań
SCSI, ale dostępna jest także warstwa synchroniczna ułatwiająca użycie
w prostszych zastosowaniach.

%package devel
Summary:	Header files for iSCSI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki iSCSI
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for iSCSI library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki iSCSI.

%package static
Summary:	Static iSCSI library
Summary(pl.UTF-8):	Statyczna biblioteka iSCSI
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static iSCSI library.

%description static -l pl.UTF-8
Statyczna biblioteka iSCSI.

%package tools
Summary:	A handful of useful iSCSI utilities
Summary(pl.UTF-8):	Zestaw przydatnych narzędzi iSCSI
License:	GPL v2+
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description tools
A handful of useful iSCSI utilities, such as logging in to and
enumerating all targets on a portal and all devices of a target.

%description tools -l pl.UTF-8
Zestaw przydatnych narzędzi iSCSI, takich jak logowanie czy listowanie
wszystkich celów oraz urządzeń.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-manpages \
	--enable-test-tool \
	--disable-werror
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libiscsi.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING specifies some details, doesn't contain LGPL/GPL text
%doc COPYING README.md TODO
%attr(755,root,root) %{_libdir}/libiscsi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiscsi.so.11

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiscsi.so
%{_includedir}/iscsi
%{_pkgconfigdir}/libiscsi.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libiscsi.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iscsi-discard
%attr(755,root,root) %{_bindir}/iscsi-inq
%attr(755,root,root) %{_bindir}/iscsi-ls
%attr(755,root,root) %{_bindir}/iscsi-md5sum
%attr(755,root,root) %{_bindir}/iscsi-perf
%attr(755,root,root) %{_bindir}/iscsi-pr
%attr(755,root,root) %{_bindir}/iscsi-readcapacity16
%attr(755,root,root) %{_bindir}/iscsi-swp
%attr(755,root,root) %{_bindir}/iscsi-test-cu
%{_mandir}/man1/iscsi-inq.1*
%{_mandir}/man1/iscsi-ls.1*
%{_mandir}/man1/iscsi-md5sum.1*
%{_mandir}/man1/iscsi-swp.1*
%{_mandir}/man1/iscsi-test-cu.1*
