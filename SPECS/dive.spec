%define debug_package %{nil}

%global gh_user wagoodman

Name:           dive
Version:        0.10.0
Release:        1
Summary:        A tool for exploring each layer in a docker image
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  golang

%description
A tool for exploring a docker image, layer contents, and discovering ways to
shrink the size of your Docker/OCI image.

%prep
%setup -q -n %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Jun 29 2021 Jamie Curnow <jc@jc21.com> 0.10.0-1
- https://github.com/wagoodman/dive/releases/tag/v0.10.0

