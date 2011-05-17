%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
%global hg_date 20110306
%global hg_version 4aebd54035c8
%global posttag %{hg_date}hg%{hg_version}

Name:           django-threaded-multihost
Version:        1.4.1
Release:        1.%{posttag}%{?dist}
Summary:        Django Threaded Multihost

Group:          Development/Languages
License:        BSD
URL:            http://bitbucket.org/bkroeze/django-threaded-multihost/
# Source0:        http://bitbucket.org/bkroeze/%{name}/get/%{hg_version}.tar.bz2
Source0:        %{name}-%{hg_version}.tar.bz2
Patch0:         %{name}-no-ez_setup.patch
Patch1:         %{name}-no-setuptools_hg.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       Django

%description
django-threaded-multihost provides support utilities to
enable easy multi-site awareness in Django apps.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%defattr(-,root,root,-)
%doc LICENSE.rst docs
%{python_sitelib}/*


%changelog
* Tue Mar 29 2011 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.4.1-1.20110306hg4aebd54035c8
- Initial package
