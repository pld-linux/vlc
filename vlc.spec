#
# TODO:
# - check the altivec patch 
# - add proper package descriptions/translations
# - check files/packages (can we keep png/xpm/bmp/ico in X11 package)
# - shorten the files section
# - change group for vlc and framebuffer video out (it's not the X11)
#
# Conditional build:
%bcond_without	alsa	# don't build alsa plugin
%bcond_without	ggi	# don't build ggi plugin
%bcond_with	mozilla	# build mozilla plugin
#
Summary:	VLC - a multimedia player and stream server
Summary(pl):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	0.8.1337
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.videolan.org/pub/videolan/vlc/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	604ff3ad7c2ed5aecd0941aab7b666ae
Source1:	%{name}.desktop
Patch0:		%{name}-altivec.patch
Patch1:		%{name}-po.patch
Patch2:		%{name}-buildflags.patch
Patch3:		%{name}-wxgtk2.patch
Patch4:		%{name}-defaultfont.patch
URL:		http://www.videolan.org/vlc/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	a52dec-libs-devel
BuildRequires:	aalib-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
BuildRequires:	artsc-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	flac-devel
BuildRequires:	fribidi-devel
BuildRequires:	gettext-devel
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
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	lirc-devel
BuildRequires:	mpeg2dec-devel
%{?with_mozilla:BuildRequires:	mozilla-devel}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
BuildRequires:	svgalib-devel
BuildRequires:	vcdimager-devel
BuildRequires:	wxGTK2-devel
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
# %patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

mv -f po/{no,nb}.po

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
	--enable-arts \
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
	--disable-glide \
	--enable-lirc \
	--enable-livedotcom \
	--enable-mad \
	--enable-mga \
	%{?with_mozilla:--enable-mozilla } \
	--enable-ncurses \
	--enable-pvr \
	--enable-sdl \
	--with-sdl=/usr \
	--enable-skins2 \
	--enable-slp \
	--enable-svgalib \
	--enable-tarkin \
	--enable-theora \
	--enable-tremor \
	--enable-v4l\
	--enable-x11 \
	--enable-xosd \
	--enable-xvid \
	--enable-oss \
	--disable-testsuite \
	--with-wx-config-path=wxgtk2-2.4-config \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations

# echo "CFLAGS += -I/usr/include/ncurses" >> Makefile.opts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README THANKS
%attr(755,root,root) %{_bindir}/vlc
%dir %{_libdir}/vlc
%dir %{_libdir}/vlc/access
%dir %{_libdir}/vlc/access_output
%dir %{_libdir}/vlc/audio_filter
%dir %{_libdir}/vlc/audio_mixer
%dir %{_libdir}/vlc/audio_output
%dir %{_libdir}/vlc/codec
%dir %{_libdir}/vlc/control
%dir %{_libdir}/vlc/demux
%dir %{_libdir}/vlc/gui
%dir %{_libdir}/vlc/misc
%dir %{_libdir}/vlc/mux
%dir %{_libdir}/vlc/packetizer
%dir %{_libdir}/vlc/stream_out
%dir %{_libdir}/vlc/video_chroma
%dir %{_libdir}/vlc/video_filter
%dir %{_libdir}/vlc/video_output
%dir %{_libdir}/vlc/visualization
%attr(755,root,root) %{_libdir}/vlc/gui/libncurses_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_asf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_avi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_mp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_mpjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_wav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libexport_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libfreetype_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libipv4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libipv6_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/liblogger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libmemcpy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libsap_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libscreensaver_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libvod_rtsp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/liblirc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libtelnet_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libnetsync_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libshowintf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/librc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libgestures_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhotkeys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhttp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_udp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libvorbis_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsvcdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsubsdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libspudec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/librawvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libmpeg_audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblibmpeg2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libdvbsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libdts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcvdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcmml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcinepak_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libaraw_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libadpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liba52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libfaad_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libflacdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/liba52sys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libaac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libaiff_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libasf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libau_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libavi_plugin.so
#%attr(755,root,root) %{_libdir}/vlc/demux/libdemux2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdemuxdump_plugin.so
#%attr(755,root,root) %{_libdir}/vlc/demux/libdemuxsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdtssys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libflac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libh264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libid3_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libid3tag_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm3u_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm4a_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm4v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm4v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmjpeg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmod_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpgv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnsv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libplaylist_plugin.so
#%attr(755,root,root) %{_libdir}/vlc/demux/libps2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libpva_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/librawdv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libreal_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libsgimb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libsubtitle_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libvobsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libwav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_directory_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_ftp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_mms_plugin.so
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
%attr(755,root,root) %{_libdir}/vlc/visualization/libvisual_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_rgb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_ymga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi422_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libfloat32_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libtrivial_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libspdif_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libadjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libblend_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libclone_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libcrop_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdeinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdistort_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libinvert_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/liblogo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmarq_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmotionblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libscale_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libtime_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libtransform_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libwall_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_description_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_duplicate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_es_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_gather_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_rtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_standard_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_transcode_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libaudio_format_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libbandlimited_resampler_plugin.so
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
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_copy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_h264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4video_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpegvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/libalsa_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/libarts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/libesd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/liboss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/libaout_file_plugin.so
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/bugreport-howto.txt
%{_datadir}/doc/%{name}/fortunes.txt
%{_datadir}/doc/%{name}/intf-cdda.txt
%{_datadir}/doc/%{name}/intf-vcd.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/http
%dir %{_datadir}/%{name}/http/vlm
%dir %{_datadir}/%{name}/http/admin
%dir %{_datadir}/%{name}/skins2
%dir %{_datadir}/%{name}/skins2/fonts
%{_datadir}/%{name}/familiar-*
%{_datadir}/%{name}/http/vlm/edit.html
%{_datadir}/%{name}/http/vlm/index.html
%{_datadir}/%{name}/http/vlm/new.html
%{_datadir}/%{name}/http/admin/dboxfiles.html
%{_datadir}/%{name}/http/admin/.access
%{_datadir}/%{name}/http/admin/index.html
%{_datadir}/%{name}/http/admin/browse.html
%{_datadir}/%{name}/http/style.css
%{_datadir}/%{name}/http/index.html
%{_datadir}/%{name}/http/info.html
%{_datadir}/%{name}/ui.rc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vlc-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/aout.h
%{_includedir}/%{name}/decoder.h
%{_includedir}/%{name}/input.h
%{_includedir}/%{name}/intf.h
%{_includedir}/%{name}/sout.h
%{_includedir}/%{name}/vlc.h
%{_includedir}/%{name}/vout.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvlc.a
%{_libdir}/%{name}/libdtstofloat32.a
%{_libdir}/%{name}/libffmpeg.a
%{_libdir}/%{name}/libi420_rgb_mmx.a
%{_libdir}/%{name}/libi420_ymga_mmx.a
%{_libdir}/%{name}/libi420_yuy2_mmx.a
%{_libdir}/%{name}/libi422_yuy2_mmx.a
%{_libdir}/%{name}/libmemcpy3dn.a
%{_libdir}/%{name}/libmemcpymmx.a
%{_libdir}/%{name}/libmemcpymmxext.a
%{_libdir}/%{name}/libmkv.a
%{_libdir}/%{name}/libtheora.a

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/svlc
%attr(755,root,root) %{_bindir}/wxvlc
%attr(755,root,root) %{_libdir}/%{name}/video_output/libx11_plugin.so
%attr(755,root,root) %{_libdir}/%{name}/video_output/libxvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/gui/libskins2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/gui/libwxwindows_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libscreen_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libaa_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libglx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libmga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libcaca_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libopengl_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_output/libsvgalib_plugin.so
%attr(755,root,root) %{_libdir}/vlc/visualization/libxosd_plugin.so
%{_datadir}/%{name}/familiar-forwardb16x16.xpm
%{_datadir}/%{name}/familiar-openb16x16.xpm
%{_datadir}/%{name}/familiar-pauseb16x16.xpm
%{_datadir}/%{name}/familiar-playb16x16.xpm
%{_datadir}/%{name}/familiar-playlistb16x16.xpm
%{_datadir}/%{name}/familiar-rewindb16x16.xpm
%{_datadir}/%{name}/familiar-stopb16x16.xpm
%{_datadir}/%{name}/kvlc16x16.png
%{_datadir}/%{name}/kvlc32x32.png
%{_datadir}/%{name}/kvlc32x32.xpm
%{_datadir}/%{name}/kvlc48x48.png
%{_datadir}/%{name}/pda-forwardb16x16.xpm
%{_datadir}/%{name}/pda-openb16x16.xpm
%{_datadir}/%{name}/pda-pauseb16x16.xpm
%{_datadir}/%{name}/pda-playb16x16.xpm
%{_datadir}/%{name}/pda-playlistb16x16.xpm
%{_datadir}/%{name}/pda-preferencesb16x16.xpm
%{_datadir}/%{name}/pda-rewindb16x16.xpm
%{_datadir}/%{name}/pda-stopb16x16.xpm
%{_datadir}/%{name}/qvlc16x16.png
%{_datadir}/%{name}/qvlc32x32.png
%{_datadir}/%{name}/qvlc32x32.xpm
%{_datadir}/%{name}/qvlc48x48.png
%{_datadir}/%{name}/skins2/default.vlt
%{_datadir}/%{name}/skins2/fonts/FreeSans.ttf
%{_datadir}/%{name}/skins2/skin.catalog
%{_datadir}/%{name}/skins2/skin.dtd
%{_datadir}/%{name}/gnome-vlc*.xpm
%{_datadir}/%{name}/gnome-vlc*.png
%{_datadir}/%{name}/gvlc*.xpm
%{_datadir}/%{name}/gvlc*.png
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
