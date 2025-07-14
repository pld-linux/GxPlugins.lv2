Summary:	A set of extra lv2 plugins from the Guitarix project
Name:		GxPlugins.lv2
Version:	0.7
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/brummer10/GxPlugins.lv2/releases/download/v%{version}/GxPlugins_%{version}.tar.gz
# Source0-md5:	05d739339bd48311b1e9590232780809
Patch0:		makefiles.patch
URL:		https://github.com/brummer10/GxPlugins.lv2
BuildRequires:	cairo-devel
BuildRequires:	lv2-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
GxPlugins.lv2 is a set of extra standalone lv2 plugins designed to
compliment the Guitarix project.

%prep
%setup -qn GxPlugins_%{version}

%patch -P0 -p1

%build
%{__make} \
	INSTALL_DIR="%{_libdir}/lv2" \
	SSE_CFLAGS="" \
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
%%dir %{_libdir}/lv2/*.lv2
%{_libdir}/lv2/*.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/*.lv2/*.so
