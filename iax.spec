Summary:	IAX (Inter Asterisk eXchange) Library
Summary(pl):	Biblioteka IAX (Inter Asterisk eXchange)
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
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks), is
the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a high
performance, feature rich protocol unrelated to SIP or H.323. Its
single-socket design allows it to interoperate with NAT and PAT
masquerade firewalls. It supports internationalization, remote
dialplans, and voice, HTML, image, DTMF, and video content. For more
information see http://www.gnophone.com.

%package devel
Summary:	IAX (Inter Asterisk eXchange) Development Package
Summary(pl):	Pliki nag³ówkowe dla biblioteki IAX
Requires:	iax = %{version}
Group:		Development/Libraries

%description devel
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks), is
the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a high
performance, feature rich protocol unrelated to SIP or H.323. Its
single-socket design allows it to interoperate with NAT and PAT
masquerade firewalls. It supports internationalization, remote
dialplans, and voice, HTML, image, DTMF, and video content. For more
information see http://www.gnophone.com. This package contains all of
the development files that you will need in order to compile IAX
applications.


%package static
Summary:	IAX (Inter Asterisk eXchange) Static Package
Summary(pl):	Wersja statyczna biblioteki IAX
Requires:	iax = %{version}
Requires:	iax-devel = %{version}
Group:		Development/Libraries

%description static
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks), is
the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a high
performance, feature rich protocol unrelated to SIP or H.323. Its
single-socket design allows it to interoperate with NAT and PAT
masquerade firewalls. It supports internationalization, remote
dialplans, and voice, HTML, image, DTMF, and video content. For more
information see http://www.gnophone.com. This package contains static
libraries that you will need in order to compile statically linked IAX
applications.

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
