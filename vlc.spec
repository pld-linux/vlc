Summary:	VideoLAN is a free MPEG, MPEG-2 and DVD software solution
Summary(pl):	Klient VideoLAN
Summary(pt_BR):	O VideoLAN é um cliente DVD e MPEG de livre distribuição que pode funcionar via rede
Name:		vlc
Version:	0.2.91
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.videolan.org/
BuildRequires:	SDL-devel >= 1.2
%ifnarch sparc sparc64
#BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	esound-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libggi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mandir		%{_prefix}/man

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
VideoLAN is a free network-aware MPEG and DVD player. The VideoLAN
Client allows to play MPEG-2 Transport Streams from the network or
from a file, as well as direct DVD playback. VideoLAN is a project of
students from the Ecole Centrale Paris. This version add MPEG-1
support, direct DVD support, DVD decryption, arbitrary, seeking in the
stream, pause, fast forward and slow motion, hardware YUV acceleration
and a few new interface features including drag'n'drop. You may
install vlc-gnome, vlc-gtk and vlc-qt vlc-gnome vlc-ncurses.

%description -l pl
VideoLAN jest darmowym rozwi±zaniem dla streamingu MPEG2.

Klient VideoLAN pozwala na odtwarzanie strumienia MPEG2 z sieci lub z
pliku jak równie¿ bezpo¶rednie odtwarzanie z DVD.

%description -l pt_BR
O VideoLAN é um cliente DVD e MPEG de livre distribuição que pode
funcionar via rede. Permite a reprodução de "transport streams" MPEG-2
a partir da rede ou de um arquivo, bem como assistir a DVDs
localmente.

%package X11
Summary:	VideoLAN Client - X11 output plugin
Summary(pl):	Klient VideoLAN - plugin dla X11
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description X11
X11 output plugin for VideoLAN Client

%description -l pl X11
Plugin X11 dla Klienta VideoLAN

%package GGI
Summary:	VideoLAN Client - GGI output plugin
Summary(pl):	Klient VideoLAN - plugin GGI
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description GGI
GGI output plugin for VideoLAN Client.

%description -l pl GGI
Plugin GGI dla Klienta VideoLAN.

%package SDL
Summary:	VideoLAN Client - SDL output plugin
Summary(pl):	Klient VideoLAN - plugin SDL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description SDL
SDL output plugin for VideoLAN Client.

%description -l pl SDL
Plugin SDL dla Klienta VideoLAN.

%package gnome
Summary:	VideoLAN Client - gnome output plugin
Summary(pl):	Klient VideoLAN - plugin gnome
Summary(pt_BR):	Plugin gnome para o VideoLAN
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description gnome
Gnome output plugin for VideoLAN Client.

%description -l pl gnome
Plugin gnome dla Klienta VideoLAN.

%description gnome -l pt_BR
Plugin gnome para o VideoLAN.

%package gtk
Summary:	VideoLAN Client - gtk output plugin
Summary(pl):	Klient VideoLAN - plugin gtk
Summary(pt_BR):	Plugin gtk para o VideoLAN
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description gtk
GTK output plugin for VideoLAN Client.

%description -l pl gtk
Plugin GTK dla Klienta VideoLAN.

%description gtk -l pt_BR
Plugin gtk para o VideoLAN.

%package esd
Summary:	VideoLAN Client - esound output plugin
Summary(pl):	Klient VideoLAN - plugin esound
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description esd
Esd audio output plugin for VideoLAN Client.

%description -l pl esd
Plugin audio esd dla Klienta VideoLAN.

#%package alsa
#Summary:	VideoLAN Client - alsa output plugin
#Summary(pl):	Klient VideoLAN - plugin alsa
#Group:		X11/Applications/Multimedia
#Group(de):	X11/Applikationen/Multimedia
#Group(pl):	X11/Aplikacje/Multimedia
#Requires:	%{name} = %{version}
#   
#%description alsa
#ALSA audio output plugin for VideoLAN Client.
#
#%description -l pl alsa
#Plugin audi ALSA dla Klienta VideoLAN.
#

%prep
%setup -q

%build
autoconf
%configure \
%ifarch i586 i686 athlon
	--enable-mmx \
%ifarch i686 athlon
	--enable-ppro \
%else
	--disable-mmx \
	--disable-ppro \
%endif
%endif
	--enable-dummy \
	--enable-dsp \
	--disable-alsa \
	--enable-esd \
	--enable-fb \
	--with-ggi \
	--with-sdl \
	--disable-glide \
	--enable-gnome \
	--enable-x11 \
	--with-sdl=/usr/X11R6 \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vlc
%dir %{_libdir}/videolan
%dir %{_libdir}/videolan/vlc
%attr(755,root,root) %{_libdir}/videolan/vlc/dsp.so
%attr(755,root,root) %{_libdir}/videolan/vlc/fb.so
%dir %{_datadir}/videolan
%{_datadir}/videolan/*.psf
%{_datadir}/videolan/vlc.png

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/x11.so

%files GGI
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/ggi.so

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/sdl.so

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvlc
%attr(755,root,root) %{_libdir}/videolan/vlc/gtk.so
%{_datadir}/videolan/gvlc.png

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-vlc
%attr(755,root,root) %{_libdir}/videolan/vlc/gnome.so
%{_datadir}/videolan/gvlc.png

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/esd.so

#%files alsa
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/videolan/vlc/alsa.so
