# TODO
# - subpackage more plugins (at least all built on bconds, better all having external dependencies)
# - use fonts-TTF-freefont as R (vlc-X11 package) (see also vlc-defaultfont.patch)
#   ./modules/misc/freetype.c:#define DEFAULT_FONT "/usr/share/vlc/skins2/fonts/FreeSans.ttf"
#   ./modules/gui/skins2/parser/builder.cpp:            string path = (*it) + sep + "fonts" + sep + "FreeSans.ttf";
# - %{_prefix}/lib cleanup for x86_64
# - configs to /etc (../http/.hosts)
# - qvlc should be in qt4 or such package not generic X11
# - /usr/share/vlc/utils scripts insecure (use /tmp hardcoded paths)
# - [recheck old TODO]: flac plugin doesn't work with mono files
# - --enable-wma-fixed (fixed-point WMA - does it make sense on non-embedded?)
# - decklink plugin (BR: Blackmagick DeckLink SDI, DeckLinkAPIDispatch.cpp) [proprietary?]
# - Hildon (hildon-1.pc hildon-fm-2.pc)
# - OSSO_SCREENSAVER (libosso.pc - Maemo platform)
# - mce (Maemo platform)
#
# Conditional build:
%bcond_without	aalib		# aalib video output plugin
%bcond_without	alsa		# ALSA access/audio output plugins
%bcond_without	bonjour		# bonjour service discovery plugin
%bcond_without	caca		# caca video output plugin
%bcond_without	crystalhd	# crystalhd codec plugin
%bcond_without	directfb	# directfb video output plugin
%bcond_without	dv		# dv access plugins
%bcond_with	fdk_aac		# FDK-AAC encoder plugin (GPL 3 incompatible; enable as subpackage?)
%bcond_without	gnomevfs	# gnomevfs access plugin
%bcond_without	gnutls		# gnutls misc plugin
%bcond_without	jack		# jack access/audio output plugin
%bcond_without	kde		# KDE Solid actions
%bcond_without	lirc		# lirc control plugin
%bcond_without	live		# live555 demuxer plugin
%bcond_with	mfx		# Intel QuickSync MPEG4-Part10/MPEG2 (H.264/H.262) encoder
%bcond_without	notify		# libnotify notification plugin
%bcond_without	opencv		# OpenCV video filter [needs vlc API update]
%bcond_with	oss4		# OSSv4
%bcond_without	projectM	# projectm visualization plugin
%bcond_without	sftp		# SFTP file transfer via libssh2
%bcond_without	shout		# shout access output plugin
%bcond_without	smb		# SMB access plugin
%bcond_without	speex		# speex codec plugin
%bcond_without	static_libs	# don't build static libraries
%bcond_without	svg		# svg text renderer plugin
%bcond_without	twolame		# twolame codec plugin
%bcond_without	udev		# udev service discovery plugin
%bcond_without	upnp		# upnp service discovery plugin
%bcond_without	vsxu		# Vovoid VSXu visualization plugin
%bcond_without	x264		# x264 codec plugin
%bcond_without	x265		# x265 codec plugin
%bcond_without	xmas		# disable "xmas joke" icons provided by vlc [unmaintained patch]

%define		qtver	4.8.3

%ifnarch i686 pentium4 athlon %{x8664} x32
# CrystalHD library requires SSE2 instructions
%undefine	with_crystalhd
%endif
%ifarch x32
%undefine	with_x265
%endif
Summary:	VLC - a multimedia player and stream server
Summary(pl.UTF-8):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	2.2.0
Release:	4
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://download.videolan.org/pub/videolan/vlc/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	faeceb614bf3946e5f90ef0d1f51db45
Patch0:		%{name}-buildflags.patch
Patch1:		%{name}-tremor.patch
Patch2:		%{name}-system-minizip.patch
Patch3:		xmas-sucks.patch

Patch7:		no-cache.patch
URL:		http://www.videolan.org/vlc/
%{?with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	SDL_image-devel >= 1.2.10
BuildRequires:	a52dec-libs-devel >= 0.7.3
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.24}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
%{?with_bonjour:BuildRequires:	avahi-devel >= 0.6}
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	desktop-file-utils
BuildRequires:	faad2-devel >= 2.5
%{?with_fdk_aac:BuildRequires:	fdk-aac-devel}
# libavcodec >= 54.36.0 < 56, libavformat >= 53.21.0, libavutil >= 51.22.0, libswscale, libpostproc
BuildRequires:	ffmpeg-devel >= 0.4.9-4.20080131.1
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	fluidsynth-devel >= 1.1.2
BuildRequires:	fontconfig-devel
BuildRequires:	freerdp-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2
BuildRequires:	fribidi-devel
BuildRequires:	game-music-emu-devel
BuildRequires:	gettext-tools >= 0.18.3
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel}
%{?with_gnutls:BuildRequires:	gnutls-devel >= 3.0.20}
%{?with_notify:BuildRequires:	gtk+2-devel >= 2.0}
# >= 0.120.1 < 1.0 or >= 1.9.7
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.120.1}
%{?with_kde:BuildRequires:	kde4-kdelibs}
BuildRequires:	libass-devel >= 0.9.8
%{?with_dv:BuildRequires:	libavc1394-devel >= 0.5.3}
BuildRequires:	libbluray-devel >= 0.2.1
%{?with_caca:BuildRequires:	libcaca-devel >= 0.99-0.beta14}
BuildRequires:	libcddb-devel >= 0.9.5
BuildRequires:	libcdio-devel >= 0.78.2
BuildRequires:	libchromaprint-devel >= 0.6.0
%{?with_crystalhd:BuildRequires:	libcrystalhd-devel}
BuildRequires:	libdc1394-devel >= 2.1.0
BuildRequires:	libdts-devel >= 0.0.5
BuildRequires:	libdvbpsi-devel >= 1.1.0
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libebml-devel >= 1.0.0
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libgoom2-devel
BuildRequires:	libidn-devel
BuildRequires:	libkate-devel >= 0.3.0
BuildRequires:	libmad-devel
BuildRequires:	libmatroska-devel >= 1.0.0
# >= 0.8.4 but not 0.8.8
BuildRequires:	libmodplug-devel >= 0.8.4
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libmpeg2-devel > 0.3.2
BuildRequires:	libmtp-devel >= 1.0.0
%{?with_notify:BuildRequires:	libnotify-devel}
BuildRequires:	libogg-devel >= 1:1.0
BuildRequires:	libpng-devel
%{?with_projectM:BuildRequires:	libprojectM-devel >= 2.0.1-3}
BuildRequires:	libproxy-devel
%{?with_dv:BuildRequires:	libraw1394-devel >= 2.0.1}
%{?with_svg:BuildRequires:	librsvg-devel >= 2.9.0}
BuildRequires:	libsamplerate-devel
%{?with_shout:BuildRequires:	libshout-devel >= 2.1}
BuildRequires:	libsidplay2-devel
%{?with_smb:BuildRequires:	libsmbclient-devel >= 3.6.13}
%{?with_sftp:BuildRequires:	libssh2-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtar-devel
BuildRequires:	libtheora-devel >= 1.0
BuildRequires:	libtiger-devel >= 0.3.1
BuildRequires:	libtool >= 2:2
%{?with_upnp:BuildRequires:	libupnp-devel}
BuildRequires:	libv4l-devel
BuildRequires:	libva-x11-devel
BuildRequires:	libva-drm-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libvncserver-devel >= 0.9.9
BuildRequires:	libvorbis-devel >= 1:1.1
# x264.pc >= 0.86
%{?with_x264:BuildRequires:	libx264-devel}
%{?with_x265:BuildRequires:	libx265-devel}
BuildRequires:	libxcb-devel >= 1.6
BuildRequires:	libxml2-devel >= 1:2.5
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_live:BuildRequires:	live-devel >= 2014.07.04}
BuildRequires:	lua52 >= 5.2
BuildRequires:	lua52-devel >= 5.2
%{?with_mfx:BuildRequires:	mfx_dispatch-devel}
BuildRequires:	minizip-devel
BuildRequires:	ncurses-devel
%{?with_opencv:BuildRequires:	opencv-devel > 2.0}
BuildRequires:	opus-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pulseaudio-devel >= 0.9.22
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	schroedinger-devel >= 1.0.10
%{?with_speex:BuildRequires:	speex-devel > 1:1.1.0}
%{?with_speex:BuildRequires:	speexdsp-devel >= 1.2}
BuildRequires:	sysfsutils-devel
BuildRequires:	taglib-devel >= 1.6.1
BuildRequires:	tremor-devel
%{?with_twolame:BuildRequires:	twolame-devel}
%{?with_udev:BuildRequires:	udev-devel >= 1:142}
BuildRequires:	vcdimager-devel >= 0.7.22
%{?with_vsxu:BuildRequires:	vsxu-devel}
BuildRequires:	xcb-util-keysyms-devel >= 0.3.4
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
BuildRequires:	zvbi-devel >= 0.2.28
Requires(post):	/sbin/ldconfig
Requires:	xdg-utils
Obsoletes:	browser-plugin-vlc
Obsoletes:	vlc-GGI
Obsoletes:	vlc-esd
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
Requires:	dbus-devel >= 1.0.0

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
Requires:	QtCore >= %{qtver}
Requires:	QtGui >= %{qtver}
Requires:	desktop-file-utils
Suggests:	dbus-x11
Suggests:	libcaca > 0.99-0.beta14.1
Obsoletes:	vlc-gnome
Obsoletes:	vlc-gtk

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

%package SDL
Summary:	VLC - SDL output plugin
Summary(pl.UTF-8):	Klient VLC - wtyczka wyjścia SDL
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	SDL >= 1.2.10

%description SDL
SDL output plugin for VLC.

%description SDL -l pl.UTF-8
Wtyczka wyjścia SDL dla klienta VLC.

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if %{without xmas}
%patch3 -p1
%endif

%patch7 -p1

sed -i -e 's#Qt5#WANT_QT4#g' configure.ac

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
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses -I/usr/include/xulrunner/stable -I/usr/include/liveMedia" \
	LUAC=luac5.2 \
	--disable-optimizations \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
%ifarch ppc
	--disable-altivec \
%endif
	--with-default-font=/usr/share/vlc/skins2/fonts/FreeSans.ttf \
	--with-default-monospace-font=/usr/share/fonts/TTF/LiberationMono-Regular.ttf \
	--with-default-font-family=Sans \
	--enable-aa%{!?with_aalib:=no} \
	%{?with_alsa:--enable-alsa} \
	--enable-avcodec \
	%{!?with_bonjour:--disable-bonjour} \
	--enable-caca%{!?with_caca:=no} \
	--enable-crystalhd%{!?with_crystalhd:=no} \
	--enable-dbus \
	%{?with_directfb:--enable-directfb} \
	--enable-dv1394%{!?with_dv:=no} \
	--enable-dvbpsi \
	--enable-dvdnav \
	--enable-dvdread \
	%{?with_fdk_aac:--enable-fdkaac} \
	--enable-faad \
	--enable-flac \
	--enable-freetype \
	--enable-fribidi \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	%{!?with_gnutls:--disable-gnutls} \
	%{?with_jack:--enable-jack} \
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
	--enable-sdl \
	%{?with_sftp:--enable-sftp} \
	--enable-shared \
	--enable-shine \
	--enable-shout%{!?with_shout:=no} \
	--enable-skins2 \
	%{!?with_smb:--disable-smbclient} \
	--enable-sout \
	%{!?with_speex:--disable-speex} \
	%{?with_svg:--enable-svg} \
	--enable-theora \
	--enable-tremor \
	%{?with_twolame:--enable-twolame} \
	%{!?with_udev:--disable-udev} \
	%{?with_upnp:--enable-upnp} \
	--enable-v4l2 \
	--enable-vcdx \
	%{!?with_vsxu:--disable-vsxu} \
	%{!?with_x264:--disable-x264} \
	%{!?with_x265:--disable-x265} \
	%{!?with_kde:--without-kde-solid}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dir for lua extensions
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/lua/extensions

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/vlc

%if "%{_lib}" != "lib"
install -d $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf %{_libdir}/vlc $RPM_BUILD_ROOT%{_prefix}/lib
%endif

# rm -f *.{a,la}
find $RPM_BUILD_ROOT%{_libdir} -type f -regex '.*\.l?a$' | xargs %{__rm}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{pt_PT,pt}
# unsupported:
# ach (Acoli)
# cgg (Chiga)
# co (Corsican)
# tet (Tetum)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ach,cgg,co,tet}

# .ico is win32 only
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/vlc*.ico

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc/plugins || :

%postun	-p /sbin/ldconfig

%post X11
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
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
%attr(755,root,root) %ghost %{_libdir}/libvlccore.so.8
%attr(755,root,root) %{_libdir}/vlc/libvlc_vdpau.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/vlc/libvlc_vdpau.so.0

%if "%{_lib}" != "lib"
%{_prefix}/lib/vlc
%endif
%dir %{_libdir}/vlc
%dir %{_libdir}/vlc/plugins
%ghost %{_libdir}/vlc/plugins/plugins.dat
%dir %{_libdir}/vlc/plugins/access
%if %{with alsa}
# R: alsa-lib >= 1.0.24
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_alsa_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libattachment_plugin.so
# R: ffmpeg-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libavio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_bd_plugin.so
%if %{with dv}
# R: libraw1394 >= 2.0.1 libavc1394 >= 0.5.3
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdv1394_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libftp_plugin.so
%if %{with gnomevfs}
# R: gnome-vfs2
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libgnomevfs_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libhttp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libimem_plugin.so
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
%attr(755,root,root) %{_libdir}/vlc/plugins/access/librar_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libaccess_realrtsp_plugin.so
%if %{with sftp}
# R: libssh2
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsftp_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libshm_plugin.so
%if %{with smb}
# R: libsmbclient
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsmb_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libtcp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libudp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvdr_plugin.so
# R: libcddb >= 0.9.5
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libcdda_plugin.so
# R: libraw1394 >= 2.0.1 libdc1394 >= 2.1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdc1394_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdtv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvb_plugin.so
# R: libdvdnav
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvdnav_plugin.so
# R: libdvdread
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libdvdread_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libfilesystem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libidummy_plugin.so
# R: libbluray >= 0.2.1
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
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libpulsesrc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libsdp_plugin.so
#%attr(755,root,root) %{_libdir}/vlc/plugins/access/libstream_filter_rar_plugin.so
# R: freerdp
%attr(755,root,root) %{_libdir}/vlc/plugins/access/librdp_plugin.so
# R: libgcrypt >= 1.1.94 (optional, for srtp functionality)
%attr(755,root,root) %{_libdir}/vlc/plugins/access/librtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libtimecode_plugin.so
%{?with_v4l1:%attr(755,root,root) %{_libdir}/vlc/plugins/access/libv4l_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libv4l2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvcd_plugin.so
# R: libcdio >= 0.78.2, vcdimager >= 0.7.22
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libvcdx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libxcb_screen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access/libzip_plugin.so
%dir %{_libdir}/vlc/plugins/access_output
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_http_plugin.so
# R: libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_livehttp_plugin.so
%if %{with shout}
# R: shout >= 2.1
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_shout_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/access_output/libaccess_output_udp_plugin.so
%dir %{_libdir}/vlc/plugins/audio_filter
# R: a52dec-libs >= 0.7.3
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/liba52tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/liba52tospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libaudio_format_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libcompressor_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so
# R: libdts >= 0.0.5
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libdtstofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libdtstospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libequalizer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libgain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libkaraoke_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libmono_plugin.so
# R: libmad
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libmpgatofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libnormvol_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libparam_eq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libremap_plugin.so
# R: libsamplerate
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libsamplerate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libscaletempo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libsimple_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libspatializer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libspeex_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_filter/libstereo_widen_plugin.so
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
# R: pulseaudio-libs >= 0.9.22
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/libpulse_plugin.so
%if %{with oss4}
%attr(755,root,root) %{_libdir}/vlc/plugins/audio_output/liboss_plugin.so
%endif
%dir %{_libdir}/vlc/plugins/codec
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liba52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaes3_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libadpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libaraw_plugin.so
# R: ffmpeg-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libavcodec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcdg_plugin.so
%if %{with crystalhd}
# R: libcrystalhd
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcrystalhd_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libcvdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libdts_plugin.so
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
# R: fluidsynth >= 1.1.2
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libfluidsynth_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libg711_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libgstdecode_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libhwdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libjpeg_plugin.so
# R: libkate >= 0.3.0 libtiger >= 0.3.1
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libkate_plugin.so
# R: libass >= 0.9.8
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblibass_plugin.so
# R: libmpeg2-libs > 0.3.2
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblibmpeg2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/liblpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libmpeg_audio_plugin.so
# R: libomxil-bellagio (dlopened, no .so NEEDED dependency)
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libomxil_plugin.so
# R: libomxil-bellagio (dlopened, no .so NEEDED dependency)
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libomxil_vout_plugin.so
# R: opus
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libopus_plugin.so
# R: libpng
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libpng_plugin.so
%if %{with mfx}
# R: mfx_dispatch
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libqsv_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/librawvideo_plugin.so
# R: schroedinger >= 1.0.10
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libschroedinger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libscte27_plugin.so
# R: SDL_image >= 1.2.10
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsdl_image_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libshine_plugin.so
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
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libsvgdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libt140_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtelx_plugin.so
# R: libtheora >= 1.0
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtheora_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libuleaddvaudio_plugin.so
%if %{with twolame}
# R: twolame-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libtwolame_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvaapi_drm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvaapi_x11_plugin.so
# R: libvorbis >= 1.1
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvorbis_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libvpx_plugin.so
# R: libx264
%{?with_x264:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libx264_plugin.so}
# R: libx265
%{?with_x265:%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libx265_plugin.so}
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libxwd_plugin.so
# R: zvbi >= 0.2.28
%attr(755,root,root) %{_libdir}/vlc/plugins/codec/libzvbi_plugin.so
%dir %{_libdir}/vlc/plugins/control
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
# # R: xcb-util-keysyms >= 0.3.4
%attr(755,root,root) %{_libdir}/vlc/plugins/control/libxcb_hotkeys_plugin.so
%dir %{_libdir}/vlc/plugins/demux
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libaiff_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libasf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libau_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libavformat_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libavi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemux_cdg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemux_stl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdemuxdump_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libdiracsys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libes_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libflacsys_plugin.so
# R: game-music-emu
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libgme_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libh264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libcaf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libhevc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libimage_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmjpeg_plugin.so
# R: libebml >= 1.0.0 libmatroska >= 1.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmkv_plugin.so
# R: libmodplug >= 0.8.4, libmodplug != 0.8.8
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmod_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmp4_plugin.so
# R: libmpcdec
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmpc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/demux/libmpgv_plugin.so
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
# R: libdvbpsi
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
%dir %{_libdir}/vlc/plugins/lua
# R: lua51
%attr(755,root,root) %{_libdir}/vlc/plugins/lua/liblua_plugin.so
%dir %{_libdir}/vlc/plugins/meta_engine
%attr(755,root,root) %{_libdir}/vlc/plugins/meta_engine/libfolder_plugin.so
# R: taglib >= 1.6.1
%attr(755,root,root) %{_libdir}/vlc/plugins/meta_engine/libtaglib_plugin.so
%dir %{_libdir}/vlc/plugins/misc
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libaddonsfsstorage_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libaddonsvorepository_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libaudioscrobbler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libdbus_screensaver_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libexport_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libfingerprinter_plugin.so
%if %{with gnutls}
# R: gnutls >= 3.0.20
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libgnutls_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/liblogger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxdg_screensaver_plugin.so

%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libstats_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libvod_rtsp_plugin.so
# R: libxml2 >= 1:2.5
%attr(755,root,root) %{_libdir}/vlc/plugins/misc/libxml_plugin.so

%dir %{_libdir}/vlc/plugins/video_chroma
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
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libchain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_rgb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi420_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libi422_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/librv32_plugin.so
# R: ffmpeg-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libswscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_chroma/libyuy2_i422_plugin.so

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
# R: libnotify gtk+2
%attr(755,root,root) %{_libdir}/vlc/plugins/notify/libnotify_plugin.so
%endif

%dir %{_libdir}/vlc/plugins/packetizer
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_avparser_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_copy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_dirac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_h264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_hevc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so
%dir %{_libdir}/vlc/plugins/services_discovery
%if %{with bonjour}
# R: avahi-libs >= 0.6
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libbonjour_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libmediadirs_plugin.so
# R: libmtp >= 1.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libmtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/services_discovery/libpodcast_plugin.so
# R: pulseaudio-libs >= 0.9.22
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
%dir %{_libdir}/vlc/plugins/stream_filter
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libdecomp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libdash_plugin.so
# R: libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libhttplive_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/librecord_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_filter/libsmooth_plugin.so
%dir %{_libdir}/vlc/plugins/stream_out
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_bridge_plugin.so
# R: libchromaprint >= 0.6.0
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_chromaprint_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_delay_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_description_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_es_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_gather_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_langfromtelx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so
# R: libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/stream_out/libstream_out_raop_plugin.so
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
%dir %{_libdir}/vlc/plugins/vdpau
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_adjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_avcodec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_chroma_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_deinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/vdpau/libvdpau_sharpen_plugin.so
%dir %{_libdir}/vlc/plugins/video_filter
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libadjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libantiflicker_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libanaglyph_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libaudiobargraph_v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libalphamask_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libatmo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libball_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libblend_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libblendbench_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libbluescreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcanvas_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcolorthres_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libcroppadd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libdeinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libdynamicoverlay_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/liberase_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libextract_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libfreeze_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgaussianblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgradfun_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgradient_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libgrain_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libhqdn3d_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libinvert_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/liblogo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmagnify_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmarq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmirror_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmosaic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmotionblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libmotiondetect_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/liboldmovie_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libopencv_example_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libposterize_plugin.so
# R: ffmpeg-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpostproc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpsychedelic_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libpuzzle_plugin.so
# R: libgcrypt >= 1.1.94
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libremoteosd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libripple_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/librotate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/librss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libscene_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libsepia_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libsharpen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libsubsdelay_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libtransform_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libwave_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libvhs_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_filter/libyuvp_plugin.so
%dir %{_libdir}/vlc/plugins/video_output
%if %{with directfb}
# R: DirectFB
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libdirectfb_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvmem_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libyuv_plugin.so
%dir %{_libdir}/vlc/plugins/video_splitter
%attr(755,root,root) %{_libdir}/vlc/plugins/video_splitter/libclone_plugin.so
# R: libxcb >= 1.6
%attr(755,root,root) %{_libdir}/vlc/plugins/video_splitter/libpanoramix_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_splitter/libwall_plugin.so
%dir %{_libdir}/vlc/plugins/visualization
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libglspectrum_plugin.so
# R: libgoom2
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libgoom_plugin.so
%if %{with projectM}
# R: libprojectM >= 2.0.0
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libprojectm_plugin.so
%endif
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libvisual_plugin.so
%if %{with vsxu}
# R: vsxu-libs
%attr(755,root,root) %{_libdir}/vlc/plugins/visualization/libvsxu_plugin.so
%endif
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lua
%dir %{_datadir}/%{name}/lua/extensions
%dir %{_datadir}/%{name}/utils
%attr(755,root,root) %{_datadir}/%{name}/utils/*.sh

%{_mandir}/man1/vlc.1*
%{_mandir}/man1/vlc-wrapper.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvlc.so
%attr(755,root,root) %{_libdir}/libvlccore.so
%attr(755,root,root) %{_libdir}/vlc/libvlc_vdpau.so
%{_includedir}/%{name}
%{_pkgconfigdir}/libvlc.pc
%{_pkgconfigdir}/vlc-plugin.pc

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qvlc
%attr(755,root,root) %{_bindir}/svlc
# R: QtCore QtGui >= %{qtver}
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libqt4_plugin.so
# R: freetype libtar xorg-lib-lib{Xext,Xinerama,Xpm} QtCore QtGui
%attr(755,root,root) %{_libdir}/vlc/plugins/gui/libskins2_plugin.so
%if %{with aalib}
# R: aalib
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libaa_plugin.so
%endif
%if %{with caca}
# R: libcaca >= 0.99-0.beta14
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libcaca_plugin.so
%endif
# R: EGL, xorg-lib-libX11
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libegl_x11_plugin.so
# R: OpenGL
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libgl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libglx_plugin.so
# R: OpenGL libxcb >= 1.6
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_glx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_window_plugin.so
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_x11_plugin.so
# R: libxcb >= 1.6
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libxcb_xv_plugin.so
%{_datadir}/%{name}/skins2
%{_iconsdir}/hicolor/*/apps/vlc*.png
%{_iconsdir}/hicolor/*/apps/vlc*.xpm
%{_desktopdir}/vlc.desktop

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/vlc/plugins/video_output/libvout_sdl_plugin.so

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
%{_datadir}/vlc/lua

%if %{with kde}
%files solid
%defattr(644,root,root,755)
%{_datadir}/apps/solid/actions/vlc-*.desktop
%endif
