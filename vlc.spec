Summary:	VideoLAN is a free MPEG, MPEG-2 and DVD software solution
Summary(pl):	VideoLAN - oprogramowanie dla MPEG, MPEG-2 i DVD
Summary(pt_BR):	O VideoLAN é um cliente DVD e MPEG de livre distribuição que pode funcionar via rede
Name:		vlc
Version:	0.3.0
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	766c603baf97ffe3ce51f8fccf554c6a
Patch0:		%{name}-altivec.patch
URL:		http://www.videolan.org/
BuildRequires:	SDL-devel >= 1.2
%ifnarch sparc sparc64
#BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	autoconf
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libggi-devel
BuildRequires:	libdvdcss-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
Requires:	%{name} = %{version}

%description X11
X11 output plugin for VideoLAN Client

%description X11 -l pl
Plugin X11 dla Klienta VideoLAN

%package GGI
Summary:	VideoLAN Client - GGI output plugin
Summary(pl):	Klient VideoLAN - plugin GGI
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description GGI
GGI output plugin for VideoLAN Client.

%description GGI -l pl
Plugin GGI dla Klienta VideoLAN.

%package SDL
Summary:	VideoLAN Client - SDL output plugin
Summary(pl):	Klient VideoLAN - plugin SDL
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description SDL
SDL output plugin for VideoLAN Client.

%description SDL -l pl
Plugin SDL dla Klienta VideoLAN.

%package gnome
Summary:	VideoLAN Client - gnome output plugin
Summary(pl):	Klient VideoLAN - plugin gnome
Summary(pt_BR):	Plugin gnome para o VideoLAN
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description gnome
Gnome output plugin for VideoLAN Client.

%description gnome -l pl
Plugin gnome dla Klienta VideoLAN.

%description gnome -l pt_BR
Plugin gnome para o VideoLAN.

%package gtk
Summary:	VideoLAN Client - gtk output plugin
Summary(pl):	Klient VideoLAN - plugin gtk
Summary(pt_BR):	Plugin gtk para o VideoLAN
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description gtk
GTK output plugin for VideoLAN Client.

%description gtk -l pl
Plugin GTK dla Klienta VideoLAN.

%description gtk -l pt_BR
Plugin gtk para o VideoLAN.

%package esd
Summary:	VideoLAN Client - esound output plugin
Summary(pl):	Klient VideoLAN - plugin esound
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description esd
Esd audio output plugin for VideoLAN Client.

%description esd -l pl
Plugin audio esd dla Klienta VideoLAN.

%package alsa
Summary:	VideoLAN Client - alsa output plugin
Summary(pl):	Klient VideoLAN - plugin alsa
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description alsa
ALSA audio output plugin for VideoLAN Client.

%description alsa -l pl
Plugin audi ALSA dla Klienta VideoLAN.


%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure \
%ifarch ppc
	--disable-altivec \
%endif
	--enable-dvdread \
	--enable-dummy \
	--enable-dsp \
	--disable-alsa \
	--enable-esd \
	--enable-fb \
	--enable-ggi \
        --enable-ncurses \
	--with-ggi \
	--with-sdl \
	--with-dvdcss \
	--disable-glide \
	--enable-gnome \
	--enable-x11 \
	--with-sdl=/usr/X11R6 \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations

echo "CFLAGS += -I/usr/include/ncurses" >> Makefile.opts
%{__make}
#CFLAGS="-I. -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/vlc
%dir %{_libdir}/videolan
%dir %{_libdir}/videolan/vlc
%attr(755,root,root) %{_libdir}/videolan/vlc/ac3_spdif.so
%attr(755,root,root) %{_libdir}/videolan/vlc/dsp.so
%attr(755,root,root) %{_libdir}/videolan/vlc/dummy.so
%attr(755,root,root) %{_libdir}/videolan/vlc/dvdread.so
%attr(755,root,root) %{_libdir}/videolan/vlc/file.so
%attr(755,root,root) %{_libdir}/videolan/vlc/fb.so
%attr(755,root,root) %{_libdir}/videolan/vlc/filter*.so
%attr(755,root,root) %{_libdir}/videolan/vlc/fx_scope.so
%attr(755,root,root) %{_libdir}/videolan/vlc/http.so
%attr(755,root,root) %{_libdir}/videolan/vlc/ipv*.so
%attr(755,root,root) %{_libdir}/videolan/vlc/logger.so
%attr(755,root,root) %{_libdir}/videolan/vlc/lpcm_adec.so
%attr(755,root,root) %{_libdir}/videolan/vlc/memcpy.so
%attr(755,root,root) %{_libdir}/videolan/vlc/mpeg_*.so
%attr(755,root,root) %{_libdir}/videolan/vlc/ncurses.so
%attr(755,root,root) %{_libdir}/videolan/vlc/null.so
%attr(755,root,root) %{_libdir}/videolan/vlc/rc.so
%attr(755,root,root) %{_libdir}/videolan/vlc/spudec.so
%attr(755,root,root) %{_libdir}/videolan/vlc/udp.so
%attr(755,root,root) %{_libdir}/videolan/vlc/vcd.so
%attr(755,root,root) %{_libdir}/videolan/vlc/vorbis.so
%dir %{_datadir}/videolan
%{_datadir}/videolan/*.psf
%{_datadir}/videolan/vlc*.png
%{_datadir}/videolan/vlc*.xpm
%{_datadir}/videolan/qvlc*
%{_datadir}/videolan/kvlc*

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
%{_datadir}/videolan/gvlc*.png
%{_datadir}/videolan/gvlc*.xpm

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-vlc
%attr(755,root,root) %{_libdir}/videolan/vlc/gnome.so
%{_datadir}/videolan/gnome-vlc*.png
%{_datadir}/videolan/gnome-vlc*.xpm

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/esd.so

#%files alsa
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/videolan/vlc/alsa.so
