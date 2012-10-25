Summary:	Clientside library to implement the iSCSI protocol
Summary(pl.UTF-8):	Biblioteka kliencka implementująca protokół iSCSI
Name:		libiscsi
Version:	1.6.0
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
#Source0Download: https://github.com/sahlberg/libiscsi/downloads
Source0:	https://github.com/downloads/sahlberg/libiscsi/%{name}-%{version}.tar.gz
# Source0-md5:	a97cd1a1c10fc3a0e0b5c8121fab27d1
URL:		https://github.com/sahlberg/libiscsi
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libiscsi is a clientside library to implement the iSCSI protocol
that can be used to access resource of an iSCSI Target.

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
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

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
Zestaw przydatnych narzędzi iSCSI, takich jak logowanie czy
listowanie wszystkich celów oraz urządzeń.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING specifies some details, doesn't contain LGPL/GPL text
%doc COPYING README TODO
%attr(755,root,root) %{_libdir}/libiscsi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiscsi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiscsi.so
%{_libdir}/libiscsi.la
%{_includedir}/iscsi

%files static
%defattr(644,root,root,755)
%{_libdir}/libiscsi.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iscsi-inq
%attr(755,root,root) %{_bindir}/iscsi-ls
%attr(755,root,root) %{_bindir}/ld_iscsi.so
