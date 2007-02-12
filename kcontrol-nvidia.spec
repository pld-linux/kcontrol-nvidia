Summary:	Kcontrol module for NVidia's NV-Control extension
Summary(pl.UTF-8):   Moduł kcontrol dla rozszerzenia NV-Control sterowników NVIDIA
Name:		kcontrol-nvidia
Version:	0
Release:	0.5
License:	GPL
Group:		X11/Applications
URL:		http://websvn.kde.org/trunk/kdenonbeta/nvidia/
Source0:	nvidia-20060130.503942.tar.bz2
Patch0:		%{name}-hide.patch
Patch1:		kde-ac260.patch
Patch2:		kde-ac260-lt.patch
Patch3:		kde-common-PLD.patch
# Source0-md5:	0ed43610bab3bbec2b4cf6999c1affe5
BuildRequires:	libXNVCtrl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains kcontrol modules which provide access to the
NV-CONTROL extension in NVIDIA's latest drivers - it duplicates the
functionality of their nvidia-settings application (which uses GTK+).

%description -l pl.UTF-8
Ten pakiet zawiera moduły kcontrol dające dostęp do rozszerzenia
NV-CONTROL w najnowszych sterownikach NVIDIA - powielające
funkcjonalność aplikacji nvidia-settings (korzystającej z GTK+).

%prep
%setup -q -n nvidia
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub admin
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_nvidia3d.la
%attr(755,root,root) %{_libdir}/kde3/kcm_nvidia3d.so
%{_libdir}/kde3/kcm_nvidiadisplay.la
%attr(755,root,root) %{_libdir}/kde3/kcm_nvidiadisplay.so
%{_desktopdir}/kde/nvidia3d.desktop
%{_desktopdir}/kde/nvidiadisplay.desktop
