#
# TODO:
# - flac plugin doesn't work with mono files
# - what really changes live bcond?
# - install mozilla plugin to some nice dir (now _libdir/mozilla/plugins/libvlcplugin.so)
# - why mozilla plugin is linked with libXt?
# - why mkv plugin is linked with libsysfs?
# - create specs and build plugins:
#	- libtar - http://www.feep.net/libtar
#	- tremor - http://xiph.org/vorbis
#	- goom - http://www.ios-software.com/?page=projet&quoi=1
#	- tarkin - http://xiph.org/vorbis (obsolete?)
#
# Conditional build:
%bcond_without	aalib	# build without aalib support
%bcond_without	alsa	# don't build alsa plugin
%bcond_without	arts	# don't build arts plugin
%bcond_without	bonjour # bonjour plugin
%bcond_without	caca	# build without caca support
%bcond_without	daap	# DAAP plugin
%bcond_without	dirac	# dirac plugin
%bcond_without	directfb	# directfb plugin
%bcond_without	dv	# build without dv support
%bcond_without	esound	# don't build esound plugin
%bcond_without	galaktos	# OpenGL visualisation plugin
%bcond_without	gnomevfs	# gnomevfs plugin
%bcond_without	gnutls	# gnutls plugin
%bcond_without	ggi	# don't build ggi plugin
%bcond_without	hal	# build with hal support
%bcond_without	jack	# jack audio module
%bcond_without	lirc	# build without lirc support
%bcond_without	live	# build without live.com support
%bcond_without	mozilla	# build mozilla plugin
%bcond_without	notify	# libnotify notification plugin
%bcond_without	portaudio	# portaudio library support
%bcond_without	shout	# shout plugin
%bcond_without	speex	# don't build speex plugin
%bcond_without	svg	# svg plugin
%bcond_without	twolame # twolame plugin
%bcond_without	svgalib	# build with svgalib video_output
%bcond_without	upnp	# upnp plugin
%bcond_without	x264	# build without x264 support
#
Summary:	VLC - a multimedia player and stream server
Summary(pl.UTF-8):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	0.8.6i
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
# use the bz2 src, its a 4mb difference
Source0:	http://download.videolan.org/pub/videolan/vlc/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	3c90520c9f22a68d287458d5a8af989e
Source1:	%{name}.desktop
Patch0:		%{name}-buildflags.patch
Patch1:		%{name}-defaultfont.patch
Patch2:		%{name}-live.patch
Patch3:		%{name}-pic-mmx.patch
Patch4:		%{name}-real_codecs_path.patch
Patch5:		%{name}-osdmenu_path.patch
Patch6:		%{name}-build.patch
Patch7:		%{name}-dirac.patch
Patch8:		%{name}-directfb.patch
URL:		http://www.videolan.org/vlc/
%{?with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	OpenGL-devel
%{?with_galaktos:BuildRequires:	 OpenGL-GLU-devel}
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	a52dec-libs-devel
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_bonjour:BuildRequires:	avahi-devel >= 0.6}
%{?with_dirac:BuildRequires:	dirac-devel}
%{?with_esound:BuildRequires:	esound-devel}
BuildRequires:	faad2-devel >= 2.5
BuildRequires:	ffmpeg-devel >= 0.4.9-4.20080131.1
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gettext-devel
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel}
%{?with_gnutls:BuildRequires:	gnutls-devel}
%{?with_hal:BuildRequires:	hal-devel >= 0.2.97}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_dv:BuildRequires:	libavc1394-devel}
%{?with_caca:BuildRequires:	libcaca-devel}
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libdts-devel
BuildRequires:	libdvbpsi-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libebml-devel >= 0.7.6
%{?with_ggi:BuildRequires:	libggi-devel}
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 0.7.5
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel >= 1.2.1
%{?with_notify:BuildRequires:	libnotify-devel}
BuildRequires:	libogg-devel
%{?with_daap:BuildRequires:	libopendaap-devel}
BuildRequires:	libpng-devel
%{?with_dv:BuildRequires:	libraw1394-devel}
%{?with_shout:BuildRequires:	libshout-devel}
BuildRequires:	libsmbclient-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
%{?with_upnp:BuildRequires:	libupnp-devel}
BuildRequires:	libvorbis-devel
%{?with_x264:BuildRequires:	libx264-devel}
BuildRequires:	libxml2-devel
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live >= 2005.03.11}
BuildRequires:	mpeg2dec-devel >= 0.3.2
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_portaudio:BuildRequires:	portaudio-devel}
%{?with_speex:BuildRequires:	speex-devel > 1:1.1.0}
%{?with_svg:BuildRequires:	librsvg-devel >= 2.9.0}
BuildRequires:	sysfsutils-devel
%{?with_svgalib:BuildRequires:	svgalib-devel}
%{?with_twolame:BuildRequires:	twolame-devel}
BuildRequires:	vcdimager-devel
BuildRequires:	wxGTK2-unicode-devel >= 2.6.2-2
%{?with_mozilla:BuildRequires:	xorg-lib-libXt-devel}
BuildRequires:	xosd-devel
%{?with_mozilla:BuildRequires:	xulrunner-devel}
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
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1

%build
cp -f /usr/share/automake/config.* .
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%configure \
%ifarch ppc
	--disable-altivec \
%endif
	--%{?with_aalib:en}%{!?with_aalib:dis}able-aa \
	%{?with_alsa:--enable-alsa} \
	%{?with_arts:--enable-arts} \
	%{!?with_arts:--disable-arts} \
	%{!?with_bonjour:--disable-bonjour} \
	--%{?with_caca:en}%{!?with_caca:dis}able-caca \
	--enable-cddax \
	%{!?with_daap:--disable-daap} \
	%{?with_dirac:--enable-dirac} \
	%{?with_directfb:--enable-directfb} \
	--%{?with_dv:en}%{!?with_dv:dis}able-dv \
	--enable-dvb \
	--enable-dvbpsi \
	--enable-dvdnav \
	--enable-dvdread \
	%{?with_esound:--enable-esd} \
	--enable-faad \
	--enable-fb \
	--enable-freetype \
	--enable-fribidi \
	--enable-ffmpeg \
	--enable-flac \
	%{?with_galaktos:--enable-galaktos} \
	--%{?with_ggi:en}%{!?with_ggi:dis}able-ggi \
	--disable-glide \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	%{!?with_gnutls:--disable-gnutls} \
	%{?with_jack:--enable-jack} \
	--%{?with_lirc:en}%{!?with_lirc:dis}able-lirc \
	--enable-mad \
	--enable-mga \
	%{?with_mozilla:--enable-mozilla } \
	%{?with_live:--enable-live555 } \
	%{!?with_live:--disable-live555 } \
	--with-live555-tree=%{_libdir}/liveMedia \
	--enable-ncurses \
	%{!?with_notify:--disable-notify} \
	%{?with_portaudio:--enable-portaudio} \
	--enable-pvr \
	--enable-real \
	--enable-realrtsp \
	--enable-sdl \
	%{?with_shout:--enable-shout} \
	--enable-skins2 \
	--enable-smb \
	--enable-snapshot \
	--enable-sout \
	%{!?with_speex:--disable-speex} \
	%{?with_svg:--enable-svg} \
	%{?with_svgalib:--enable-svgalib} \
	--enable-tarkin \
	--enable-theora \
	--enable-tremor \
	%{?with_twolame:--enable-twolame} \
	%{?with_upnp:--enable-upnp} \
	--enable-v4l\
	--enable-vcdx \
	--enable-x11 \
	%{!?with_x264:--disable-x264} \
	--enable-xosd \
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
%dir %{_libdir}/vlc/access
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_directory_plugin.so
%{?with_dv:%attr(755,root,root) %{_libdir}/vlc/access/libaccess_dv_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_fake_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_ftp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_mms_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_realrtsp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_smb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_tcp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_udp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libcdda_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libcddax_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvdnav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvdread_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libpvr_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libv4l_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libvcd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libvcdx_plugin.so
%dir %{_libdir}/vlc/access_filter
%attr(755,root,root) %{_libdir}/vlc/access_filter/libaccess_filter_dump_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_filter/libaccess_filter_record_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_filter/libaccess_filter_timeshift_plugin.so
%dir %{_libdir}/vlc/access_output
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_shout_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_udp_plugin.so
%dir %{_libdir}/vlc/audio_filter
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libaudio_format_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libbandlimited_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libdolby_surround_decoder_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libdtstospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libequalizer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfixed32tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfixed32tos16_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tos16_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tos8_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tou16_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tou8_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libheadphone_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liblinear_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libmpgatofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libnormvol_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libparam_eq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs16tofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs16tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs16tofloat32swab_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs8tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libsimple_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libtrivial_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libtrivial_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libu8tofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libu8tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libugly_resampler_plugin.so
%dir %{_libdir}/vlc/audio_mixer
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libfloat32_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libspdif_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libtrivial_mixer_plugin.so
%dir %{_libdir}/vlc/audio_output
%attr(755,root,root) %{_libdir}/vlc/audio_output/libaout_file_plugin.so
%{?with_arts:%attr(755,root,root) %{_libdir}/vlc/audio_output/libarts_plugin.so}
%{?with_jack:%attr(755,root,root) %{_libdir}/vlc/audio_output/libjack_plugin.so}
%{?with_portaudio:%attr(755,root,root) %{_libdir}/vlc/audio_output/libportaudio_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/audio_output/liboss_plugin.so
%dir %{_libdir}/vlc/codec
%attr(755,root,root) %{_libdir}/vlc/codec/liba52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libadpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libaraw_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcinepak_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcmml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcvdsub_plugin.so
%{?with_dirac:%attr(755,root,root) %{_libdir}/vlc/codec/libdirac_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/codec/libdts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libdvbsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libfaad_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libfake_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libffmpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libflacdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblibmpeg2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libmpeg_audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libpng_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/librawvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/librealaudio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsdl_image_plugin.so
%{?with_speex:%attr(755,root,root) %{_libdir}/vlc/codec/libspeex_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/codec/libspudec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsubsdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsvcdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libtelx_plugin.so
%{?with_twolame:%attr(755,root,root) %{_libdir}/vlc/codec/libtwolame_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/codec/libvorbis_plugin.so
%{?with_x264:%attr(755,root,root) %{_libdir}/vlc/codec/libx264_plugin.so}
%dir %{_libdir}/vlc/control
%attr(755,root,root) %{_libdir}/vlc/control/libgestures_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhotkeys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhttp_plugin.so
%{?with_lirc:%attr(755,root,root) %{_libdir}/vlc/control/liblirc_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/control/libnetsync_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/librc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libshowintf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libtelnet_plugin.so
%dir %{_libdir}/vlc/demux
%attr(755,root,root) %{_libdir}/vlc/demux/liba52sys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libaiff_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libasf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libau_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libavi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdemuxdump_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdtssys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libflac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libh264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libid3tag_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm3u_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm4a_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm4v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmkv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmod_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpgv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnsc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnsv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnuv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libplaylist_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libpva_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/librawdv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libreal_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libsgimb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libsubtitle_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libtta_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libty_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libvobsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libvoc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libwav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libxa_plugin.so
%dir %{_libdir}/vlc/gui
%attr(755,root,root) %{_libdir}/vlc/gui/libncurses_plugin.so
%dir %{_libdir}/vlc/misc
%attr(755,root,root) %{_libdir}/vlc/misc/libdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libexport_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libfreetype_plugin.so
%{?with_gnutls:%attr(755,root,root) %{_libdir}/vlc/misc/libgnutls_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/misc/libgrowl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libipv4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libipv6_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/liblogger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libmemcpy_plugin.so
%{?with_notify:%attr(755,root,root) %{_libdir}/vlc/misc/libnotify_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/misc/libscreensaver_plugin.so
%{?with_svg:%attr(755,root,root) %{_libdir}/vlc/misc/libsvg_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/misc/libvod_rtsp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libxml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libxtag_plugin.so
%dir %{_libdir}/vlc/mux
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_asf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_avi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_mp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_mpjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_wav_plugin.so
%dir %{_libdir}/vlc/packetizer
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_copy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_h264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4video_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpegvideo_plugin.so
%dir %{_libdir}/vlc/services_discovery
%{?with_hal:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libhal_plugin.so}
%{?with_bonjour:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libbonjour_plugin.so}
%{?with_daap:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libdaap_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/services_discovery/libpodcast_plugin.so
%attr(755,root,root) %{_libdir}/vlc/services_discovery/libsap_plugin.so
%attr(755,root,root) %{_libdir}/vlc/services_discovery/libshout_plugin.so
%{?with_upnp:%attr(755,root,root) %{_libdir}/vlc/services_discovery/libupnp_intel_plugin.so}
%dir %{_libdir}/vlc/stream_out
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_bridge_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_description_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_duplicate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_es_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_gather_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_mosaic_bridge_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_rtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_standard_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_switcher_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_transcode_plugin.so
%dir %{_libdir}/vlc/video_chroma
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_rgb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_ymga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi422_yuy2_plugin.so
%dir %{_libdir}/vlc/video_filter
%attr(755,root,root) %{_libdir}/vlc/video_filter/libadjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libblend_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libclone_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libcrop_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdeinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdistort_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libinvert_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/liblogo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmagnify_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmarq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmosaic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmotionblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmotiondetect_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libosdmenu_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/librss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/librv32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libtime_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libtransform_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libwall_plugin.so
%dir %{_libdir}/vlc/video_output
%{?with_svgalib:%attr(755,root,root) %{_libdir}/vlc/video_output/libsvgalib_plugin.so}
%{?with_directfb:%attr(755,root,root) %{_libdir}/vlc/video_output/libdirectfb_plugin.so}
%attr(755,root,root) %{_libdir}/vlc//video_output/libsnapshot_plugin.so
%dir %{_libdir}/vlc/visualization
%attr(755,root,root) %{_libdir}/vlc/visualization/libvisual_plugin.so
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
%{?with_gnomevfs:%attr(755,root,root) %{_libdir}/vlc/access/libaccess_gnomevfs_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/access/libscreen_plugin.so
%{?with_aalib:%attr(755,root,root) %{_libdir}/vlc/video_output/libaa_plugin.so}
%{?with_caca:%attr(755,root,root) %{_libdir}/vlc/video_output/libcaca_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/video_output/libglx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libimage_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libmga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libopengl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libx11_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libxvideo_plugin.so
%{?with_galaktos:%attr(755,root,root) %{_libdir}/vlc/visualization/libgalaktos_plugin.so}
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

%if %{with esound}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libesd_plugin.so
%endif

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libalsa_plugin.so
%endif
