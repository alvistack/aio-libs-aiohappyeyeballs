# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-aiohappyeyeballs
Epoch: 100
Version: 2.4.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Happy Eyeballs for asyncio Asynchronous HTTP client/server framework for asyncio and Python
License: Apache-2.0
URL: https://github.com/aio-libs/aiohappyeyeballs/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This library exists to allow connecting with Happy Eyeballs (RFC 8305)
when you already have a list of addrinfo and not a DNS name.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-aiohappyeyeballs
Summary: Happy Eyeballs for asyncio Asynchronous HTTP client/server framework for asyncio and Python
Requires: python3
Provides: python3-aiohappyeyeballs = %{epoch}:%{version}-%{release}
Provides: python3dist(aiohappyeyeballs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiohappyeyeballs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiohappyeyeballs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiohappyeyeballs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiohappyeyeballs) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-aiohappyeyeballs
This library exists to allow connecting with Happy Eyeballs (RFC 8305)
when you already have a list of addrinfo and not a DNS name.

%files -n python%{python3_version_nodots}-aiohappyeyeballs
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-aiohappyeyeballs
Summary: Happy Eyeballs for asyncio Asynchronous HTTP client/server framework for asyncio and Python
Requires: python3
Provides: python3-aiohappyeyeballs = %{epoch}:%{version}-%{release}
Provides: python3dist(aiohappyeyeballs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-aiohappyeyeballs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(aiohappyeyeballs) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-aiohappyeyeballs = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(aiohappyeyeballs) = %{epoch}:%{version}-%{release}

%description -n python3-aiohappyeyeballs
This library exists to allow connecting with Happy Eyeballs (RFC 8305)
when you already have a list of addrinfo and not a DNS name.

%files -n python3-aiohappyeyeballs
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
