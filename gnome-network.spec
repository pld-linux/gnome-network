Summary:	GNOME network programs
Summary(pl):	GNOME - programy sieciowe
Summary(uk):	GNOME - програми роботи з мережею
Summary(ru):	GNOME - программы работы с сетью
Summary(pt_BR):	Programas de rede do GNOME
Summary(es):	Programas de red del GNOME
Name:		gnome-network
Version:	1.0.2
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-network/%{name}-%{version}.tar.gz
Patch0:		%{name}-applnk.patch
Patch1:		%{name}-GNU_GETTEXT.patch
BuildRequires:	gnome-libs >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-objc-devel
BuildRequires:	gnome-core-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	autoconf
BuildRequires:	automake
URL:		http://www.gnome.org/
Icon:		gnome-network.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var/lib

%description
GNOME network programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl
Programy sieciowe dla GNOME.

%description -l uk
GNOME - програми роботи з мережею.

%description -l ru
GNOME - программы работы с сетью.

%description -l pt_BR
Programas de rede do GNOME

GNOME И o Ambiente de Rede Modelado por Objetos da GNU. и um nome
fantasioso, mas o GNOME И realmente um bom ambiente grАfico. Ele torna
seu computador fАcil, poderoso e fАcil de configurar.

%description -l es
Programas de red del GNOME GNOME es el Ambiente de Red Modelado por
Objetos de la GNU. Es un nombre fantasioso, pero GNOME es realmente un
buen ambiente grАfico. Hace tu ordenador sencillo, potente y fАcil de
configurar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
#rm -rf missing
OBJC="%{__cc}"; export OBJC
install /usr/share/automake/config.* .
%{__gettextize}
aclocal -I macros
#autoconf
#automake -a -c
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	Networkdir=%{_applnkdir}/Network/Misc \
	install

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/*/*
%{_pixmapsdir}/*
%{_datadir}/gnome/help/gnome-ppp
%{_sysconfdir}/CORBA/servers/*.goad
