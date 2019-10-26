Summary:	Clientside library to implement the iSCSI protocol
Summary(pl.UTF-8):	Biblioteka kliencka implementująca protokół iSCSI
Name:		libiscsi
Version:	1.19.0
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
#Source0Download: https://github.com/sahlberg/libiscsi/releases
Source0:	https://github.com/sahlberg/libiscsi/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fe0c0c7b677f3b6fbe535e758838ccf2
Patch0:		%{name}-link.patch
URL:		https://github.com/sahlberg/libiscsi
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libgcrypt-devel
BuildRequires:	libibverbs-devel
BuildRequires:	librdmacm-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# libiscsi conflicts with libiscsi from open-iscsi
%define		pkglibdir	%{_libdir}/iscsi

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libdir=%{pkglibdir} \
	--disable-werror
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{pkglibdir}/libiscsi.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING specifies some details, doesn't contain LGPL/GPL text
%doc COPYING README TODO
%dir %{pkglibdir}
%attr(755,root,root) %{pkglibdir}/libiscsi.so.*.*.*
%attr(755,root,root) %{pkglibdir}/libiscsi.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{pkglibdir}/libiscsi.so
%{_includedir}/iscsi
%{_pkgconfigdir}/libiscsi.pc

%files static
%defattr(644,root,root,755)
%{pkglibdir}/libiscsi.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iscsi-inq
%attr(755,root,root) %{_bindir}/iscsi-ls
%attr(755,root,root) %{_bindir}/iscsi-perf
%attr(755,root,root) %{_bindir}/iscsi-readcapacity16
%attr(755,root,root) %{_bindir}/iscsi-swp
%attr(755,root,root) %{_bindir}/iscsi-test-cu
%attr(755,root,root) %{_bindir}/ld_iscsi.so
%{_mandir}/man1/iscsi-inq.1*
%{_mandir}/man1/iscsi-ls.1*
%{_mandir}/man1/iscsi-swp.1*
%{_mandir}/man1/iscsi-test-cu.1*
