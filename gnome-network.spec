Summary:	GNOME network programs
Summary(es):	Programas de red del GNOME
Summary(pl):	GNOME - programy sieciowe
Summary(pt_BR):	Programas de rede do GNOME
Summary(ru):	GNOME - ��������� ������ � �����
Summary(uk):	GNOME - �������� ������ � �������
Name:		gnome-network
Version:	1.99.2
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-network/1.99/%{name}-%{version}.tar.bz2
# Source0-md5:	ba71a10c0606379ac80d1d0a24555a41
Patch0:		%{name}-no_zvt.patch
Patch1:		%{name}-help-button.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-locale_names.patch
Patch4:		%{name}-ac.patch
Patch5:		%{name}-netinfo.patch
URL:		http://www.gnome.org/
Icon:		gnome-network.xpm
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.4.0
#Requires:	bind-utils
#Requires:	bsd-finger
#Requires:	iputils
#Requires:	net-tools
#Requires:	ssh-clients
#Requires:	telnet
#Requires:	vnc-client
Obsoletes:	gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME network programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l es
Programas de red del GNOME GNOME es el Ambiente de Red Modelado por
Objetos de la GNU. Es un nombre fantasioso, pero GNOME es realmente un
buen ambiente gr�fico. Hace tu ordenador sencillo, potente y f�cil de
configurar.

%description -l pl
Programy sieciowe dla GNOME.

%description -l pt_BR
Programas de rede do GNOME

GNOME � o Ambiente de Rede Modelado por Objetos da GNU. � um nome
fantasioso, mas o GNOME � realmente um bom ambiente gr�fico. Ele torna
seu computador f�cil, poderoso e f�cil de configurar.

%description -l ru
GNOME - ��������� ������ � �����.

%description -l uk
GNOME - �������� ������ � �������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0

mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-ifconfig="/sbin/ifconfig" \
	--with-vncviewer="/usr/bin/vncviewer" \
	--with-xnest="/usr/X11R6/bin/Xnest"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/gnome/apps/*/* $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome-network
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
