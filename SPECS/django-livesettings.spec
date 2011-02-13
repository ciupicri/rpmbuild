%global hg_version 9467c4bb5471

Name:           django-livesettings
Version:        1.4.7
Release:        1
Summary:        Django livesettings

Group:          Development/Languages
License:        BSD
URL:            http://bitbucket.org/bkroeze/django-livesettings/
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
Django-Livesettings is a project split from the Satchmo Project. It provides
the ability to configure settings via an admin interface, rather than by
editing "settings.py".


%prep
%setup -q -n %{name}
%patch0 -p1
find -name '*.mo' -exec rm -f {} \+


%build
%{__python} setup.py compile_catalog --domain django -d livesettings/locale
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_ROOT}%{python_sitelib}/tests
%find_lang django
find $RPM_BUILD_ROOT -name "*.po" -exec rm -f {} \+

 
%files -f django.lang
%defattr(-,root,root,-)
%doc AUTHORS LICENSE docs
%{python_sitelib}/*


%changelog
* Wed Mar 02 2011 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.4.7-1
- Initial package
