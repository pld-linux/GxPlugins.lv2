# TODO: consider renaming to lv2-gx-plugins
Summary:	A set of extra LV2 plugins from the Guitarix project
Summary(pl.UTF-8):	Zbiór dodatkowych wtyczek LV2 z peojektu Guitarix
Name:		GxPlugins.lv2
Version:	1.0
Release:	1
License:	GPL v3
Group:		Libraries
#Source0Download: https://github.com/brummer10/GxPlugins.lv2/releases
Source0:	https://github.com/brummer10/GxPlugins.lv2/releases/download/v%{version}/gxplugins_%{version}_src.tar.bz2
# Source0-md5:	1ba27e193d61f8134a719535252edd8d
Patch0:		makefiles.patch
URL:		https://github.com/brummer10/GxPlugins.lv2
BuildRequires:	cairo-devel
BuildRequires:	lv2-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
GxPlugins.lv2 is a set of extra standalone LV2 plugins designed to
compliment the Guitarix project.

%description -l pl.UTF-8
GxPlugins.lv2 to zbiór dodatkowych, samodzielnych wtyczek LV2,
mających na celu uzupełnienie projektu Guitarix.

%prep
%setup -q -n GxPlugins.lv2
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	INSTALL_DIR="%{_libdir}/lv2" \
	SSE_CFLAGS="" \
	STRIP=: \
	rpmcxxflags="%{rpmcxxflags}" \
	rpmldflags="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR="%{_libdir}/lv2" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/gx_*.lv2
%{_libdir}/lv2/gx_*.lv2/gx_*.so
%{_libdir}/lv2/gx_*.lv2/*.ttl
