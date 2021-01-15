%global pypi_name PyChromecast
%define name python3-chromecast
%define srcname PyChromecast
%define version 7.7.2
%define unmangled_version 7.7.2
%define release 2

Name:       	%{name}    
Version:      %{version}
Release:      %{release}
Source0:      %{name}-%{unmangled_version}.tar.gz
Summary:      Python module to talk to Google Chromecast
License:      MIT
URL:          https://github.com/home-assistant-libs/pychromecast
BuildArch:    noarch
BuildRoot: 	  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: 	    %{_prefix}
Packager:     Sinan H <sinan@haliyo.net>

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-netifaces
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-zeroconf
Requires:       python%{python3_pkgversion}-protobuf

%description
Library for Python 3 to communicate with the Google Chromecast. It currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%prep
%autosetup -n %{name}-%{unmangled_version}

%build
%py3_build

%install
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}
%license LICENSE
%{python3_sitelib}/pychromecast
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%doc README.rst

%changelog
* Thu Jan 14 2021 mockbuilder - 7.7.2-1
- Initial package. SH.
