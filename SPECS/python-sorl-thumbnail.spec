%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
%global srcname sorl-thumbnail
%global hg_date 20100820
%global hg_version 0ce451b2f815
%global posttag %{hg_date}hg%{hg_version}

Name:           python-sorl-thumbnail
Version:        3.2.5
Release:        1.%{posttag}%{?dist}
Summary:        Thumbnails for Django

Group:          Development/Languages
License:        BSD
URL:            http://code.google.com/p/sorl-thumbnail/
# hg clone http://sorl-thumbnail.googlecode.com/hg/
# cd sorl-thumbnail
# hg archive -t tbz2 -p %{srcname} %{srcname}-%{hg_version}.tar.bz2
Source0:        %{srcname}-%{hg_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel
# for documentation
%if ! (0%{?fedora} > 13 || 0%{?rhel} > 5)
BuildRequires:  python-sphinx10
%else
BuildRequires:  python-sphinx
%endif
Requires:       python-imaging
# To enable PDF thumbnails you need ImageMagick
Requires:       ImageMagick
# For Word document thumbnail handling you need ImageMagick and wvWare.
Requires:       wv

%description
sorl-thumbnail is a simple to use thumbnailing application for Django.


%prep
%setup -q -n %{srcname}


%build
%{__python} setup.py build
# documentation
%{__sed} -i 's/\r//' README
pushd docs
%if ! (0%{?fedora} > 13 || 0%{?rhel} > 5)
	make SPHINXBUILD=sphinx-1.0-build html
%else
	make html
%endif
rm _build/html/.buildinfo
popd


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%defattr(-,root,root,-)
%doc LICENSE README docs/_build/html
%{python_sitelib}/*


%changelog
* Thu Nov 04 2010 Cristian Ciupitu <cristian.ciupitu@yahoo.com> - 3.2.5-1.20100820hg0ce451b2f815
- Initial package
