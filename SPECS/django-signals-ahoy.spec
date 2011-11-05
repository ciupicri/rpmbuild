%global hg_date 20110420
%global hg_version 87f60574d64b
%global posttag %{hg_date}hg%{hg_version}

Name:           django-signals-ahoy
Version:        0.1.1
Release:        1.%{posttag}%{?dist}
Summary:        Django Signals Ahoy

Group:          Development/Languages
License:        BSD
URL:            http://bitbucket.org/bkroeze/django-signals-ahoy/
# Source0:        http://bitbucket.org/bkroeze/%{name}/get/%{hg_version}.tar.bz2
Source0:        %{name}-%{hg_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       Django

%description
Django Signals Ahoy provides very useful common signals for
larger Django applications.


%prep
%setup -q -n %{name}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_ROOT}%{python_sitelib}/tests

 
%files
%defattr(-,root,root,-)
%doc LICENSE.rst
%{python_sitelib}/*


%changelog
* Thu Nov 04 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 0.1.1-1.20110420hg87f60574d64b
- Initial package
