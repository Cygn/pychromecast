# Created by pyp2rpm-3.3.5
%global pypi_name PyChromecast

Name:           python3-chromecast
Version:        7.7.2
Release:        1%{?dist}
Summary:        Python module to talk to Google Chromecast

License:        MIT
URL:            https://github.com/balloob/pychromecast
Source0:        https://files.pythonhosted.org/packages/7c/a0/7c34881d2130d43feb40a37961e71a6158c8df5c1c2e7fed5b57299d5c50/PyChromecast-7.7.2.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Library for Python 3.6+ to communicate with the Google Chromecast.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Python module to talk to Google Chromecast

Requires:       python%{python3_pkgversion}-autobahn
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-twisted
%description -n python%{python3_pkgversion}-%{pypi_name}
UNKNOWN


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/pychromecast
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jan 14 2021 mockbuilder - 7.7.2-1
- Initial package. SH.
