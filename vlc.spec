Summary:	VideoLAN Client
Name:		vlc
Version:	0.1.99i
Release:	1
License:	GPL
Group:		Applications/Multimedia
######		Unknown group!
Source0:	http://www.videolan.org/packages/%{version}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-SDL.patch
URL:		http://www.videolan.org/
BuildRequires:	gnome-libs-devel
BuildRequires:	libggi-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%description
VideoLAN is a free MPEG2 software solution.

The VideoLAN Client allows to play MPEG2 Transport Streams from the
network or from a file, as well as direct DVD playback.

%package X11
Summary:	VideoLAN Client - X11 output plugin
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description X11
X11 output plugin for VideoLAN Client

%package GGI
Summary:	VideoLAN Client - GGI output plugin
Group:		Applications/Multimedia
######		Unknown group!
Requires:	%{name} = %{version}
   
%description GGI
GGI output plugin for VideoLAN Client

%package SDL
Summary:	VideoLAN Client - SDL output plugin
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description SDL
SDL output plugin for VideoLAN Client

%package gnome
Summary:	VideoLAN Client - gnome output plugin
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description gnome
gnome output plugin for VideoLAN Client

%package esd
Summary:	VideoLAN Client - esound output plugin
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description esd
esd output plugin for VideoLAN Client

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
%ifarch i586 i686
	--enable-mmx \
%else
	--disable-mmx \
%endif
	--enable-dummy \
	--enable-dsp \
	--enable-esd \
	--enable-fb \
	--enable-ggi \
	--enable-sdl \
	--disable-glide \
	--enable-gnome \
	--enable-x11
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=${RPM_BUILD_ROOT}/%{_prefix}
gzip -9nf README TODO ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/vlc
%attr(755,root,root) %{_bindir}/fbvlc
%dir %{_libdir}/videolan/vlc
%{_libdir}/videolan/vlc/dsp.so
%{_libdir}/videolan/vlc/dummy.so
%{_libdir}/videolan/vlc/fb.so
%{_libdir}/videolan/vlc/yuv*.so
%dir %{_datadir}/videolan
%{_datadir}/videolan/*.psf
%{_datadir}/videolan/vlc.png

%files X11
%defattr(644,root,root,755)
%{_libdir}/videolan/vlc/x11.so

%files GGI
%defattr(644,root,root,755)
%{_libdir}/videolan/vlc/ggi.so

%files SDL
%defattr(644,root,root,755)
%{_libdir}/videolan/vlc/sdl.so

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvlc
%{_libdir}/videolan/vlc/gnome.so
%{_datadir}/videolan/gvlc.png

%files esd
%defattr(644,root,root,755)
%{_libdir}/videolan/vlc/esd.so
