%global hg_date 20120328
%global hg_version fe16a426b273
%global posttag %{hg_date}hg%{hg_version}

Name:           django-livesettings
Version:        1.4.11
Release:        1.%{posttag}%{?dist}
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
BuildRequires:  Django
BuildRequires:  gettext
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
* Wed May 02 2012 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 1.4.11-1.20120328hgfe16a426b273
- Initial package
