Summary:	Clientside library to implement the iSCSI protocol
Name:		libiscsi
Version:	1.1.0
Release:	1
License:	GPLv2 / LGPLv2.1
Group:		Libraries
Source0:	https://github.com/downloads/sahlberg/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	53d0fc75c4d0e8db9344aa2565421930
URL:		https://github.com/sahlberg/libiscsi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libiscsi is a clientside library to implement the iSCSI protocol
that can be used to access resource of an iSCSI Target.

The library is fully async with regards to iscsi commands and scsi
tasks, but a sync layer is also provided for ease of use for simpler
applications.

%package tools
Summary:	A handful of useful iscsi utilities
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
A handful of useful iscsi utilities
such as logging in to and enumerating all targets on a portal
and all devices of a target.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

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
%doc README TODO
%attr(755,root,root) %{_libdir}/libiscsi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiscsi.so.1

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiscsi.so
%{_libdir}/libiscsi.la
%{_includedir}/iscsi

%files static
%defattr(644,root,root,755)
%{_libdir}/libiscsi.a
