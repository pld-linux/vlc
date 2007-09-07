#
# TODO:
# - check the altivec patch
# - add proper package descriptions/translations
# - bcondize this damn spec! (it should be automated too)
# - go through the configure --help and add all options with proper
#   reqs and bconds
# - flac plugin doesn't work with mono files
#
# Conditional build:
%bcond_without	aa	# build without aalib support
%bcond_without	caca	# build without caca support
%bcond_without	dv	# build without dv support
%bcond_without	lirc	# build without lirc support
%bcond_without	x264	# build without x264 support
%bcond_without	alsa	# don't build alsa plugin
%bcond_without	arts	# don't build arts plugin
%bcond_without	ggi	# don't build ggi plugin
%bcond_without	live	# build without live.com support
%bcond_without	speex	# don't build speex plugin
%bcond_with	mozilla	# build mozilla plugin
%bcond_with	slp	# build with slp, broken
%bcond_with	svgalib	# build with svgalib video_output
%bcond_with	hal	# build with hal support
#
Summary:	VLC - a multimedia player and stream server
Summary(pl.UTF-8):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	0.8.6c
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
# use the bz2 src, its a 4mb difference
Source0:	http://download.videolan.org/pub/videolan/vlc/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	c207f931f768e4dcde4bfaffdbf378cd
Source1:	%{name}.desktop
Patch0:		%{name}-altivec.patch
Patch1:		%{name}-buildflags.patch
Patch2:		%{name}-defaultfont.patch
Patch3:		%{name}-live.patch
Patch4:		%{name}-pic-mmx.patch
Patch5:		%{name}-real_codecs_path.patch
Patch6:		%{name}-osdmenu_path.patch
Patch7:		%{name}-wx.patch
URL:		http://www.videolan.org/vlc/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	a52dec-libs-devel
%{?with_aa:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	faad2-devel >= 2.5
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	fribidi-devel
BuildRequires:	gettext-devel
%{?with_hal:BuildRequires:	hal-devel >= 0.2.97}
%{?with_dv:BuildRequires:	libavc1394-devel}
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdts-devel
%{?with_dv:BuildRequires:	libdv-devel}
BuildRequires:	libdvbpsi-devel
BuildRequires:	libdvdcss-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libebml-devel >= 0.7.6
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 0.7.5
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
%{?with_dv:BuildRequires:	libraw1394-devel}
BuildRequires:	libsmbclient-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
%{?with_x264:BuildRequires:	libx264-devel}
BuildRequires:	libxml2-devel
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live >= 2005.03.11}
%{?with_mozilla:BuildRequires:	mozilla-devel}
BuildRequires:	mpeg2dec-devel >= 0.3.2
BuildRequires:	ncurses-devel
%{?with_slp:BuildRequires:	openslp-devel}
BuildRequires:	pkgconfig
%{?with_speex:BuildRequires:	speex-devel > 1:1.1.0}
%{?with_svgalib:BuildRequires:	svgalib-devel}
BuildRequires:	vcdimager-devel
BuildRequires:	wxGTK2-unicode-devel >= 2.6.2-2
BuildRequires:	xosd-devel
BuildRequires:	xvid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VLC (initially VideoLAN Client) is a multimedia player for various
audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX, MP3, Ogg, ...)
as well as DVDs, VCDs, and various streaming protocols. It can also be
used as a server to stream in unicast or multicast in IPv4 or IPv6 on
a high-bandwidth network.

%description -l pl.UTF-8
VLC (wcześniej znany pod nazwą VideoLAN Client) jest odtwarzaczem
multimedialnym dla wielu formatów wideo i dźwięku (MPEG-1, MPEG-2,
MPEG-4, DivX, MP3, Ogg, ...), płyt DVD, VCD oraz różnych protokołów
strumieniowych. Może być wykorzystany jako serwer do wysyłania
strumieni unicast lub multicast w protokołach IPv4 lub IPv6 w
wysokoprzepustowych sieciach.

%package devel
Summary:	VLC header files
Summary(pl.UTF-8):	Pliki nagłówkowe VLC
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
VLC header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe VLC.

%package static
Summary:	VLC static libraries
Summary(pl.UTF-8):	Biblioteki statyczne VLC
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
VLC static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne VLC.

%package X11
Summary:	VLC - X11 output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia X11
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Obsoletes:	vlc-gnome
Obsoletes:	vlc-gtk

%description X11
X11 output plugin for VLC. Contains GUI image/icon resources.

%description X11 -l pl.UTF-8
Wtyczka wyjścia X11 dla klienta VLC. Zawiera zasoby interfejsu GUI
(obrazy/ikony).

%package GGI
Summary:	VLC - GGI output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia GGI
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description GGI
GGI output plugin for VLC.

%description GGI -l pl.UTF-8
Wtyczka wyjścia GGI dla klienta VLC.

%package fb
Summary:	VLC - fb output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia fb
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description fb
fb output plugin for VLC.

%description fb -l pl.UTF-8
Wtyczka wyjścia fb dla klienta VLC.

%package SDL
Summary:	VLC - SDL output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia SDL
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description SDL
SDL output plugin for VLC.

%description SDL -l pl.UTF-8
Wtyczka wyjścia SDL dla klienta VLC.

%package esd
Summary:	VLC - EsounD audio output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia dźwięku EsounD
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description esd
EsounD audio output plugin for VLC.

%description esd -l pl.UTF-8
Wtyczka wyjścia dźwięku EsounD dla klienta VLC.

%package alsa
Summary:	VLC - ALSA audio output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia dźwięku ALSA
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description alsa
ALSA audio output plugin for VLC.

%description alsa -l pl.UTF-8
Wtyczka wyjścia dźwięku ALSA dla klienta VLC.

%prep
%setup -q
## %patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
cp -f /usr/share/automake/config.* .
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%configure \
%ifarch ppc
	--disable-altivec \
%endif
	--%{?with_aa:en}%{!?with_aa:dis}able-aa \
	%{?with_alsa:--enable-alsa} \
	%{?with_arts:--enable-arts} \
	%{!?with_arts:--disable-arts} \
	--%{?with_caca:en}%{!?with_caca:dis}able-caca \
	--enable-dsp \
	--enable-dummy \
	--%{?with_dv:en}%{!?with_dv:dis}able-dv \
	--enable-dvb \
	--enable-dvbpsi \
	--with-dvdcss \
	--enable-dvdnav \
	--enable-dvdread \
	--enable-esd \
	--enable-faad \
	--enable-fb \
	--enable-freetype \
	--enable-fribidi \
	--enable-ffmpeg \
	--enable-flac \
	--%{?with_ggi:en}%{!?with_ggi:dis}able-ggi \
	%{!?with_speex:--disable-speex} \
	--disable-glide \
	--%{?with_lirc:en}%{!?with_lirc:dis}able-lirc \
	--enable-mad \
	--enable-mga \
	%{?with_mozilla:--enable-mozilla } \
	%{?with_live:--enable-live555 } \
	%{!?with_live:--disable-live555 } \
	--with-live555-tree=%{_libdir}/liveMedia \
	--enable-ncurses \
	--enable-pvr \
	--enable-real \
	--enable-realrtsp \
	--enable-sdl \
	--with-sdl=/usr \
	--enable-skins2 \
	%{?with_slp:--enable-slp} \
	%{!?with_slp:--disable-slp} \
	--enable-smb \
	%{?with_svgalib:--enable-svgalib} \
	--enable-tarkin \
	--enable-theora \
	--enable-tremor \
	--enable-v4l\
	--enable-x11 \
	%{!?with_x264:--disable-x264} \
	--enable-xosd \
	--enable-xvid \
	--enable-oss \
	--disable-testsuite \
	--disable-macosx \
	--with-wx-config=wx-gtk2-unicode-config \
	%{!?with_hal:--disable-hal} \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations

# echo "CFLAGS += -I/usr/include/ncurses" >> Makefile.opts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install doc/vlc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%if "%{_lib}" != "lib"
install -d $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf %{_libdir}/vlc $RPM_BUILD_ROOT%{_prefix}/lib
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/co

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README THANKS
%doc doc/bugreport-howto.txt doc/intf-cdda.txt
%doc doc/intf-vcd.txt doc/translations.txt
%attr(755,root,root) %{_bindir}/vlc
%if "%{_lib}" != "lib"
%{_prefix}/lib/vlc
%endif
%dir %{_libdir}/vlc
%dir %{_libdir}/vlc/gui
%dir %{_libdir}/vlc/visualization
%attr(755,root,root) %{_libdir}/vlc/gui/libncurses_plugin.so
%attr(755,root,root) %{_libdir}/vlc/visualization/libvisual_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux
%attr(755,root,root) %{_libdir}/vlc/misc
%attr(755,root,root) %{_libdir}/vlc/control
%attr(755,root,root) %{_libdir}/vlc/access_output
%attr(755,root,root) %{_libdir}/vlc/codec
%attr(755,root,root) %{_libdir}/vlc/demux
%attr(755,root,root) %{_libdir}/vlc/access
%exclude %{_libdir}/vlc/access/libscreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma
%attr(755,root,root) %{_libdir}/vlc/audio_mixer
%attr(755,root,root) %{_libdir}/vlc/video_filter
%dir %{_libdir}/vlc/video_output
%attr(755,root,root) %{_libdir}/vlc/stream_out
%attr(755,root,root) %{_libdir}/vlc/audio_filter
%attr(755,root,root) %{_libdir}/vlc/packetizer
%attr(755,root,root) %{_libdir}/vlc/access_filter
%attr(755,root,root) %{_libdir}/vlc/services_discovery
%dir %{_libdir}/vlc/audio_output
%exclude %{_libdir}/%{name}/audio_output/libaout_sdl_plugin.so
%{?with_alsa:%exclude %{_libdir}/%{name}/audio_output/libalsa_plugin.so}
%exclude %{_libdir}/%{name}/audio_output/libesd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/*.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/http
%{_datadir}/%{name}/osdmenu
%{_mandir}/man1/vlc.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vlc-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libvlc.a
%{_libdir}/%{name}/*.a

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/svlc
%attr(755,root,root) %{_bindir}/wxvlc
%attr(755,root,root) %{_libdir}/vlc/gui/libskins2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/gui/libwxwidgets_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libscreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output
%{?with_ggi:%exclude %{_libdir}/%{name}/video_output/libggi_plugin.so}
%exclude %{_libdir}/%{name}/video_output/libvout_sdl_plugin.so
%exclude %{_libdir}/%{name}/video_output/libfb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/visualization/libxosd_plugin.so
%{_datadir}/%{name}/skins2
%{_datadir}/%{name}/vlc*.xpm
%{_datadir}/%{name}/pda*.xpm
%{_datadir}/%{name}/vlc*.png
%{_datadir}/%{name}/vlc*.ico
%{_desktopdir}/*.desktop

%if %{with ggi}
%files GGI
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/video_output/libggi_plugin.so
%endif

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/video_output/libvout_sdl_plugin.so
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libaout_sdl_plugin.so

%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/video_output/libfb_plugin.so

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libesd_plugin.so

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libalsa_plugin.so
%endif
