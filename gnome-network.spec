Summary:	GNOME network programs
Name:		gnome-network
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-network/%{name}-%{version}.tar.gz
Patch:		gnome-network-applnk.patch
BuildRequires:	gnome-libs >= 1.0.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-objc-devel
BuildRequires:	gnome-core-devel
BuildRequires:	gnome-libs-devel
URL:		http://www.gnome.org/
Icon:		gnome-network.xpm
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_applnkdir	%{_datadir}/applnk
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var/lib

%description
GNOME network programs.

GNOME is the GNU Network Object Model Environment. That's a fancy name but
really GNOME is a nice GUI desktop environment. It makes using your computer
easy, powerful, and easy to configure.

%prep
%setup -q
%patch -p1

%build
export OBJC=gcc
LDFLAGS="-s"; export LDFLAGS
gettextize --copy --force
automake
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/gnome/help/gnome-ppp
