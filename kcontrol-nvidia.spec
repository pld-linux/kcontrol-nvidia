Summary:	Kcontrol module for NVidia's NV-Control extension
Name:		kcontrol-nvidia
Version:	0
Release:	0.3
License:	GPL
Group:		X11/Applications
URL:		http://websvn.kde.org/trunk/kdenonbeta/nvidia/
Source0:	nvidia-20060130.503942.tar.bz2
# Source0-md5:	0ed43610bab3bbec2b4cf6999c1affe5
BuildRequires:	libXNVCtrl-devel
BuildRequires:	unsermake >= 051225
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains kcontrol modules which provide access to the
NV-CONTROL extension in NVIDIA's latest drivers - it duplicates the
functionality of their nvidia-settings application (which uses gtk).

%prep
%setup -q -n nvidia

%build
cp -f /usr/share/automake/config.sub admin
export PATH=/usr/share/unsermake:$PATH
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
    --enable-libsuffix=64 \
%endif
    --%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
    --with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

# kde 3.5.1 already loads them as tabls in kcontrol module
rm -f $RPM_BUILD_ROOT%{_desktopdir}/kde/{nvidia3d,nvidiadisplay}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_nvidia3d.la
%{_libdir}/kde3/kcm_nvidia3d.so
%{_libdir}/kde3/kcm_nvidiadisplay.la
%{_libdir}/kde3/kcm_nvidiadisplay.so
