Summary:	VideoLAN Client
Summary(pl):	Klient VideoLAN
Name:		vlc
Version:	0.2.80
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
BuildRequires:	alsa-lib-devel
BuildRequires:	SDL-devel >= 1.2
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

%package gtk
Summary:	VideoLAN Client - gtk output plugin
Summary(pl):	Klient VideoLAN - plugin gtk
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description gtk
GTK output plugin for VideoLAN Client.

%description -l pl gtk
Plugin GTK dla Klienta VideoLAN.

%package esd
Summary:	VideoLAN Client - esound output plugin
Summary(pl):	Klient VideoLAN - plugin esound
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Requires:	%{name} = %{version}
   
%description esd
Esd audio output plugin for VideoLAN Client.

%description -l pl esd
Plugin audio esd dla Klienta VideoLAN.

#%package alsa
#Summary:	VideoLAN Client - alsa output plugin
#Summary(pl):	Klient VideoLAN - plugin alsa
#Group:		X11/Applications/Multimedia
#Group(de):	X11/Applikationen/Multimedia
#Group(pl):	X11/Aplikacje/Multimedia
#Requires:	%{name} = %{version}
#   
#%description alsa
#ALSA audio output plugin for VideoLAN Client.
#
#%description -l pl alsa
#Plugin audi ALSA dla Klienta VideoLAN.
#

%prep
%setup -q

%build
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
	--disable-alsa \
	--enable-esd \
	--enable-fb \
	--with-ggi \
	--with-sdl \
	--disable-glide \
	--enable-gnome \
	--enable-x11 \
	--with-sdl=/usr/X11R6 \
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
%attr(755,root,root) %{_libdir}/videolan/vlc/fb.so
%dir %{_datadir}/videolan
%{_datadir}/videolan/*.psf
%{_datadir}/videolan/vlc.png

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/x11.so
%attr(755,root,root) %{_libdir}/videolan/vlc/xvideo.so

%files GGI
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/ggi.so

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/sdl.so

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvlc
%attr(755,root,root) %{_libdir}/videolan/vlc/gtk.so
%{_datadir}/videolan/gvlc.png

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-vlc
%attr(755,root,root) %{_libdir}/videolan/vlc/gnome.so
%{_datadir}/videolan/gvlc.png

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/videolan/vlc/esd.so

#%files alsa
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/videolan/vlc/alsa.so
