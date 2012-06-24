Summary:	GNOME network programs
Summary(es):	Programas de red del GNOME
Summary(pl):	GNOME - programy sieciowe
Summary(pt_BR):	Programas de rede do GNOME
Summary(ru):	GNOME - ��������� ������ � �����
Summary(uk):	GNOME - �������� ������ � �������
Name:		gnome-network
Version:	1.99.0
Release:	1
License:	GPL
Group:		X11/Applications
# Source0-md5:	3c8bb27a941b7132a27880e6ebb1e771
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-network/1.99/%{name}-%{version}.tar.bz2
Patch0:		%{name}-no_zvt.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2
BuildRequires:	libgnomeui
URL:		http://www.gnome.org/
Icon:		gnome-network.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

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

%build
rm -rf missing
glib-gettextize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/gnome-backup
%{_datadir}/gnome-network
%{_datadir}/gnome-remote-desktop
