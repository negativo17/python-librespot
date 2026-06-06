%global srcname librespot-python

Name:           python-librespot
Version:        0.0.10
Release:        2%{?dist}
Summary:        Open Source Spotify Client
License:        Apache-2.0
URL:            http://librespot-python.rtfd.io/
BuildArch:      noarch

Source0:        https://github.com/kokarare1212/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch0:         %{name}-requirements.patch

BuildRequires:  python3-devel

%global _description %{expand:
A python port of Spotify’s open source client library librespot.}

%description %_description

%package -n     python3-librespot
Summary:        %{summary}

%description -n python3-librespot %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files librespot

%files -n python3-librespot -f %{pyproject_files}
%license LICENSE.txt
%doc README.md CONTRIBUTING.md SECURITY.md CODE_OF_CONDUCT.md
%{python3_sitelib}/librespot_player

%changelog
* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 0.0.10-2
- Fix requirements.

* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 0.0.10-1
- First build.

