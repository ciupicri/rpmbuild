%global hg_date 20100612
%global hg_version dd9c1dccfea8
%global posttag %{hg_date}hg%{hg_version}

Name:           django-caching-app-plugins
Version:        0.1.2
Release:        1.%{posttag}%{?dist}
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
BuildRequires:  python-babel
Requires:       Django

%description
A fork of "django-app-plugins" which caches the results of the lookups,
saving several db queries per page.


%prep
%setup -q -n %{name}
%patch0 -p1
find -name '*.mo' -exec rm -f {} \+


%build
%{__python} setup.py compile_catalog --domain django -d app_plugins/locale
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%find_lang django
find $RPM_BUILD_ROOT -name "*.po" -exec rm -f {} \+

 
%files -f django.lang
%defattr(-,root,root,-)
%doc LICENSE.rst
%{python_sitelib}/*


%changelog
* Thu Nov 04 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 0.1.2-1.20100612hgdd9c1dccfea8
- Initial package
