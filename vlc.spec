Summary:	VideoLAN Client
Summary(pl):	Klient VideoLAN
Name:		vlc
Version:	0.2.62
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.videolan.org/packages/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.videolan.org/
BuildRequires:	gnome-libs-devel
BuildRequires:	libggi-devel
BuildRequires:	esound-devel
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_mandir		%{_prefix}/man

%description
VideoLAN is a free MPEG2 software solution.

The VideoLAN Client allows to play MPEG2 Transport Streams from the
network or from a file, as well as direct DVD playback.

%description -l pl
VideoLAN jest darmowym rozwi±zaniem dla streamingu MPEG2.

Klient VideoLAN pozwala na odtwarzanie strumienia MPEG2 z sieci lub z
pliku jak równie¿ bezpo¶rednie odtwarzanie z DVD.

%package X11
Summary:	VideoLAN Client - X11 output plugin
Summary(pl):	Klient VideoLAN - plugin dla X11
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description X11
X11 output plugin for VideoLAN Client

%description -l pl X11
Plugin X11 dla Klienta VideoLAN

%package GGI
Summary:	VideoLAN Client - GGI output plugin
Summary(pl):	Klient VideoLAN - plugin GGI
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}

%description GGI
GGI output plugin for VideoLAN Client.

%description -l pl GGI
Plugin GGI dla Klienta VideoLAN.

%package SDL
Summary:	VideoLAN Client - SDL output plugin
Summary(pl):	Klient VideoLAN - plugin SDL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description SDL
SDL output plugin for VideoLAN Client.

%description -l pl SDL
Plugin SDL dla Klienta VideoLAN.

%package gnome
Summary:	VideoLAN Client - gnome output plugin
Summary(pl):	Klient VideoLAN - plugin gnome
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description gnome
Gnome output plugin for VideoLAN Client.

%description -l pl gnome
Plugin gnome dla Klienta VideoLAN.

%package esd
Summary:	VideoLAN Client - esound output plugin
Summary(pl):	Klient VideoLAN - plugin esound
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description esd
Esd output plugin for VideoLAN Client.

%description -l pl esd
Plugin esd dla Klienta VideoLAN.

%prep
%setup -q

%build
autoconf
%configure \
%ifarch i586 i686
	--enable-mmx \
%ifarch i686
	--enable-ppro \
%endif
%else
	--disable-mmx \
	--disable-ppro \
%endif
	--enable-dummy \
	--enable-dsp \
	--enable-esd \
	--enable-fb \
	--with-ggi \
	--with-sdl \
	--disable-glide \
	--enable-gnome \
	--enable-x11 \
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vlc
%dir %{_libdir}/videolan
%dir %{_libdir}/videolan/vlc
%attr(755,root,root) %{_libdir}/videolan/vlc/dsp.so
%attr(755,root,root) %{_libdir}/videolan/vlc/dummy.so
%attr(755,root,root) %{_libdir}/videolan/vlc/dvd.so
%attr(755,root,root) %{_libdir}/videolan/vlc/fb.so
%attr(755,root,root) %{_libdir}/videolan/vlc/idct.so
%attr(755,root,root) %{_libdir}/videolan/vlc/idctclassic.so
%attr(755,root,root) %{_libdir}/videolan/vlc/motion.so
%attr(755,root,root) %{_libdir}/videolan/vlc/null.so
%attr(755,root,root) %{_libdir}/videolan/vlc/ps.so
%attr(755,root,root) %{_libdir}/videolan/vlc/ts.so
%attr(755,root,root) %{_libdir}/videolan/vlc/yuv.so
%ifarch i586 i686
%attr(755,root,root) %{_libdir}/videolan/vlc/*mmx*.so
%endif
%dir %{_datadir}/videolan
%{_datadir}/videolan/*.psf
%{_datadir}/videolan/vlc.png

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/x11.so

%files GGI
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/ggi.so

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/sdl.so

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvlc
%attr(755,root,root) %{_libdir}/videolan/vlc/gnome.so
%{_datadir}/videolan/gvlc.png

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/esd.so
