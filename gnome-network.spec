Summary:	GNOME network programs
Summary(es):	Programas de red del GNOME
Summary(pl):	GNOME - programy sieciowe
Summary(pt_BR):	Programas de rede do GNOME
Summary(ru):	GNOME - программы работы с сетью
Summary(uk):	GNOME - програми роботи з мережею
Name:		gnome-network
Version:	1.99.0
Release:	2
License:	GPL
Group:		X11/Applications
# Source0-md5:	3c8bb27a941b7132a27880e6ebb1e771
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-network/1.99/%{name}-%{version}.tar.bz2
Patch0:		%{name}-no_zvt.patch
URL:		http://www.gnome.org/
Icon:		gnome-network.xpm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
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
	--with-netstat="/bin/netstat" \
	--with-ping="/bin/ping" \
	--with-tcptraceroute="/usr/sbin/tcptraceroute" \
	--with-vncviewer="/usr/bin/vncviewer" \
	--with-xnest="/usr/X11R6/bin/Xnest"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome-backup
%{_datadir}/gnome-network
%{_datadir}/gnome-remote-desktop
%{_desktopdir}/*
