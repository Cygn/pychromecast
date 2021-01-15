%global pypi_name pychromecast
%define name python3-chromecast

Name:       	%{name}    
Version:        7.7.2
Release:        1%{?dist}
Summary:        Python module to talk to Google Chromecast

License:        MIT
URL:            https://github.com/balloob/pychromecast
Source0:        python3-chromecast-7.7.2.tar.gz
BuildArch:      noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: 	%{_prefix}
Summary:        Python module to talk to Google Chromecast devices.

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-zeroconf
Requires:       python%{python3_pkgversion}-protobuf

%description
Library for Python 3.6+ to communicate with the Google Chromecast.

%prep
%autosetup -n %{name}-%{unmangled_version}

%build
%py3_build

%install
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}
%{python3_sitelib}/pychromecast
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%doc README.md

%changelog
* Thu Jan 14 2021 mockbuilder - 7.7.2-1
- Initial package. SH.
