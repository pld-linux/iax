Summary:	IAX library
Summary(pl):	Biblioteka IAX
Name:		iax
Version:	0.2.2
Release:	2.1
License:	LGPL/GPL
Group:		Libraries
Source0:	ftp://ftp.gnophone.com/pub/gnophone/%{name}-%{version}.tar.gz
#Source0-md5:	d9c14e0a2ad9cb710761795a3497a21c
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gnophone.com
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
empty

%package devel
Summary:	Development files for IAX library
Summary(pl):	Pliki nag³ówkowe dla biblioteki IAX
Requires:	iax = %{version}
Group:		Development/Libraries

%description devel
empty

%package static
Summary:	Static version of IAX
Summary(pl):	Wersja statyczna IAX
Requires:	iax = %{version}
Requires:	iax-devel = %{version}
Group:		Development/Libraries

%description static
empty

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iax-config
%{_libdir}/libiax.so.0.0.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/iax/*
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
