Summary:	GNOME network programs
Summary(es):	Programas de red del GNOME
Summary(pl):	GNOME - programy sieciowe
Summary(pt_BR):	Programas de rede do GNOME
Summary(ru):	GNOME - программы работы с сетью
Summary(uk):	GNOME - програми роботи з мережею
Name:		gnome-network
Version:	1.99.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.99/%{name}-%{version}.tar.bz2
# Source0-md5:	ba71a10c0606379ac80d1d0a24555a41
Patch0:		%{name}-no_zvt.patch
URL:		http://www.gnome.org/
Icon:		gnome-network.xpm
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
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
buen ambiente grАfico. Hace tu ordenador sencillo, potente y fАcil de
configurar.

%description -l pl
Programy sieciowe dla GNOME.

%description -l pt_BR
Programas de rede do GNOME

GNOME И o Ambiente de Rede Modelado por Objetos da GNU. и um nome
fantasioso, mas o GNOME И realmente um bom ambiente grАfico. Ele torna
seu computador fАcil, poderoso e fАcil de configurar.

%description -l ru
GNOME - программы работы с сетью.

%description -l uk
GNOME - програми роботи з мережею.

%prep
%setup -q
%patch0 -p1

%build
rm -rf missing
glib-gettextize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome-network
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/application-registry/*
%{_datadir}/mime-info/*
