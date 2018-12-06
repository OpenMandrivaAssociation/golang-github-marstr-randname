# Run tests in check section
%bcond_without check

%global goipath         github.com/marstr/randname
%global commit          48a63b6052f1f9373db9388a658da30c6ab53db1

%global common_description %{expand:
A Go package which creates random names with an emphasis on flexibility and 
ease of use.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        A Go package which creates random names
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/marstr/collection)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git48a63b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628git48a63b6
- Bump to commit 48a63b6052f1f9373db9388a658da30c6ab53db1

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416git3ef1f47
- First package for Fedora

