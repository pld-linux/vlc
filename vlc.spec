# TODO
# - use fonts-TTF-freefont as R
# - %{_prefix}/lib cleanup for x86_64
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
%bcond_without	esound		# don't build esound plugin
%bcond_without	galaktos	# OpenGL visualisation plugin
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
%bcond_without	shout		# shout plugin
%bcond_without	speex		# don't build speex plugin
%bcond_without	svg		# svg plugin
%bcond_without	svgalib		# build with svgalib video_output
%bcond_without	twolame		# twolame plugin
%bcond_without	udev		# udev services discovery
%bcond_without	upnp		# upnp plugin
%bcond_without	x264		# build without x264 support
#
Summary:	VLC - a multimedia player and stream server
Summary(pl.UTF-8):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	1.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
# use the bz2 src, its a 4mb difference
Source0:	http://download.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	3a0db00380b6d5b24dc7eb73e5d8ae51
Patch0:		%{name}-buildflags.patch
Patch1:		%{name}-defaultfont.patch
Patch2:		%{name}-real_codecs_path.patch
Patch3:		%{name}-osdmenu_path.patch
Patch4:		%{name}-rtp_segv.patch
Patch5:		%{name}-system-minizip.patch
URL:		http://www.videolan.org/vlc/
%{?with_directfb:BuildRequires:	DirectFB-devel}
%{?with_galaktos:BuildRequires:	OpenGL-GLU-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	QtGui-devel >= 4.2.0
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	a52dec-libs-devel
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_bonjour:BuildRequires:	avahi-devel >= 0.6}
BuildRequires:	dbus-devel
%{?with_dirac:BuildRequires:	dirac-devel}
%{?with_esound:BuildRequires:	esound-devel}
BuildRequires:	faad2-devel >= 2.5
BuildRequires:	ffmpeg-devel >= 0.4.9-4.20080131.1
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	fluidsynth-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gettext-devel
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel}
%{?with_gnutls:BuildRequires:	gnutls-devel}
%{?with_hal:BuildRequires:	hal-devel >= 0.2.97}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%if %{with dv}
BuildRequires:	libavc1394-devel
BuildRequires:	libraw1394-devel < 2.0.0
%endif
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdts-devel
BuildRequires:	libdvbpsi-devel >= 0.1.6
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libebml-devel >= 0.7.6
BuildRequires:	libgcrypt-devel
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 0.7.5
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libmpeg2-devel
BuildRequires:	libmtp-devel
%{?with_notify:BuildRequires:	libnotify-devel}
BuildRequires:	libogg-devel
%{?with_daap:BuildRequires:	libopendaap-devel}
BuildRequires:	libpng-devel
%{?with_dv:BuildRequires:	libraw1394-devel}
%{?with_svg:BuildRequires:	librsvg-devel >= 2.9.0}
%{?with_shout:BuildRequires:	libshout-devel}
BuildRequires:	libsmbclient-devel
BuildRequires:	libtar-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
%{?with_upnp:BuildRequires:	libupnp-devel}
BuildRequires:	libvorbis-devel
BuildRequires:	libv4l-devel
%{?with_x264:BuildRequires:	libx264-devel}
BuildRequires:	libxml2-devel
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel > 2009.07.09-3}
BuildRequires:	lua51-devel
BuildRequires:	minizip-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_portaudio:BuildRequires:	portaudio-devel}
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build
BuildRequires:	schroedinger-devel
%{?with_speex:BuildRequires:	speex-devel > 1:1.1.0}
%{?with_svgalib:BuildRequires:	svgalib-devel}
BuildRequires:	sysfsutils-devel
BuildRequires:	taglib-devel
%{?with_twolame:BuildRequires:	twolame-devel}
%{?with_udev:BuildRequires:	udev-devel >= 1:142}
BuildRequires:	vcdimager-devel
BuildRequires:	xorg-lib-libXpm-devel
%{?with_mozilla:BuildRequires:	xorg-lib-libXt-devel}
BuildRequires:	xosd-devel
%{?with_mozilla:BuildRequires:	xulrunner-devel}
BuildRequires:	xvid-devel
BuildRequires:	zvbi-devel
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

%package -n browser-plugin-%{name}
Summary:	VLC - Mozilla compatible browser plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka do przeglądarki Mozilla
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
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
	--disable-static \
%ifarch ppc
	--disable-altivec \
%endif
	--disable-gme \
	--disable-hd1000v \
	--disable-macosx \
	--disable-testsuite \
	--%{?with_aalib:en}%{!?with_aalib:dis}able-aa \
	%{?with_alsa:--enable-alsa} \
	%{!?with_bonjour:--disable-bonjour} \
	--%{?with_caca:en}%{!?with_caca:dis}able-caca \
	--enable-cddax \
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
	%{?with_galaktos:--enable-galaktos} \
	--%{?with_ggi:en}%{!?with_ggi:dis}able-ggi \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	%{!?with_gnutls:--disable-gnutls} \
	%{?with_jack:--enable-jack} \
	--%{?with_lirc:en}%{!?with_lirc:dis}able-lirc \
	--enable-mad \
	--enable-mga \
	%{?with_mozilla:--enable-mozilla } \
	%{?with_live:--enable-live555 } \
	%{!?with_live:--disable-live555 } \
	--enable-ncurses \
	%{!?with_notify:--disable-notify} \
	%{?with_portaudio:--enable-portaudio} \
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
	--enable-static \
	--enable-switcher \
	%{!?with_speex:--disable-speex} \
	%{?with_svg:--enable-svg} \
	%{?with_svgalib:--enable-svgalib} \
	--enable-tarkin \
	--enable-telepathy \
	--enable-theora \
	--enable-tremor \
	%{?with_twolame:--enable-twolame} \
	%{!?with_udev:--disable-udev} \
	%{?with_upnp:--enable-upnp} \
	--enable-v4l\
	--enable-vcdx \
	--enable-x11 \
	%{!?with_x264:--disable-x264} \
	--enable-xosd \
	--enable-oss \
	%{!?with_hal:--disable-hal} \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations

%{__make} \
	npvlcdir=%{_browserpluginsdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	npvlcdir=%{_browserpluginsdir} \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT/usr/share/doc/vlc

%if "%{_lib}" != "lib"
install -d $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf %{_libdir}/vlc $RPM_BUILD_ROOT%{_prefix}/lib
%endif

# rm -f *.{a,la}
find $RPM_BUILD_ROOT%{_libdir} -type f -regex '.*\.?a$' -exec rm -f {} ';'

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}
# needs fixed?
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ckb,co,my,no,ps,tet}

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
%doc AUTHORS MAINTAINERS NEWS README THANKS
%doc doc/bugreport-howto.txt doc/intf-cdda.txt
%doc doc/intf-vcd.txt doc/translations.txt
%attr(755,root,root) %{_bindir}/cvlc
%attr(755,root,root) %{_bindir}/nvlc
%attr(755,root,root) %{_bindir}/rvlc
%attr(755,root,root) %{_bindir}/vlc
%attr(4754,root,video) %{_bindir}/vlc-wrapper
%attr(755,root,root) %{_libdir}/libvlc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvlc.so.[0-9]
%attr(755,root,root) %{_libdir}/libvlccore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvlccore.so.[0-9]

%if "%{_lib}" != "lib"
%{_prefix}/lib/vlc
%endif
%dir %{_libdir}/vlc
%dir %{_libdir}/vlc/access
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_alsa_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_bd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_directory_plugin.so
%{?with_dv:%attr(755,root,root) %{_libdir}/vlc/access/libaccess_dv_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_fake_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_ftp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_http_plugin.so
%{?with_jack:%attr(755,root,root) %{_libdir}/vlc/access/libaccess_jack_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_mmap_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_mms_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_mtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_oss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_realrtsp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_rtmp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_smb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_tcp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_udp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libcdda_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libcddax_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvdnav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvdread_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libpvr_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/librtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libv4l_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libv4l2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libvcd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libvcdx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libx11_screen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libzip_plugin.so
%dir %{_libdir}/vlc/access_output
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_rtmp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_shout_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_udp_plugin.so
%dir %{_libdir}/vlc/audio_filter
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libaudio_format_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libbandlimited_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libconverter_fixed_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libconverter_float_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libdolby_surround_decoder_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libdtstospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libequalizer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libheadphone_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liblinear_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libmono_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libmpgatofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libnormvol_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libparam_eq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libscaletempo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libsimple_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libspatializer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libtrivial_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libtrivial_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libugly_resampler_plugin.so
%dir %{_libdir}/vlc/audio_mixer
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libfloat32_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libspdif_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libtrivial_mixer_plugin.so
%dir %{_libdir}/vlc/audio_output
%attr(755,root,root) %{_libdir}/vlc/audio_output/libaout_file_plugin.so
%{?with_jack:%attr(755,root,root) %{_libdir}/vlc/audio_output/libjack_plugin.so}
%{?with_portaudio:%attr(755,root,root) %{_libdir}/vlc/audio_output/libportaudio_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/audio_output/libpulse_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/liboss_plugin.so
%dir %{_libdir}/vlc/codec
%attr(755,root,root) %{_libdir}/vlc/codec/liba52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libaes3_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libadpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libaraw_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libavcodec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcdg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcmml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcvdsub_plugin.so
%{?with_dirac:%attr(755,root,root) %{_libdir}/vlc/codec/libdirac_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/codec/libdts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libdvbsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libfaad_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libfake_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libflac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libfluidsynth_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libinvmem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblibmpeg2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libmpeg_audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libpng_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/librawvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/librealaudio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/librealvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libschroedinger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsdl_image_plugin.so
%{?with_speex:%attr(755,root,root) %{_libdir}/vlc/codec/libspeex_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/codec/libspudec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsubsdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsubsusf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsvcdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libt140_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libtelx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libtheora_plugin.so
%{?with_twolame:%attr(755,root,root) %{_libdir}/vlc/codec/libtwolame_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/codec/libvorbis_plugin.so
%{?with_x264:%attr(755,root,root) %{_libdir}/vlc/codec/libx264_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/codec/libzvbi_plugin.so
%dir %{_libdir}/vlc/control
%attr(755,root,root) %{_libdir}/vlc/control/libdbus_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libgestures_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libglobalhotkeys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhotkeys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhttp_plugin.so
%{?with_lirc:%attr(755,root,root) %{_libdir}/vlc/control/liblirc_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/control/libmotion_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/librc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libshowintf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libsignals_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libtelnet_plugin.so
%dir %{_libdir}/vlc/demux
%attr(755,root,root) %{_libdir}/vlc/demux/libaiff_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libasf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libau_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libavformat_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libavi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdemux_cdg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdemuxdump_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdirac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libes_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libflacsys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libh264_plugin.so
%{?with_live:%attr(755,root,root) %{_libdir}/vlc/demux/liblive555_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/demux/libm4v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmkv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmod_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpgv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnsc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnsv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnuv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libplaylist_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libpva_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/librawaud_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/librawdv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/librawvid_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libreal_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libsmf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libsubtitle_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libtta_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libty_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libvc1_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libvobsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libvoc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libwav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libxa_plugin.so
%dir %{_libdir}/vlc/gui
%attr(755,root,root) %{_libdir}/vlc/gui/libncurses_plugin.so
%dir %{_libdir}/vlc/meta_engine
%attr(755,root,root) %{_libdir}/vlc/meta_engine/libfolder_plugin.so
%attr(755,root,root) %{_libdir}/vlc/meta_engine/libtaglib_plugin.so
%dir %{_libdir}/vlc/misc
%attr(755,root,root) %{_libdir}/vlc/misc/libaudioscrobbler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libexport_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libfreetype_plugin.so
%{?with_gnutls:%attr(755,root,root) %{_libdir}/vlc/misc/libgnutls_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/misc/liblua_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libinhibit_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/liblogger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libmemcpy_plugin.so

%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_libdir}/vlc/misc/libmemcpy3dn_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libmemcpymmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libmemcpymmxext_plugin.so
%endif

%{?with_notify:%attr(755,root,root) %{_libdir}/vlc/misc/libnotify_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/misc/libosd_parser_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libprobe_hal_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libscreensaver_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libstats_plugin.so
%{?with_svg:%attr(755,root,root) %{_libdir}/vlc/misc/libsvg_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/misc/libtelepathy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libvod_rtsp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libxml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libxosd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libxtag_plugin.so
%dir %{_libdir}/vlc/mux
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_asf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_avi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_mp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_mpjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_wav_plugin.so
%dir %{_libdir}/vlc/packetizer
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_copy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_dirac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_h264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mlp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4video_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpegvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_vc1_plugin.so
%dir %{_libdir}/vlc/services_discovery
%{?with_hal:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libhal_plugin.so}
%{?with_bonjour:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libbonjour_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/services_discovery/libmtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/services_discovery/libpodcast_plugin.so
%attr(755,root,root) %{_libdir}/vlc/services_discovery/libsap_plugin.so
%attr(755,root,root) %{_libdir}/vlc/services_discovery/libshout_plugin.so
%{?with_udev:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libudev_plugin.so}
%{?with_upnp:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libupnp_intel_plugin.so}
%dir %{_libdir}/vlc/stream_filter
%attr(755,root,root) %{_libdir}/vlc/stream_filter/libdecomp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_filter/libstream_filter_rar_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_filter/libstream_filter_record_plugin.so
%dir %{_libdir}/vlc/stream_out
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_autodel_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_bridge_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_description_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_duplicate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_es_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_gather_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_mosaic_bridge_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_raop_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_record_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_rtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_standard_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_transcode_plugin.so
%dir %{_libdir}/vlc/video_chroma
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libgrey_yuv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_rgb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_ymga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi422_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi422_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libyuy2_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libyuy2_i422_plugin.so

%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_rgb_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_ymga_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_yuy2_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi422_yuy2_mmx_plugin.so
%ifnarch i486 i586
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_rgb_sse2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_yuy2_sse2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi422_yuy2_sse2_plugin.so
%endif
%endif

%dir %{_libdir}/vlc/video_filter
%attr(755,root,root) %{_libdir}/vlc/video_filter/libadjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libalphamask_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libatmo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libblend_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libblendbench_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libbluescreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libcanvas_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libchain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libclone_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libcolorthres_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libcrop_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libcroppadd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdeinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdynamicoverlay_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/liberase_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libextract_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libgaussianblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libgradient_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libgrain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libinvert_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/liblogo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmagnify_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmarq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmosaic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmotionblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmotiondetect_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libnoise_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libosdmenu_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libpanoramix_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libpostproc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libpsychedelic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libpuzzle_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libremoteosd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libripple_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/librotate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/librss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/librv32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libscene_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libsharpen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libswscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libtransform_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libwall_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libwave_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libyuvp_plugin.so
%dir %{_libdir}/vlc/video_output
%attr(755,root,root) %{_libdir}/vlc/video_output/libdrawable_plugin.so
%{?with_svgalib:%attr(755,root,root) %{_libdir}/vlc/video_output/libsvgalib_plugin.so}
%{?with_directfb:%attr(755,root,root) %{_libdir}/vlc/video_output/libdirectfb_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/video_output/libsnapshot_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libvmem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libyuv_plugin.so
%dir %{_libdir}/vlc/visualization
%attr(755,root,root) %{_libdir}/vlc/visualization/libvisual_plugin.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/http
%{_datadir}/%{name}/lua
%if %{with mozilla}
%{_datadir}/%{name}/mozilla
%endif
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
%attr(755,root,root) %{_libdir}/vlc/gui/libqt4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/gui/libskins2_plugin.so
%{?with_aalib:%attr(755,root,root) %{_libdir}/vlc/video_output/libaa_plugin.so}
%{?with_caca:%attr(755,root,root) %{_libdir}/vlc/video_output/libcaca_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/video_output/libglx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libmga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libopengl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libx11_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libxvideo_plugin.so
%{?with_galaktos:%attr(755,root,root) %{_libdir}/vlc/visualization/libgalaktos_plugin.so}
%{_datadir}/%{name}/skins2
%{_datadir}/%{name}/vlc*.xpm
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

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libalsa_plugin.so
%endif

%if %{with mozilla}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libvlcplugin.so
%endif
