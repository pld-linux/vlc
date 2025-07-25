# TODO
# - subpackage more plugins (at least all built on bconds, better all having external dependencies)
# - use fonts-TTF-freefont as R (vlc-X11 package) (see also vlc-defaultfont.patch)
#   --with-default-font=/usr/share/vlc/skins2/fonts/FreeSans.ttf
#   ./modules/gui/skins2/parser/builder.cpp:            string path = (*it) + sep + "fonts" + sep + "FreeSans.ttf";
# - %{_prefix}/lib cleanup for x86_64
# - configs to /etc (../http/.hosts)
# - qvlc should be in qt5 or such package not generic X11
# - /usr/share/vlc/utils scripts insecure (use /tmp hardcoded paths)
# - [recheck old TODO]: flac plugin doesn't work with mono files
# - --enable-wma-fixed (fixed-point WMA - does it make sense on non-embedded?)
# - Hildon (hildon-1.pc hildon-fm-2.pc)
# - OSSO_SCREENSAVER (libosso.pc - Maemo platform)
# - mce (Maemo platform)
# - x262
# - x26410b (x264 >= 0.153)
# - evas (ecore >= 1.16)
# - AMF (AMD HQScaler, AMD VQ Enhancer components)
#
# Conditional build:
%bcond_without	aalib		# aalib video output plugin
%bcond_without	alsa		# ALSA access/audio output plugins
%bcond_without	bonjour		# bonjour service discovery plugin
%bcond_without	bpg		# BPG files support
%bcond_without	caca		# caca video output plugin
%bcond_without	crystalhd	# crystalhd codec plugin
%bcond_with	daala		# daala codec plugin (experimental)
%bcond_with	decklink	# Blackmagic DeskLink output support (BR: proprietary SDK)
%bcond_without	dv		# dv access plugins
%bcond_with	fdk_aac		# FDK-AAC encoder plugin (GPL 3 incompatible; enable as subpackage?)
%bcond_with	fluidlite	# FluidLite instead of FluidSynth library in fluidsynth plugin
%bcond_with	freerdp		# RDP/Remote Desktop client support
%bcond_with	glesv1		# OpenGL ES v1 support
%bcond_with	glesv2		# OpenGL ES v2 support
%bcond_without	gnutls		# gnutls misc plugin
%bcond_without	goom		# GOOM! audio visualization
%bcond_without	jack		# jack access/audio output plugin
%bcond_with	kde		# KDE Solid actions
%bcond_without	lirc		# lirc control plugin
%bcond_with	libplacebo	# libplacebo support in gl plugin
%bcond_without	live		# live555 demuxer plugin
%bcond_with	mfx		# Intel QuickSync MPEG4-Part10/MPEG2 (H.264/H.262) encoder
%bcond_without	notify		# libnotify notification plugin
%bcond_with	opencv		# OpenCV video filter [needs vlc API update]
%bcond_with	oss4		# OSSv4
%bcond_with	projectM	# projectm visualization plugin
%bcond_without	sftp		# SFTP file transfer via libssh2
%bcond_without	shout		# shout access output plugin
%bcond_without	smb		# SMB access plugin
%bcond_without	smb2		# SMB2 access plugin
%bcond_without	speex		# speex codec plugin
%bcond_without	svg		# svg text renderer plugin
%bcond_without	twolame		# twolame codec plugin
%bcond_without	udev		# udev service discovery plugin
%bcond_without	upnp		# upnp service discovery plugin
%bcond_without	vsxu		# Vovoid VSXu visualization plugin
%bcond_without	x264		# x264 codec plugin
%bcond_without	x265		# x265 codec plugin
%bcond_without	xmas		# disable "xmas joke" icons provided by vlc [unmaintained patch]

%define		qt_ver	5.5.0

%ifnarch i686 pentium4 athlon %{x8664} x32
# CrystalHD library requires SSE2 instructions
%undefine	with_crystalhd
%endif
Summary:	VLC - a multimedia player and stream server
Summary(pl.UTF-8):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	3.0.21
Release:	8
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	https://download.videolan.org/pub/videolan/vlc/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	cde72f38943c685a1a39acc82da2339f
Patch0:		%{name}-buildflags.patch
Patch1:		%{name}-tremor.patch
Patch2:		%{name}-mpc.patch
Patch3:		xmas-sucks.patch
Patch4:		no-cache.patch
Patch5:		%{name}-fdk_aac.patch
Patch6:		%{name}-asdcplib.patch
Patch7:		%{name}-vsxu.patch
Patch8:		qt-5.15.patch
Patch9:		x32.patch
Patch10:	%{name}-libplacebo-5.patch
Patch11:	opencv4.patch
Patch12:	ffmpeg6.patch
Patch13:	%{name}-taglib2.patch
Patch14:	%{name}-x265.patch
Patch15:	%{name}-live555-update.patch
URL:		http://www.videolan.org/vlc/
%{?with_decklink:BuildRequires:	Blackmagic_DeckLink_SDK}
# 1.0 for X11 or GLESv1, 1.1 for GLESv2
BuildRequires:	EGL-devel >= %{?with_glesv2:1.1}%{!?with_glesv2:1.0}
BuildRequires:	OpenGL-devel
%{?with_glesv1:BuildRequires:	OpenGLESv1-devel >= 1.1}
%{?with_glesv2:BuildRequires:	OpenGLESv2-devel >= 2.0}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	SDL_image-devel >= 1.2.10
BuildRequires:	a52dec-libs-devel >= 0.7.3
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.24}
BuildRequires:	aom-devel
BuildRequires:	aribb24-devel >= 1.0.1
BuildRequires:	aribb25-devel >= 0.2.6
BuildRequires:	asdcplib-devel >= 2.12.2
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
%{?with_bonjour:BuildRequires:	avahi-devel >= 0.6}
%{?with_svg:BuildRequires:	cairo-devel >= 1.13.1}
%{?with_daala:BuildRequires:	daala-devel}
BuildRequires:	dav1d-devel
BuildRequires:	dbus-devel >= 1.6.0
BuildRequires:	desktop-file-utils
BuildRequires:	faad2-devel >= 2.5
%{?with_fdk_aac:BuildRequires:	fdk-aac-devel}
# libavcodec >= 57.37.100, libavformat >= 53.21.0, libavutil >= 52.4.0, libswscale, libpostproc
BuildRequires:	ffmpeg-devel >= 3.1
BuildRequires:	flac-devel >= 1.1.3
%if %{with fluidlite}
BuildRequires:	fluidlite-devel
%else
BuildRequires:	fluidsynth-devel >= 1.1.2
%endif
BuildRequires:	fontconfig-devel >= 1:2.11
%{?with_freerdp:BuildRequires:	freerdp-devel >= 1.0.1}
BuildRequires:	freetype-devel >= 2
BuildRequires:	fribidi-devel
BuildRequires:	game-music-emu-devel
BuildRequires:	gettext-tools >= 0.19.8
%{?with_gnutls:BuildRequires:	gnutls-devel >= 3.3.6}
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
%{?with_notify:BuildRequires:	gtk+3-devel >= 3.0}
BuildRequires:	harfbuzz-devel
# >= 0.120.1 < 1.0 or >= 1.9.7
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.120.1}
%{?with_kde:BuildRequires:	kde4-kdelibs}
BuildRequires:	libarchive-devel >= 3.1.0
BuildRequires:	libass-devel >= 0.9.8
%{?with_dv:BuildRequires:	libavc1394-devel >= 0.5.3}
BuildRequires:	libbluray-devel >= 0.6.2
%{?with_bpg:BuildRequires:	libbpg-devel}
%{?with_caca:BuildRequires:	libcaca-devel >= 0.99-0.beta20}
BuildRequires:	libcddb-devel >= 0.9.5
BuildRequires:	libcdio-devel >= 0.78.2
BuildRequires:	libchromaprint-devel >= 0.6.0
%{?with_crystalhd:BuildRequires:	libcrystalhd-devel}
BuildRequires:	libdc1394-devel >= 2.1.0
BuildRequires:	libdsm-devel >= 0.2.0
BuildRequires:	libdts-devel >= 0.0.5
BuildRequires:	libdvbpsi-devel >= 1.2.0
BuildRequires:	libdvdnav-devel > 4.9.0
BuildRequires:	libdvdread-devel >= 4.9.1
BuildRequires:	libebml-devel >= 1.3.6
BuildRequires:	libgcrypt-devel >= 1.6.0
%{?with_goom:BuildRequires:	libgoom2-devel}
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libkate-devel >= 0.3.0
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 1.0.0
BuildRequires:	libmodplug-devel >= 0.8.9.0
BuildRequires:	libmpeg2-devel > 0.3.2
BuildRequires:	libmpg123-devel
BuildRequires:	libmtp-devel >= 1.0.0
%{?with_notify:BuildRequires:	libnotify-devel}
BuildRequires:	libnfs-devel >= 1.10.0
BuildRequires:	libogg-devel >= 1:1.0
%{?with_libplacebo:BuildRequires:	libplacebo-devel >= 4}
BuildRequires:	libpng-devel
%{?with_projectM:BuildRequires:	libprojectM-devel >= 2.0.1-3}
BuildRequires:	libproxy-devel
%{?with_dv:BuildRequires:	libraw1394-devel >= 2.0.1}
%{?with_svg:BuildRequires:	librsvg-devel >= 2.9.0}
BuildRequires:	libsamplerate-devel
BuildRequires:	libsecret-devel >= 0.18
%{?with_shout:BuildRequires:	libshout-devel >= 2.1}
BuildRequires:	libsidplay2-devel
%{?with_smb2:BuildRequires:	libsmb2-devel >= 4.0.0}
%{?with_smb:BuildRequires:	libsmbclient-devel >= 3.6.13}
%{?with_sftp:BuildRequires:	libssh2-devel}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtar-devel
BuildRequires:	libtheora-devel >= 1.0
BuildRequires:	libtiger-devel >= 0.3.1
BuildRequires:	libtool >= 2:2
%{?with_upnp:BuildRequires:	libupnp-devel}
BuildRequires:	libv4l-devel
BuildRequires:	libva-devel >= 0.38
BuildRequires:	libva-drm-devel
BuildRequires:	libva-wayland-devel
BuildRequires:	libva-x11-devel
BuildRequires:	libvdpau-devel >= 0.6
BuildRequires:	libvncserver-devel >= 0.9.9
BuildRequires:	libvorbis-devel >= 1:1.1
BuildRequires:	libvpx-devel >= 1.5.0
# x264.pc >= 0.148
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.3-1.20190110_2245.1}
%{?with_x265:BuildRequires:	libx265-devel}
# xcb >= 1.6, xcb-shm, xcb-composite, xcb-xv >= 1.1.90.1, xcb-randr >= 1.3
BuildRequires:	libxcb-devel >= 1.6
BuildRequires:	libxml2-devel >= 1:2.5
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel >= 2020.12.23}
BuildRequires:	lua52 >= 5.2
BuildRequires:	lua52-devel >= 5.2
%{?with_mfx:BuildRequires:	mfx_dispatch-devel}
BuildRequires:	microdns-devel >= 0.1.2
BuildRequires:	minizip-devel
BuildRequires:	musepack-devel
BuildRequires:	ncurses-devel
%{?with_opencv:BuildRequires:	opencv-devel > 4}
BuildRequires:	opus-devel >= 1.0.3
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	protobuf-devel >= 2.5.0
BuildRequires:	pulseaudio-devel >= 1.0
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	schroedinger-devel >= 1.0.10
BuildRequires:	shine-devel >= 3.0.0
BuildRequires:	soxr-devel >= 0.1.2
BuildRequires:	spatialaudio-devel
%{?with_speex:BuildRequires:	speex-devel > 1:1.1.0}
%{?with_speex:BuildRequires:	speexdsp-devel >= 1.2}
BuildRequires:	srt-devel >= 1.3.0
BuildRequires:	sysfsutils-devel
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	taglib-devel >= 1.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	tpm2-tss-devel
BuildRequires:	tremor-devel
%{?with_twolame:BuildRequires:	twolame-devel}
%{?with_udev:BuildRequires:	udev-devel >= 1:142}
%{?with_vsxu:BuildRequires:	vsxu-devel}
BuildRequires:	wayland-devel >= 1.5.91
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.4
BuildRequires:	xcb-util-keysyms-devel >= 0.3.4
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRequires:	zvbi-devel >= 0.2.28
Requires(post):	/sbin/ldconfig
Requires:	SDL_image >= 1.2.10
%{?with_alsa:Requires:	alsa-lib >= 1.0.24}
Requires:	aribb24 >= 1.0.1
Requires:	aribb25 >= 0.2.6
%{?with_svg:Requires:	cairo >= 1.13.1}
%if %{without fluidlite}
Requires:	fluidsynth >= 1.1.2
%endif
Requires:	fontconfig-libs >= 1:2.11
%{?with_gnutls:Requires:	gnutls >= 3.3.6}
Requires:	libarchive >= 3.1.0
Requires:	libass >= 0.9.8
Requires:	libbluray >= 0.6.2
Requires:	libcddb >= 0.9.5
Requires:	libchromaprint >= 0.6.0
Requires:	libdsm >= 0.2.0
Requires:	libdvbpsi >= 1.2.0
Requires:	libebml >= 1.3.6
Requires:	libgcrypt >= 1.6.0
Requires:	libkate >= 0.3.0
Requires:	libmodplug >= 0.8.9.0
Requires:	libmpeg2 > 0.3.2
Requires:	libmtp >= 1.0.0
Requires:	libnfs >= 1.10.0
Requires:	libogg >= 1:1.0
%{?with_libplacebo:Requires:	libplacebo >= 4}
%{?with_svg:Requires:	librsvg >= 2.9.0}
Requires:	libsecret >= 0.18
%{?with_smb2:Requires:	libsmb2 >= 4.0.0}
Requires:	libtheora >= 1.0
Requires:	libtiger >= 0.3.1
Requires:	libvncserver >= 0.9.9
Requires:	libvorbis >= 1:1.1
Requires:	libvpx >= 1.5.0
Requires:	libxcb >= 1.6
Requires:	libxml2 >= 1:2.5
Requires:	lua52-libs > 5.2.3-2
Requires:	microdns >= 0.1.2
Requires:	opus >= 1.0.3
Requires:	pulseaudio-libs >= 1.0
Requires:	schroedinger >= 1.0.10
Requires:	soxr >= 0.1.2
%{?with_speex:Requires:	speex > 1:1.1.0}
%{?with_speex:Requires:	speexdsp >= 1.2}
Requires:	srt >= 1.3.0
Requires:	taglib >= 1.9
Requires:	wayland >= 1.5.91
Requires:	xcb-util-keysyms >= 0.3.4
Requires:	xdg-utils
Obsoletes:	browser-plugin-vlc < 2
Obsoletes:	vlc-GGI < 2
Obsoletes:	vlc-SDL < 2.2.6-3
Obsoletes:	vlc-esd < 1
Obsoletes:	vlc-iceweasel-plugin < 1.0.0-2
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
Requires:	dbus-devel >= 1.6.0
Obsoletes:	vlc-static < 1.0.0-3

%description devel
VLC header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe VLC.

%package X11
Summary:	VLC - X11 output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia X11
Group:		X11/Applications/Multimedia
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Gui-platform-xcb >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	desktop-file-utils
Requires:	hicolor-icon-theme
Suggests:	dbus-x11 >= 1.6.0
%{?with_caca:Suggests:	libcaca > 0.99-0.beta20}
Obsoletes:	vlc-gnome < 0.8.1-2
Obsoletes:	vlc-gnome1 < 0.8.1-2
Obsoletes:	vlc-gtk < 0.8.1-2

%description X11
X11 output plugin for VLC. Contains GUI image/icon resources.

%description X11 -l pl.UTF-8
Wtyczka wyjścia X11 dla klienta VLC. Zawiera zasoby interfejsu GUI
(obrazy/ikony).

%package fb
Summary:	VLC - fb output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia fb
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description fb
fb output plugin for VLC.

%description fb -l pl.UTF-8
Wtyczka wyjścia fb dla klienta VLC.

%package alsa
Summary:	VLC - ALSA audio output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia dźwięku ALSA
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib >= 1.0.24

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

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0
%if %{without xmas}
%patch -P3 -p1
%endif
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%{?with_libplacebo:%patch -P10 -p1}
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
# NOTE:
# --disable-optimizations is to use own RPM_OPT_FLAGS optimalizations
# iomx is Android-specific omxil codec option
%configure \
	BUILDCC="%{__cc}" \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses -I/usr/include/xulrunner/stable -I/usr/include/liveMedia" \
%if %{with decklink}
	CPPFLAGS_decklink=-I/usr/include/decklink \
	CPPFLAGS_decklinkoutput=-I/usr/include/decklink \
%endif
	LUAC=luac5.2 \
	--disable-optimizations \
	--disable-silent-rules \
	--disable-static \
%ifarch ppc
	--disable-altivec \
%endif
	--enable-aa%{!?with_aalib:=no} \
	%{?with_alsa:--enable-alsa} \
	--enable-aom \
	--enable-avcodec \
	%{!?with_bonjour:--disable-bonjour} \
	%{?with_bpg:--enable-bpg} \
	--enable-caca%{!?with_caca:=no} \
	--enable-crystalhd%{!?with_crystalhd:=no} \
	%{?with_daala:--enable-daala} \
	--enable-dbus \
	--enable-decklink%{!?with_decklink:=no} \
	--enable-dv1394%{!?with_dv:=no} \
	--enable-dvbpsi \
	--enable-dvdnav \
	--enable-dvdread \
	%{?with_fdk_aac:--enable-fdkaac} \
	--enable-faad \
	--enable-flac \
%if %{with fluidlite}
	--disable-fluidsynth \
%else
	--disable-fluidlite \
%endif
	%{?with_freerdp:--enable-freerdp}%{!?with_freerdp:--disable-freerdp} \
	--enable-freetype \
	--enable-fribidi \
	%{?with_glesv1:--enable-gles1} \
	%{?with_glesv2:--enable-gles2} \
	%{!?with_gnutls:--disable-gnutls} \
	--enable-goom%{!?with_goom:=no} \
	%{?with_jack:--enable-jack} \
	%{__enable_disable libplacebo} \
	--enable-lirc%{!?with_lirc:=no} \
	--enable-mad \
	--enable-libva \
	--enable-live555%{!?with_live:=no} \
	%{!?with_mfx:--disable-mfx} \
	--enable-ncurses \
	%{!?with_notify:--disable-notify} \
	--enable-omxil \
	--enable-omxil-vout \
	--enable-opencv%{!?with_opencv:=no} \
	--enable-oss%{!?with_oss4:=no} \
	%{!?with_projectM:--disable-projectm} \
	--enable-realrtsp \
	%{?with_sftp:--enable-sftp} \
	--enable-shared \
	--enable-shine \
	--enable-shout%{!?with_shout:=no} \
	--enable-skins2 \
	%{?with_smb2:--enable-smb2} \
	%{!?with_smb:--disable-smbclient} \
	--enable-sout \
	%{!?with_speex:--disable-speex} \
	%{!?with_svg:--disable-svg} \
	%{!?with_svg:--disable-svgdec} \
	--enable-theora \
	--enable-tremor \
	%{?with_twolame:--enable-twolame} \
	%{!?with_udev:--disable-udev} \
	%{?with_upnp:--enable-upnp} \
	--enable-v4l2 \
	%{!?with_vsxu:--disable-vsxu} \
	--enable-wayland \
	%{!?with_x264:--disable-x264} \
	%{!?with_x265:--disable-x265} \
	--with-default-font=/usr/share/vlc/skins2/fonts/FreeSans.ttf \
	--with-default-monospace-font=/usr/share/fonts/TTF/LiberationMono-Regular.ttf \
	--with-default-font-family=Sans \
	%{!?with_kde:--without-kde-solid}%{?with_kde:--with-kde-solid=%{_datadir}/apps/solid/actions}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dir for lua extensions
install -d $RPM_BUILD_ROOT%{_datadir}/vlc/lua/extensions

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/vlc

%if "%{_lib}" != "lib"
install -d $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf %{_libdir}/vlc $RPM_BUILD_ROOT%{_prefix}/lib
%endif

# rm -f *.{a,la}
find $RPM_BUILD_ROOT%{_libdir} -type f -regex '.*\.l?a$' | xargs %{__rm}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{as_IN,as}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{ks_IN,ks}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{or_IN,or}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{pt_PT,pt}
# am_ET: am_ET.po is more complete than am.po
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/am
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{am_ET,am}
# unsupported by glibc (as of 2.39):
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ach,cgg,co,ie,ku_IQ}

# .ico is win32 only
%{__rm} $RPM_BUILD_ROOT%{_datadir}/vlc/vlc*.ico

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins || :

%postun	-p /sbin/ldconfig

%post X11
%update_icon_cache hicolor
%update_desktop_database
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins || :

%postun X11
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
#%doc doc/bugreport-howto.txt
%doc doc/translations.txt
%attr(755,root,root) %{_bindir}/cvlc
%attr(755,root,root) %{_bindir}/nvlc
%attr(755,root,root) %{_bindir}/rvlc
%attr(755,root,root) %{_bindir}/vlc
%attr(4754,root,video) %{_bindir}/vlc-wrapper
%attr(755,root,root) %{_libdir}/vlc/vlc-cache-gen
%attr(755,root,root) %{_libdir}/libvlc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvlc.so.5
%attr(755,root,root) %{_libdir}/libvlccore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvlccore.so.9
%if "%{_lib}" != "lib"
%{_prefix}/lib/vlc
%endif
%dir %{_libdir}/vlc
%attr(755,root,root) %{_libdir}/vlc/libvlc_pulse.so.*.*.*
%attr(755,root,root) %{_libdir}/vlc/libvlc_pulse.so.0
# R: libX11
%attr(755,root,root) %{_libdir}/vlc/libvlc_vdpau.so.*.*.*
%attr(755,root,root) %{_libdir}/vlc/libvlc_vdpau.so.0
%attr(755,root,root) %{_libdir}/vlc/libvlc_xcb_events.so.*.*.*
%attr(755,root,root) %{_libdir}/vlc/libvlc_xcb_events.so.0

%dir %{_libdir}/vlc/plugins
%ghost %{_libdir}/vlc/plugins/plugins.dat
%dir %{_libdir}/vlc/plugins/access
%if %{with alsa}
# R: alsa-lib >= 1.0.24
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_alsa_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_concat_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_imem_plugin.so
%if %{with jack}
# R: jack-audio-connection-kit-libs >= 0.120.1 < 1.0 or >= 1.9.7 (depending on build)
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_jack_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_mms_plugin.so
# R: libmtp >= 1.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_mtp_plugin.so
%if %{with oss4}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_oss_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_realrtsp_plugin.so
# R: srt >= 1.3.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_srt_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libattachment_plugin.so
# R: ffmpeg-libs (libavformat >= 53.21.0 libavcodec libavutil)
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libavio_plugin.so
# R: asdcplib libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdcp_plugin.so
%if %{with dv}
# R: libraw1394 >= 2.0.1 libavc1394 >= 0.5.3
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdv1394_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libftp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libhttp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libhttps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libimem_plugin.so
# R: libnfs >= 1.10.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libnfs_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/librist_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsatip_plugin.so
%if %{with sftp}
# R: libssh2
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsftp_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libshm_plugin.so
%if %{with smb}
# R: libsmbclient
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsmb_plugin.so
%endif
%if %{with smb2}
# R: libsmb2 >= 3.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsmb2_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libtcp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libudp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvdr_plugin.so
# R: libcddb >= 0.9.5
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libcdda_plugin.so
# R: libraw1394 >= 2.0.1 libdc1394 >= 2.1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdc1394_plugin.so
%if %{with decklink}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdecklink_plugin.so
%endif
# R: libdsm >= 0.2.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdsm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdtv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvb_plugin.so
# R: libdvdnav >= 4.9.1
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvdnav_plugin.so
# R: libdvdread >= 4.9.1
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvdread_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libfilesystem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libidummy_plugin.so
# R: libbluray >= 0.6.2
%attr(755,root,root) %{_libdir}/vlc/plugins/access/liblibbluray_plugin.so
# R: libvncserver >= 0.9.9
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvnc_plugin.so
# R: zvbi >= 0.2.28
%attr(755,root,root) %{_libdir}/vlc/plugins/access/liblinsys_hdsdi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/liblinsys_sdi_plugin.so
%if %{with live}
# R: live
%attr(755,root,root) %{_libdir}/vlc/plugins/access/liblive555_plugin.so
%endif
# R: pulseaudio-libs >= 1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libpulsesrc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsdp_plugin.so
# R: freerdp >= 1.0.1
%{?with_freerdp:%attr(755,root,root) %{_libdir}/vlc/plugins/access/librdp_plugin.so}
# R: libgcrypt >= 1.1.94 (optional, for srtp functionality)
%attr(755,root,root) %{_libdir}/vlc/plugins/access/librtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libtimecode_plugin.so
%{?with_v4l1:%attr(755,root,root) %{_libdir}/vlc/plugins/access/libv4l_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libv4l2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvcd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
%dir %{_libdir}/vlc/plugins/access_output
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_http_plugin.so
# R: libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_livehttp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_rist_plugin.so
%if %{with shout}
# R: shout >= 2.1
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_shout_plugin.so
%endif
# R: srt >= 1.3.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_srt_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_udp_plugin.so
%dir %{_libdir}/vlc/plugins/audio_filter
# R: spatialaudio
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libspatialaudio_plugin.so
# R: a52dec-libs >= 0.7.3
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libaudio_format_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libcompressor_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libequalizer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libgain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libkaraoke_plugin.so
# R: libmad
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libmad_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libmono_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libnormvol_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libparam_eq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libremap_plugin.so
# R: libsamplerate
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libsamplerate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libscaletempo_pitch_plugin.so
# R: soxr >= 0.1.2
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libsoxr_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libscaletempo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libsimple_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libspatializer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libspeex_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libstereo_widen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libtospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libtrivial_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libugly_resampler_plugin.so
%dir %{_libdir}/vlc/plugins/audio_mixer
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_mixer/libfloat_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_mixer/libinteger_mixer_plugin.so
%dir %{_libdir}/vlc/plugins/audio_output
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libadummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libamem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libafile_plugin.so
%if %{with jack}
# R: jack-audio-connection-kit-libs >= 0.120.1 < 1.0 or >= 1.9.7 (depending on build)
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libjack_plugin.so
%endif
# R: pulseaudio-libs >= 1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so
%if %{with oss4}
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/liboss_plugin.so
%endif
%dir %{_libdir}/vlc/plugins/codec
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libdav1d_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liba52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaes3_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaom_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libadpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaraw_plugin.so
# R: aribb24 >= 1.0.1
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaribsub_plugin.so
# R: ffmpeg-libs (libavcodec >= 54.34.0 libavutil >= 51.22.0)
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libavcodec_plugin.so
# R: libbpg
%{?with_bpg:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libbpg_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcdg_plugin.so
%if %{with crystalhd}
# R: libcrystalhd
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcrystalhd_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcvdsub_plugin.so
# R: libdts >= 0.0.5
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libdca_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libddummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libdvbsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libedummy_plugin.so
# R: tremor
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtremor_plugin.so
# R: faad2-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libfaad_plugin.so
%if %{with fdk_aac}
# R: fdk-aac
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libfdkaac_plugin.so
%endif
# R: flac
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libflac_plugin.so
# R: fluidsynth >= 1.1.2 or fluidlite
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libg711_plugin.so
# R: gstreamer-plugins-base >= 1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libgstdecode_plugin.so
# R: libjpeg
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libjpeg_plugin.so
# R: libkate >= 0.3.0 libtiger >= 0.3.1
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libkate_plugin.so
# R: libass >= 0.9.8
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblibass_plugin.so
# R: libmpeg2-libs > 0.3.2
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblibmpeg2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblpcm_plugin.so
# R: libmpg123
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libmpg123_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liboggspots_plugin.so
# R: libomxil-bellagio (dlopened, no .so NEEDED dependency)
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libomxil_plugin.so
# R: libomxil-bellagio (dlopened, no .so NEEDED dependency)
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libomxil_vout_plugin.so
# R: opus >= 1.0.3
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libopus_plugin.so
# R: libpng
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libpng_plugin.so
%if %{with mfx}
# R: mfx_dispatch
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libqsv_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/librawvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/librtpvideo_plugin.so
# R: schroedinger >= 1.0.10
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libschroedinger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libscte18_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libscte27_plugin.so
# R: SDL_image >= 1.2.10
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsdl_image_plugin.so
# R: shine >= 3.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libshine_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libspdif_plugin.so
%if %{with speex}
# R: speex >= 1.0.5
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libspeex_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libspudec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libstl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsubsdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsubstx3g_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsubsusf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsvcdsub_plugin.so
%if %{with svg}
# R: cairo >= 1.13.1 librsvg >= 2.9.0
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsvgdec_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libt140_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtelx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtextst_plugin.so
# R: libtheora >= 1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtheora_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libttml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libuleaddvaudio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libwebvtt_plugin.so
%if %{with twolame}
# R: twolame-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtwolame_plugin.so
%endif
#%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvaapi_plugin.so
#%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvaapi_drm_plugin.so
# R: libvorbis >= 1.1
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvorbis_plugin.so
# R: libvpx >= 1.5.0
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvpx_plugin.so
# R: libx264
%{?with_x264:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libx264_plugin.so}
%{?with_x264:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libx26410b_plugin.so}
# R: libx265
%{?with_x265:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libx265_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libxwd_plugin.so
# R: zvbi >= 0.2.28
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libzvbi_plugin.so
%dir %{_libdir}/vlc/plugins/control
# R: dbus-libs >= 1.6.0
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libdbus_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libgestures_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libhotkeys_plugin.so
%if %{with lirc}
# R: lirc-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/control/liblirc_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libmotion_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libnetsync_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/control/liboldrc_plugin.so
# R: xcb-util-keysyms >= 0.3.4
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libxcb_hotkeys_plugin.so
%dir %{_libdir}/vlc/plugins/demux
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libadaptive_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libaiff_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libasf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libau_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libavformat_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libavi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libcaf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemux_cdg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemux_chromecast_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemux_stl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemuxdump_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdiracsys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdirectory_demux_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libes_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libflacsys_plugin.so
# R: game-music-emu
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libgme_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libh26x_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libimage_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmjpeg_plugin.so
# R: libebml >= 1.0.0 libmatroska >= 1.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmkv_plugin.so
# R: libmodplug >= 0.8.9.0
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmod_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmp4_plugin.so
# R: musepack-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmpc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmpgv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libnoseek_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libnsc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libnsv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libnuv_plugin.so
# R: libogg >= 1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libplaylist_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libpva_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/librawaud_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/librawdv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/librawvid_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libreal_plugin.so
# R: libsidplay2
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libsid_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libsmf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libsubtitle_plugin.so
# R: libdvbpsi >= 1.2.0
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libtta_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libty_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libvc1_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libvobsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libvoc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libwav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libxa_plugin.so
%dir %{_libdir}/vlc/plugins/gui
# R: ncurses
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libncurses_plugin.so
%dir %{_libdir}/vlc/plugins/keystore
%attr(755,root,root) %{_libdir}/vlc/plugins/keystore/libfile_keystore_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/keystore/libkwallet_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/keystore/libmemory_keystore_plugin.so
# R: libsecret >= 0.18
%attr(755,root,root) %{_libdir}/vlc/plugins/keystore/libsecret_plugin.so
%dir %{_libdir}/vlc/plugins/logger
%attr(755,root,root) %{_libdir}/vlc/plugins/logger/libconsole_logger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/logger/libfile_logger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/logger/libsd_journal_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/logger/libsyslog_plugin.so
%dir %{_libdir}/vlc/plugins/lua
# R: lua52
%attr(755,root,root) %{_libdir}/vlc/plugins/lua/liblua_plugin.so
%dir %{_libdir}/vlc/plugins/meta_engine
%attr(755,root,root) %{_libdir}/vlc/plugins/meta_engine/libfolder_plugin.so
# R: taglib >= 1.9
%attr(755,root,root) %{_libdir}/vlc/plugins/meta_engine/libtaglib_plugin.so
%dir %{_libdir}/vlc/plugins/misc
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libaddonsfsstorage_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libaddonsvorepository_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libaudioscrobbler_plugin.so
# R: dbus-libs >= 1.6.0
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libdbus_screensaver_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libexport_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libfingerprinter_plugin.so
%if %{with gnutls}
# R: gnutls >= 3.0.20
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libgnutls_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/liblogger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libstats_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libvod_rtsp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxdg_screensaver_plugin.so
# R: libxml2 >= 1:2.5
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxml_plugin.so
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

%if %{with notify}
%dir %{_libdir}/vlc/plugins/notify
# R: libnotify gtk+3
%attr(755,root,root) %{_libdir}/vlc/plugins/notify/libnotify_plugin.so
%endif

%dir %{_libdir}/vlc/plugins/packetizer
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_a52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_av1_plugin.so
# R: ffmpeg-libs (libavcodec >= 53.34.0 libavutil >= 51.22.0)
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_avparser_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_copy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_dirac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_dts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_h264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_hevc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegaudio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so
%dir %{_libdir}/vlc/plugins/services_discovery
%if %{with bonjour}
# R: avahi-libs >= 0.6
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libavahi_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libmediadirs_plugin.so
# R: microdns
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libmicrodns_plugin.so
# R: libmtp >= 1.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libmtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libpodcast_plugin.so
# R: pulseaudio-libs >= 1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libpulselist_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libsap_plugin.so
%if %{with udev}
# R: udev-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libudev_plugin.so
%endif
%if %{with upnp}
# R: libupnp
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libupnp_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libxcb_apps_plugin.so
%dir %{_libdir}/vlc/plugins/spu
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/libaudiobargraph_v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/libdynamicoverlay_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/liblogo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/libmarq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/libmosaic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/libremoteosd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/librss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/spu/libsubsdelay_plugin.so
%dir %{_libdir}/vlc/plugins/stream_extractor
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_extractor/libarchive_plugin.so
%dir %{_libdir}/vlc/plugins/stream_filter
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libadf_plugin.so
# R: aribb25 >= 0.2.6
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libaribcam_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libcache_block_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libcache_read_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libdecomp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libhds_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libinflate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libprefetch_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/librecord_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libskiptags_plugin.so
%dir %{_libdir}/vlc/plugins/stream_out
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_bridge_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_chromecast_plugin.so
# R: libchromaprint >= 0.6.0
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_chromaprint_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_cycle_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_delay_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_description_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_es_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_gather_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so
# R: libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_record_plugin.so
# R: libgcrypt >= 1.1.94 (optional, for srtp functionality)
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_rtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_stats_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_setid_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_smem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_standard_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_transcode_plugin.so
%dir %{_libdir}/vlc/plugins/text_renderer
# R: freetype >= 2 fribidi
%attr(755,root,root) %{_libdir}/vlc/plugins/text_renderer/libfreetype_plugin.so
# R: librsvg >= 2.9.0
%attr(755,root,root) %{_libdir}/vlc/plugins/text_renderer/libsvg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/text_renderer/libtdummy_plugin.so
%dir %{_libdir}/vlc/plugins/vaapi
%attr(755,root,root) %{_libdir}/vlc/plugins/vaapi/libvaapi_filters_plugin.so
# R: libvdpau >= 0.6 (all plugins in vdpau dir)
%dir %{_libdir}/vlc/plugins/vdpau
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_adjust_plugin.so
# R: + ffmpeg-libs (libavutil >= 52.4.0 libavcodec >= 55.42.100)
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_avcodec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_chroma_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_deinterlace_plugin.so
# R: + libX11 libxcb
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_sharpen_plugin.so
%dir %{_libdir}/vlc/plugins/video_chroma
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libchain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_10_p010_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_nv12_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_rgb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_plugin.so
%ifarch %{ix86} %{x8664} x32
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_rgb_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_mmx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_mmx_plugin.so
%ifnarch i386 i486 i586
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_rgb_sse2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_sse2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_sse2_plugin.so
%endif
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/librv32_plugin.so
# R: ffmpeg-libs (libswscale)
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libswscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libyuvp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libyuy2_i422_plugin.so
%dir %{_libdir}/vlc/plugins/video_filter
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libadjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libantiflicker_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libanaglyph_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libalphamask_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libball_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libblend_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libblendbench_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libbluescreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcanvas_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcolorthres_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcroppadd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libdeinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libedgedetection_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/liberase_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libextract_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libfps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libfreeze_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgaussianblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgradfun_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgradient_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgrain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libhqdn3d_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libinvert_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmagnify_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmirror_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmotionblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmotiondetect_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/liboldmovie_plugin.so
%if %{with opencv}
# R: opencv
#%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libposterize_plugin.so
# R: ffmpeg-libs (libpostproc libavutil)
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpostproc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpsychedelic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpuzzle_plugin.so
# R: libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libripple_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/librotate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libscene_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libsepia_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libsharpen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libtransform_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libwave_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libvhs_plugin.so
%dir %{_libdir}/vlc/plugins/video_output
%if %{with decklink}
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libdecklinkoutput_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libegl_wl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libflaschen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libglconv_vaapi_drm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libglconv_vaapi_wl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libglconv_vaapi_x11_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libglconv_vdpau_plugin.so
%if %{with glesv1}
# R: OpenGLESv1 >= 1.1
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libgles1_plugin.so
%endif
%if %{with glesv2}
# R: OpenGLESv2 >= 2.0
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libgles2_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libwl_shell_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libwl_shm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvmem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxdg_shell_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libyuv_plugin.so
%dir %{_libdir}/vlc/plugins/video_splitter
%attr(755,root,root) %{_libdir}/vlc/plugins/video_splitter/libclone_plugin.so
# R: libxcb >= 1.6
%attr(755,root,root) %{_libdir}/vlc/plugins/video_splitter/libpanoramix_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_splitter/libwall_plugin.so
%dir %{_libdir}/vlc/plugins/visualization
# R: OpenGL
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libglspectrum_plugin.so
# R: libgoom2
%{?with_goom:%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libgoom_plugin.so}
%if %{with projectM}
# R: libprojectM >= 2.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libvisual_plugin.so
%if %{with vsxu}
# R: vsxu-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libvsxu_plugin.so
%endif
%dir %{_datadir}/vlc
%dir %{_datadir}/vlc/utils
%attr(755,root,root) %{_datadir}/vlc/utils/*.sh
%{_datadir}/metainfo/vlc.appdata.xml

%{_mandir}/man1/vlc.1*
%{_mandir}/man1/vlc-wrapper.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvlc.so
%attr(755,root,root) %{_libdir}/libvlccore.so
%attr(755,root,root) %{_libdir}/vlc/libvlc_pulse.so
%attr(755,root,root) %{_libdir}/vlc/libvlc_vdpau.so
%attr(755,root,root) %{_libdir}/vlc/libvlc_xcb_events.so
%{_includedir}/vlc
%{_pkgconfigdir}/libvlc.pc
%{_pkgconfigdir}/vlc-plugin.pc

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qvlc
%attr(755,root,root) %{_bindir}/svlc
# R: QtCore QtGui >= %{qt_ver}
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libqt_plugin.so
# R: freetype libtar xorg-lib-lib{Xext,Xinerama,Xpm} QtCore QtGui
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%if %{with aalib}
# R: aalib
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libaa_plugin.so
%endif
%if %{with caca}
# R: libcaca >= 0.99-0.beta20
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libcaca_plugin.so
%endif
# R: EGL, xorg-lib-libX11
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libegl_x11_plugin.so
# R: OpenGL %{?with_libplacebo:libplacebo >= 0.2.1}
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libgl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libglx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so
# R: libxcb >= 1.6
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_xv_plugin.so
%{_datadir}/vlc/skins2
%{_iconsdir}/hicolor/*/apps/vlc*.png
%{_iconsdir}/hicolor/*/apps/vlc*.xpm
%{_desktopdir}/vlc.desktop

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
%{_datadir}/vlc/lua
%{_libdir}/vlc/lua

%if %{with kde}
%files solid
%defattr(644,root,root,755)
%{_datadir}/apps/solid/actions/vlc-*.desktop
%endif
