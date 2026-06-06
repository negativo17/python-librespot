%global srcname librespot-python
%global protobuf_version 3.20.3

%global __requires_exclude_from %{python3_sitelib}/librespot/_vendor/

Name:           python-librespot
Version:        0.0.10
Release:        3%{?dist}
Summary:        Open Source Spotify Client
License:        Apache-2.0
URL:            http://librespot-python.rtfd.io/
BuildArch:      noarch

Source0:        https://github.com/kokarare1212/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/p/protobuf/protobuf-%{protobuf_version}.tar.gz
Patch0:         %{name}-requirements.patch
Patch1:         %{name}-vendor-protobuf.patch
# Upstream patches:
Patch10:        https://github.com/kokarare1212/librespot-python/commit/b88bafdb110e6d9351050d10fffdfff001271317.patch
Patch11:        https://github.com/kokarare1212/librespot-python/commit/5e108e943985313fe65806fe7c08200a45fe2d71.patch
Patch12:        https://github.com/kokarare1212/librespot-python/commit/e7dcf4b2998a7102b241712e0e3d63d976db6ed7.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
A python port of Spotify’s open source client library librespot.}

%description %_description

%package -n     python3-librespot
Summary:        %{summary}
Provides:       bundled(python3dist(protobuf)) = %{protobuf_version}

%description -n python3-librespot %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Extract bundled protobuf source alongside the main source
tar -xf %{SOURCE1} -C %{_builddir}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# Build bundled protobuf wheel into a separate directory so it does not
# end up in the shared pyproject wheeldir and get picked up by %pyproject_install
%{python3} -m pip wheel --no-deps --no-build-isolation \
    --wheel-dir %{_builddir}/protobuf-dist \
    %{_builddir}/protobuf-%{protobuf_version}

%install
%pyproject_install
%pyproject_save_files librespot
# Install bundled protobuf into the vendor subdirectory
%{python3} -m pip install --no-deps --no-build-isolation \
    --target %{buildroot}%{python3_sitelib}/librespot/_vendor \
    %{_builddir}/protobuf-dist/protobuf-%{protobuf_version}-*.whl

%files -n python3-librespot -f %{pyproject_files}
%license LICENSE.txt
%doc README.md CONTRIBUTING.md SECURITY.md CODE_OF_CONDUCT.md
%{python3_sitelib}/librespot/_vendor/
%{python3_sitelib}/librespot_player

%changelog
* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 0.0.10-3
- Bundle protobuf 3.20.3.

* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 0.0.10-2
- Fix requirements.
- Backport upstream fixes.

* Sat Jun 06 2026 Simone Caronni <negativo17@gmail.com> - 0.0.10-1
- First build.

