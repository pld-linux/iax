Summary:	IAX (Inter Asterisk eXchange) library
Summary(pl.UTF-8):	Biblioteka IAX (Inter Asterisk eXchange)
Name:		iax
Version:	0.2.2
Release:	3
License:	LGPL/GPL
Group:		Libraries
Source0:	ftp://ftp.gnophone.com/pub/gnophone/%{name}-%{version}.tar.gz
#Source0-md5:	d9c14e0a2ad9cb710761795a3497a21c
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gnophone.com/
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
information see http://www.gnophone.com/.

%description -l pl.UTF-8
Inter Asterisk eXchange, z lubością nazywany IAX (wymawiany "eeks") to
protokół używany przez system PBX Asterisk do wewnętrznej komunikacji.
Inne aplikacje mogą używać libiax do komunikowania ze sobą i innymi
serwerami asterisk. IAX to wysoko wydajny, bogaty w możliwości
protokół nie powiązany z SIP czy H.323. Jego jednogniazdowa
architektura pozwala współpracować z firewallami z maskowaniem NAT i
PAT. Biblioteka wspiera umiędzynarodowienie, zdalne plany dzwonienia
oraz dane w postaci głosu, HTML-a, obrazków, DTMF i obrazu. Więcej
informacji pod adresem http://www.gnophone.com/.

%package devel
Summary:	IAX (Inter Asterisk eXchange) development package
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki IAX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks), is
the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a high
performance, feature rich protocol unrelated to SIP or H.323. Its
single-socket design allows it to interoperate with NAT and PAT
masquerade firewalls. It supports internationalization, remote
dialplans, and voice, HTML, image, DTMF, and video content. For more
information see http://www.gnophone.com/. This package contains all of
the development files that you will need in order to compile IAX
applications.

%description devel -l pl.UTF-8
Inter Asterisk eXchange, z lubością nazywany IAX (wymawiany "eeks") to
protokół używany przez system PBX Asterisk do wewnętrznej komunikacji.
Inne aplikacje mogą używać libiax do komunikowania ze sobą i innymi
serwerami asterisk. IAX to wysoko wydajny, bogaty w możliwości
protokół nie powiązany z SIP czy H.323. Jego jednogniazdowa
architektura pozwala współpracować z firewallami z maskowaniem NAT i
PAT. Biblioteka wspiera umiędzynarodowienie, zdalne plany dzwonienia
oraz dane w postaci głosu, HTML-a, obrazków, DTMF i obrazu. Więcej
informacji pod adresem http://www.gnophone.com/. Ten pakiet zawiera
wszystkie pliki potrzebne do kompilowania aplikacji IAX.

%package static
Summary:	IAX (Inter Asterisk eXchange) static library
Summary(pl.UTF-8):	Wersja statyczna biblioteki IAX
Group:		Development/Libraries
Requires:	iax = %{version}
Requires:	iax-devel = %{version}

%description static
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks), is
the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a high
performance, feature rich protocol unrelated to SIP or H.323. Its
single-socket design allows it to interoperate with NAT and PAT
masquerade firewalls. It supports internationalization, remote
dialplans, and voice, HTML, image, DTMF, and video content. For more
information see <http://www.gnophone.com/>. This package contains
static libraries that you will need in order to compile statically
linked IAX applications.

%description static -l pl.UTF-8
Inter Asterisk eXchange, z lubością nazywany IAX (wymawiany "eeks") to
protokół używany przez system PBX Asterisk do wewnętrznej komunikacji.
Inne aplikacje mogą używać libiax do komunikowania ze sobą i innymi
serwerami asterisk. IAX to wysoko wydajny, bogaty w możliwości
protokół nie powiązany z SIP czy H.323. Jego jednogniazdowa
architektura pozwala współpracować z firewallami z maskowaniem NAT i
PAT. Biblioteka wspiera umiędzynarodowienie, zdalne plany dzwonienia
oraz dane w postaci głosu, HTML-a, obrazków, DTMF i obrazu. Więcej
informacji pod adresem <http://www.gnophone.com/>. Ten pakiet zawiera
statyczne biblioteki potrzebne do kompilowania statycznie
konsolidowanych aplikacji IAX.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iax-config
%attr(755,root,root) %{_libdir}/libiax.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/iax

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
