%global hg_date 20120224
%global hg_version 49f24c711518
%global posttag %{hg_date}hg%{hg_version}

Name:           django-keyedcache
Version:        1.4.6
Release:        1.%{posttag}%{?dist}
Summary:        Django Keyedcache

Group:          Development/Languages
License:        BSD
URL:            http://bitbucket.org/bkroeze/django-keyedcache/
# Source0:        http://bitbucket.org/bkroeze/%{name}/get/%{hg_version}.tar.bz2
Source0:        %{name}-%{hg_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# for message catalog compilation
BuildRequires:  Django
BuildRequires:  gettext
Requires:       Django

%description
Django Keyedcache provides utilities and class mix-ins for simplified
development of cache-aware objects. Used in Satchmo.


%prep
%setup -q -n %{name}
find -name '*.mo' -exec rm -f {} \+


%build
find -name locale -exec sh -c 'cd $0 && cd .. && django-admin compilemessages' {} \;
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_ROOT}%{python_sitelib}/tests
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
%doc AUTHORS LICENSE docs
%{python_sitelib}/*


%changelog
* Wed May 01 2012 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.4.6-1.20120224hg49f24c711518
- Initial package
