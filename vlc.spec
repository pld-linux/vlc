# TODO
# - use fonts-TTF-freefont as R (vlc-X11 package) (see also vlc-defaultfont.patch)
#   ./modules/misc/freetype.c:#define DEFAULT_FONT "/usr/share/vlc/skins2/fonts/FreeSans.ttf"
#   ./modules/gui/skins2/parser/builder.cpp:            string path = (*it) + sep + "fonts" + sep + "FreeSans.ttf";
# - %{_prefix}/lib cleanup for x86_64
# - configs to /etc (../http/.hosts)
# - package lua files
# - qvlc should be in qt4 or such package not generic X11
#
# Conditional build:
%bcond_without	aalib		# build without aalib support
%bcond_without	alsa		# don't build alsa plugin
%bcond_without	bonjour		# bonjour plugin
%bcond_without	caca		# build without caca support
%bcond_without	daap		# DAAP plugin
%bcond_without	dirac		# dirac plugin
%bcond_without	directfb	# directfb plugin
%bcond_with	dv		# build with dv support (FIXME: doesn't build with libraw1394 >= 2.0.0 (new API))
%bcond_without	ggi		# don't build ggi plugin
%bcond_without	gnomevfs	# gnomevfs plugin
%bcond_without	gnutls		# gnutls plugin
%bcond_without	hal		# build with hal support
%bcond_without	jack		# jack audio module
%bcond_without	lirc		# build without lirc support
%bcond_without	live		# build without live.com support
%bcond_without	mozilla		# build mozilla plugin
%bcond_without	notify		# libnotify notification plugin
%bcond_without	portaudio	# portaudio library support
%bcond_without	projectM	# don't build projectM plugin
%bcond_with	rtmp		# RTMP output plugin
%bcond_without	shout		# shout plugin
%bcond_without	speex		# don't build speex plugin
%bcond_without	static_libs	# don't build static libraries
%bcond_without	svg		# svg plugin
%bcond_with	svgalib		# build with svgalib video_output
%bcond_without	twolame		# twolame plugin
%bcond_without	udev		# udev services discovery
%bcond_without	upnp		# upnp plugin
%bcond_without	x264		# build without x264 support

Summary:	VLC - a multimedia player and stream server
Summary(pl.UTF-8):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	1.1.11
Release:	2
License:	GPL v2+
Group:		X11/Applications/Multimedia
# use the bz2 src, its a 4mb difference
Source0:	http://download.videolan.org/pub/videolan/vlc/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	a64846d6f21ea179ae8e8bfb6f9447fe
Patch0:		%{name}-buildflags.patch
Patch1:		%{name}-defaultfont.patch
Patch2:		%{name}-osdmenu_path.patch
Patch3:		%{name}-system-minizip.patch
Patch4:		%{name}-upnp.patch
Patch5:		%{name}-ffmpeg.patch
URL:		http://www.videolan.org/vlc/
%{?with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	QtGui-devel >= 4.2.0
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	a52dec-libs-devel
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_bonjour:BuildRequires:	avahi-devel >= 0.6}
BuildRequires:	dbus-devel
%{?with_dirac:BuildRequires:	dirac-devel}
BuildRequires:	faad2-devel >= 2.5
BuildRequires:	ffmpeg-devel >= 0.4.9-4.20080131.1
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	fluidsynth-devel >= 1.1.1-3
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	game-music-emu-devel
BuildRequires:	gettext-devel
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel}
%{?with_gnutls:BuildRequires:	gnutls-devel}
%{?with_hal:BuildRequires:	hal-devel >= 0.2.97}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	kde4-kdelibs
BuildRequires:	libass-devel
%if %{with dv}
BuildRequires:	libavc1394-devel
#BuildRequires:	libraw1394-devel < 2.0.0
%endif
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdc1394-devel >= 2.1.0
BuildRequires:	libdts-devel >= 0.0.5
BuildRequires:	libdvbpsi-devel >= 0.1.6
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libebml-devel >= 0.7.6
BuildRequires:	libgcrypt-devel
%{?with_ggi:BuildRequires:	libggi-devel}
#BuildRequires:	libid3tag-devel
BuildRequires:	libkate-devel
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 0.7.5
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libmpeg2-devel
BuildRequires:	libmtp-devel >= 1.0.0
%{?with_notify:BuildRequires:	libnotify-devel}
BuildRequires:	libogg-devel
#%{?with_daap:BuildRequires:	libopendaap-devel}
BuildRequires:	libpng-devel
%{?with_projectM:BuildRequires:	libprojectM-devel >= 2.0.1-3}
#%{?with_dv:BuildRequires:	libraw1394-devel}
%{?with_svg:BuildRequires:	librsvg-devel >= 2.9.0}
%{?with_shout:BuildRequires:	libshout-devel}
BuildRequires:	libsmbclient-devel
BuildRequires:	libtar-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
%{?with_upnp:BuildRequires:	libupnp-devel}
BuildRequires:	libv4l-devel
BuildRequires:	libva-devel
BuildRequires:	libvorbis-devel
%{?with_x264:BuildRequires:	libx264-devel}
BuildRequires:	libxml2-devel
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel > 2009.07.09-3}
BuildRequires:	lua51
BuildRequires:	lua51-devel
BuildRequires:	minizip-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_portaudio:BuildRequires:	portaudio-devel}
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build
BuildRequires:	schroedinger-devel >= 1.0.10
%{?with_speex:BuildRequires:	speex-devel > 1:1.1.0}
BuildRequires:	sqlite3-devel
%{?with_svgalib:BuildRequires:	svgalib-devel}
BuildRequires:	sysfsutils-devel
BuildRequires:	taglib-devel
%{?with_twolame:BuildRequires:	twolame-devel}
%{?with_udev:BuildRequires:	udev-devel >= 1:142}
BuildRequires:	vcdimager-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xorg-lib-libXpm-devel
%{?with_mozilla:BuildRequires:	xorg-lib-libXt-devel}
BuildRequires:	xosd-devel
%{?with_mozilla:BuildRequires:	xulrunner-devel >= 1.9.2}
#BuildRequires:	xvid-devel
BuildRequires:	zvbi-devel
Requires:	xdg-utils
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

%package alsa
Summary:	VLC - ALSA audio output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia dźwięku ALSA
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description alsa
ALSA audio output plugin for VLC.

%description alsa -l pl.UTF-8
Wtyczka wyjścia dźwięku ALSA dla klienta VLC.

%package lua
Summary:	VLC - Lua plugins
Summary(pl.UTF-8):	Klient VLC - wtyczki Lua
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description lua
Lua plugins for VLC.

%description lua -l pl.UTF-8
Wtyczki Lua dla klienta VLC.

%package solid
Summary:	VLC - actions for Solid
Summary(pl.UTF-8):	Klient VLC - akcje dla Solid
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description solid
VLC actions for Solid.

%description solid -l pl.UTF-8
Akcje klienta VLC dla Solid.

%package -n browser-plugin-%{name}
Summary:	VLC - Mozilla compatible browser plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka do przeglądarki Mozilla
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})

%description -n browser-plugin-%{name}
Mozilla compatible browser plugin.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka do przeglądarki internetowej Mozilla.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cp -f /usr/share/automake/config.* .
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses -I/usr/include/xulrunner/stable -I/usr/include/liveMedia" \
	--enable-shared \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
%ifarch ppc
	--disable-altivec \
%endif
	--disable-hd1000v \
	--disable-macosx \
	--%{?with_aalib:en}%{!?with_aalib:dis}able-aa \
	%{?with_alsa:--enable-alsa} \
	%{!?with_bonjour:--disable-bonjour} \
	--%{?with_caca:en}%{!?with_caca:dis}able-caca \
	%{!?with_daap:--disable-daap} \
	--enable-dbus \
	%{?with_dirac:--enable-dirac} \
	%{?with_directfb:--enable-directfb} \
	--%{?with_dv:en}%{!?with_dv:dis}able-dv \
	--enable-dvb \
	--enable-dvbpsi \
	--enable-dvdnav \
	--enable-dvdread \
	--enable-faad \
	--enable-fb \
	--enable-freetype \
	--enable-fribidi \
	--enable-avcodec \
	--enable-flac \
	--%{?with_ggi:en}%{!?with_ggi:dis}able-ggi \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	%{!?with_gnutls:--disable-gnutls} \
	%{?with_jack:--enable-jack} \
	--%{?with_lirc:en}%{!?with_lirc:dis}able-lirc \
	--enable-mad \
	%{?with_mozilla:--enable-mozilla } \
	--enable-libva \
	%{?with_live:--enable-live555 } \
	%{!?with_live:--disable-live555 } \
	--enable-ncurses \
	%{!?with_notify:--disable-notify} \
	--%{?with_portaudio:en}%{!?with_portaudio:dis}able-portaudio \
	--enable-pvr \
	--enable-real \
	--enable-realrtsp \
	--enable-sdl \
	--enable-shared \
	%{?with_shout:--enable-shout} \
	--enable-skins2 \
	--enable-smb \
	--enable-snapshot \
	--enable-sout \
	--enable-sqlite \
	--enable-switcher \
	%{!?with_speex:--disable-speex} \
	%{?with_svg:--enable-svg} \
	%{?with_svgalib:--enable-svgalib} \
	--enable-telepathy \
	--enable-theora \
	--enable-tremor \
	%{?with_twolame:--enable-twolame} \
	%{!?with_udev:--disable-udev} \
	%{?with_upnp:--enable-upnp} \
	--enable-v4l\
	--enable-vcdx \
	%{!?with_x264:--disable-x264} \
	--enable-xosd \
	--enable-oss \
	%{!?with_hal:--disable-hal} \
	%{!?with_projectM:--disable-projectm} \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations

%{__make} \
	npvlcdir=%{_browserpluginsdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	npvlcdir=%{_browserpluginsdir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/vlc

%if "%{_lib}" != "lib"
install -d $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf %{_libdir}/vlc $RPM_BUILD_ROOT%{_prefix}/lib
%endif

# rm -f *.{a,la}
find $RPM_BUILD_ROOT%{_libdir} -type f -regex '.*\.?a$' | xargs %{__rm}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}
# unsupported:
# ckb (Sorani Kurdish - maybe ku_IQ/ku_IR?)
# co (Corsican)
# tet (Tetum)
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ach,cgg,ckb,co,ff,tet}

# .ico is win32 only
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/vlc*.ico

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post   -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README THANKS
%doc doc/bugreport-howto.txt
%doc doc/intf-vcd.txt doc/translations.txt
%attr(755,root,root) %{_bindir}/cvlc
%attr(755,root,root) %{_bindir}/nvlc
%attr(755,root,root) %{_bindir}/rvlc
%attr(755,root,root) %{_bindir}/vlc
%attr(4754,root,video) %{_bindir}/vlc-wrapper
%attr(755,root,root) %{_libdir}/vlc/vlc-cache-gen
%attr(755,root,root) %{_libdir}/libvlc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvlc.so.5
%attr(755,root,root) %{_libdir}/libvlccore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvlccore.so.4

%if "%{_lib}" != "lib"
%{_prefix}/lib/vlc
%endif
%dir %{_libdir}/vlc
%dir %{_libdir}/vlc/plugins
%dir %{_libdir}/vlc/plugins/access
%{?with_alsa:%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_alsa_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_attachment_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_avio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_bd_plugin.so
%{?with_dv:%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_dv_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_fake_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_ftp_plugin.so
%{?with_gnomevfs:%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_gnomevfs_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_imem_plugin.so
%{?with_jack:%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_mmap_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_mms_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_mtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_oss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_realrtsp_plugin.so
%{?with_rtmp:%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_rtmp_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_smb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_tcp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_udp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libcdda_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdc1394_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvdnav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvdread_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libfilesystem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libpvr_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/librtp_plugin.so
#%attr(755,root,root) %{_libdir}/vlc/plugins/access/libv4l_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libv4l2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvcd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvcdx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libzip_plugin.so
%dir %{_libdir}/vlc/plugins/access_output
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_http_plugin.so
%{?with_rtmp:%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_rtmp_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_shout_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_udp_plugin.so
%dir %{_libdir}/vlc/plugins/audio_filter
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/liba52tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/liba52tospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libaudio_format_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
#%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libbandlimited_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libconverter_fixed_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libdtstofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libdtstospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libequalizer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libmono_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libmpgatofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libnormvol_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libparam_eq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libscaletempo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libsimple_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libspatializer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libtrivial_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libugly_resampler_plugin.so
%dir %{_libdir}/vlc/plugins/audio_mixer
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_mixer/libfloat32_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_mixer/libspdif_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_mixer/libtrivial_mixer_plugin.so
%dir %{_libdir}/vlc/plugins/audio_output
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libalsa_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libaout_file_plugin.so
%{?with_jack:%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libjack_plugin.so}
%{?with_portaudio:%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libportaudio_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/liboss_plugin.so
%dir %{_libdir}/vlc/plugins/codec
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liba52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaes3_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libadpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaraw_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libavcodec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcdg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcvdsub_plugin.so
%{?with_dirac:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libdirac_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libdts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libdvbsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libfaad_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libfake_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libflac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libinvmem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libkate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblibass_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblibmpeg2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libmpeg_audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libpng_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/librawvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/librealvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libschroedinger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsdl_image_plugin.so
%{?with_speex:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libspeex_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libspudec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsubsdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsubsusf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libt140_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtelx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtheora_plugin.so
%{?with_twolame:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtwolame_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvorbis_plugin.so
%{?with_x264:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libx264_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libzvbi_plugin.so
%dir %{_libdir}/vlc/plugins/control
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libdbus_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libgestures_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libglobalhotkeys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libhotkeys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/liboldhttp_plugin.so
%{?with_lirc:%attr(755,root,root) %{_libdir}/vlc/plugins/control/liblirc_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libmotion_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libnetsync_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/liboldrc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libsignals_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/liboldtelnet_plugin.so
%dir %{_libdir}/vlc/plugins/demux
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libaiff_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libasf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libau_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libavformat_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libavi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemux_cdg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemuxdump_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdirac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libes_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libflacsys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libgme_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libh264_plugin.so
%{?with_live:%attr(755,root,root) %{_libdir}/vlc/plugins/demux/liblive555_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmkv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmod_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmpc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmpgv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libnsc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libnsv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libnuv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libplaylist_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libpva_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/librawaud_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/librawdv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/librawvid_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libreal_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libsmf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libsubtitle_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libtta_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libty_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libvc1_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libvobsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libvoc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libwav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libxa_plugin.so
%dir %{_libdir}/vlc/plugins/gui
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libncurses_plugin.so
%dir %{_libdir}/vlc/plugins/meta_engine
%attr(755,root,root) %{_libdir}/vlc/plugins/meta_engine/libfolder_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/meta_engine/libtaglib_plugin.so
%dir %{_libdir}/vlc/plugins/misc
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libaudioscrobbler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libexport_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libfreetype_plugin.so
%{?with_gnutls:%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libgnutls_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/liblua_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libinhibit_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/liblogger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libsqlite_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxdg_screensaver_plugin.so

%ifarch %{ix86} %{x8664}
%dir %{_libdir}/vlc/plugins/3dnow
%attr(755,root,root) %{_libdir}/vlc/plugins/3dnow/libmemcpy3dn_plugin.so
%endif

%{?with_notify:%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libnotify_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libosd_parser_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libstats_plugin.so
%{?with_svg:%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libsvg_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libtelepathy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libvod_rtsp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxosd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxtag_plugin.so

%ifarch %{ix86} %{x8664}
%dir %{_libdir}/vlc/plugins/mmx
%attr(755,root,root) %{_libdir}/vlc/plugins/mmx/libi420_rgb_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mmx/libi420_yuy2_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mmx/libi422_yuy2_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mmx/libmemcpymmx_plugin.so
%dir %{_libdir}/vlc/plugins/mmxext
%attr(755,root,root) %{_libdir}/vlc/plugins/mmxext/libmemcpymmxext_plugin.so
%ifnarch i486 i586
%dir %{_libdir}/vlc/plugins/sse2
%attr(755,root,root) %{_libdir}/vlc/plugins/sse2/libi420_rgb_sse2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/sse2/libi420_yuy2_sse2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/sse2/libi422_yuy2_sse2_plugin.so
%endif
%endif

%dir %{_libdir}/vlc/plugins/mux
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_asf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_avi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_mp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_mpjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_ogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_ps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_ts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/mux/libmux_wav_plugin.so
%dir %{_libdir}/vlc/plugins/packetizer
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_copy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_dirac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_h264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so
%dir %{_libdir}/vlc/plugins/services_discovery
#%%{?with_hal:%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libhal_plugin.so}
%{?with_bonjour:%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libbonjour_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libmediadirs_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libmtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libpodcast_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libsap_plugin.so
%{?with_udev:%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libudev_plugin.so}
%{?with_upnp:%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libupnp_intel_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libxcb_apps_plugin.so
%dir %{_libdir}/vlc/plugins/stream_filter
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libdecomp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libstream_filter_rar_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libstream_filter_record_plugin.so
%dir %{_libdir}/vlc/plugins/stream_out
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_bridge_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_description_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_es_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_gather_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_raop_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_record_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_rtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_smem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_standard_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_switcher_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_transcode_plugin.so
%dir %{_libdir}/vlc/plugins/video_chroma
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_rgb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libyuy2_i422_plugin.so
%dir %{_libdir}/vlc/plugins/video_filter
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libadjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libaudiobargraph_v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libalphamask_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libatmo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libball_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libblend_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libblendbench_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libbluescreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcanvas_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libchain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libclone_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcolorthres_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcrop_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcroppadd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libdeinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libdynamicoverlay_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/liberase_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libextract_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgaussianblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgradient_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgrain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libinvert_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/liblogo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmagnify_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmarq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmirror_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmosaic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmotionblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmotiondetect_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libnoise_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libosdmenu_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpanoramix_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpostproc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpsychedelic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpuzzle_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libremoteosd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libripple_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/librotate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/librss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/librv32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libscene_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libsharpen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libswscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libtransform_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libvideo_filter_wrapper_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libwall_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libwave_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libyuvp_plugin.so
%dir %{_libdir}/vlc/plugins/video_output
%{?with_svgalib:%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libsvgalib_plugin.so}
%{?with_directfb:%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libdirectfb_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libsnapshot_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvmem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvout_wrapper_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libyuv_plugin.so
%dir %{_libdir}/vlc/plugins/visualization
%{?with_projectM:%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libvisual_plugin.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/http
%{_datadir}/%{name}/lua
%{_datadir}/%{name}/osdmenu
%dir %{_datadir}/%{name}/utils
%attr(755,root,root) %{_datadir}/%{name}/utils/*.sh

%{_mandir}/man1/vlc.1*
%{_mandir}/man1/vlc-wrapper.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
%attr(755,root,root) %{_libdir}/libvlc.so
%attr(755,root,root) %{_libdir}/libvlccore.so
%{_mandir}/man1/vlc-config.1*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qvlc
%attr(755,root,root) %{_bindir}/svlc
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libqt4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxscreensaver_plugin.so
%{?with_aalib:%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libaa_plugin.so}
%{?with_caca:%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libcaca_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_glx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_xv_plugin.so
%{_datadir}/%{name}/skins2
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.xpm
%{_desktopdir}/*.desktop

%if %{with ggi}
%files GGI
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libggi_plugin.so
%endif

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvout_sdl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libaout_sdl_plugin.so

%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libfb_plugin.so

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libalsa_plugin.so
%endif

%files lua
%defattr(644,root,root,755)
%{_libdir}/vlc/lua

%files solid
%defattr(644,root,root,755)
%{_datadir}/apps/solid/actions/vlc-*.desktop

%if %{with mozilla}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libvlcplugin.so
%{_datadir}/%{name}/mozilla
%endif
