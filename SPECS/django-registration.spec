%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
Name:           django-registration
Version:        0.7
Release:        1%{?dist}
Summary:        An extensible user-registration application for Django

Group:          Development/Languages
License:        BSD
URL:            http://www.bitbucket.org/ubernostrum/django-registration/wiki/
#Source0:        http://bitbucket.org/ubernostrum/django-registration/get/v%{version}.tar.bz2
Source0:        %{name}-v%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       Django

%description
An extensible user-registration application for Django.


%prep
%setup -q -n %{name}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%if ! (0%{?fedora} > 13 || 0%{?rhel} > 6)
	(cd $RPM_BUILD_ROOT && find . -name 'django*.mo') | %{__sed} -e 's|^.||' | %{__sed} -e \
		's:\(.*/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:' \
		>> django.lang
%else
	%find_lang django
%endif
find $RPM_BUILD_ROOT -name "*.po" -exec rm -f {} \+

 
%files -f django.lang
%defattr(-,root,root,-)
%doc AUTHORS.txt CHANGELOG.txt INSTALL.txt LICENSE.txt README.txt docs
%{python_sitelib}/*


%changelog
* Thu Nov 04 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 0.7-1
- Initial package
