Summary:	ALSA <--> Jack bridge
Name:		zita-ajbridge
Version:	0.4.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	9b834537b26063cc9ea6990cadeef62d
Patch0:		%{name}-make.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zita-alsa-pcmi-devel
BuildRequires:	zita-resampler-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides two applications, zita-a2j and zita-j2a.
They allow to use an ALSA device as a Jack client, to provide
additional capture (a2j) or playback (j2a) channels.
Functionally these are equivalent to the alsa_in and alsa_out
clients that come with Jack, but they provide much better audio
quality. The resampling ratio will typically be stable within
1 PPM and change only very smoothly. Delay will be stable as
well even under worse case conditions, e.g. the Jack client
running near the end of the cycle.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} -C source \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*

