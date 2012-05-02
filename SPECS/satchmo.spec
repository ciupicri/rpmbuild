%global hg_date 20120428
%global hg_version 953206665bff
%global posttag %{hg_date}hg%{hg_version}

Name:           satchmo
Version:        0.9.2
Release:        1.%{posttag}%{?dist}
Summary:        The web shop for perfectionists with deadlines

Group:          Development/Languages
License:        BSD
URL:            http://www.satchmoproject.com
# Source0:        http://bitbucket.org/chris1610/%{name}/get/%{hg_version}.tar.bz2
Source0:        %{name}-%{hg_version}.tar.bz2
Patch0:         %{name}-no-ez_setup.patch
Patch1:         %{name}-no-setuptools_hg.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# for documentation
%if ! (0%{?fedora} > 13 || 0%{?rhel} > 6)
BuildRequires:  python-sphinx10
%else
BuildRequires:  python-sphinx
%endif
# for message catalog compilation
BuildRequires:  Django
BuildRequires:  gettext
Requires:       Django
Requires:       python-sorl-thumbnail
Requires:       python-crypto
Requires:       python-trml2pdf
Requires:       django-threaded-multihost
Requires:       django-caching-app-plugins
Requires:       django-livesettings
Requires:       django-keyedcache
Requires:       django-signals-ahoy
Requires:       django-registration
# The following package is required to load the initial data and run the unit tests:
Requires:       PyYAML

%description
Satchmo is an e-commerce framework created using Django.

%package doc
Summary:        Documentation for Satchmo
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-docs = %{version}-%{release}
Obsoletes:      %{name}-docs < %{version}-%{release}

%description doc
This package contains the documentation for the Satchmo e-commerce framework.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
find -name '*.mo' -exec rm -f {} \+


%build
find -name locale -exec sh -c 'cd $0 && cd .. && django-admin compilemessages' {} \;
%{__python} setup.py build
pushd docs
%if ! (0%{?fedora} > 13 || 0%{?rhel} > 6)
	make SPHINXBUILD=sphinx-1.0-build html
%else
	make html
%endif
rm .build/html/.buildinfo
popd


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
mv ${RPM_BUILD_ROOT}/%{_bindir}/clonesatchmo.py ${RPM_BUILD_ROOT}/%{_bindir}/clonesatchmo
%if ! (0%{?fedora} > 13 || 0%{?rhel} > 6)
	(cd $RPM_BUILD_ROOT && find . -name 'django*.mo') | %{__sed} -e 's|^.||' | %{__sed} -e \
		's:\(.*/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:' \
		>> django.lang
%else
	%find_lang django
%endif
find $RPM_BUILD_ROOT -name "*.po" -exec rm -f {} \+
rm -rf ${RPM_BUILD_ROOT}%{python_sitelib}/docs


%files -f django.lang
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG CONTRIBUTORS LICENSE
%{python_sitelib}/*
%{_bindir}/clonesatchmo

%files doc
%defattr(-,root,root,-)
%doc docs/.build/html/*


%changelog
* Wed May 02 2012 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 0.9.2-1.20120428hg953206665bff
- Initial package
