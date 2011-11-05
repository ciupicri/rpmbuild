%global hg_date 20111018
%global hg_version b0e77d2243cb
%global posttag %{hg_date}hg%{hg_version}

Name:           django-caching-app-plugins
Version:        0.1.3
Release:        1%{?dist}
Summary:        Django caching app plugins

Group:          Development/Languages
License:        BSD
URL:            http://bitbucket.org/bkroeze/django-caching-app-plugins
# Source0:        http://bitbucket.org/bkroeze/%{name}/get/%{hg_version}.tar.bz2
Source0:        %{name}-%{hg_version}.tar.bz2
Patch0:         %{name}-no-setuptools_hg.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# for message catalog compilation
BuildRequires:  Django
BuildRequires:  gettext
Requires:       Django

%description
A fork of "django-app-plugins" which caches the results of the lookups,
saving several db queries per page.


%prep
%setup -q -n %{name}
%patch0 -p1
find -name '*.mo' -exec rm -f {} \+


%build
find -name locale -exec sh -c 'cd $0 && cd .. && django-admin compilemessages' {} \;
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
%doc LICENSE.rst
%{python_sitelib}/*


%changelog
* Thu Nov 05 2011 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 0.1.3-1
- Initial package
