%global git_version 3fc530c
%global github_username benoitc

Name:           gunicorn
Version:        0.12.1
Release:        1%{?dist}
Summary:        WSGI HTTP Server for UNIX

Group:          Development/Languages
License:        MIT
URL:            http://gunicorn.org
Source0:        https://download.github.com/%{github_username}-%{name}-%{version}-0-g%{git_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-setuptools

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly
compatible with various web frameworks, simply implemented, light on server
resource usage, and fairly speedy.


%prep
%setup -q -n %{github_username}-%{name}-%{git_version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README.rst THANKS
%{python_sitelib}/*
%{_bindir}/*


%changelog
* Thu Mar 03 2011 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 0.12.1-1
- Initial package
