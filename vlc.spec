#
# TODO:
# - check the altivec patch 
# - add proper package descriptions/translations
#
# Conditional build:
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
Summary(pl):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	0.8.2
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.videolan.org/pub/videolan/vlc/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0e56141a54055686c28e3de4dbed5990
Source1:	%{name}.desktop
Patch0:		%{name}-altivec.patch
Patch1:		%{name}-buildflags.patch
Patch2:		%{name}-defaultfont.patch
Patch3:		%{name}-live.patch
Patch4:		%{name}-x8664.patch
Patch5:		%{name}-samba.patch
Patch6:		%{name}-pic-mmx.patch
Patch7:		%{name}-matroska-shared.patch
URL:		http://www.videolan.org/vlc/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	a52dec-libs-devel
BuildRequires:	aalib-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	flac-devel
BuildRequires:	fribidi-devel
BuildRequires:	gettext-devel
%{?with_hal:BuildRequires:	hal-devel >= 0.2.97}
BuildRequires:	libcaca-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcddb-devel
BuildRequires:	libdts-devel
BuildRequires:	libdv-devel
BuildRequires:	libdvbpsi-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libdvdcss-devel
BuildRequires:	libebml-devel >= 0.7.3
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 0.7.5
BuildRequires:	libmodplug-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	lirc-devel
%{?with_live:BuildRequires:	live >= 2005.03.11}
BuildRequires:	mpeg2dec-devel
%{?with_mozilla:BuildRequires:	mozilla-devel}
BuildRequires:	ncurses-devel
%{?with_slp:BuildRequires:	openslp-devel}
BuildRequires:	pkgconfig
%{?with_speex:BuildRequires:	speex-devel > 1.1.0}
%{?with_svgalib:BuildRequires:	svgalib-devel}
BuildRequires:	vcdimager-devel
BuildRequires:	wxGTK2-devel >= 2.5.5
BuildRequires:	xosd-devel
BuildRequires:	xvid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VLC (initially VideoLAN Client) is a multimedia player for various 
audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX, MP3, Ogg, ...)
as well as DVDs, VCDs, and various streaming protocols. It can also 
be used as a server to stream in unicast or multicast in IPv4 
or IPv6 on a high-bandwidth network.

%description -l pl
VLC (wcze¶niej znany pod nazw± VideoLAN Client) jest odtwarzaczem 
multimedialnym dla wielu formatów wideo i d¼wiêku (MPEG-1, MPEG-2, 
MPEG-4, DivX, MP3, Ogg, ...), p³yt DVD, VCD oraz ró¿nych protoko³ów 
strumieniowych. Mo¿e byæ wykorzystany jako serwer do wysy³ania 
strumieni unicast lub multicast w protoko³ach IPv4 lub IPv6 
w wysokoprzepustowych sieciach.

%package devel
Summary:	VLC header files
Summary(pl):	Pliki nag³ówkowe VLC
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
VLC header files.

%description devel -l pl
Pliki nag³ówkowe VLC.

%package static
Summary:	VLC static libraries
Summary(pl):	Biblioteki statyczne VLC
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
VLC static libraries.

%description static -l pl
Biblioteki statyczne VLC.

%package X11
Summary:	VLC - X11 output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia X11
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Obsoletes:	vlc-gnome
Obsoletes:	vlc-gtk

%description X11
X11 output plugin for VLC. Contains GUI image/icon resources.

%description X11 -l pl
Wtyczka wyj¶cia X11 dla klienta VLC. Zawiera zasoby interfejsu 
GUI (obrazy/ikony).

%package GGI
Summary:	VLC - GGI output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia GGI
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description GGI
GGI output plugin for VLC.

%description GGI -l pl
Wtyczka wyj¶cia GGI dla klienta VLC.

%package fb
Summary:	VLC - fb output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia fb
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description fb
fb output plugin for VLC.

%description fb -l pl
Wtyczka wyj¶cia fb dla klienta VLC.

%package SDL
Summary:	VLC - SDL output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia SDL
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description SDL
SDL output plugin for VLC.

%description SDL -l pl
Wtyczka wyj¶cia SDL dla klienta VLC.

%package esd
Summary:	VLC - EsounD audio output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia d¼wiêku EsounD
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description esd
EsounD audio output plugin for VLC.

%description esd -l pl
Wtyczka wyj¶cia d¼wiêku EsounD dla klienta VLC.

%package alsa
Summary:	VLC - ALSA audio output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia d¼wiêku ALSA
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description alsa
ALSA audio output plugin for VLC.

%description alsa -l pl
Wtyczka wyj¶cia d¼wiêku ALSA dla klienta VLC.

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
CFLAGS="%{rpmcflags} -DALSA_PCM_OLD_HW_PARAMS_API"
%configure \
%ifarch ppc
	--disable-altivec \
%endif
	--enable-aa \
	%{?with_alsa:--enable-alsa} \
	%{?with_arts:--enable-arts} \
	%{!?with_arts:--disable-arts} \
	--enable-caca \
	--enable-dsp \
	--enable-dummy \
	--enable-dv \
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
	%{?with_ggi:--enable-ggi} \
	%{?with_ggi:--with-ggi} \
	%{!?with_ggi:--disable-ggi} \
	%{!?with_speex:--disable-speex} \
	--disable-glide \
	--enable-lirc \
	--enable-mad \
	--enable-mga \
	%{?with_mozilla:--enable-mozilla } \
	%{?with_live:--enable-livedotcom } \
	%{!?with_live:--disable-livedotcom } \
	--with-livedotcom-tree=%{_libdir}/liveMedia \
	--enable-ncurses \
	--enable-pvr \
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
	--enable-xosd \
	--enable-xvid \
	--enable-oss \
	--disable-testsuite \
	--with-wx-config=wx-gtk2-ansi-config \
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
%attr(755,root,root) %{_libdir}/vlc/audio_output
%attr(755,root,root) %{_libdir}/vlc/access_filter
%attr(755,root,root) %{_libdir}/vlc/services_discovery
%exclude %{_libdir}/%{name}/audio_output/libaout_sdl_plugin.so
%{?with_alsa:%exclude %{_libdir}/%{name}/audio_output/libalsa_plugin.so}
%exclude %{_libdir}/%{name}/audio_output/libesd_plugin.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/http
%dir %{_datadir}/%{name}/http/vlm
%dir %{_datadir}/%{name}/http/admin
%dir %{_datadir}/%{name}/skins2
%dir %{_datadir}/%{name}/skins2/fonts
%{_datadir}/%{name}/http/vlm/*.html
%{_datadir}/%{name}/http/admin/*.html
%{_datadir}/%{name}/http/admin/.access
%{_datadir}/%{name}/http/style.css
%{_datadir}/%{name}/http/*.html
%{_datadir}/%{name}/ui.rc
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
%attr(755,root,root) %{_libdir}/vlc/gui/libwxwindows_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libscreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output
%{?with_ggi:%exclude %{_libdir}/%{name}/video_output/libggi_plugin.so}
%exclude %{_libdir}/%{name}/video_output/libvout_sdl_plugin.so
%exclude %{_libdir}/%{name}/video_output/libfb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/visualization/libxosd_plugin.so
%{_datadir}/%{name}/skins2/default.vlt
%{_datadir}/%{name}/skins2/fonts/FreeSans.ttf
%{_datadir}/%{name}/skins2/skin.catalog
%{_datadir}/%{name}/skins2/skin.dtd
%{_datadir}/%{name}/vlc*.xpm
%{_datadir}/%{name}/vlc*.png
%{_desktopdir}/*

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
