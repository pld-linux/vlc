Summary:	VideoLAN - a free MPEG, MPEG-2 and DVD software solution
Summary(pl):	VideoLAN - darmowe oprogramowanie dla MPEG, MPEG-2 i DVD
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
#BuildRequires:	alsa-lib-devel
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
support, direct DVD support, DVD decryption, arbitrary seeking in the
stream, pause, fast forward and slow motion, hardware YUV acceleration
and a few new interface features including drag'n'drop. You may
install vlc-gnome, vlc-gtk, vlc-qt, vlc-gnome or vlc-ncurses.

%description -l pl
VideoLAN jest darmowym, obs³uguj±cym sieæ odtwarzaczem MPEG i DVD.
Klient VideoLAN pozwala na odtwarzanie strumieni MPEG-2 z sieci lub z
pliku, jak równie¿ bezpo¶rednie odtwarzanie z DVD. VideoLAN to projekt
studentów z Ecole Centrale Paris. Ta wersja ma tak¿e obs³ugê MPEG-1,
bezpo¶redniego dostêpu do DVD, dekodowania DVD, przemieszczania w
strumieniu, pauzowania, szybkiego przewijania i spowolniania,
sprzêtowej akceleracji YUV oraz parê nowych mo¿liwo¶ci interfejsu,
w³±cznie z drag'n'drop. Mo¿na zainstalowaæ jeden z dostêpnych
frontendów: vlc-gnome, vlc-gtk, vlc-qt, vlc-gnome albo vlc-ncurses.

%description -l pt_BR
O VideoLAN é um cliente DVD e MPEG de livre distribuição que pode
funcionar via rede. Permite a reprodução de "transport streams" MPEG-2
a partir da rede ou de um arquivo, bem como assistir a DVDs
localmente.

%package X11
Summary:	VideoLAN Client - X11 output plugin
Summary(pl):	Klient VideoLAN - wtyczka wyj¶cia X11
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description X11
X11 output plugin for VideoLAN Client

%description X11 -l pl
Wtyczka wyj¶cia X11 dla klienta VideoLAN.

%package GGI
Summary:	VideoLAN Client - GGI output plugin
Summary(pl):	Klient VideoLAN - wtyczka wyj¶cia GGI
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description GGI
GGI output plugin for VideoLAN Client.

%description GGI -l pl
Wtyczka wyj¶cia GGI dla klienta VideoLAN.

%package SDL
Summary:	VideoLAN Client - SDL output plugin
Summary(pl):	Klient VideoLAN - wtyczka wyj¶cia SDL
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description SDL
SDL output plugin for VideoLAN Client.

%description SDL -l pl
Wtyczka wyj¶cia SDL dla klienta VideoLAN.

%package gnome
Summary:	VideoLAN Client - GNOME output plugin
Summary(pl):	Klient VideoLAN - wtyczka wyj¶cia GNOME
Summary(pt_BR):	Plugin gnome para o VideoLAN
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description gnome
GNOME output plugin for VideoLAN Client.

%description gnome -l pl
Wtyczka wyj¶cia GNOME dla klienta VideoLAN.

%description gnome -l pt_BR
Plugin gnome para o VideoLAN.

%package gtk
Summary:	VideoLAN Client - GTK+ output plugin
Summary(pl):	Klient VideoLAN - wtyczka wyj¶cia GTK+
Summary(pt_BR):	Plugin GTK+ para o VideoLAN
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description gtk
GTK+ output plugin for VideoLAN Client.

%description gtk -l pl
Wtyczka wyj¶cia GTK+ dla klienta VideoLAN.

%description gtk -l pt_BR
Plugin GTK+ para o VideoLAN.

%package esd
Summary:	VideoLAN Client - EsounD audio output plugin
Summary(pl):	Klient VideoLAN - wtyczka wyj¶cia d¼wiêku EsounD
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description esd
EsounD audio output plugin for VideoLAN Client.

%description esd -l pl
Wtyczka wyj¶cia d¼wiêku EsounD dla klienta VideoLAN.

%package alsa
Summary:	VideoLAN Client - ALSA audio output plugin
Summary(pl):	Klient VideoLAN - wtyczka wyj¶cia d¼wiêku ALSA
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description alsa
ALSA audio output plugin for VideoLAN Client.

%description alsa -l pl
Wtyczka wyj¶cia d¼wiêku ALSA dla klienta VideoLAN.

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
