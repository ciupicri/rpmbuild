%global hg_date 20101128
%global hg_version 93fc130080b1
%global posttag %{hg_date}hg%{hg_version}

Name:           satchmo
Version:        0.9.1
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
# for message catalog compilation
BuildRequires:  python-babel
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
find -name locale -exec %{__python} setup.py compile_catalog --domain django -d {} \;
%{__python} setup.py build
pushd docs
make html
rm .build/html/.buildinfo
popd


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%find_lang django
find $RPM_BUILD_ROOT -name "*.po" -exec rm -f {} \+
rm -rf ${RPM_BUILD_ROOT}%{python_sitelib}/docs


%files -f django.lang
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG CONTRIBUTORS LICENSE
%{python_sitelib}/*
%{_bindir}/clonesatchmo.py

%files doc
%defattr(-,root,root,-)
%doc docs/.build/html/*


%changelog
* Mon Nov 29 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 0.9.1-1.20101128hg93fc130080b1
- Initial package