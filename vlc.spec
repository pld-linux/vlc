#
# TODO:
# - return to gettextize/aclocal/autoconf 
# - check the altivec patch 
# - check the po patch 
# - add proper package descriptions/translations
# - check files/packages (can we keep png/xpm/bmp/ico in X11 package)
# - shorten the files section
# - check this no->nb locale stuff 
# - check find_lang macro
# - change group for vlc and framebuffer video out (it's not the X11)
# - default subtitles font change (btw. you can change this in your ~/.vlc/vlcrc)
#
# Conditional build:
%bcond_without	alsa	# don't build alsa plugin
#
Summary:	VLC - a multimedia player and stream server 
Summary(pl):	VLC - odtwarzacz multimedialny oraz serwer strumieni
Name:		vlc
Version:	0.7.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	25dfcc804cb92f46c0b64ce1466515cc
Patch0:		%{name}-altivec.patch
Patch1:		%{name}-po.patch
Patch2:		%{name}-buildflags.patch
URL:		http://www.videolan.org/vlc/
BuildRequires:	SDL-devel >= 1.2
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libdvdcss-devel
BuildRequires:	libdts-devel
BuildRequires:	libebml-devel
BuildRequires:	libggi-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcddb-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libpostproc-devel
BuildRequires:	mpeg2dec-devel
BuildRequires:	vcdimager-devel
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

%package static
Summary:	VLC static libraries
Summary(pl):	Biblioteli statyczne VLC 
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
VLC static libraries.

%package X11
Summary:	VLC - X11 output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia X11
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

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

%description GGI -l pl
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

%package gnome
Summary:	VLC - GNOME output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia GNOME
Summary(pt_BR):	Plugin GNOME para o VLC
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME output plugin for VLC.

%description gnome -l pl
Wtyczka wyj¶cia GNOME dla klienta VLC.

%description gnome -l pt_BR
Plugin GNOME para o VLC.

%package gtk
Summary:	VLC - GTK+ output plugin
Summary(pl):	Klient VLC - wtyczka wyj¶cia GTK+
Summary(pt_BR):	Plugin GTK+ para o VLC
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+ output plugin for VLC.

%description gtk -l pl
Wtyczka wyj¶cia GTK+ dla klienta VLC.

%description gtk -l pt_BR
Plugin GTK+ para o VLC.

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
# %patch1 -p1
%patch2 -p0

# mv -f po/{no,nb}.po

%build
#cp -f /usr/share/automake/config.* .
#% {__gettextize}
#% {__aclocal}
#% {__autoconf}
CFLAGS="%{rpmcflags} -DALSA_PCM_OLD_HW_PARAMS_API"
%configure \
%ifarch ppc
	--disable-altivec \
%endif
	--enable-dvdread \
	--enable-dummy \
	--enable-dsp \
	%{?with_alsa:--enable-alsa} \
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
	--with-sdl=/usr \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations

# echo "CFLAGS += -I/usr/include/ncurses" >> Makefile.opts
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README THANKS
%attr(755,root,root) %{_bindir}/vlc
%attr(755,root,root) %{_bindir}/svlc
%attr(755,root,root) %{_bindir}/vlc-config
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
%attr(755,root,root) %{_libdir}/vlc/gui/libskins2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/gui/libncurses_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_asf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_mp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_avi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ts_dvbpsi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/mux/libmux_ps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libipv4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libdummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libexport_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libscreensaver_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/liblogger_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libipv6_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libfreetype_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libsap_plugin.so
%attr(755,root,root) %{_libdir}/vlc/misc/libmemcpy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libtelnet_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/librc_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libgestures_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhotkeys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/control/libhttp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_udp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access_output/libaccess_output_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libdvbsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libadpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libvorbis_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcinepak_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libmpeg_audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblpcm_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcmml_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libspudec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsubsdec_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libsvcdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libaraw_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libcvdsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liba52_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/liblibmpeg2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/librawvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/codec/libdts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libplaylist_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libogg_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpgv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdemuxsub_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libwav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libavi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/liba52sys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libau_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libid3_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdvdnav_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libsgimb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libts2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libps2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libh264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm4v_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libts_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libm3u_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libnsv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdemux2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libasf_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdemuxdump_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/librawdv_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libts_dvbpsi_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libaiff_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmp4_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libmpeg_system_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libpva_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libps_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libaac_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libdtssys_plugin.so
%attr(755,root,root) %{_libdir}/vlc/demux/libreal_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_udp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_file_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_directory_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvd_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libcddax_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_mms_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libvcdx_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_http_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_ftp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libaccess_tcp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/access/libdvdread_plugin.so
%attr(755,root,root) %{_libdir}/vlc/visualization/libvisual_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_ymga_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi422_yuy2_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_chroma/libi420_rgb_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libfloat32_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libtrivial_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_mixer/libspdif_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/liblogo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libadjust_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libclone_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libtransform_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libcrop_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdeinterlace_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libmotionblur_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libdistort_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libinvert_plugin.so
%attr(755,root,root) %{_libdir}/vlc/video_filter/libwall_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_rtp_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_es_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_dummy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_standard_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_display_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_gather_plugin.so
%attr(755,root,root) %{_libdir}/vlc/stream_out/libstream_out_duplicate_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tos16_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libu8tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libu8tofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs8tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs16tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs16tofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libheadphone_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfixed32tos16_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libtrivial_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libmpgatofixed32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfixed32tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libs16tofloat32swab_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libbandlimited_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liblinear_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tou16_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libtrivial_channel_mixer_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/liba52tofloat32_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tos8_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libugly_resampler_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libdtstospdif_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_filter/libfloat32tou8_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4video_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpeg4audio_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_h264_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_copy_plugin.so
%attr(755,root,root) %{_libdir}/vlc/packetizer/libpacketizer_mpegvideo_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/liboss_plugin.so
%attr(755,root,root) %{_libdir}/vlc/audio_output/libaout_file_plugin.so
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/bugreport-howto.txt
%{_datadir}/doc/%{name}/fortunes.txt
%{_datadir}/doc/%{name}/intf-cdda.txt
%{_datadir}/doc/%{name}/intf-vcd.txt
%{_datadir}/doc/%{name}/vlc-howto.sgml
%{_datadir}/doc/%{name}/web-streaming.html
# %dir %{_datadir}/doc/%{name}-%{version}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/http
%dir %{_datadir}/%{name}/http/vlm
%dir %{_datadir}/%{name}/http/admin
%dir %{_datadir}/%{name}/skins
%dir %{_datadir}/%{name}/skins/default
%dir %{_datadir}/%{name}/skins2
%dir %{_datadir}/%{name}/skins2/default
%dir %{_datadir}/%{name}/skins2/fonts
%{_datadir}/%{name}/familiar-preferencesb16x16.xpm
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
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/vlc.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/vlc.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/vlc.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/vlc.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/vlc.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/vlc.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/vlc.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/vlc.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/vlc.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/vlc.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/vlc.mo
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/vlc.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/vlc.mo

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/vlc.h
%{_includedir}/%{name}/decoder.h
%{_includedir}/%{name}/aout.h
%{_includedir}/%{name}/intf.h
%{_includedir}/%{name}/sout.h
%{_includedir}/%{name}/vout.h
%{_includedir}/%{name}/input.h

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}/libmemcpymmxext.a
%{_libdir}/%{name}/libi420_rgb_mmx.a
%{_libdir}/%{name}/libi420_yuy2_mmx.a
%{_libdir}/%{name}/libmemcpy3dn.a
%{_libdir}/%{name}/libstream_out_transcode.a
%{_libdir}/%{name}/libffmpeg.a
%{_libdir}/%{name}/libmemcpymmx.a
%{_libdir}/%{name}/libi422_yuy2_mmx.a
%{_libdir}/%{name}/libi420_ymga_mmx.a
%{_libdir}/%{name}/libmkv.a
%{_libdir}/libvlc.a

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/video_output/libx11_plugin.so
%attr(755,root,root) %{_libdir}/%{name}/video_output/libxvideo_plugin.so
%{_datadir}/%{name}/pda-preferencesb16x16.xpm
%{_datadir}/%{name}/vlc32x32.png
%{_datadir}/%{name}/vlc32x32.xpm
%{_datadir}/%{name}/kvlc32x32.png
%{_datadir}/%{name}/kvlc32x32.xpm
%{_datadir}/%{name}/familiar-forwardb16x16.xpm
%{_datadir}/%{name}/pda-playlistb16x16.xpm
%{_datadir}/%{name}/skins/default/slider1.bmp
%{_datadir}/%{name}/skins/default/slider2.bmp
%{_datadir}/%{name}/skins/default/playlist1.bmp
%{_datadir}/%{name}/skins/default/playlist2.bmp
%{_datadir}/%{name}/skins/default/playlist3.bmp
%{_datadir}/%{name}/skins/default/next1.bmp
%{_datadir}/%{name}/skins/default/next2.bmp
%{_datadir}/%{name}/skins/default/next3.bmp
%{_datadir}/%{name}/skins/default/next4.bmp
%{_datadir}/%{name}/skins/default/play1.bmp
%{_datadir}/%{name}/skins/default/play2.bmp
%{_datadir}/%{name}/skins/default/play3.bmp
%{_datadir}/%{name}/skins/default/play4.bmp
%{_datadir}/%{name}/skins/default/prefs1.bmp
%{_datadir}/%{name}/skins/default/prefs2.bmp
%{_datadir}/%{name}/skins/default/prefs3.bmp
%{_datadir}/%{name}/skins/default/quit1.bmp
%{_datadir}/%{name}/skins/default/quit2.bmp
%{_datadir}/%{name}/skins/default/quit3.bmp
%{_datadir}/%{name}/skins/default/prev1.bmp
%{_datadir}/%{name}/skins/default/prev2.bmp
%{_datadir}/%{name}/skins/default/prev3.bmp
%{_datadir}/%{name}/skins/default/prev4.bmp
%{_datadir}/%{name}/skins/default/open1.bmp
%{_datadir}/%{name}/skins/default/open2.bmp
%{_datadir}/%{name}/skins/default/open3.bmp
%{_datadir}/%{name}/skins/default/add1.bmp
%{_datadir}/%{name}/skins/default/add2.bmp
%{_datadir}/%{name}/skins/default/add3.bmp
%{_datadir}/%{name}/skins/default/del1.bmp
%{_datadir}/%{name}/skins/default/del2.bmp
%{_datadir}/%{name}/skins/default/del3.bmp
%{_datadir}/%{name}/skins/default/theme.xml
%{_datadir}/%{name}/skins/default/stop1.bmp
%{_datadir}/%{name}/skins/default/stop2.bmp
%{_datadir}/%{name}/skins/default/stop3.bmp
%{_datadir}/%{name}/skins/default/stop4.bmp
%{_datadir}/%{name}/skins/default/body.bmp
%{_datadir}/%{name}/skins/default/playlist_body.bmp
%{_datadir}/%{name}/skins/default/pause1.bmp
%{_datadir}/%{name}/skins/default/pause2.bmp
%{_datadir}/%{name}/skins/default/pause3.bmp
%{_datadir}/%{name}/skins/default/pause4.bmp
%{_datadir}/%{name}/familiar-playlistb16x16.xpm
%{_datadir}/%{name}/vlc48x48.ico
%{_datadir}/%{name}/vlc48x48.png
%{_datadir}/%{name}/kvlc48x48.png
%{_datadir}/%{name}/vlc16x16.png
%{_datadir}/%{name}/vlc16x16.xpm
%{_datadir}/%{name}/kvlc16x16.png
%{_datadir}/%{name}/pda-rewindb16x16.xpm
%{_datadir}/%{name}/pda-openb16x16.xpm
%{_datadir}/%{name}/qvlc32x32.png
%{_datadir}/%{name}/qvlc32x32.xpm
%{_datadir}/%{name}/pda-playb16x16.xpm
%{_datadir}/%{name}/qvlc48x48.png
%{_datadir}/%{name}/pda-stopb16x16.xpm
%{_datadir}/%{name}/skins2/default/slider2.png
%{_datadir}/%{name}/skins2/default/vout.png
%{_datadir}/%{name}/skins2/default/stop_onclick.png
%{_datadir}/%{name}/skins2/default/add_item.png
%{_datadir}/%{name}/skins2/default/slow_disabled.png
%{_datadir}/%{name}/skins2/default/rev.png
%{_datadir}/%{name}/skins2/default/slider_volume_onclick.png
%{_datadir}/%{name}/skins2/default/sort.png
%{_datadir}/%{name}/skins2/default/next_onclick.png
%{_datadir}/%{name}/skins2/default/vout_top_right.png
%{_datadir}/%{name}/skins2/default/vout2.png
%{_datadir}/%{name}/skins2/default/volume.png
%{_datadir}/%{name}/skins2/default/next_disabled.png
%{_datadir}/%{name}/skins2/default/resize.png
%{_datadir}/%{name}/skins2/default/vout_bottom.png
%{_datadir}/%{name}/skins2/default/stop_disabled.png
%{_datadir}/%{name}/skins2/default/fast.png
%{_datadir}/%{name}/skins2/default/playlist_button_onclick2.png
%{_datadir}/%{name}/skins2/default/close_mouseover.png
%{_datadir}/%{name}/skins2/default/rev_disabled.png
%{_datadir}/%{name}/skins2/default/close_onclick.png
%{_datadir}/%{name}/skins2/default/playlist_button2.png
%{_datadir}/%{name}/skins2/default/vout_right.png
%{_datadir}/%{name}/skins2/default/rev_onclick.png
%{_datadir}/%{name}/skins2/default/vout_left.png
%{_datadir}/%{name}/skins2/default/previous.png
%{_datadir}/%{name}/skins2/default/reduce_disabled.png
%{_datadir}/%{name}/skins2/default/slider_onclick.png
%{_datadir}/%{name}/skins2/default/vout_bottom_right.png
%{_datadir}/%{name}/skins2/default/slider.png
%{_datadir}/%{name}/skins2/default/vout_top_left.png
%{_datadir}/%{name}/skins2/default/sort_onclick.png
%{_datadir}/%{name}/skins2/default/vout_body1.png
%{_datadir}/%{name}/skins2/default/vout_top.png
%{_datadir}/%{name}/skins2/default/pause.png
%{_datadir}/%{name}/skins2/default/slider_volume.png
%{_datadir}/%{name}/skins2/default/previous_disabled.png
%{_datadir}/%{name}/skins2/default/theme.xml
%{_datadir}/%{name}/skins2/default/delete_item_onclick.png
%{_datadir}/%{name}/skins2/default/play_onclick.png
%{_datadir}/%{name}/skins2/default/reduce.png
%{_datadir}/%{name}/skins2/default/preferences_onclick.png
%{_datadir}/%{name}/skins2/default/slow.png
%{_datadir}/%{name}/skins2/default/playlist.png
%{_datadir}/%{name}/skins2/default/next.png
%{_datadir}/%{name}/skins2/default/close.png
%{_datadir}/%{name}/skins2/default/slow_onclick.png
%{_datadir}/%{name}/skins2/default/pause_onclick.png
%{_datadir}/%{name}/skins2/default/play.png
%{_datadir}/%{name}/skins2/default/body.png
%{_datadir}/%{name}/skins2/default/previous_onclick.png
%{_datadir}/%{name}/skins2/default/slider_playlist.png
%{_datadir}/%{name}/skins2/default/FreeSansBold.ttf
%{_datadir}/%{name}/skins2/default/disabled.png
%{_datadir}/%{name}/skins2/default/fast_onclick.png
%{_datadir}/%{name}/skins2/default/preferences.png
%{_datadir}/%{name}/skins2/default/vout_body.png
%{_datadir}/%{name}/skins2/default/stop.png
%{_datadir}/%{name}/skins2/default/delete_item.png
%{_datadir}/%{name}/skins2/default/add_item_onclick.png
%{_datadir}/%{name}/skins2/default/playlist_button_onclick.png
%{_datadir}/%{name}/skins2/default/playlist_button.png
%{_datadir}/%{name}/skins2/default/reduce_onclick.png
%{_datadir}/%{name}/skins2/default/vout_bottom_left.png
%{_datadir}/%{name}/skins2/default/playlist_body1.png
%{_datadir}/%{name}/skins2/default/playlist_body2.png
%{_datadir}/%{name}/skins2/default/playlist_body3.png
%{_datadir}/%{name}/skins2/default/playlist_body4.png
%{_datadir}/%{name}/skins2/default/playlist_body6.png
%{_datadir}/%{name}/skins2/default/playlist_body7.png
%{_datadir}/%{name}/skins2/default/playlist_body8.png
%{_datadir}/%{name}/skins2/default/playlist_body9.png
%{_datadir}/%{name}/skins2/default/fast_disabled.png
%{_datadir}/%{name}/skins2/default/vout_onclick.png
%{_datadir}/%{name}/skins2/fonts/FreeSans.ttf
%{_datadir}/%{name}/skins2/skin.catalog
%{_datadir}/%{name}/skins2/skin.dtd
%{_datadir}/%{name}/familiar-openb16x16.xpm
%{_datadir}/%{name}/qvlc16x16.png
%{_datadir}/%{name}/familiar-pauseb16x16.xpm
%{_datadir}/%{name}/pda-forwardb16x16.xpm
%{_datadir}/%{name}/familiar-playb16x16.xpm
%{_datadir}/%{name}/pda-pauseb16x16.xpm
%{_datadir}/%{name}/familiar-stopb16x16.xpm
%{_datadir}/%{name}/familiar-rewindb16x16.xpm

%files GGI
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/video_output/libggi_plugin.so

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/video_output/libvout_sdl_plugin.so
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libaout_sdl_plugin.so

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvlc
%attr(755,root,root) %{_libdir}/%{name}/gui/libgtk_plugin.so
%attr(755,root,root) %{_libdir}/%{name}/misc/libgtk_main_plugin.so
%{_datadir}/%{name}/gvlc32x32.png
%{_datadir}/%{name}/gvlc32x32.xpm
%{_datadir}/%{name}/gvlc48x48.ico
%{_datadir}/%{name}/gvlc48x48.png
%{_datadir}/%{name}/gvlc16x16.png

%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/video_output/libfb_plugin.so

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-vlc
%attr(755,root,root) %{_libdir}/%{name}/gui/libgnome_plugin.so
%attr(755,root,root) %{_libdir}/%{name}/misc/libgnome_main_plugin.so
%{_datadir}/%{name}/gnome-vlc32x32.png
%{_datadir}/%{name}/gnome-vlc32x32.xpm
%{_datadir}/%{name}/gnome-vlc48x48.png
%{_datadir}/%{name}/gnome-vlc16x16.png

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libesd_plugin.so

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/audio_output/libalsa_plugin.so
%endif
